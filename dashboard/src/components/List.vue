<template>
  <div>
    <transition name="fade" :duration="{ enter: 1000, leave: 0 }">
      <span v-show="loading" class="icon loading" />
    </transition>
    <transition name="content" :duration="{ enter: 400, leave: 0 }">
      <div v-show="!loading && show">
        <table class="table table-list">
          <thead>
            <tr>
              <th v-for="field in fields"> {{ field.name }}</th>
            </tr>
          </thead>
          <tbody>
            <tr
              v-for="instance in instances.results"
              @click="goToEdit(instance)">
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
    </transition>
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
  data () {
    return {
      instances: {},
      loading: false,
      show: false
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
  updated () {
    this.$set(
      this,
      'show',
      true
    )
  },
  methods: {
    async getInstances () {
      var loadingTimer = setTimeout(() => {
        this.$set(
          this,
          'loading',
          true
        )
      }, 200)

      let instances = await this.$api.getByPage(
        this.info.path,
        this.info.limit,
        this.currentPage,
        true
      )

      this.$set(
        this,
        'instances',
        instances
      )

      clearTimeout(loadingTimer)

      this.$set(
        this,
        'loading',
        false
      )
    },
    goToEdit (instance) {
      let params = {}
      params[this.info.router.field] = instance[this.info.router.field]
      this.$router.push({ name: this.info.router.edit, params: params })
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
@import '@/modules/transitions.scss';

tbody {
  tr {
    cursor: pointer;
  }
}

.loading {
  margin: 0px auto 0px auto;
}
</style>
