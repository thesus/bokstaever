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
        model: 'settings',
        singleton: true,
        fields: [
          {
            name: 'Title',
            identifier: 'name',
            component: 'string'
          },
          {
            name: 'Info',
            identifier: 'info',
            component: 'text'
          },
          {
            name: 'Behavior',
            identifier: 'behavior',
            component: 'select',
            extra: [
              ['site', 'Site'],
              ['blog', 'Blog']
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
          },
          {
            name: 'E-Mail',
            identifier: 'email',
            component: 'email'
          },
          {
            name: 'Image',
            identifier: 'image',
            component: 'image',
            extra: {
              multiple: false,
              required: false
            }
          },
          {
            name: 'Pagesize',
            identifier: 'pagesize',
            component: 'number'
          }
        ]
      }
    }
  }
}
</script>
