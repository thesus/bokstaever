import axios from 'axios'
import store from '@/store'

const propExists = (obj, path) => {
  return !!path.split('.').reduce((obj, prop) => {
    return obj && obj[prop] ? obj[prop] : undefined
  }, obj)
}

const run = async (func) => {
  let loadingTimer = setTimeout(() => {
    store.dispatch('loading')
  }, 200)

  let result = await func()

  clearTimeout(loadingTimer)
  store.dispatch('finished')

  return result
}

class Request {
  constructor () {
    this.url = '/api'
    this.config = {}
  }

  authenticate () {
    this.config['headers'] += { 'Authorization': 'JWT ' + store.getters.jwt }
  }

  async list (model, limit, page) {
    let offset = limit * (page - 1)

    this['url'] += `/${model}/?limit=${limit}&offset=${offset}`
    this['config']['method'] = 'get'

    let response = await axios(
      this.url,
      this.config
    )

    let count = response.data.count || 0
    let pages = Math.ceil(count / limit)

    return {
      count: count,
      pages: pages,
      results: response.data.results
    }
  }

  execute () {
    return axios(
      this.url,
      this.config
    )
  }
}

export {
  propExists,
  run,
  Request
}
