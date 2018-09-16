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
        limit: 16,
        path: 'posts',
        router: {
          field: 'id',
          edit: 'post-edit',
          create: 'post-create',
          createText: 'Create Post'
        }
      },
      fields: [
        {
          name: 'ID',
          identifier: 'id'
        },
        {
          name: 'Headline',
          identifier: 'headline'
        },
        {
          name: 'Date',
          identifier: 'published'
        }
      ]
    }
  }
}
</script>
