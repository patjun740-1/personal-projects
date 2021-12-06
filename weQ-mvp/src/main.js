import Vue from 'vue'
import App from './App.vue' 
import router from './router'
import {BootstrapVue, IconsPlugin} from 'bootstrap-vue'


require('./assets/main.css')
Vue.config.productionTip = false

Vue.use(BootstrapVue)
Vue.use(IconsPlugin)  


import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import vuetify from './plugins/vuetify'

new Vue({
  router,
  vuetify,
  render: function (h) { return h(App) }, 
  


}).$mount('#app')
