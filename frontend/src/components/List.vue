<template>
  <div>
    <table class="table table-list">
      <thead>
        <tr>
          <th v-for="field in fields"> {{ field.name }}</th>
        </tr>
      </thead>
      <tbody>
        <tr
          v-for="instance in instances.results"
          @click="$router.push({ name: info.router.edit, params: { id: instance.id }})">
          <td v-for="field in fields" v-html="instance[field.identifier]" />
        </tr>
      </tbody>
    </table>
    <router-link
      class="btn btn-default btn-right"
      :to="{ name: info.router.create }">
        {{ info.router.createText }}
    </router-link>
    <pagination-component :count="instances.pages" />
  </div>
</template>

<script>
import Pagination from '@/components/Pagination'

export default {
  components: {
    'pagination-component': Pagination
  },
  props: {
    fields: {
      type: Array,
      required: true
    },
    info: {
      type: Object,
      required: true
    }
  },
  data() {
    return {
      instances: {}
    }
  },
  mounted () {
    this.getInstances()
  },
  computed: {
    currentPage () {
      return parseInt(this.$route.query.page) || 1
    }
  },
  methods: {
    async getInstances () {
      this.$set(
        this,
        'instances',
        await this.$api.getByPage(
          this.info.path,
          this.info.limit,
          this.currentPage,
          true
        )
      )
    }
  },
  watch: {
    currentPage () {
      this.getInstances()
    }
  }
}
</script>

<style lang="scss" scoped>
@import '@/modules/buttons.scss';
@import '@/modules/tables.scss';

tbody {
  tr {
    cursor: pointer;
  }
}
</style>
