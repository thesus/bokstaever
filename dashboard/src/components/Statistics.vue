<template>
  <transition name="fade">
    <activity :values="data.activity" v-if="data" />
  </transition>
</template>

<script>
import { Request } from '@/utils'
import Activity from '@/components/Activity'

export default {
  components: {
    'activity': Activity
  },
  data () {
    return {
      data: null
    }
  },
  mounted () {
    this.getStatistics()
  },
  methods: {
    async getStatistics () {
      try {
        let request = new Request()
        this.$set(
          this,
          'data',
          await request.get('statistics')
        )
      } catch (e) {
        // Error is handled elsewhere
      }
    }
  }
}
</script>

<style lang="scss" scoped>
@import '@/modules/transitions.scss';
</style>
