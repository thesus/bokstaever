<template>
  <edit-component :instance="instance" :fields="fields" @update="submitObject" />
</template>

<script>
import Edit from '@/components/Edit'

export default {
  props: {
    fields: {},
    router: {},
    url: {}
  },
  components: {
    'edit-component': Edit,
  },
  data () {
    return {
      instance: {},
      showModal: false,
    }
  },
  mounted () {
    if (!this.isNew) {
      this.getObject()
    }
  },
  computed: {
    isNew () {
      return this.$route.name === this.router.create
    },
    getURL () {
      return this.isNew ? this.url : this.url + this.$route.params[this.router.field] + '/'
    },
    getMethod () {
      return this.isNew ? 'post' : 'put'
    }
  },
  methods: {
    setInstance (data) {
      this.$set(
        this,
        'instance',
        data
      )
    },
    async getObject () {
      this.setInstance(
          await this.$api.get(this.getURL, true)
      )
    },
    async submitObject () {
      let data = {}
      for (let i of this.fields) {
        if (!i.readonly) {
          //TODO (till@cryptec.at): Add validation with required=true, maybe default
          data[i.identifier] = this.instance[i.identifier]
        }
      }
      let response = await this.$api.send(
        this.getURL,
        data,
        this.getMethod,
        true
      )
      // TODO: Catch if error
      if (this.isNew) {
        let params = {}
        params[this.router.field] = response[this.router.field]

        this.$router.push(
          {
            name: this.router.edit,
            params: params
          }
        )
      } else {
        this.setInstance(response)
      }
    }
  }
}
</script>

<style lang="scss" scoped>
</style>
