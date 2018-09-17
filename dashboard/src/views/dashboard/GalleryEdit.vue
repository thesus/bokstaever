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
        router: {
          'field': 'id',
          'create': 'gallery-create',
          'edit': 'gallery-edit'
        },
        model: 'galleries',
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
        ]
      }
    }
  }
}
</script>
