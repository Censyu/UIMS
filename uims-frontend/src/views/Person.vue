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
                    label="身份证号"
                    :rules="[() => !!editedItem.id || '该项不能为空']"
                    :disabled="editedIndex > -1"
                  ></v-text-field>
                </v-col>
                <v-col cols="12" sm="6" md="4">
                  <v-text-field
                    v-model="editedItem.chinese_name"
                    label="中文名"
                    :rules="[() => !!editedItem.chinese_name || '该项不能为空']"
                  ></v-text-field>
                </v-col>
                <!-- <v-col cols="12" sm="6" md="4">
                  <v-text-field
                    v-model="editedItem.birth_date"
                    label="出生日期"
                  ></v-text-field>
                </v-col> -->

                <v-col cols="12" sm="6" md="4">
                  <v-menu
                    v-model="menu"
                    :close-on-content-click="false"
                    :nudge-right="40"
                    transition="scale-transition"
                    offset-y
                    min-width="290px"
                  >
                    <template v-slot:activator="{ on }">
                      <v-text-field
                        v-model="editedItem.birth_date"
                        label="出生日期"
                        readonly
                        v-on="on"
                        :rules="[
                          () => !!editedItem.birth_date || '该项不能为空'
                        ]"
                      ></v-text-field>
                    </template>
                    <v-date-picker
                      v-model="editedItem.birth_date"
                      @input="menu = false"
                    ></v-date-picker>
                  </v-menu>
                </v-col>

                <!-- <v-col cols="12" sm="6" md="4">
                  <v-text-field
                    v-model="editedItem.id_type"
                    label="身份证件类型"
                  ></v-text-field>
                </v-col> -->

                <v-col cols="12" sm="6" md="4">
                  <v-select
                    v-model="editedItem.id_type"
                    :items="['ID_Card', 'Passport']"
                    label="证件类型"
                    :rules="[() => !!editedItem.id_type || '该项不能为空']"
                  ></v-select>
                </v-col>

                <!-- <v-col cols="12" sm="6" md="4">
                  <v-text-field
                    v-model="editedItem.gender"
                    label="性别"
                  ></v-text-field>
                </v-col> -->

                <v-col cols="12" sm="6" md="4">
                  <v-select
                    v-model="editedItem.gender"
                    :items="['Male', 'Female']"
                    label="性别"
                    :rules="[() => !!editedItem.gender || '该项不能为空']"
                  ></v-select>
                </v-col>

                <v-col cols="12" sm="6" md="4">
                  <v-text-field
                    v-model="editedItem.country"
                    label="国籍"
                    :rules="[() => !!editedItem.country || '该项不能为空']"
                  ></v-text-field>
                </v-col>
                <v-col cols="12" sm="6" md="4">
                  <v-text-field
                    v-model="editedItem.email"
                    label="电子邮箱"
                    :rules="[() => !!editedItem.email || '该项不能为空']"
                  ></v-text-field>
                </v-col>
                <v-col cols="12" sm="6" md="4">
                  <v-text-field
                    v-model="editedItem.home_address"
                    label="家庭住址"
                  ></v-text-field>
                </v-col>
                <v-col cols="12" sm="6" md="4">
                  <v-text-field
                    v-model="editedItem.home_zipcode"
                    label="家庭邮政编码"
                  ></v-text-field>
                </v-col>
                <v-col cols="12" sm="6" md="4">
                  <v-text-field
                    v-model="editedItem.home_phone_num"
                    label="家庭电话"
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
  name: "Person",
  data() {
    return {
      search: "",
      menu: false,
      dialog: false,
      editedIndex: -1,
      editedItem: {
        id: "",
        chinese_name: "",
        birth_date: "",
        id_type: "",
        gender: "",
        country: "",
        email: "",
        home_address: "",
        home_zipcode: "",
        home_phone_num: ""
      },
      defaultItem: {
        id: "",
        chinese_name: "",
        birth_date: "",
        id_type: "",
        gender: "",
        country: "",
        email: "",
        home_address: "",
        home_zipcode: "",
        home_phone_num: ""
      },
      contents: {
        id: "person",
        title: "人员",
        headers: [
          {
            text: "身份证号",
            value: "id"
          },
          {
            text: "中文名",
            value: "chinese_name"
          },
          {
            text: "出生日期",
            value: "birth_date"
          },
          {
            text: "身份证件类型",
            value: "id_type"
          },
          {
            text: "性别",
            value: "gender"
          },
          {
            text: "国籍",
            value: "country"
          },
          {
            text: "电子邮箱",
            value: "email"
          },
          {
            text: "家庭住址",
            value: "home_address"
          },
          {
            text: "家庭邮政编码",
            value: "home_zipcode"
          },
          {
            text: "家庭电话",
            value: "home_phone_num"
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
            this.url + this.contents.items[this.editedIndex].id + "/",
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
