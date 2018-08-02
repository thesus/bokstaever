<template>
  <text-component :path="`/posts/${this.$route.params.id}`" />
</template>

<script>
import Text from '@/components/Text'

export default {
  components: {
    'text-component': Text
  }
}
</script>
