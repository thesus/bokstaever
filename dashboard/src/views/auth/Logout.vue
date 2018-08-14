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
    localStorage.removeItem('jwt_token')
  }
}
</script>
