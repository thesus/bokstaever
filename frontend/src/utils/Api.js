let checkAuth = (config, authenticated) => {
  if (authenticated) {
    let token = localStorage.getItem('jwt_token')
    config['headers'] = {'Authorization': 'JWT ' + token}
  }
  return config
}

const ApiPlugin = {
  apiRoot: process.env.VUE_APP_API_ROOT,
  mediaRoot: process.env.VUE_APP_MEDIA_ROOT,

  install (Vue, options) {
    Vue.prototype.$apiRoot = this.apiRoot
    Vue.prototype.$mediaRoot = this.mediaRoot

    Vue.prototype.$api = {
      get: (url, authenticated=false) => {
        let config = {
          method: 'get',
          url: this.apiRoot + url,
        }
        checkAuth(config, authenticated)

        return Vue.axios(config).then((response) => {
          return response.data
        })
      },
      send: (url, data, method, authenticated=false) => {
        let config = {
          method: method,
          url: this.apiRoot + url,
          data: data
        }
        checkAuth(config, authenticated)
        console.log(config)
        return Vue.axios(config).then((response) => {
          return response.data
        })
      },
      async getByPage (url, limit, page, authenticated=false) {
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
        }).catch((response) => {
          return false
        })
      }
    }
  }
}

export default ApiPlugin
