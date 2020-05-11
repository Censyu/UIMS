<template>
  <v-app>
    <v-navigation-drawer :mini-variant.sync="mini" app>
      <v-list-item class="px-2">
        <v-btn icon @click.stop="mini = !mini">
          <v-icon>mdi-menu</v-icon>
        </v-btn>
        <v-list-item-title class="title ml-5">UIMS</v-list-item-title>
      </v-list-item>

      <v-divider></v-divider>

      <v-list shaped dense>
        <v-list-item-group v-model="item" color="primary">
          <v-list-item
            v-for="item in nav_drawer_items"
            :key="item.title"
            :color="item.color"
            link
          >
            <v-list-item-icon>
              <v-icon>{{ item.icon }}</v-icon>
            </v-list-item-icon>

            <v-list-item-content>
              <v-list-item-title>{{ item.title }}</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list-item-group>
      </v-list>
    </v-navigation-drawer>

    <v-content>
      <Uims-Table />
    </v-content>
  </v-app>
</template>

<script>
import UimsTable from "./components/UimsTable";

export default {
  name: "App",

  components: {
    UimsTable
  },

  data: () => ({
    nav_drawer_items: [
      {
        title: "校区",
        icon: "mdi-map",
        color: "#0088ff"
      },
      {
        title: "专业",
        icon: "mdi-table",
        color: "#0088ff"
      },
      {
        title: "教师",
        icon: "mdi-account",
        color: "#0088ff"
      },
      {
        title: "学生",
        icon: "mdi-account-group",
        color: "#0088ff"
      }
    ],
    mini: false
  }),

  computed: {
    formTitle() {
      return this.editedIndex === -1 ? "New Item" : "Edit Item";
    }
  }
};
</script>
