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
            }
        ],
        router: {
          'field': 'id',
          'create': 'post-create',
          'edit': 'post-edit'
        },
        url: '/posts/'
      }
    }
  }
}
</script>
