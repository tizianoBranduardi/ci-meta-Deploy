import axios from 'axios';
import { BootstrapVue, BootstrapVueIcons, IconsPlugin } from 'bootstrap-vue';
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap-vue/dist/bootstrap-vue.css';
import Vue from 'vue';
import App from './App.vue';
import router from './router';
import '@/assets/styles.css';
import store from '@/store/index';
import VueSingleSelect from "vue-single-select";

Vue.component('vue-single-select', VueSingleSelect);
Vue.prototype.$http = axios;
Vue.config.productionTip = false;
Vue.use(BootstrapVue);
Vue.use(BootstrapVueIcons);
Vue.use(IconsPlugin);

new Vue({
  store,
  axios,
  router,
  render: (h) => h(App),
}).$mount('#app');
