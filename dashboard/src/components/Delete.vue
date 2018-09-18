<template>
  <div>
    <button
      class="btn btn-danger btn-right"
      @click="showModal = true"
    >
      Delete
    </button>
    <modal-component
      v-if="showModal"
      @close="showModal = false"
      title="Delete this instance?"
    >
      <span class="info">
        You're about to delete this instance! Press "Proceed" to continue. This can't be undone.
      </span>

      <button
        type="button"
        class="btn btn-default btn-right"
        @click="showModal = false"
      >
        Cancel
      </button>

      <button
        type="button"
        class="btn btn-default btn-right"
        @click="deleteInstance()"
      >
        Proceed
      </button>
    </modal-component>
  </div>
</template>

<script>
import Modal from '@/components/Modal'

import { Request } from '@/utils'

export default {
  components: {
    'modal-component': Modal
  },
  props: ['id', 'model'],
  data () {
    return {
      'showModal': false
    }
  },
  methods: {
    async deleteInstance () {
      try {
        let request = new Request()
        await request.delete(this.model, this.id)

        this.$router.replace('/')
      } catch (e) {} // Discard the error here.
    }
  }
}
</script>

<style lang="scss" scoped>
@import '@/modules/buttons.scss';

.info {
  display: block;
}
</style>
