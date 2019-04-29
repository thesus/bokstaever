<template>
  <input type="checkbox" v-model="dirty">
</template>

<script>
export default {
  props: ['value'],
  data () {
    return {
      dirty: this.value || false
    }
  },
  watch: {
    value () {
      this.dirty = this.value
    },
    dirty () {
      this.$emit(
        'input',
        { target: { value: this.dirty } }
      )
    }
  }
}
</script>

<style lang="scss" scoped>
  @import '@/modules/inputs.scss';
</style>
