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
                    label="课程编号"
                  ></v-text-field>
                </v-col>
                <v-col cols="12" sm="6" md="4">
                  <v-text-field
                    v-model="editedItem.year"
                    label="开课年份"
                  ></v-text-field>
                </v-col>
                <!-- <v-col cols="12" sm="6" md="4">
                  <v-text-field
                    v-model="editedItem.semester"
                    label="开课学期"
                  ></v-text-field>
                </v-col> -->

                <v-col cols="12" sm="6" md="4">
                  <v-select
                    v-model="editedItem.semester"
                    :items="['Spring', 'Autumn']"
                    label="开课学期"
                  ></v-select>
                </v-col>

                <v-col cols="12" sm="6" md="4">
                  <v-text-field
                    v-model="editedItem.time"
                    label="开课时间"
                  ></v-text-field>
                </v-col>
                <v-col cols="12" sm="6" md="4">
                  <v-text-field
                    v-model="editedItem.teacher_work_id"
                    label="开课教师工号"
                  ></v-text-field>
                </v-col>
                <v-col cols="12" sm="6" md="4">
                  <v-text-field
                    v-model="editedItem.course_id"
                    label="课程编号"
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
  name: "CourseInfo",
  data() {
    return {
      search: "",
      dialog: false,
      editedIndex: -1,
      editedItem: {
        id: "",
        year: "",
        semester: "",
        time: "",
        teacher_work_id: "",
        course_id: ""
      },
      defaultItem: {
        id: "",
        year: "",
        semester: "",
        time: "",
        teacher_work_id: "",
        course_id: ""
      },
      contents: {
        id: "course-info",
        title: "开课信息",
        headers: [
          {
            text: "开课信息编号",
            value: "id"
          },
          {
            text: "开课年份",
            value: "year"
          },
          {
            text: "开课学期",
            value: "semester"
          },
          {
            text: "开课时间",
            value: "time"
          },
          {
            text: "开课教师工号",
            value: "teacher_work_id"
          },
          {
            text: "课程编号",
            value: "course_id"
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
