<template>
  <div>
    <notification />
    <div class="indicator" v-show="sending || loading">
      <span class="icon loading" />
    </div>
    <div
      :class="{
        cover: (sending || loading),
      }"
    >
      <img class="thumbnail" :src="image.thumbnail">
      <input type="text" v-model="image.title">
      <button
        class="btn btn-default"
        @click="submitImage"
      >
        Submit
      </button>
    </div>
  </div>
</template>

<script>
import Notification from '@/components/Notification'
import { Request, create, resolve } from '@/utils'

export default {
  components: {
    'notification': Notification
  },
  props: ['id'],
  data () {
    return {
      loading: true,
      sending: null,
      success: null,
      image: {}
    }
  },
  mounted () {
    this.getImage()
  },
  methods: {
    async getImage () {
      let timer = create(() => {
        this.$set(this, 'loading', true)
      })

      try {
        let request = new Request()
        this.$set(
          this,
          'image',
          await request.get('images', this.id)
        )
      } catch (e) {
        // TODO: Dismiss error later on.
        console.log(e)
      } finally {
        resolve(timer, () => {
          this.$set(this, 'loading', false)
        })
      }
    },
    async submitImage () {
      let timer = create(() => {
        this.$set(this, 'sending', true)
      })

      let data = {
        id: this.image.id,
        title: this.image.title
      }
      try {
        let request = new Request()
        await request.patch('images', this.image.id, data)

        this.$emit('success')
      } catch (e) {
        resolve(timer, () => {
          this.$set(this, 'sending', false)
        })
      }
    }
  }
  // watch: {
  //   id () {
  //     if (this.id !== null && this.id !== undefined) {
  //       this.getImage()
  //     }
  //   }
  // }
}
</script>

<style lang="scss" scoped>
@import '@/modules/inputs.scss';
@import '@/modules/buttons.scss';

.cover {
  opacity: 0.2;
}

.thumbnail {
  height: 200px;
  width: 200px;
}

.indicator {
  position: absolute;
  top: calc(50% - 36px);
  left: calc(50% - 41px); // padding + icon width / 2
}

.icon.loading {
  width: 50px;
  height: 50px;
}
</style>
