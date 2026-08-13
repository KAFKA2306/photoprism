<template>
  <div id="p-navigation" :class="{ 'sidenav-visible': drawer }">
    <template v-if="visible">
      <v-toolbar
        v-if="$vuetify.display.smAndDown"
        position="fixed"
        flat
        density="compact"
        color="navigation"
        class="nav-small elevation-2"
      >
        <v-btn icon variant="text" class="bg-transparent nav-logo" @click.stop.prevent="toggleDrawer">
          <img :src="appIcon" :alt="appName" :class="{ 'animate-hue': indexing }" />
        </v-btn>
        <v-toolbar-title class="nav-toolbar-title">{{ page.title }}</v-toolbar-title>
        <v-btn icon="mdi-dots-vertical" variant="text" :ripple="false" @click.stop.prevent="speedDial = true"></v-btn>
      </v-toolbar>

      <v-navigation-drawer v-if="auth" v-model="drawer" :rail="isMini" color="navigation" class="nav-sidebar navigation">
        <div class="nav-container">
          <v-toolbar flat>
            <v-list class="navigation-home elevation-0" bg-color="navigation-home" width="100%" density="compact">
              <v-list-item class="px-3" :ripple="false" @click.stop.prevent="onHome">
                <template #prepend>
                  <div class="v-avatar bg-transparent nav-logo">
                    <img :src="appIcon" :alt="appName" :class="{ 'animate-hue': indexing }" />
                  </div>
                </template>
                <template #append>
                  <v-btn
                    v-if="!$vuetify.display.smAndDown"
                    icon
                    variant="text"
                    :ripple="false"
                    :title="isMini ? 'メニューを広げる' : 'メニューを縮める'"
                    @click.stop.prevent="toggleIsMini"
                  >
                    <v-icon :icon="isMini ? 'mdi-chevron-right' : 'mdi-chevron-left'"></v-icon>
                  </v-btn>
                </template>
                <v-list-item-title v-if="!isMini" class="nav-toolbar-title">{{ appName }}</v-list-item-title>
              </v-list-item>
            </v-list>
          </v-toolbar>

          <v-list nav class="nav-menu" bg-color="navigation" color="primary" :density="$vuetify.display.smAndDown ? 'compact' : 'comfortable'">
            <v-list-item v-if="$config.feature('search')" :to="{ name: 'browse' }" class="nav-browse" :title="isMini ? '検索' : undefined">
              <template #prepend><v-icon>mdi-magnify</v-icon></template>
              <v-list-item-title v-if="!isMini">検索</v-list-item-title>
            </v-list-item>

            <v-list-item v-if="$config.feature('moments')" :to="{ name: 'moments' }" class="nav-moments" :title="isMini ? '思い出' : undefined">
              <template #prepend><v-icon>mdi-filmstrip-box</v-icon></template>
              <v-list-item-title v-if="!isMini">思い出</v-list-item-title>
            </v-list-item>

            <v-list-item v-if="$config.feature('places') && canSearchPlaces" :to="{ name: 'places' }" class="nav-places" :title="isMini ? '旅行・場所' : undefined">
              <template #prepend><v-icon>mdi-map-marker</v-icon></template>
              <v-list-item-title v-if="!isMini">旅行・場所</v-list-item-title>
            </v-list-item>

            <v-list-item v-if="$config.feature('calendar')" :to="{ name: 'calendar' }" class="nav-calendar" :title="isMini ? '月ごとの記録' : undefined">
              <template #prepend><v-icon>mdi-calendar-month</v-icon></template>
              <v-list-item-title v-if="!isMini">月ごとの記録</v-list-item-title>
            </v-list-item>

            <v-list-item v-if="$config.feature('albums')" :to="{ name: 'albums' }" class="nav-albums" :title="isMini ? 'アルバム' : undefined">
              <template #prepend><v-icon>mdi-bookmark</v-icon></template>
              <v-list-item-title v-if="!isMini">アルバム</v-list-item-title>
            </v-list-item>

            <v-list-item v-if="$config.feature('favorites')" :to="{ name: 'favorites' }" class="nav-favorites" :title="isMini ? 'お気に入り' : undefined">
              <template #prepend><v-icon>mdi-star</v-icon></template>
              <v-list-item-title v-if="!isMini">お気に入り</v-list-item-title>
            </v-list-item>

            <v-list-item
              v-if="$config.feature('people') && (canManagePeople || config.count.people > 0)"
              :to="{ name: 'people' }"
              class="nav-people"
              :title="isMini ? '人物' : undefined"
            >
              <template #prepend><v-icon>mdi-account</v-icon></template>
              <v-list-item-title v-if="!isMini">人物</v-list-item-title>
            </v-list-item>

            <v-list-item v-if="$config.feature('videos')" :to="{ name: 'media' }" class="nav-media" :title="isMini ? '動画・メディア' : undefined">
              <template #prepend><v-icon>mdi-play-circle</v-icon></template>
              <v-list-item-title v-if="!isMini">動画・メディア</v-list-item-title>
            </v-list-item>

            <v-divider class="my-2"></v-divider>

            <v-list-item
              v-if="!config.readonly && $config.feature('upload')"
              class="nav-upload"
              :title="isMini ? '写真を追加' : undefined"
              @click.prevent="openUpload"
            >
              <template #prepend><v-icon>mdi-cloud-upload</v-icon></template>
              <v-list-item-title v-if="!isMini">写真を追加</v-list-item-title>
            </v-list-item>

            <v-list-item v-if="$config.feature('library')" :to="{ name: 'library_index' }" class="nav-library" :title="isMini ? 'ライブラリ管理' : undefined">
              <template #prepend><v-icon>mdi-film</v-icon></template>
              <v-list-item-title v-if="!isMini">ライブラリ管理</v-list-item-title>
            </v-list-item>

            <v-list-item v-if="!config.disable.settings && $config.feature('settings')" :to="{ name: 'settings' }" class="nav-settings" :title="isMini ? '設定' : undefined">
              <template #prepend><v-icon>mdi-cog</v-icon></template>
              <v-list-item-title v-if="!isMini">設定</v-list-item-title>
            </v-list-item>

            <v-list-item :to="{ name: 'about' }" class="nav-about" :title="isMini ? 'このアプリについて' : undefined">
              <template #prepend><v-icon>mdi-information-outline</v-icon></template>
              <v-list-item-title v-if="!isMini">このアプリについて</v-list-item-title>
            </v-list-item>
          </v-list>

          <div v-if="disconnected" class="nav-info connection-info clickable" @click.stop="showServerConnectionHelp">
            <div class="text-center"><v-icon icon="mdi-wifi-off" color="warning" size="21"></v-icon></div>
            <div v-if="!isMini" class="text-start text-body-2">サーバーとの接続が切れています</div>
          </div>

          <div v-show="auth && !isPublic && !disconnected" class="nav-info user-info">
            <p-auth-menu @account="onAccount" @logout="onLogout">
              <div class="nav-user-avatar text-center my-1 mx-2">
                <img :src="userAvatarURL" :alt="accountInfo" class="rounded-circle" />
              </div>
              <template v-if="!isMini">
                <div class="nav-user-text text-start mt-1 flex-grow-1">
                  <p class="text-body-2">{{ displayName }}</p>
                  <p class="text-caption opacity-70">{{ accountInfo }}</p>
                </div>
                <div class="text-center"><v-btn icon="mdi-dots-vertical" variant="text"></v-btn></div>
              </template>
            </p-auth-menu>
          </div>
        </div>
      </v-navigation-drawer>
    </template>

    <div id="mobile-menu" :class="{ active: speedDial }" @click.stop="speedDial = false">
      <div class="menu-content grow-top-end">
        <div class="menu-icons">
          <a v-if="auth && !isPublic" href="#" title="ログアウト" class="menu-action navigation-logout" @click.prevent="onLogout">
            <v-icon>mdi-power</v-icon>
          </a>
          <a href="#" title="再読み込み" class="menu-action nav-reload" @click.prevent="reloadApp">
            <v-icon>mdi-refresh</v-icon>
          </a>
          <router-link v-if="auth && $config.feature('settings')" :to="{ name: 'settings' }" title="設定" class="menu-action nav-settings">
            <v-icon>mdi-cog</v-icon>
          </router-link>
          <a v-if="auth && !config.readonly && $config.feature('upload')" href="#" title="写真を追加" class="menu-action nav-upload" @click.prevent="openUpload">
            <v-icon>mdi-cloud-upload</v-icon>
          </a>
        </div>
        <div class="menu-actions">
          <div v-if="auth && $config.feature('search')" class="menu-action nav-search">
            <router-link :to="{ name: 'browse' }"><v-icon>mdi-magnify</v-icon>検索</router-link>
          </div>
          <div v-if="auth && $config.feature('moments')" class="menu-action nav-moments">
            <router-link :to="{ name: 'moments' }"><v-icon>mdi-filmstrip-box</v-icon>思い出</router-link>
          </div>
          <div v-if="auth && canSearchPlaces && $config.feature('places')" class="menu-action nav-places">
            <router-link :to="{ name: 'places' }"><v-icon>mdi-map-marker</v-icon>旅行・場所</router-link>
          </div>
          <div v-if="auth && $config.feature('calendar')" class="menu-action nav-calendar">
            <router-link :to="{ name: 'calendar' }"><v-icon>mdi-calendar-month</v-icon>月ごとの記録</router-link>
          </div>
          <div v-if="auth && $config.feature('albums')" class="menu-action nav-albums">
            <router-link :to="{ name: 'albums' }"><v-icon>mdi-bookmark</v-icon>アルバム</router-link>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { getAppStorage } from "common/storage";
