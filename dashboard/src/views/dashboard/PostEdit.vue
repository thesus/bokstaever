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
            component: 'string'
          },
          {
            name: 'Text',
            identifier: 'text',
            component: 'text'
          },
          {
            name: 'Type',
            identifier: 'type',
            component: 'select',
            extra: [
              ['md', 'Markdown'],
              ['html', 'HTML'],
              ['mdhtml', 'Markdown with inline HTML'],
              ['raw', 'Raw with linebreaks']
            ]
          },
          {
            name: 'Image',
            identifier: 'image',
            component: 'image',
            extra: {
              multiple: false
            }
          }
        ],
        router: {
          'field': 'id',
          'create': 'post-create',
          'edit': 'post-edit'
        },
        model: 'posts'
      }
    }
  }
}
</script>
