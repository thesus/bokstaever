<template>
  <text-component :path="`/pages/${this.$route.params.slug}/`" />
</template>

<script>
import Text from '@/components/Text'

export default {
  components: {
    'text-component': Text
  }
}
</script>