import PAuthMenu from "component/auth/menu.vue";

const appStorage = getAppStorage();

export default {
  name: "PNavigation",
  components: { PAuthMenu },
  data() {
    const isPublic = this.$config.get("public");
    const isRestricted = this.$config.deny("photos", "access_library");

    return {
      canSearchPlaces: this.$config.allow("places", "search"),
      canManagePeople: this.$config.allow("people", "manage"),
      appName: this.$config.getName(),
      appIcon: this.$config.getIcon(),
      disconnected: this.$config.disconnected,
      indexing: false,
      drawer: null,
      isRestricted,
      isMini: appStorage.getItem("navigation.mode") !== "false" || isRestricted,
      isPublic,
      session: this.$session,
      config: this.$config.values,
      page: this.$config.page,
      speedDial: false,
      subscriptions: [],
    };
  },
  computed: {
    auth() {
      return this.session.auth || this.isPublic;
    },
    visible() {
      return !this.$route.meta.hideNav;
    },
    displayName() {
      return this.$session.getUser()?.getDisplayName?.() || "個人ユーザー";
    },
    userAvatarURL() {
      return this.$session.getUser()?.getAvatarURL?.("tile_50", this.$config) || this.appIcon;
    },
    accountInfo() {
      return this.$session.getUser()?.getAccountInfo?.() || "個人アカウント";
    },
  },
  created() {
    this.subscriptions.push(this.$event.subscribe("index", this.onIndex));
    this.subscriptions.push(this.$event.subscribe("import", this.onIndex));
  },
  beforeUnmount() {
    this.subscriptions.forEach((subscription) => this.$event.unsubscribe(subscription));
  },
  methods: {
    reloadApp() {
      this.$notify.info("再読み込みします…");
      this.$notify.blockUI();
      setTimeout(() => window.location.reload(), 100);
    },
    openUpload() {
      this.$event.publish("dialog.upload");
    },
    onHome(ev) {
      if (this.$vuetify.display.smAndDown) {
        this.toggleDrawer(ev);
        return;
      }
      if (this.$route.name !== "home") {
        this.$router.push({ name: "home" });
      }
    },
    showDrawer() {
      if (this.auth) {
        this.drawer = true;
        this.isMini = this.isRestricted;
      }
    },
    hideDrawer() {
      if (this.auth) {
        this.drawer = false;
        this.isMini = this.isRestricted;
      }
    },
    toggleDrawer(ev) {
      if (!ev || ev.target === undefined) {
        return;
      }
      if (this.$vuetify.display.smAndDown) {
        this.drawer ? this.hideDrawer() : this.showDrawer();
      } else {
        this.toggleIsMini();
      }
    },
    toggleIsMini() {
      if (this.isRestricted) {
        return;
      }
      this.isMini = !this.isMini;
      appStorage.setItem("navigation.mode", `${this.isMini}`);
    },
    showServerConnectionHelp() {
      this.$router.push({ path: "/help/websockets" });
    },
    onAccount() {
      this.$router.push({ name: this.$config.feature("account") ? "settings_account" : "settings" });
    },
    onLogout() {
      this.$session.logout();
    },
    onIndex(ev) {
      if (!ev) {
        return;
      }
      const type = ev.split(".")[1];
      if (["file", "folder", "indexing"].includes(type)) {
        this.indexing = true;
      } else if (type === "completed") {
        this.indexing = false;
      }
    },
  },
};
</script>
