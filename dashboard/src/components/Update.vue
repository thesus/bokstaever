<template>
  <div>
    <notifications />
    <transition name="fade" :duration="{ enter: 2000, leave: 0 }">
      <span v-if="this.isNew ? false : loading" class="icon loading" />
    </transition>
    <transition name="content" :duration="{ enter: 100, leave: 0 }">
      <edit-component
        v-if="(!loading && instance) || this.isNew"
        :sending="sending"
        :success="success"
        :instance="instance"
        :fields="fields"
        @update="success = null"
        @submit="submitObject" />
    </transition>
  </div>
</template>

<script>
import Edit from '@/components/Edit'
import { Request, create, resolve } from '@/utils'

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
    model: {
      type: String,
      required: true
    },
    singleton: {
      type: Boolean,
      default: false
    }
  },
  components: {
    'edit-component': Edit
  },
  data () {
    return {
      instance: null,
      loading: null,
      sending: null,
      success: null
    }
  },
  created () {
    if (!this.isNew) {
      this.getObject()
    } else {
      this.setInstance({})
    }
  },
  computed: {
    isNew () {
      return this.$route.name === this.router.create
    },
    getIdentifier () {
      if (this.singleton) {
        return null
      } else if (this.isNew) {
        return undefined
      } else {
        return this.$route.params[this.router.field]
      }
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
      let timer = create(() => {
        this.$set(this, 'loading', true)
      })

      try {
        let request = new Request()
        this.setInstance(
          await request.get(this.model, this.getIdentifier)
        )
      } catch (e) {

      } finally {
        resolve(timer, () => {
          this.$set(this, 'loading', false)
        })
      }
    },
    async submitObject () {
      let timer = create(() => {
        this.$set(this, 'sending', true)
      })

      let data = {}
      for (let i of this.fields) {
        if (!i.readonly) {
          // TODO (till@cryptec.at): Add validation with required=true, maybe default
          data[i.identifier] = this.instance[i.identifier]
        }
      }

      try {
        let request = new Request('send')
        let response = await request.send(this.model, this.getIdentifier, data)

        this.$set(this, 'success', true)

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
      } catch (e) { // Discard error, since it's handled elsewhere
        this.$set(this, 'success', false)
      } finally {
        resolve(timer, () => {
          this.$set(this, 'sending', false)
        })
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
