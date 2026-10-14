<template>
  <div class="p-page p-page-about" tabindex="-1">
    <v-toolbar flat :density="$vuetify.display.smAndDown ? 'compact' : 'default'" color="secondary" class="page-toolbar p-page__navigation">
      <v-toolbar-title>
        <span class="text-ltr">{{ $config.getAbout() }}</span>
      </v-toolbar-title>

      <v-btn icon href="https://www.photoprism.app/" target="_blank" rel="noopener" class="action-info mx-2" :title="$gettext('Learn more')">
        <v-icon size="26" color="surface-variant">mdi-diamond-stone</v-icon>
      </v-btn>
    </v-toolbar>
    <div class="pa-6">
      <p class="text-body-1 pb-2">
        <a href="https://www.photoprism.app/" target="_blank" rel="noopener">
          <strong>
            {{ $gettext("Our mission is to provide the most user- and privacy-friendly solution to keep your pictures organized and accessible.") }}
            {{
              $gettext(
                "That's why PhotoPrism was built from the ground up to run wherever you need it, without compromising freedom, privacy, or functionality."
              )
            }}
          </strong>
        </a>
      </p>


      <div class="py-2 text-columns text-ltr">
        <h3>Getting Started</h3>
        <p>
          Follow our
          <a :href="links.firstSteps" class="text-link" target="_blank" rel="noopener">First Steps 👣</a>
          tutorial to learn how to navigate the user interface and ensure your library is indexed according to your individual preferences. Additional help and
          product-specific information can be found in our
          <a href="https://www.photoprism.app/plus/kb/" class="text-link" target="_blank" rel="noopener">Knowledge Base</a>.
        </p>

        <h3>User Guide</h3>
        <p>
          Visit
          <a :href="links.docs" class="text-link" target="_blank" rel="noopener">docs.photoprism.app/user-guide</a>
          to learn how to sync, organize, and share your pictures. Our
          <a :href="links.userGuide" class="text-link" target="_blank" rel="noopener">User Guide</a> also covers many advanced topics, such as
          <a href="https://docs.photoprism.app/user-guide/use-cases/google/" class="text-link" target="_blank" rel="noopener">migrating from Google Photos</a>
          and
          <a href="https://docs.photoprism.app/user-guide/settings/advanced/#preview-images" class="text-link" target="_blank" rel="noopener"
            >thumbnail quality settings</a
          >. Common issues can be quickly diagnosed and solved using the troubleshooting checklists we provide at
          <a :href="links.troubleshooting" class="text-link" target="_blank" rel="noopener">docs.photoprism.app/getting-started/troubleshooting</a>.
        </p>

        <h3>Getting Support</h3>
        <p>
          Before reporting a bug, please use our
          <a :href="links.troubleshooting" class="text-link" target="_blank" rel="noopener">Troubleshooting Checklists</a>
          to determine the cause of your problem. If you have a general question, need help, it could be a local configuration issue, or a misunderstanding in
          how the software works, you are welcome to ask in our
          <a href="https://link.photoprism.app/chat" class="text-link" target="_blank" rel="noopener">Community Chat</a>
          or post your question in
          <a href="https://link.photoprism.app/discussions" class="text-link" target="_blank" rel="noopener">GitHub Discussions</a>.
        </p>
        <p>
          When reporting a problem, always include the software versions you are using and
          <a :href="links.bugs" class="text-link" target="_blank" rel="noopener">other information about your environment</a>
          such as
          <a href="https://docs.photoprism.app/getting-started/troubleshooting/browsers/" class="text-link" target="_blank" rel="noopener"
            >browser, browser plugins</a
          >, operating system, storage type, memory size, and processor.
        </p>
        <p>
          We kindly ask you not to report bugs via GitHub Issues unless you are certain to have found a fully reproducible and previously unreported issue that
          must be fixed directly in the app.
        </p>

        <h3>Developer Guide</h3>
        <p>
          Our
          <a :href="links.developerGuide" class="text-link" target="_blank" rel="noopener">Developer Guide</a>
          contains all the information you need to get started as a developer. It guides you from
          <a :href="links.developerSetup" class="text-link" target="_blank" rel="noopener">setting up your development environment</a>
          and
          <a href="https://docs.photoprism.app/developer-guide/pull-requests/" class="text-link" target="_blank" rel="noopener">creating pull requests</a>
          to
          <a href="https://docs.photoprism.app/developer-guide/tests/" class="text-link" target="_blank" rel="noopener">running tests</a>
          and
          <a href="https://docs.photoprism.app/developer-guide/translations-weblate/" class="text-link" target="_blank" rel="noopener">adding translations</a>.
          Multiple subsections provide details on specific features and links to external resources for further information.
        </p>

        <h3>Terms &amp; Privacy</h3>
        <p>
          Visit
          <a href="https://www.photoprism.app/terms/" class="text-link" target="_blank" rel="noopener"><strong>photoprism.app/terms</strong></a>
          to learn how we work, what you can expect from us, and what we expect from you. What information we collect, how we use it, and under what
          circumstances we share it is explained in our
          <a href="https://www.photoprism.app/privacy/" class="text-link" target="_blank" rel="noopener">Privacy Policy</a>.
        </p>

        <p>
          Read our
          <a href="https://www.photoprism.app/privacy/gdpr/" class="text-link" target="_blank" rel="noopener">GDPR Compliance Statement</a>
          to learn more about the rights you have as a resident of the European Economic Area ("EEA"), our ongoing commitment to user privacy, and the General
          Data Protection Regulation ("GDPR").
        </p>

        <p>
          Our
          <a href="https://www.photoprism.app/trademark/" class="text-link" target="_blank" rel="noopener">Trademark and Brand Guidelines</a>, which may be
          updated from time to time, describe how our brand assets may be used. It is important to us that any permitted use of our brand assets is fair and
          meets the highest standards.
        </p>
      </div>

      <p class="text-caption mt-6 mb-0 text-center text-ltr">
        PhotoPrism® is a
        <a href="https://www.photoprism.app/trademark/" target="_blank" rel="noopener" class="text-link">registered trademark</a>. By using the software and
        services we provide, you agree to our <a href="https://www.photoprism.app/terms/" target="_blank" rel="noopener" class="text-link">Terms of Service</a>,
        <a href="https://www.photoprism.app/privacy/" target="_blank" rel="noopener" class="text-link">Privacy Policy</a>, and
        <a href="https://www.photoprism.app/code-of-conduct/" target="_blank" rel="noopener" class="text-link">Code of Conduct</a>.
      </p>
    </div>
    <p-about-footer></p-about-footer>
  </div>
</template>

<script>
import links from "common/links";

import PAboutFooter from "component/about/footer.vue";

export default {
  name: "PPageAbout",
  components: {
    PAboutFooter,
  },
  data() {
    return {
      links,
      rtl: this.$isRtl,
    };
  },
  mounted() {
    this.$view.enter(this);
  },
  unmounted() {
    this.$view.leave(this);
  },
};
</script>
