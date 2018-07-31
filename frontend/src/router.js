import Vue from 'vue'
import VueRouter from 'vue-router'

import Dashboard from './views/dashboard/Dashboard'
import DashboardHome from './views/dashboard/Home'
import PostList from './views/dashboard/PostList'
import PostEdit from './views/dashboard/PostEdit'

import ImageList from './views/dashboard/ImageList'
import ImageUpload from './views/dashboard/ImageUpload'

import SettingsEdit from './views/dashboard/SettingsEdit'

import Public from './views/public/Public'
import PublicHome from './views/public/Home'
import PublicPost from './views/public/Post'
import PublicPage from './views/public/Page'

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
      path: '/dashboard',
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
        },
        {
          name: 'page',
          path: ':slug',
          component: PublicPage
        }
      ]
    }
  ],
  scrollBehavior (to, from, savedPosition) {
    return { x: 0, y: 0}
  }
})

export default router
