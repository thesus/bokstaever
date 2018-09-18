import Vue from 'vue'
import Vuex from 'vuex'

import createLogger from 'vuex/dist/logger'

import createPersistedState from 'vuex-persistedstate'

import authentication from './modules/authentication'

Vue.use(Vuex)

const debug = process.env.NODE_ENV !== 'production'

let plugins = [createPersistedState()]

if (debug) {
  plugins.push(createLogger())
}

export default new Vuex.Store({
  modules: {
    authentication
  },
  strict: debug,
  plugins: plugins
})
