<template>
  <div class="detail-container">
    <div class="image-container" v-if="page.image">
      <div class="post-image">
          <img :src="$mediaRoot + page.image_url">
      </div>
    </div>
      <div class="post-content">
          <h1>{{ page.name }}</h1>
          <div class="text" lang="en">
            <p v-for="chunk in getTextChunks" v-html="chunk" />
          </div>
      </div>
  </div>
</template>

<script>
import { chunkify } from '@/filters/Text'

export default {
  data () {
    return {
      page: {}
    }
  },
  computed: {
    getTextChunks () {
      return chunkify(this.page.text || '')
    }
  },
  mounted () {
    this.getPost()
  },
  methods: {
    async getPost () {
      this.$set(
        this,
        'page',
        await this.$api.get(`/pages/${this.$route.params.slug}/`)
      )
    }
  }
}
</script>

<style lang="scss" scoped>
@import '@/modules/post.scss';
</style>
