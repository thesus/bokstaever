<template>
  <div>
    <notifications />
    <transition name="fade" :duration="{ enter: 2000, leave: 0 }">
      <span v-if="$store.getters.isLoading()" class="icon loading" />
    </transition>
    <transition name="content" :duration="{ enter: 100, leave: 0 }">
      <edit-component
        :success="success"
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
      showModal: false,
      pushing: false,
      success: false
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
      if (!this.singleton && !this.isNew) {
        return this.$route.params[this.router.field]
      } else {
        return null
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
      var pushingTimer = setTimeout(() => {
        this.$set(
          this,
          'pushing',
          true
        )
      }, 200)
      this.$set(
        this,
        'success',
        false
      )

      let data = {}
      for (let i of this.fields) {
        if (!i.readonly) {
          // TODO (till@cryptec.at): Add validation with required=true, maybe default
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
      } catch (error) {
        // Error handling is done elsewhere. :)
        return
      } finally {
        clearTimeout(pushingTimer)
        this.$set(
          this,
          'pushing',
          false
        )
      }

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

      this.$set(
        this,
        'success',
        true
      )
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
