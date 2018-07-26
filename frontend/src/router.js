import Vue from 'vue'
import VueRouter from 'vue-router'

import Dashboard from './views/dashboard/Dashboard.vue'
import DashboardHome from './views/dashboard/Home.vue'

import Public from './views/public/Public.vue'
import PublicHome from './views/public/Home.vue'

Vue.use(VueRouter)

export default new VueRouter({
  routes: [
    {
      path: '/dashboard',
      name: 'dashboard',
      component: Dashboard,
      children: [{
        path: '',
        component: DashboardHome
      }]
    },
    {
      path: '',
      name: 'public',
      component: Public,
      children: [{
        path: '',
        component: PublicHome
      }]
    }
  ]
})
