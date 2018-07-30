<template>
  <div>
    <image-component :limit="30" @selected="console.log('fixme')"></image-component>
    <router-link :to="{ name: 'image-upload' }">Upload</router-link>
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
