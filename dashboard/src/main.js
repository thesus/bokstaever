import Vue from 'vue'

import router from './router'
import store from './store'

import axios from 'axios'
import VueAxios from 'vue-axios'

import NotifyPlugin from '@/plugins/Notify.js'

import App from './App.vue'

Vue.use(NotifyPlugin)

// Axios http library
Vue.use(VueAxios, axios)

Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')

// If the status code of a http request is 401 or 403 (unauthenticated), redirect
// to the logout side. If other errors are catched, reject them with a Promise
Vue.axios.interceptors.response.use(
  (response) => {
    return response
  },
  (error) => {
    if (error &&
        error.response &&
        (error.response.status === 401 || error.response.status === 403)
    ) {
      router.push('/logout')
    } else {
      return Promise.reject(error)
    }
  }
)
