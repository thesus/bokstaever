<template>
  <div class="dashboard">
    <navbar></navbar>
    <div class="content">
      <router-view />
    </div>
  </div>
</template>

<script>
import Navbar from '@/components/Navbar'

export default {
  components: {
    'navbar': Navbar
  }
}
</script>

<style lang="scss" scoped>
.content {
  padding: 8px;
}
</style>
