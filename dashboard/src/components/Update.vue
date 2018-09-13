<template>
  <div>
    <notifications />
    <transition name="fade" :duration="{ enter: 2000, leave: 0 }">
      <span v-if="loading" class="icon loading" />
    </transition>
    <transition name="content" :duration="{ enter: 400, leave: 0 }">
      <edit-component v-if="!loading" :instance="instance" :fields="fields" @update="submitObject" />
    </transition>
  </div>
</template>

<script>
import Edit from '@/components/Edit'

export default {
  props: {
    fields: {},
    router: {
      type: Object,
      default: () => {
        return {
          'field': null,
          'create': null,
          'edit': null
        }
      }
    },
    url: {
      type: String,
      required: true
    },
    singleton: {
      type: Boolean,
      default: false
    }
  },
  components: {
    'edit-component': Edit,
  },
  data () {
    return {
      instance: {},
      showModal: false,
      loading: false
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
      if (!this.singleton) {
        return this.isNew ? this.url : this.url + this.$route.params[this.router.field] + '/'
      } else {
        return this.url
      }
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
      var loadingTimer = setTimeout(() => {
        this.$set(
          this,
          'loading',
          true
        )
      }, 200)

      this.setInstance(
          await this.$api.get(this.getURL, true)
      )

      clearTimeout(loadingTimer)
      this.$set(this, 'loading', false)
    },
    async submitObject () {
      let data = {}
      for (let i of this.fields) {
        if (!i.readonly) {
          //TODO (till@cryptec.at): Add validation with required=true, maybe default
          data[i.identifier] = this.instance[i.identifier]
        }
      }

      try {
        var response = await this.$api.send(
          this.getURL,
          data,
          this.getMethod,
          true
        )
      } catch(error) {
          // If request was unsuccessfull, return here,
          // Notification already created in ApiPlugin
          return
      }

      this.$notify({
        'type': 'success',
        'title': 'Successfull',
        'text': 'Saving of instance was successfull!',
        'timeout': 4000
      })

      if (this.isNew && !this.singleton) {
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
@import '@/modules/transitions.scss';

.loading {
  margin: 0px auto 0px auto;
}
</style>
