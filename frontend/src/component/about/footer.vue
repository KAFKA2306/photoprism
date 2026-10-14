<template>
  <footer class="p-about-footer text-ltr">
    <div class="flex-fill text-sm-start">
      <strong>
        <router-link to="/about" class="text-link text-selectable">{{ about }}</router-link>
      </strong>
      <span :title="version" class="body-link text-selectable">
        <span class="cursor-copy" @click.stop.prevent="$util.copyText(about, version)">Build</span>
        <a href="https://docs.photoprism.app/release-notes/" target="_blank" rel="noopener" class="body-link text-truncate">{{ build }}</a>
      </span>
    </div>
    <div class="hidden-xs text-sm-end">
      <a href="https://raw.githubusercontent.com/photoprism/photoprism/develop/NOTICE" target="_blank" rel="noopener" class="text-link"
        >3rd-party software packages</a
      >
      <a href="https://www.photoprism.app/about/team/" target="_blank" rel="noopener" class="body-link">© 2018-2026 PhotoPrism UG</a>
    </div>
  </footer>
</template>

<script>
export default {
  name: "PAboutFooter",
  data() {
    return {
      about: this.$config.getAbout(),
      version: this.$config.getVersion(),
    };
  },
  computed: {
    build() {
      if (this.$vuetify.display.xs) {
        return this.$config.getVersion().split("-").slice(0, 1).join("-");
      }

      return this.$config.getVersion().split("-").slice(0, 2).join("-");
    },
  },
};
</script>
