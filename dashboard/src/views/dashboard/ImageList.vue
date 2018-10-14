<template>
  <div>
    <image-component :limit="30" @submit="openImage"></image-component>
    <router-link class="btn btn-default btn-right" :to="{ name: 'image-upload' }">Upload</router-link>
    <image-edit :id="imageID" />
  </div>
</template>

<script>
import ImageSelect from '@/components/ImageSelect'
import EditImage from '@/components/EditImage'

export default {
  components: {
    'image-component': ImageSelect,
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
