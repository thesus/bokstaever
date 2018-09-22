import Vue from 'vue'
import router from '@/router'

import { propExists } from '@/utils'

const state = {
  jwt: null,
  payload: null,
  isLoggedIn: false
}

const getters = {
  username: state => state.payload ? state.payload.username : null,
  isLoggedIn: state => state.isLoggedIn,
  jwt: state => state.jwt
}

const actions = {
  async login ({ commit, state }, { username, password }) {
    try {
      const response = await Vue.axios({
        method: 'post',
        url: `/api/auth/jwt/create/`,
        data: {
          username: username,
          password: password
        }
      })
      // JWT consists of a header and a payload part. They're separated by a dot.
      let encodedPayload = response.data.token.split('.')[1]
      commit(
        'login',
        {
          jwt: response.data.token,
          payload: JSON.parse(
            atob(encodedPayload)
          )
        }
      )
    } catch (error) {
      // If there's a proper response with serialization / login errors
      // show them. Otherwise show an unknown error!
      if (propExists(error, 'response.data.non_field_errors')) {
        let errors = error.response.data.non_field_errors
        for (let error of errors) {
          Vue.notify({
            type: 'danger',
            title: 'Login failed',
            text: error,
            timeout: 5000
          })
        }
      } else {
        Vue.notify({
          type: 'danger',
          title: 'Login failed!',
          text: 'Unknown error occurred!',
          timeout: 5000
        })
      }
    }
  },
  logout ({ commit, state }) {
    if (this.getters.isLoggedIn) {
      commit('logout')
    }
  }
}

const mutations = {
  login (state, { jwt, payload }) {
    state.jwt = jwt
    state.payload = payload
    state.isLoggedIn = true

    router.push({ 'path': router.currentRoute.query.next || '/' })
  },
  logout (state) {
    state.jwt = null
    state.payload = null
    state.isLoggedIn = false
  }
}

export default {
  state,
  getters,
  actions,
  mutations
}
