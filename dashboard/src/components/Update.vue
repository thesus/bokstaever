<template>
  <div>
    <notifications />
    <transition name="fade" :duration="{ enter: 2000, leave: 0 }">
      <span v-if="$store.getters.isLoading()" class="icon loading" />
    </transition>
    <transition name="content" :duration="{ enter: 100, leave: 0 }">
      <edit-component
        v-if="!$store.getters.isLoading() && instance"
        :instance="instance"
        :fields="fields"
        @update="submitObject" />
    </transition>
  </div>
</template>

<script>
import Edit from '@/components/Edit'
import { Request } from '@/utils'

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
      showModal: false
    }
  },
  mounted () {
    if (!this.isNew) {
      this.getObject()
    } else {
      this.$set(
        this,
        'instance',
        {}
      )
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
      let request = new Request()
      this.setInstance(
        await request.get(this.model, this.getIdentifier)
      )
    },
    async submitObject () {
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
      } catch (e) {} // Discard error, since it's handled elsewhere
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
