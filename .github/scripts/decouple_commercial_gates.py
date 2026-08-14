from pathlib import Path
import re


def read(path: str) -> str:
    return Path(path).read_text()


def write(path: str, text: str) -> None:
    Path(path).write_text(text)


def replace_once(path: str, old: str, new: str) -> None:
    text = read(path)
    count = text.count(old)
    if count != 1:
        raise SystemExit(f"{path}: expected exactly one match, got {count}: {old!r}")
    write(path, text.replace(old, new, 1))


# Local SVG/vector support is capability-based: explicit disable flag or missing rsvg-convert.
path = "internal/config/config_features.go"
text = read(path)
if text.count("c.options.DisableVectors || !c.Sponsor()") != 2:
    raise SystemExit("unexpected vector sponsor gate count")
text = text.replace("c.options.DisableVectors || !c.Sponsor()", "c.options.DisableVectors")
write(path, text)

# Keep the upstream shared geocoding service protected from forced bulk refreshes,
# but express the restriction without a commercial-membership runtime dependency.
replace_once(
    "internal/commands/places.go",
    'if force && !conf.Sponsor() && !conf.Test() {\n\t\tlog.Errorf("Since updating the location details of all pictures puts a high load on our infrastructure, this option cannot be used with our Community Edition.")\n\t\treturn nil\n\t}',
    'if force && !conf.Test() {\n\t\tlog.Errorf("Forced bulk location refresh is disabled when using the shared geocoding infrastructure; run the normal incremental update instead.")\n\t\treturn nil\n\t}',
)

# Tests now assert local converter availability rather than sponsor state.
path = "internal/config/config_features_test.go"
text = read(path)
text, n = re.subn(
    r"func TestConfig_DisableVector\(t \*testing\.T\) \{.*?\n\}\n\nfunc TestConfig_DisableRsvgConvert\(t \*testing\.T\) \{.*?\n\}",
    '''func TestConfig_DisableVector(t *testing.T) {
\tc := NewConfig(CliTestContext())
\tmissing := c.RsvgConvertBin() == ""

\tassert.Equal(t, missing, c.DisableVectors())
\tc.options.DisableVectors = true
\tassert.True(t, c.DisableVectors())
\tc.options.DisableVectors = false
\tassert.Equal(t, missing, c.DisableVectors())
}

func TestConfig_DisableRsvgConvert(t *testing.T) {
\tc := NewConfig(CliTestContext())
\tmissing := c.RsvgConvertBin() == ""

\tassert.Equal(t, missing, c.DisableRsvgConvert())
\tc.options.DisableVectors = true
\tassert.True(t, c.DisableRsvgConvert())
\tc.options.DisableVectors = false
\tassert.Equal(t, missing, c.DisableRsvgConvert())
}''',
    text,
    flags=re.S,
)
if n != 1:
    raise SystemExit(f"unexpected vector test block count: {n}")
write(path, text)

# Map styles that need a key are capability-gated, not membership-gated.
path = "frontend/src/options/options.js"
text = read(path)
count = text.count("sponsor: true,")
if count != 5:
    raise SystemExit(f"unexpected map sponsor marker count: {count}")
write(path, text.replace("sponsor: true,", "requiresMapKey: true,"))

replace_once(
    "frontend/src/page/places.vue",
    "this.mapStyles = options.MapsStyle(this.featExperimental).filter((s) => !s.Sponsor);",
    "this.mapStyles = options.MapsStyle(this.featExperimental).filter((s) => !s.requiresMapKey);",
)

# General settings: expose keyed styles only when this instance actually has a map key.
path = "frontend/src/page/settings/general.vue"
text = read(path)
text = text.replace('    <p-confirm-sponsor :visible="dialog.sponsor" @close="dialog.sponsor = false"></p-confirm-sponsor>\n', "")
text = text.replace('import PConfirmSponsor from "component/confirm/sponsor.vue";\n', "")
text = text.replace("    PAboutFooter,\n    PConfirmSponsor,\n", "    PAboutFooter,\n")
text = text.replace(
    '      mapsStyle: options.MapsStyle(this.$config.get("experimental")),',
    '      mapsStyle: options.MapsStyle(this.$config.get("experimental")).filter((s) => !s.requiresMapKey || this.$config.has("mapKey")),',
)
text = text.replace("      dialog: {\n        sponsor: false,\n      },\n", "")
text = text.replace(
    '        this.mapsStyle = options.MapsStyle(this.$config.get("experimental"));',
    '        this.mapsStyle = options.MapsStyle(this.$config.get("experimental")).filter((s) => !s.requiresMapKey || this.$config.has("mapKey"));',
)
text, n = re.subn(
    r"    onChangeMapsStyle\(value\) \{.*?\n    \},\n    onChange\(\) \{",
    '''    onChangeMapsStyle(value) {
      if (!value || !this.mapsStyle.find((s) => s.value === value)) {
        this.settings.maps.style = this.currentMapsStyle;
        return false;
      }

      this.currentMapsStyle = value;
      this.onChange();
    },
    onChange() {''',
    text,
    flags=re.S,
)
if n != 1:
    raise SystemExit(f"unexpected onChangeMapsStyle block count: {n}")
if "PConfirmSponsor" in text or "$sponsorFeatures" in text or "dialog.sponsor" in text:
    raise SystemExit("general settings still contains sponsor dialog dependencies")
write(path, text)

# Advanced settings: local vector toggle is visible to all non-demo personal instances.
replace_once(
    "frontend/src/page/settings/advanced.vue",
    '<v-col v-if="isSponsor" cols="12" sm="6" lg="4">',
    '<v-col cols="12" sm="6" lg="4">',
)
replace_once("frontend/src/page/settings/advanced.vue", "      isSponsor: this.$config.isSponsor(),\n", "")

# Remove the now-unused global membership promise helper.
path = "frontend/src/app.js"
text = read(path)
text, n = re.subn(
    r"  app\.config\.globalProperties\.\$sponsorFeatures = \(\) => \{.*?\n  \};\n",
    "",
    text,
    flags=re.S,
)
if n != 1:
    raise SystemExit(f"unexpected $sponsorFeatures helper count: {n}")
write(path, text)

# Remove commercial-only dialog/icon from global component registries.
path = "frontend/src/component/components.js"
text = read(path)
for line in [
    'import IconSponsor from "component/icon/sponsor.vue";\n',
    'import PConfirmSponsor from "component/confirm/sponsor.vue";\n',
    '  app.component("IconSponsor", IconSponsor);\n',
    '  app.component("PConfirmSponsor", PConfirmSponsor);\n',
]:
    if line not in text:
        raise SystemExit(f"{path}: expected line missing: {line.strip()}")
    text = text.replace(line, "")
write(path, text)

path = "frontend/src/component/icons.js"
text = read(path)
replace = 'import IconSponsor from "./icon/sponsor.vue";\n'
if replace not in text:
    raise SystemExit("sponsor icon import missing")
text = text.replace(replace, "")
text, n = re.subn(
    r'  sponsor: \{\n    component: IconSponsor,\n    props: \{\n      name: "sponsor",\n    \},\n  \},\n',
    "",
    text,
)
if n != 1:
    raise SystemExit(f"unexpected sponsor icon registry count: {n}")
write(path, text)

for path in ["frontend/src/component/confirm/sponsor.vue", "frontend/src/component/icon/sponsor.vue"]:
    p = Path(path)
    if not p.exists():
        raise SystemExit(f"expected commercial-only file missing: {path}")
    p.unlink()
