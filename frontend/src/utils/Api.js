const ApiPlugin = {
  apiRoot: process.env.VUE_APP_API_ROOT,
  mediaRoot: process.env.VUE_APP_MEDIA_ROOT,

  install (Vue, options) {
    Vue.prototype.$apiRoot = this.apiRoot
    Vue.prototype.$mediaRoot = this.mediaRoot

    Vue.prototype.$api = {
      get: (url) => {
        return Vue.axios({
          method: 'get',
          url: this.apiRoot + url
        }).then((response) => {
          return response.data
        })
      },
      async getByPage (url, limit, page) {
        let offset = limit * (page - 1)
        let data = await this.get(
          `${url}?limit=${limit}&offset=${offset}`
        )

        let count = data.count || 0
        let pages = Math.ceil(count / limit)

        return {
          count: count,
          pages: pages,
          results: data.results
        }
      }
    }
  }
}

export default ApiPlugin
