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
              component: 'string',
            },
            {
              name: 'E-Mail',
              identifier: 'email',
              component: 'email'
            },
            {
              name: 'Info',
              identifier: 'info',
              component: 'text'
            },
            {
              name: 'Image',
              identifier: 'image',
              component: 'image'
            },
            {
              name: 'Behavior',
              identifier: 'behavior',
              component: 'select',
              extra: [
                ['site', 'Site'],
                ['blog', 'Blog'],
              ]
            },
            {
              name: 'Theme',
              identifier: 'theme',
              component: 'select',
              extra: [
                ['css/brevlada.css', 'brevlåda'],
                ['css/frimarke.css', 'frimärke']
              ]
            }
        ],
        url: '/settings/',
        singleton: true
      }
    }
  }
}
</script>
