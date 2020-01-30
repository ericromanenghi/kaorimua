import Vue from 'vue'
import VueRouter from 'vue-router'
import axios from 'axios'
import App from './App.vue'
import { routes } from './components/routes'

import './scss/global.scss'

Vue.config.productionTip = false
Vue.use(VueRouter)

Vue.prototype.$http = axios

const router = new VueRouter({
  mode: 'history',
  linkActiveClass: 'navigation__item--active',
  routes
})

new Vue({
  render: h => h(App),
  router
}).$mount('#app')
