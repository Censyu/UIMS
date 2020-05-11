<template>
  <v-container :id="contents.id" class="pa-10">
    <v-row align="end">
      <h1>{{ contents.title }}</h1>
      <v-spacer></v-spacer>
      <!-- dialog -->
      <v-dialog v-model="dialog" max-width="500px">
        <template v-slot:activator="{ on }">
          <v-btn color="primary" dark class="mb-2" v-on="on">New Item</v-btn>
        </template>
        <v-card class="pa-2">
          <v-card-title>
            <span class="headline">{{ contents.title }}</span>
          </v-card-title>

          <v-card-text>
            <v-container>
              <v-row>
                <!-- FIXME: using v-for -->
                <!-- <v-col
                  v-for="(header, i) in contents.headers"
                  :key="i"
                  cols="12"
                  sm="6"
                  md="4"
                >
                  <v-text-field v-model="editedItem.id" :label="header.text"></v-text-field>
                </v-col> -->
                <v-col cols="12" sm="6" md="4">
                  <v-text-field
                    v-model="editedItem.id"
                    label="ID"
                  ></v-text-field>
                </v-col>
                <v-col cols="12" sm="6" md="4">
                  <v-text-field
                    v-model="editedItem.name"
                    label="Name"
                  ></v-text-field>
                </v-col>
                <v-col cols="12" sm="6" md="4">
                  <v-text-field
                    v-model="editedItem.gender"
                    label="Gender"
                  ></v-text-field>
                </v-col>
              </v-row>
            </v-container>
          </v-card-text>

          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="blue darken-1" text @click="save">Save</v-btn>
            <v-btn color="blue darken-1" text @click="close">Cancel</v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
    </v-row>

    <!-- search -->
    <v-text-field
      v-model="search"
      append-icon="mdi-magnify"
      label="请输入查询关键字"
      single-line
      hide-details
    ></v-text-field>

    <!-- data table -->
    <p v-if="contents.items.length === 0">There is no item.</p>
    <v-data-table
      v-else
      :headers="contents.headers"
      :items="contents.items"
      :search="search"
    >
      <template v-slot:item.actions="{ item }">
        <v-icon small class="mr-2" @click="editItem(item)">mdi-pencil</v-icon>
        <v-icon small @click="deleteItem(item)">mdi-delete</v-icon>
      </template>
    </v-data-table>
  </v-container>
</template>

<script>
export default {
  name: "UimsTable",
  data() {
    return {
      search: "",
      dialog: false,
      editedIndex: -1,
      editedItem: {
        id: "",
        name: "",
        gender: ""
      },
      defaultItem: {
        id: "PB",
        name: "NULL",
        gender: "NULL"
      },
      contents: {
        id: "students",
        title: "学生",
        headers: [
          {
            text: "ID",
            align: "start",
            sortable: true,
            value: "id"
          },
          {
            text: "Name",
            value: "name"
          },
          {
            text: "Gender",
            value: "gender"
          },
          {
            text: "Actions",
            value: "actions",
            sortable: false
          }
        ],
        items: [
          {
            id: "PB17000000",
            name: "同学A",
            gender: "男"
          },
          {
            id: "PB17000003",
            name: "同学B",
            gender: "女"
          },
          {
            id: "PB17000010",
            name: "同学C",
            gender: "男"
          },
          {
            id: "PB17000002",
            name: "同学D",
            gender: "女"
          },
          {
            id: "PB17000009",
            name: "同学E",
            gender: "男"
          },
          {
            id: "PB17000018",
            name: "同学F",
            gender: "男"
          },
          {
            id: "PB17000018",
            name: "Test",
            gender: "男"
          }
        ]
      }
    };
  },
  props: {
    // contents: Object
  },
  watch: {
    dialog(val) {
      val || this.close();
    }
  },
  methods: {
    editItem(item) {
      this.editedIndex = this.contents.items.indexOf(item);
      this.editedItem = Object.assign({}, item);
      this.dialog = true;
    },

    deleteItem(item) {
      const index = this.contents.items.indexOf(item);
      confirm("Are you sure you want to delete this item?") &&
        this.contents.items.splice(index, 1);
    },

    close() {
      this.dialog = false;
      this.$nextTick(() => {
        this.editedItem = Object.assign({}, this.defaultItem);
        this.editedIndex = -1;
      });
    },

    save() {
      if (this.editedIndex > -1) {
        Object.assign(this.contents.items[this.editedIndex], this.editedItem);
      } else {
        this.contents.items.push(this.editedItem);
      }
      this.close();
    }
  }
};
</script>

<style></style>
