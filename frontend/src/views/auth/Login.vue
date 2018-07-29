<template>
  <div>
    <form @submit.prevent="submit">
      <input type="text" v-model="username" placeholder="Username">
      <input type="password" v-model="password" placeholder="Password">
      <button type="submit">Login</button>
    </form>
    {{ status }}
  </div>
</template>

<script>
export default {
  data () {
    return {
      username: null,
      password: null,
      status: null
    }
  },
  methods: {
    async submit () {
      if (await this.$api.authenticate(this.username, this.password)) {
        // console.log(this.$route.query.next)
        this.$router.push({ path: this.$route.query.next || '/' })
      }
    }
  }
}
</script>
