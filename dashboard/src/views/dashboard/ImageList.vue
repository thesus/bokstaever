<template>
  <div>
    <image-component :limit="30" @submit="openImage"></image-component>
    <router-link class="btn btn-default btn-right" :to="{ name: 'image-upload' }">Upload</router-link>
    <modal-component v-if="imageID != null" :title="'Edit Image (' + imageID + ')'" @close="imageID = null" min="220px" max="230px">
      <image-edit :id="imageID" @success="imageID = null"/>
    </modal-component>
  </div>
</template>

<script>
import ImageSelect from '@/components/ImageSelect'
import EditImage from '@/components/EditImage'
import Modal from '@/components/Modal'

export default {
  components: {
    'image-component': ImageSelect,
    'modal-component': Modal,
    'image-edit': EditImage
  },
  data () {
    return {
      imageID: null
    }
  },
  methods: {
    openImage (id) {
      this.$set(this, 'imageID', id)
    }
  }
}
</script>

<style lang="scss" scoped>
@import '@/modules/buttons.scss';
</style>
