import axios from 'axios'
import store from '@/store'

const propExists = (obj, path) => {
  /**
   * Checks if a nested Property exists
   * @param {object} [obj] - The object to check on
   * @param {string} [path] - Path to check. e.g. "results.users.count"
   * @returns {boolean}
  */
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
  constructor (loading = 'default') {
    this.config = {
      url: '/api',
      headers: {}
    }
    this.loading = loading

    // If loading is set to true, start a timer to run a mutation
    // for a loading indicator in 200 ms.
    if (loading) {
      this.timer = setTimeout(() => {
        store.dispatch('loading', this.loading)
      }, 200)
    }

    this.authenticate()
  }

  authenticate () {
    /**
     * Add JSON Web Token as a Authorization header to the request.
    */

    this.config['headers']['Authorization'] = 'JWT ' + store.getters.jwt
  }

  resolve (result) {
    /**
     * Clear the timer and return the given parameter
    */

    if (this.loading) {
      clearTimeout(this.timer)
      store.dispatch('finished', this.loading)
    }

    return result
  }

  async list (model, limit, page) {
    /**
     * Return a list of instances from the server by a given model.
     @param {string} [model] - The model from that'll be fetched
     @param {number} [limit] - Items per Page
     @param {number} [page] - Number of the returned pages
    */

    let offset = limit * (page - 1)

    this['config']['url'] += `/${model}/?limit=${limit}&offset=${offset}`
    this['config']['method'] = 'get'

    let response = await this.execute()

    let count = response.data.count || 0
    let pages = Math.ceil(count / limit)

    return this.resolve({
      count: count,
      pages: pages,
      results: response.data.results
    })
  }

  async get (model, identifier) {
    /**
     * Get one specific instance by it's unique identifier
     * @param {string} [model] - The model from that'll be fetched
     * @param {string} [identifier] - Unique identifier of the instance
    */

    this['config']['url'] += `/${model}/${identifier}`
    this['config']['method'] = 'get'

    let response = await this.execute()

    return this.resolve(response.data)
  }

  execute () {
    return axios(
      this.config
    )
  }
}

export {
  propExists,
  run,
  Request
}
