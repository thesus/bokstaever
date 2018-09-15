<template>
  <div>
    <image-component :limit="30" @selected="console.log('fixme')"></image-component>
    <router-link class="btn btn-default btn-right" :to="{ name: 'image-upload' }">Upload</router-link>
  </div>
</template>

<script>
import ImageSelect from '@/components/ImageSelect'

export default {
  components: {
    'image-component': ImageSelect
  }
}
</script>

<style lang="scss" scoped>
@import '@/modules/buttons.scss';
</style>
