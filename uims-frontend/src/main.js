import Vue from "vue";
import "./plugins/axios";
import App from "./App.vue";
import vuetify from "./plugins/vuetify";
import router from "./router";

Vue.config.productionTip = false;

Vue.prototype.$hostname = "http://127.0.0.1:8000"

new Vue({
  vuetify,
  router,
  render: h => h(App)
}).$mount("#app");
