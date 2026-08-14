from pathlib import Path
import re


def replace(path: str, old: str, new: str) -> None:
    p = Path(path)
    text = p.read_text()
    if old not in text:
        raise SystemExit(f"expected block not found: {path}")
    p.write_text(text.replace(old, new))


def regex_replace(path: str, pattern: str, new: str, count: int = 1) -> None:
    p = Path(path)
    text = p.read_text()
    out, n = re.subn(pattern, new, text, count=count, flags=re.S)
    if n != count:
        raise SystemExit(f"expected {count} regex match in {path}, got {n}")
    p.write_text(out)


replace(
    "frontend/src/common/config.js",
    "  isSponsor() {\n    if (!this.values || !this.values.sponsor) {\n      return false;\n    }\n\n    return !this.values.demo && !this.values.test;\n  }\n\n",
    "",
)
regex_replace(
    "frontend/src/common/config.js",
    r"  getTier\(\) \{.*?\n  \}\n\n  getMembership\(\) \{.*?\n  \}\n\n  getCustomer\(\) \{.*?\n  \}\n\n",
    "",
)
replace(
    "frontend/src/page/settings/advanced.vue",
    '<v-col v-if="isSponsor" cols="12" sm="6" lg="4">',
    '<v-col cols="12" sm="6" lg="4">',
)
replace("frontend/src/page/settings/advanced.vue", "      isSponsor: this.$config.isSponsor(),\n", "")
replace("frontend/src/page/auth/login.vue", "      sponsor: this.$config.isSponsor(),\n", "")
replace(
    "frontend/src/page/settings/general.vue",
    '    <p-confirm-sponsor :visible="dialog.sponsor" @close="dialog.sponsor = false"></p-confirm-sponsor>\n',
    "",
)
replace("frontend/src/page/settings/general.vue", 'import PConfirmSponsor from "component/confirm/sponsor.vue";\n', "")
replace("frontend/src/page/settings/general.vue", "    PConfirmSponsor,\n", "")
replace("frontend/src/page/settings/general.vue", "      dialog: {\n        sponsor: false,\n      },\n", "")
regex_replace(
    "frontend/src/page/settings/general.vue",
    r"    onChangeMapsStyle\(value\) \{.*?\n    \},\n    onChange\(\) \{",
    "    onChangeMapsStyle(value) {\n      if (!value) {\n        this.currentMapsStyle = value;\n        this.onChange();\n        return;\n      }\n\n      const style = this.mapsStyle.find((s) => s.value === value);\n      if (!style) {\n        return false;\n      }\n\n      this.currentMapsStyle = value;\n      this.onChange();\n    },\n    onChange() {",
)
replace("frontend/src/component/components.js", 'import IconSponsor from "component/icon/sponsor.vue";\n', "")
replace("frontend/src/component/components.js", 'import PConfirmSponsor from "component/confirm/sponsor.vue";\n', "")
replace("frontend/src/component/components.js", '  app.component("IconSponsor", IconSponsor);\n', "")
replace("frontend/src/component/components.js", '  app.component("PConfirmSponsor", PConfirmSponsor);\n', "")
replace("frontend/src/component/icons.js", 'import IconSponsor from "./icon/sponsor.vue";\n', "")
regex_replace(
    "frontend/src/component/icons.js",
    r'  sponsor: \{\n    component: IconSponsor,\n    props: \{\n      name: "sponsor",\n    \},\n  \},\n',
    "",
)
replace(
    "frontend/src/page/about/about.vue",
    '<span class="text-ltr">{{ $config.getAbout() }}{{ getMembership() }}</span>',
    '<span class="text-ltr">{{ $config.getAbout() }}</span>',
)
regex_replace(
    "frontend/src/page/about/about.vue",
    r'\n      <template v-if="canUpgrade">.*?\n      </template>\n      <template v-else-if="isSuperAdmin">.*?\n      </template>\n',
    "\n",
)
regex_replace(
    "frontend/src/page/about/about.vue",
    r"  data\(\) \{\n    const tier = this\.\$config\.getTier\(\);.*?\n  \},\n  mounted\(\) \{",
    "  data() {\n    return {\n      links,\n      rtl: this.$isRtl,\n    };\n  },\n  mounted() {",
)
regex_replace(
    "frontend/src/page/about/about.vue",
    r"  methods: \{\n    getMembership\(\) \{.*?\n    \},\n  \},\n",
    "",
)
Path("frontend/src/component/confirm/sponsor.vue").unlink()
Path("frontend/src/component/icon/sponsor.vue").unlink()
