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
        <tr>
          <td>Image</td>
          <td>
            <div class="image-select">
              <div class="current-image" v-if="post.thumbnail_url">
                <img :src="$mediaRoot + post.thumbnail_url">
              </div>
              <button class="btn btn-default" @click="showModal = true">
                Select Image
              </button>
            </div>
          </td>
        </tr>
      </table>
      <button class="btn btn-default btn-right" type="submit">Submit</button>
    </form>
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
      url: 'null',
      showModal: false,
    }
  },
  mounted () {
    if (!this.isNew) {
      this.getPost()
    }
  },
  computed: {
    isNew () {
      return this.$route.name === 'post-create'
    },
    getURL () {
      if (!this.isNew) {
        return `/posts/${this.$route.params.id}/`
      } else {
        return '/posts/'
      }
    },
    getMethod () {
      return this.isNew ? 'post' : 'put'
    }
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
          await this.$api.get(this.getURL, true)
      )
    },
    async submitPost () {
      let data = {
        headline: this.post.headline || '',
        text: this.post.text || '',
        draft: false, // fixme
        image: this.post.image || null
      }
      let response = await this.$api.send(
        this.getURL,
        data,
        this.getMethod,
        true
      )
      if (this.isNew) {
        this.$router.push({ name: 'post-edit', params: {'id': response.id }})
      } else {
        this.setPost(response)
      }
    }
  }
}
</script>

<style lang="scss" scoped>
@import '@/modules/tables.scss';
@import '@/modules/buttons.scss';
@import '@/modules/inputs.scss';

.image-select {
    display: flex;

    .btn {
      margin: auto 0 auto 0;
    }
}

.current-image {
  height: 150px;
  width: 150px;
  margin-right: 8px;
  img {
      height: 100%;
      width: 100%;
      object-fit: cover;
  }
}
</style>
