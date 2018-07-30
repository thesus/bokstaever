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
.detail-container {
  .image-container {
      .post-image {
        width: 100%;
        @media screen and (max-width: 500px) {
            height: 350px;
        }
        @media screen and (min-width: 500px) and (max-width: 800px){
            height: 450px;
        }
        @media screen and (min-width: 800px) and (max-width: 1300px){
            height: 600px;
        }
        @media screen and (min-width: 1300px) {
            height: 750px;
        }

        overflow: hidden;
        top: 5rem;
        img {
            object-fit: cover;
            width: 100%;
            height: 100%;

        }
      }
      .image-title {
        margin: 8px auto 10px auto;
        width: 80%;
        display: block;
        text-align: center;
        font-size: 15px;
        color: #828282;
      }
    }

    .post-content {
        @media screen and (min-width: 1300px) {
            width: 45%;
        }
        @media screen and (min-width: 700px) and (max-width: 1300px) {
            width: 60%;
        }
        @media screen and (min-width: 500px) and (max-width: 700px) {
            width: 80%;
        }
        @media screen and (max-width: 500px) {
            width: 95%;
        }
        margin: auto;
        h1 {
          //font-family: Georgia;
          font-size: 40px;
        }

        .text {
            text-align: justify;
            word-break: break-word;
            hyphens: auto;
            font-size: 18px;
            p:first-child:first-letter {
              // color: #903;
              float: left;
              font-family: Georgia;
              font-size: 55px;
              line-height: 41px;
              padding: 3px 4px 0 0;
            }
        }
    }
}
</style>
