<template>
  <div class="detail-container">
    <div class="image-container">
      <div class="post-image">
          <img :src="$mediaRoot + post.image_url">
      </div>
      <span class="image-title">{{ post.image_title }}</span>
    </div>
      <div class="post-content">
          <h1>{{ post.headline }}</h1>
          <div class="text" lang="en">
            <p v-for="chunk in getTextChunks">
              {{ chunk }}
            </p>
          </div>
      </div>
  </div>
</template>

<script>
import { chunkify } from '@/filters/Text'

export default {
  data () {
    return {
      post: {}
    }
  },
  computed: {
    getTextChunks () {
      return chunkify(this.post.text || '')
    }
  },
  mounted () {
    this.getPost()
  },
  methods: {
    async getPost () {
      this.$set(
        this,
        'post',
        await this.$api.get(`/posts/${this.$route.params.id}`)
      )
    }
  }
}
</script>

<style lang="scss" scoped>
@import '@/modules/post.scss';
</style>
