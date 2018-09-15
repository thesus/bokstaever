<template>
  <div>
    You're locked out!
    <router-link :to="{ name: 'login' }">Login</router-link>
    <a href="/">Home</a>
  </div>
</template>

<script>
export default {
  mounted () {
    this.$store.dispatch('logout')
  }
}
</script>
