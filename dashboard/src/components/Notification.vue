<template>
  <div class="notifications">
    <transition-group name="message" tag="div">
      <div
        class="card"
        :class="message.type"
        v-for="message in messages"
        :key="message.ID"
        @click="destroy(message.ID)">
        <div class="id">{{ message.ID }}</div>
        <div class="header">{{ message.title }}</div>
        <div class="content">{{ message.text }}</div>
      </div>
    </transition-group>
  </div>
</template>

<script>
import { events } from '@/utils/event'

const ID = (i => () => i++)(0)

export default {
  data () {
    return {
      messages: []
    }
  },
  mounted () {
    events.$on('add', this.addMessage)
  },
  beforeDestroy () {
    events.$off('add')
  },
  methods: {
    addMessage (message) {
      let data = {
        ID: ID(),
        title: message.title || '',
        text: message.text || '',
        type: message.type || 'default'
      }

      this.messages.unshift(data)

      let timeout = message.timeout ? message.timeout : 0
      if (timeout > 0) {
        window.setTimeout(this.destroy, timeout, data.ID)
      }
    },
    destroy (id) {
      this.messages = this.messages.filter(message => message.ID != id)
    }
  }
}
</script>

<style lang="scss" scoped>
.message-enter-active, .message-leave-active {
  transition: all .3s;
}
.message-enter {
  margin-top: -60px;
}
.message-enter-to, .messeage-leave {
  margin-top: 0px;
  opacity: 1;
}

.message-leave-to {
  opacity: 0;
}

.notifications {
  position: absolute;
  right: 10px;
  top: 8px;
  width: 400px;
  max-width: calc(100vw - 20px);
  display: block;

  z-index: 1000;
}

.card {
  position: relative;
  margin-bottom: 8px;
  cursor: pointer;

  .id {
    position: absolute;
    top: 3px;
    right: 6px;
    font-size: 14px;
  }

  .header {
    height: 20px;
    padding: 2px 0 2px 5px;
    border-bottom: 1px solid;
  }
  .content {
    padding: 5px;
  }
  &.default {
    background-color: rgba(44, 70, 127, 0.9);
    color: white;
    .header {
      background-color: rgba(36, 57, 105, 0.9);
    }
  }
  &.danger {
    background-color: rgba(178, 18, 49, 0.9);
    color: white;
    .header {
       background-color: rgba(148, 15, 40, 0.9);
    }
  }
  &.success {
    background-color: rgba(8, 133, 39, 0.9);
    color: white;
    .header {
      background-color: rgba(7, 112, 33, 0.9);
    }
  }
}
</style>
