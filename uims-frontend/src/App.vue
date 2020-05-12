<template>
  <v-app>
    <v-app-bar dense flat clipped-left app>
      <v-btn
        icon
        @click.stop="
          mini = drawer ? !mini : false;
          drawer = drawer ? true : !drawer;
        "
      >
        <v-icon>mdi-menu</v-icon>
      </v-btn>
      <v-toolbar-title style="width: 300px" class="ml-0 pl-4">
        <span>UIMS</span>
      </v-toolbar-title>
    </v-app-bar>

    <v-navigation-drawer v-model="drawer" :mini-variant.sync="mini" clipped app>
      <v-list dense>
        <v-list-item-group v-model="item">
          <router-link
            v-for="(item, i) in nav_drawer_items"
            :key="i"
            :to="item.to"
          >
            <v-list-item :color="item.color" link>
              <v-list-item-icon>
                <v-icon>{{ item.icon }}</v-icon>
              </v-list-item-icon>

              <v-list-item-content>
                <v-list-item-title>{{ item.title }}</v-list-item-title>
              </v-list-item-content>
            </v-list-item>
          </router-link>
        </v-list-item-group>
      </v-list>
    </v-navigation-drawer>

    <v-content>
      <router-view />
    </v-content>
  </v-app>
</template>

<script>
export default {
  name: "App",

  components: {},

  data: () => ({
    nav_drawer_items: [
      {
        title: "校区",
        to: "/campus",
        icon: "mdi-map",
        color: "#0088ff"
      },
      {
        title: "专业",
        to: "/major",
        icon: "mdi-table",
        color: "#0088ff"
      },
      {
        title: "人员",
        to: "/person",
        icon: "mdi-account",
        color: "#0088ff"
      },
      {
        title: "教师",
        to: "/teacher",
        icon: "mdi-account",
        color: "#0088ff"
      },
      {
        title: "学生",
        to: "/student",
        icon: "mdi-account-group",
        color: "#0088ff"
      },
      {
        title: "学籍异动",
        to: "/student_status_change",
        icon: "mdi-table",
        color: "#0088ff"
      },
      {
        title: "班级",
        to: "/class",
        icon: "mdi-table",
        color: "#0088ff"
      },
      {
        title: "课程",
        to: "/course",
        icon: "mdi-table",
        color: "#0088ff"
      },
      {
        title: "开课信息",
        to: "/course_info",
        icon: "mdi-table",
        color: "#0088ff"
      },
      {
        title: "学生选课",
        to: "/course_selection",
        icon: "mdi-table",
        color: "#0088ff"
      }
    ],
    drawer: true,
    mini: false
  }),

  computed: {
    // formTitle() {
    //   return this.editedIndex === -1 ? "New Item" : "Edit Item";
    // }
  }
};
</script>

<style>
a {
  text-decoration: none;
}
</style>
