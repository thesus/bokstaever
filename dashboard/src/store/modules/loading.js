import Vue from 'vue'

const state = {
  indicators: {
    'default': false
  }
}

const getters = {
  isLoading: state => (name = 'default') => {
    return (typeof (state.indicators[name]) === 'boolean') ? state.indicators['default'] : false
  }
}

const actions = {
  loading ({ commit }, name = 'default') {
    commit('loading', { name: name })
  },
  finished ({ commit }, name = 'default') {
    commit('finished', { name: name })
  }
}

const mutations = {
  loading (state, { name }) {
    Vue.set(state.indicators, name, true)
  },
  finished (state, { name }) {
    Vue.set(state.indicators, name, false)
  }
}

export default {
  state,
  getters,
  actions,
  mutations
}
