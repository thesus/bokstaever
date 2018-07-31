<template>
  <div>
    <form v-on:submit.prevent="submitSettings">
      <table class="table">
        <tr>
          <td>Title</td>
          <td><input type="text" v-model="settings.name"></td>
        </tr>
        <tr>
          <td>E-Mail</td>
          <td><input type="email" v-model="settings.email"></td>
        </tr>
        <tr>
          <td>Info</td>
          <td><textarea v-model="settings.info"></textarea></td>
        </tr>
      </table>
      <button type="submit" class="btn btn-default btn-right">Submit</button>
    </form>
  </div>
</template>

<script>
export default {
  data () {
    return {
      settings: {}
    }
  },
  mounted () {
    this.getSettings()
  },
  methods: {
    async getSettings () {
      this.$set(
        this,
        'settings',
        await this.$api.get('/settings/', true)
      )
    },
    submitSettings () {
      this.$api.send(
        '/settings/',
        this.settings,
        'put',
        true
      )
    }
  }
}
</script>

<style lang="scss" scoped>
@import '@/modules/tables.scss';
@import '@/modules/inputs.scss';
@import '@/modules/buttons.scss';
</style>
