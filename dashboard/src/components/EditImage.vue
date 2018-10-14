<template>
  <div>
    <input v-model="image.title">
    {{ id }}
    <button
      class="btn btn-default"
      @click="submitImage"
    >
      Submit
    </button>
  </div>
</template>

<script>
import { Request, create, resolve } from '@/utils'

export default {
  props: ['id'],
  data () {
    return {
      loading: null,
      sending: null,
      success: null,
      image: {}
    }
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

        this.$set(this, 'success', true)
      } catch (e) {

      } finally {
        resolve(timer, () => {
          this.$set(this, 'sending', false)
        })
      }
    }
  },
  watch: {
    id () {
      if (this.id !== null && this.id !== undefined) {
        this.getImage()
      }
    }
  }
}
</script>

<style lang="scss" scoped>

</style>
