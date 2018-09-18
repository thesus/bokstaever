<template>
  <div>
    <notifications />
    <transition name="fade" :duration="{ enter: 2000, leave: 0 }">
      <span v-if="isNew ? false : loading" class="icon loading" />
    </transition>
    <transition name="content" :duration="{ enter: 100, leave: 0 }">
      <div v-if="(!loading && instance) || isNew">
        <edit-component
          :instance="instance"
          :fields="fields"
          @input="success = null"
          @rendered="buttons = true"
        />

        <button
          class="btn btn-default btn-right"
          :class="{'success': (success === true)}"
          @click="submitObject"
        >
          Submit
          <span v-if="(sending === true)" class="icon loading inline inverse" />
          <span v-if="(success === true)" class="icon check" />
        </button>

        <delete v-if="(!isNew && !singleton)" :model="model" :id="getIdentifier" />
      </div>
    </transition>
  </div>
</template>

<script>
import Edit from '@/components/Edit'
import Delete from '@/components/Delete'

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
    'edit-component': Edit,
    'delete': Delete
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
@import '@/modules/inputs.scss';
@import '@/modules/buttons.scss';

.icon.check {
  height: 12px;
  width: 12px;
  margin-left: 3px;
}

.success, .success:hover {
  background-color: rgba(7, 112, 33, 0.9) !important;
}

.loading {
  margin: 0px auto 0px auto;
}
</style>
