import Vue from 'vue'
import VueRouter from 'vue-router'

import Dashboard from './views/dashboard/Dashboard'
import DashboardHome from './views/dashboard/Home'

import Public from './views/public/Public'
import PublicHome from './views/public/Home'
import PublicPost from './views/public/Post'

import Login from './views/auth/Login'

Vue.use(VueRouter)

let loginRequired = (to, from, next) => {
  if (!localStorage.getItem('jwt_token')) {
    next({
      name: 'login',
      query: {
        next: to.path
      }
    })
  } else {
    next()
  }
}

let loggedIn = (to, from, next) => {
  if (localStorage.getItem('jwt_token')) {
    next({ name: 'dashboard' })
  }  else {
    next()
  }
}

const router = new VueRouter({
  routes: [
    {
      path: '/dashboard',
      component: Dashboard,
      children: [{
        path: '',
        name: 'dashboard',
        component: DashboardHome,
        beforeEnter: loginRequired
      }],
    },
    {
      path: '/login',
      name: 'login',
      component: Login,
      beforeEnter: loggedIn
    },
    {
      path: '',
      component: Public,
      children: [
        {
          path: '',
          name: 'home',
          component: PublicHome,
          props: (route) => {
            ({ page: route.query.page ? route.query.page : 1 })
          }
        },
        {
          name: 'detail',
          path: '/post/:id/:slug',
          component: PublicPost,
        }
      ]
    }
  ],
  scrollBehavior (to, from, savedPosition) {
    return { x: 0, y: 0}
  }
})

export default router
