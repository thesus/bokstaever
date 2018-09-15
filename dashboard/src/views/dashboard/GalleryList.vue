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
      posts: {},
      info: {
        limit: 10,
        path: '/galleries/',
        router: {
          field: 'id',
          edit: 'gallery-edit',
          create: 'gallery-create',
          createText: 'Create Gallery'
        }
      },
      fields: [
        {
          name: 'Name',
          identifier: 'name'
        },
        {
          name: 'Identifier',
          identifier: 'id'
        }
      ]
    }
  }
}
</script>
