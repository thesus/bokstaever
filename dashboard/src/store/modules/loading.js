import Vue from 'vue'

const initialState = () => {
  return {
    indicators: {
      'default': {
        finished: false,
        success: null
      }
    },
    progress: {
      'default': 0
    }
  }
}

const state = initialState()

const getters = {
  isLoading: state => (name = 'default') => {
    let exists = ((state.indicators[name] !== undefined) && (typeof (state.indicators[name]['finished']) === 'boolean'))
    return exists ? !state.indicators[name]['finished'] : false
  },
  isSucceded: state => (name = 'default') => {
    let exists = ((state.indicators[name]) && (typeof (state.indicators[name]['success']) === 'boolean'))
    return exists ? state.indicators[name]['success'] : false
  },
  requestExists: state => (name = 'default') => {
    return (typeof (state.indicators[name]) === 'object')
  },
  getProgress: state => (name = 'default') => {
    return (state.progress[name]) ? state.progress[name] : 0
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
  },
  setProgress ({ commit }, { value, name }) {
    commit('progress', { value, name })
  },
  reset ({ commit }) {
    commit('reset')
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
  },
  progress (state, { value, name }) {
    Vue.set(state.progress, name, value)
  },
  reset (state) {
    const s = initialState()
    Object.keys(s).forEach(key => {
      state[key] = s[key]
    })
  }
}

export default {
  state,
  getters,
  actions,
  mutations
}
