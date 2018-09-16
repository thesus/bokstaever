import store from '@/store'

let checkAuth = (config, authenticated) => {
  if (authenticated) {
    config['headers'] = { 'Authorization': 'JWT ' + store.getters.jwt }
  }
  return config
}

const ApiPlugin = {
  apiRoot: '/api',
  mediaRoot: '',

  install (Vue, options) {
    Vue.prototype.$apiRoot = this.apiRoot
    Vue.prototype.$mediaRoot = this.mediaRoot

    Vue.prototype.$api = {
      Request: Request,
      get: (url, authenticated = false) => {
        let config = {
          method: 'get',
          url: this.apiRoot + url
        }
        config = checkAuth(config, authenticated)

        return Vue.axios(config).then((response) => {
          return response.data
        })
      },
      send: (url, data, method, authenticated = false) => {
        let config = {
          method: method,
          url: this.apiRoot + url,
          data: data
        }
        config = checkAuth(config, authenticated)

        return Vue.axios(config).then((response) => {
          return response.data
        }).catch(error => {
          if (error.response && error.response.data) {
            let data = error.response.data
            if (typeof data === 'object') {
              for (let key in data) {
                Vue.notify({
                  type: 'danger',
                  title: `Error on Field: ${key}`,
                  text: `${data[key]}`,
                  timeout: 5000
                })
              }
            }
          }
          throw new Error(error)
        })
      },
      sendFile: (url, data, method = 'post', authenticated = false, instance) => {
        let config = {
          method: 'post',
          url: this.apiRoot + url,
          data: data,
          headers: {
            'Content-Type': 'multipart/form-data'
          },
          onUploadProgress: (progressEvent) => {
            let progress = (progressEvent.loaded / progressEvent.total) * 100
            Vue.set(instance, 'progress', progress)
          }
        }

        config = checkAuth(config, authenticated)
        return Vue.axios(config)
      }
    }
  }
}

export default ApiPlugin
