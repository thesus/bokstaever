<template>
  <update-component v-bind="data" />
</template>

<script>
import Update from '@/components/Update'

export default {
  components: {
    'update-component': Update
  },
  data () {
    return {
      data: {
        fields: [
            {
              name: 'Title',
              identifier: 'headline',
              component: 'string',
            },
            {
              name: 'Text',
              identifier: 'text',
              component: 'text'
            },
            {
              name: 'Image',
              identifier: 'image',
              component: 'image'
            }
        ],
        router: {
          'field': 'slug',
          'create': 'page-create',
          'edit': 'page-edit'
        },
        url: '/pages/'
      }
    }
  }
}
</script>
