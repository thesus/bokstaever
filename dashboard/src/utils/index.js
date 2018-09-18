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

const create = (func) => {
  return setTimeout(func, 200)
}

const resolve = (timer, func) => {
  clearTimeout(timer)
  func()
}

class Request {
  constructor () {
    this.config = {
      url: '/api',
      headers: {}
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

    return {
      count: count,
      pages: pages,
      results: response.data.results
    }
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

    return response.data
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

    return response.data
  }

  async upload (model, identifier, instance, func) {
    /**
     * Send an instance to the server that contains files.
    */
    this.createSendConfig(model, identifier, instance)

    this['config']['headers']['Content-Type'] = 'multipart/form-data'
    this['config']['onUploadProgress'] = (event) => {
      let progress = (event.loaded / event.total) * 100
      func(progress)
    }

    let response = await this.execute(false)

    return response.data
  }

  async delete (model, identifier) {
    /**
     * Delete a given instance from the server
     * @param {string} [model] - Model of the instance
     * @param {string} [identifier] - Unique identifier of the instance
    */

    this['config']['url'] += `/${model}/${identifier}/`
    this['config']['method'] = 'delete'

    let response = await this.execute()

    return response.data
  }

  async execute (notify = true) {
    try {
      return await axios(
        this.config
      )
    } catch (error) {
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
  create,
  resolve,
  Request
}
