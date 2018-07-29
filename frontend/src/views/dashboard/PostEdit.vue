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
    <button type="iuae" @click="showModal = true">Select Image</button>
    <modal-component v-if="showModal" @close="showModal = false">
      <image-component multiple="true"/>
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
