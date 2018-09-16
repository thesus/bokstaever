<template>
  <list-component :fields="fields" :info="info" />
</template>

<script>
import List from '@/components/List'

export default {
  components: {
    'list-component': List
  },
  data () {
    return {
      info: {
        limit: 8,
        path: '/pages/',
        router: {
          field: 'slug',
          edit: 'page-edit',
          create: 'page-create',
          createText: 'Create Page'
        }
      },
      fields: [
        {
          name: 'Slug',
          identifier: 'slug'
        },
        {
          name: 'Headline',
          identifier: 'headline'
        }
      ]
    }
  }
}
</script>
