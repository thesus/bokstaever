<template>
  <div>
    <notifications/>
    <div class="login">
      <form @submit.prevent="submit">
        <input type="text" v-model="username" placeholder="Username">
        <input type="password" v-model="password" placeholder="Password">
        <button type="submit" class="btn btn-default btn-right">Login</button>
      </form>
      {{ status }}
    </div>
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
        this.$router.push({ path: this.$route.query.next || '/' })
      }
    }
  }
}
</script>

<style lang="scss" scoped>
@import '@/modules/inputs.scss';
@import '@/modules/buttons.scss';

.login {
  position: absolute;
  left: 40%;
  right: 40%;
  top: calc(50% - 200px);
  background-color: rgb(245, 245, 245);
  padding: 30px;
  @media screen and (max-width: 1600px) {
    left: 35%;
    right: 35%;
  }
  @media screen and (max-width: 1200px) {
    left: 30%;
    right: 30%;
  }
  @media screen and (max-width: 1000px) {
    left: 20%;
    right: 20%;
  }
  @media screen and (max-width: 500px) {
    left: 0px;
    right: 0px;
    top: 0;
    bottom: 0;
  }
}

.btn {
  margin: 8px 0px 0px 0px;
}

input {
  width: 100%;
  &:first-child {
    border-bottom: none;
  }
}
</style>
