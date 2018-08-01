<template>
  <div class="notifications">
    <div v-for="message in messages">
      {{ message.text }}
    </div>
  </div>
</template>

<script>
import { events } from '@/utils/event'

export default {
  data () {
    return {
      messages: []
    }
  },
  created () {
    events.$on('add', this.addMessage)
  },
  beforeDestroy () {
    events.$off('add')
  },
  methods: {
    addMessage (message) {
      this.messages.push(message)
    }
  }
}
</script>

<style lang="css">
</style>
