import Vue from 'vue'
import App from './App.vue'
import router from './router'

import axios from 'axios'
import VueAxios from 'vue-axios'

import ApiPlugin from '@/utils/Api.js'


Vue.use(ApiPlugin)
Vue.use(VueAxios, axios)

Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')

Vue.axios.interceptors.response.use (
  (response) => {
    return response
  },
  (error) => {
    if (error && error.response && error.response.status === 401) {
      router.push('logout')
    } else {
      return response
    }
  }
)
