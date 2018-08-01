<template>
  <form @submit.prevent="$emit('update', instance)">
    <table class="table">
      <tr v-for="field in fields">
        <td>{{ field.name }}</td>
        <td>
          <component
          v-bind="getComponentData(field)"
          @input="instance[field.identifier] = $event.target.value" >
          </component>
        </td>
      </tr>
    </table>
    <button class="btn btn-default btn-right" type="submit">Submit</button>
  </form>
</template>

<script>
import ImageInput from "@/components/inputs/ImageInput"
import TextInput from "@/components/inputs/TextInput"

const components = {
  'string': {
    is: 'input',
    type: 'text'
  },
  'text': {
    is: 'text-component'
  },
  'image': {
    is: 'image-component'
  }
}

export default {
  components: {
    'image-component': ImageInput,
    'text-component': TextInput
  },
  props: {
    instance: {
      required: false
    },
    fields: {
      required: true
    }
  },
  methods: {
    getComponentData (field) {
      let component = components[field.component]
      this.$set(component, 'value', this.instance[field.identifier])
      return component
    }
  }
}
</script>

<style lang="scss" scoped>
@import '@/modules/inputs.scss';
@import '@/modules/tables.scss';
@import '@/modules/buttons.scss';
</style>
