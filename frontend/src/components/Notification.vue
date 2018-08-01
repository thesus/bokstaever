<template>
  <div class="notifications">
    <div class="card" v-for="message in messages" :class="message.type">
      <div class="header">{{ message.title }}</div>
      <div class="content">{{ message.text }}</div>
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
  beforeMount () {
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

<style lang="scss" scoped>
.notifications {
  position: absolute;
  right: 5px;
  top: 5px;
  width: 400px;

  display: block;

  .card {
    margin: 8px 0 8px 0;
    background-color: pink;
    .header {
      height: 20px;
      padding: 2px 0 2px 5px;
      border-bottom: 1px solid;
    }
    .content {
      padding: 5px;
    }
    &.danger {
        background-color: rgb(178, 18, 49);
        color: white;
        opacity: 0.9;
      .header {
         background-color: rgb(148, 15, 40);
      }
    }
    &.success {
      background-color: rgb(8, 133, 39);
      color: white;
      opacity: 0.9;
      .header {
        background-color: rgb(7, 112, 33);
      }
    }
  }
}
</style>
