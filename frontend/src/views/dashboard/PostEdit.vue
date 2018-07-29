<template>
  <div>
    <form v-on:submit.prevent="submitPost">
        <table class="table">
            <tr>
                <td>Title</td>
                <td><input type="text" v-model="post.headline"></td>
           </tr>
           <tr>
               <td>Content</td>
               <td><textarea v-model="post.text"></textarea></td>
           </tr>
        </table>
        <button class="btn btn-default btn-right" type="submit">Submit</button>
    </form>
    <img :src="$mediaRoot + post.thumbnail_url" v-if="post.thumbnail_url">
    <button type="iuae" @click="showModal = true">Select Image</button>
    <modal-component v-if="showModal" @close="showModal = false">
      <image-component @selected="selectImage"/>
    </modal-component>
  </div>
</template>

<script>
import Modal from '@/components/Modal'
import ImageSelect from '@/components/ImageSelect'

export default {
  components: {
    'modal-component': Modal,
    'image-component': ImageSelect
  },
  data () {
    return {
      post: {},
      url: `/posts/${this.$route.params.id}/`,
      showModal: false
    }
  },
  mounted () {
    this.getPost()
  },
  methods: {
    selectImage (image) {
      this.$set(this.post, 'image', image.id)
      this.$set(this.post, 'thumbnail_url', image.thumbnail)
      this.showModal = false
    },
    setPost (data) {
      this.$set(
        this,
        'post',
        data
      )
    },
    async getPost () {
      this.setPost(
          await this.$api.get(this.url, true)
      )
    },
    async submitPost () {
      let data = {
        headline: this.post.headline || '',
        text: this.post.text || '',
        draft: false, // fixme
        image: this.post.image || null
      }
      this.setPost(
          await this.$api.post(this.url, data, true)
      )
    }
  }
}
</script>
