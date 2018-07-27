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
      component: Dashboard,
      children: [{
        path: '',
        component: DashboardHome,
        name: 'dashboard'
      }]
    },
    {
      path: '',
      component: Public,
      children: [{
        path: '',
        component: PublicHome,
        name: 'home',
        props: (route) => {
          ({ page: route.query.page ? route.query.page : 1 })
        }
      }]
    }
  ]
})
