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
            name: 'Short information for the footer',
            identifier: 'info',
            component: 'text'
          },
          {
            name: 'E-Mail',
            identifier: 'email',
            component: 'email'
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
