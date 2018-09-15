let checkAuth = (config, authenticated) => {
  if (authenticated) {
    let token = localStorage.getItem('jwt_token')
    config['headers'] = { 'Authorization': 'JWT ' + token }
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
      },
      async getByPage (url, limit, page, authenticated = false) {
        let offset = limit * (page - 1)
        let data = await this.get(
          `${url}?limit=${limit}&offset=${offset}`,
          authenticated
        )

        let count = data.count || 0
        let pages = Math.ceil(count / limit)

        return {
          count: count,
          pages: pages,
          results: data.results
        }
      },
      authenticate: (username, password) => {
        return Vue.axios({
          method: 'post',
          url: `${this.apiRoot}/auth/jwt/create/`,
          data: {
            username: username,
            password: password
          }
        }).then((response) => {
          let data = response.data
          localStorage.setItem('jwt_token', data.token)
          return true
        }).catch((error) => {
          let errors = error.response.data || {}
          if (errors.non_field_errors && errors.non_field_errors.length > 0) {
            for (let i of errors.non_field_errors) {
              Vue.notify({
                type: 'danger',
                title: 'Login failed!',
                text: i,
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
          return false
        })
      }
    }
  }
}

export default ApiPlugin
