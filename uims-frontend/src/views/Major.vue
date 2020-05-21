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
                <v-col cols="12" sm="6" md="4">
                  <v-text-field
                    v-model="editedItem.code"
                    label="专业代码"
                    :rules="[() => !!editedItem.code || '该项不能为空']"
                    :disabled="editedIndex > -1"
                  ></v-text-field>
                </v-col>
                <v-col cols="12" sm="6" md="4">
                  <v-text-field
                    v-model="editedItem.name"
                    label="专业名称"
                    :rules="[() => !!editedItem.name || '该项不能为空']"
                  ></v-text-field>
                </v-col>
                <v-col cols="12" sm="6" md="4">
                  <v-text-field
                    v-model="editedItem.address"
                    label="专业地址"
                    :rules="[() => !!editedItem.address || '该项不能为空']"
                  ></v-text-field>
                </v-col>
                <v-col cols="12" sm="6" md="4">
                  <v-text-field
                    v-model="editedItem.campus_code"
                    label="校区代码"
                    :rules="[() => !!editedItem.campus_code || '该项不能为空']"
                  ></v-text-field>
                </v-col>
                <v-col cols="12" sm="6" md="4">
                  <v-text-field
                    v-model="editedItem.director_id"
                    label="负责人工号"
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
    <h3 v-if="contents.items.length === 0" class="mt-5">这里还没有信息...</h3>
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
import axios from "axios";

export default {
  name: "Campus",
  data() {
    return {
      search: "",
      dialog: false,
      editedIndex: -1,
      editedItem: {
        code: "",
        name: "",
        address: "",
        campus_code: "",
        director_id: ""
      },
      defaultItem: {
        code: "",
        name: "",
        address: "",
        campus_code: "",
        director_id: ""
      },
      contents: {
        id: "major",
        title: "专业",
        headers: [
          {
            text: "专业代码",
            align: "start",
            sortable: true,
            value: "code"
          },
          {
            text: "专业名称",
            value: "name"
          },
          {
            text: "专业地址",
            value: "address"
          },
          {
            text: "校区代码",
            value: "campus_code"
          },
          {
            text: "负责人工号",
            value: "director_id"
          },
          {
            text: "操作",
            value: "actions",
            sortable: false
          }
        ],
        items: []
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
  mounted() {
    axios
      .get(this.url)
      .then(response => {
        this.contents.items = response.data;
      })
      .catch(error => {
        console.log(error);
      });
  },
  methods: {
    editItem(item) {
      this.editedIndex = this.contents.items.indexOf(item);
      this.editedItem = Object.assign({}, item);
      this.dialog = true;
    },

    deleteItem(item) {
      const index = this.contents.items.indexOf(item);
      if (confirm("确定要删除该项吗?")) {
        axios
          .delete(this.url + item.code + "/")
          .then(() => {
            this.contents.items.splice(index, 1);
          })
          .catch(error => {
            alert("出现错误：\n\n" + JSON.stringify(error.response.data));
          });
      }
    },

    close() {
      this.dialog = false;
      this.$nextTick(() => {
        this.editedItem = Object.assign({}, this.defaultItem);
        this.editedIndex = -1;
      });
    },

    save() {
      const index = this.editedIndex;

      if (this.editedIndex > -1) {
        axios
          .put(
            this.url + this.contents.items[this.editedIndex].code + "/",
            this.editedItem
          )
          .then(response => {
            Object.assign(this.contents.items[index], response.data);
          })
          .catch(error => {
            alert("出现错误：\n\n" + JSON.stringify(error.response.data));
          });
      } else {
        axios
          .post(this.url, this.editedItem)
          .then(response => {
            this.contents.items.push(response.data);
          })
          .catch(error => {
            alert("出现错误：\n\n" + JSON.stringify(error.response.data));
          });
      }
      this.close();
    }
  },
  computed: {
    url: function() {
      return this.$hostname + "/api/" + this.contents.id + "/";
    }
  }
};
</script>

<style></style>
