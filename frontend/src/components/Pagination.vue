<template>
  <div class="pagination">
    <button :disabled="!hasPrevious" @click="previousPage" class="icon left" />
    <button :disabled="!hasNext" @click="nextPage" class="icon right" />
  </div>
</template>

<script>
export default {
  props: ['count'],
  computed: {
    currentPage () {
      return this.$route.query.page ? parseInt(this.$route.query.page) : 1
    },
    hasNext () {
      return this.currentPage < this.$props.count
    },
    hasPrevious () {
      return this.currentPage > 1
    }
  },
  methods: {
    nextPage () {
      this.$router.replace(
        {
          query: {
            page: this.currentPage + 1
          }
        }
      )
    },
    previousPage () {
      this.$router.replace(
        {
          query: {
            page: this.currentPage - 1
          }
        }
      )
    }
  }
}
</script>

<style lang="scss" scoped>
.pagination {
    margin: auto;
    width: 48px;
    button {
      padding: 0;
      &:hover {
        opacity: 0.8;
      }
      &:disabled {
        opacity: 0.6;
      }
      &:first-child {
        margin-right: 2px;
      }
      &:last-child {
        margin-left: 2px;
      }
    }
}
</style>
