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
            identifier: 'name',
            component: 'string'
          },
          {
            name: 'Image',
            identifier: 'images',
            component: 'image',
            extra: {
              'multiple': true
            }
          }
        ],
        router: {
          'field': 'id',
          'create': 'gallery-create',
          'edit': 'gallery-edit'
        },
        url: '/galleries/'
      }
    }
  }
}
</script>
