<template>
  <div class="detail">
    <div class="header" v-if="instance.image_url">
      <div class="image">
          <img :src="$mediaRoot + instance.image_url">
          <span class="caption" v-if="instance.image_title">
            {{ instance.image_title }}
          </span>
      </div>
    </div>
    <div class="content">
        <h1>{{ instance.headline }}</h1>
        <div class="text" lang="en">
          <p v-for="chunk in getTextChunks" v-html="chunk" />
        </div>
    </div>
  </div>
</template>

<script>
import { chunkify } from '@/filters/Text'

export default {
  props: {
    path: {
      type: String,
      required: true
    }
  },
  data () {
    return {
      instance: {}
    }
  },
  computed: {
    getTextChunks () {
      return chunkify(this.instance.text || '')
    }
  },
  mounted () {
    this.getInstance()
  },
  methods: {
    async getInstance () {
      this.$set(
        this,
        'instance',
        await this.$api.get(this.path)
      )
    }
  }
}
</script>

<style lang="scss" scoped>
.header {
  .image {
    width: 100%;
    overflow: hidden;
    top: 5rem;

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

    img {
        object-fit: cover;
        width: 100%;
        height: 100%;

    }
  }
  .caption {
    margin: 8px auto 10px auto;
    width: 80%;
    display: block;
    text-align: center;
    font-size: 15px;
    color: #828282;
  }
}

.content {
    margin: auto;

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
</style>
