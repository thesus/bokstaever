import Vue from 'vue'
import VueRouter from 'vue-router'

import Dashboard from './views/dashboard/Dashboard'
import DashboardHome from './views/dashboard/Home'
import PostList from './views/dashboard/PostList'
import PostEdit from './views/dashboard/PostEdit'
import PageList from './views/dashboard/PageList'
import PageEdit from './views/dashboard/PageEdit'

import ImageList from './views/dashboard/ImageList'
import ImageUpload from './views/dashboard/ImageUpload'

import SettingsEdit from './views/dashboard/SettingsEdit'

import Login from './views/auth/Login'
import Logout from './views/auth/Logout'

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
      path: '',
      component: Dashboard,
      children: [
        {
          path: '',
          name: 'dashboard',
          component: DashboardHome,
          beforeEnter: loginRequired
        },
        {
          path: 'posts/list',
          name: 'post-list',
          component: PostList,
          beforeEnter: loginRequired
        },
        {
          path: 'posts/edit/',
          name: 'post-create',
          component: PostEdit,
          beforeEnter: loginRequired
        },
        {
          path: 'posts/edit/:id',
          name: 'post-edit',
          component: PostEdit,
          beforeEnter: loginRequired
        },
        {
          path: 'pages/list',
          name: 'page-list',
          component: PageList,
          beforeEnter: loginRequired
        },
        {
          path: 'pages/edit',
          name: 'page-create',
          component: PageEdit,
          beforeEnter: loginRequired
        },
        {
          path: 'pages/edit/:slug',
          name: 'page-edit',
          component: PageEdit,
          beforeEnter: loginRequired
        },
        {
          path: 'images/list',
          name: 'image-list',
          component: ImageList,
          beforeEnter: loginRequired
        },
        {
          path: 'image/upload',
          name: 'image-upload',
          component: ImageUpload,
          beforeEnter: loginRequired
        },
        {
          path: 'settings/',
          name: 'settings-edit',
          component: SettingsEdit,
          beforeEnter: loginRequired
        },
      ],
    },
    {
      path: '/login',
      name: 'login',
      component: Login,
      beforeEnter: loggedIn
    },
    {
      path: '/logout',
      name: 'logout',
      component: Logout,
    },
  ],
  scrollBehavior (to, from, savedPosition) {
    return { x: 0, y: 0}
  }
})

export default router
