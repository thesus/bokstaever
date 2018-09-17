import axios from 'axios'
import Vue from 'vue'

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
  /**
   * Set's up a timer running as long as the given function.
  */
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
    // Add Authorization Header
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
      store.dispatch('success', this.loading)
      if (this.timer) {
        clearTimeout(this.timer)
      }
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
    this['config']['url'] += `/${model}/`
    if (identifier) {
      this['config']['url'] += `${identifier}/`
    }

    this['config']['method'] = 'get'

    let response = await this.execute()

    return this.resolve(response.data)
  }

  createSendConfig (model, identifier, instance) {
    this['config']['url'] += `/${model}/`

    if (identifier) {
      this['config']['url'] += `${identifier}/`
    }

    this['config']['method'] = (identifier !== undefined) ? 'put' : 'post'
    this['config']['data'] = instance
  }

  async send (model, identifier, instance) {
    /**
     * POST or PUT an instance to the server
     * @param {string} [model] - The model that'll be saved
     * @param {string} [identifier] - Identifier of the instance.
     * If undefined, create a new instance. -> POST.
     * If null, assume the model has no identifier. -> PUT
     * @param {object} [instance] - Instance that gets send to the server
    */
    this.createSendConfig(model, identifier, instance)

    let response = await this.execute()

    return this.resolve(response.data)
  }

  async upload (model, identifier, instance, name) {
    /**
     * Send an instance to the server that contains files.
    */
    this.createSendConfig(model, identifier, instance)

    this['config']['headers']['Content-Type'] = 'multipart/form-data'
    this['config']['onUploadProgress'] = (event) => {
      let progress = (event.loaded / event.total) * 100
      store.dispatch('setProgress', { value: progress, name: name })
    }

    let response = await this.execute(false)

    return this.resolve(response.data)
  }

  async execute (notify = true) {
    try {
      return await axios(
        this.config
      )
    } catch (error) {
      if (this.timer) {
        clearTimeout(this.timer)

        store.dispatch('failure', this.loading)

        delete this.loading
        delete this.timer
      }

      if (notify) {
        /* Error handling */
        if (propExists(error, 'response.data')) {
          let data = error.response.data
          if (typeof data === 'object') {
            for (let key in data) {
              Vue.notify({
                type: 'danger',
                title: `Error: ${key}`,
                text: `${data[key]}`,
                timeout: 5000
              })
            }
          }
        } else {
          Vue.notify({
            type: 'danger',
            title: 'Error ocurred!',
            text: error,
            timeout: 5000
          })
        }
      }

      // Return error for further processing.
      return Promise.reject(error)
    }
  }
}

export {
  propExists,
  run,
  Request
}
