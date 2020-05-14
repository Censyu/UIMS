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
                    v-model="editedItem.id"
                    label="异动编号"
                  ></v-text-field>
                </v-col>
                <v-col cols="12" sm="6" md="4">
                  <v-text-field
                    v-model="editedItem.date"
                    label="异动日期"
                  ></v-text-field>
                </v-col>
                <v-col cols="12" sm="6" md="4">
                  <v-text-field
                    v-model="editedItem.downgrade_reason"
                    label="降级原因"
                  ></v-text-field>
                </v-col>
                <v-col cols="12" sm="6" md="4">
                  <v-text-field
                    v-model="editedItem.membership_transfer"
                    label="是否转出团关系"
                  ></v-text-field>
                </v-col>
                <v-col cols="12" sm="6" md="4">
                  <v-text-field
                    v-model="editedItem.student_id"
                    label="学生学号"
                  ></v-text-field>
                </v-col>
                <v-col cols="12" sm="6" md="4">
                  <v-text-field
                    v-model="editedItem.origin_class_code"
                    label="原班级编号"
                  ></v-text-field>
                </v-col>
                <v-col cols="12" sm="6" md="4">
                  <v-text-field
                    v-model="editedItem.new_class_code"
                    label="现班级编号"
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
  name: "StudentStatusChange",
  data() {
    return {
      search: "",
      dialog: false,
      editedIndex: -1,
      editedItem: {
        id: "",
        date: "",
        downgrade_reason: "",
        membership_transfer: "",
        student_id: "",
        origin_class_code: "",
        new_class_code: ""
      },
      defaultItem: {
        id: "",
        date: "",
        downgrade_reason: "",
        membership_transfer: "",
        student_id: "",
        origin_class_code: "",
        new_class_code: ""
      },
      contents: {
        id: "student-status-change",
        title: "学籍异动",
        headers: [
          {
            text: "异动编号",
            value: "id"
          },
          {
            text: "异动日期",
            value: "date"
          },
          {
            text: "降级原因",
            value: "downgrade_reason"
          },
          {
            text: "是否转出团关系",
            value: "membership_transfer"
          },
          {
            text: "学生学号",
            value: "student_id"
          },
          {
            text: "原班级编号",
            value: "origin_class_code"
          },
          {
            text: "现班级编号",
            value: "new_class_code"
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
          .delete(this.url + item.id + "/")
          .then(() => {
            this.contents.items.splice(index, 1);
          })
          .catch(error => {
            alert("出现错误：\n" + error.message);
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
            this.url + this.contents.items[this.editedIndex].id + "/",
            this.editedItem
          )
          .then(response => {
            Object.assign(this.contents.items[index], response.data);
          })
          .catch(error => {
            alert("出现错误：\n" + error.message);
          });
      } else {
        axios
          .post(this.url, this.editedItem)
          .then(response => {
            this.contents.items.push(response.data);
          })
          .catch(error => {
            alert("出现错误：\n" + error.message);
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
