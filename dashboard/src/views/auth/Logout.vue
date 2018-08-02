<template>
  <div>
    You're locked out!
    <router-link :to="{ name: 'login' }">Login</router-link>
    <router-link :to="{ name: 'home' }">Home</router-link>
  </div>
</template>

<script>
export default {
  mounted () {
    localStorage.removeItem('jwt_token')
  }
}
</script>
