<template>
  <textarea v-model="text"></textarea>
</template>

<script>
export default {
  props: ['value'],
  data () {
    return {
      text: this.value || ''
    }
  },
  watch: {
    value () {
      this.text = this.value
    },
    text () {
      this.$emit(
        'input',
        { target: { value: this.text } }
      )
    }
  }
}
</script>

<style lang="scss" scoped>
  @import '@/modules/inputs.scss';
</style>
