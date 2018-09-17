import Vue from 'vue'

const state = {
  indicators: {
    'default': {
      finished: false,
      success: null
    }
  }
}

const getters = {
  isLoading: state => (name = 'default') => {
    let exists = ((state.indicators[name] !== undefined) && (typeof (state.indicators[name]['finished']) === 'boolean'))
    return exists ? !state.indicators[name]['finished'] : false
  },
  isSucceded: state => (name = 'default') => {
    let exists = ((state.indicators[name]) && (typeof (state.indicators[name]['success']) === 'boolean'))
    return exists ? state.indicators[name]['success'] : false
  }
}

const actions = {
  loading ({ commit }, name = 'default') {
    commit('loading', { name: name })
  },
  success ({ commit }, name = 'default') {
    commit('success', { name: name })
  },
  failure ({ commit }, name = 'default') {
    commit('failed', { name: name })
  }
}

const mutations = {
  loading (state, { name }) {
    Vue.set(state.indicators, name, { finished: false, success: null })
  },
  success (state, { name }) {
    Vue.set(state.indicators, name, { finished: true, success: true })
  },
  failed (state, { name }) {
    Vue.set(state.indicators, name, { finished: true, success: false })
  }
}

export default {
  state,
  getters,
  actions,
  mutations
}
