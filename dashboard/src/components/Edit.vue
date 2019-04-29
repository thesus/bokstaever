<template>
  <form @submit.prevent="$emit('submit', instance)">
    <div class="edit">
      <div class="field" v-for="field in fields" :key="field.identifier">
        <div class="label">{{ field.name }}</div>
        <div class="input">
          <component
          v-bind="getComponentData(field)"
          @input="update(field.identifier, $event.target.value)"
          >
          </component>
        </div>
      </div>
    </div>
  </form>
</template>

<script>
import ImageInput from '@/components/inputs/ImageInput'
import TextInput from '@/components/inputs/TextInput'
import BooleanInput from '@/components/inputs/BooleanInput'
import SelectInput from '@/components/inputs/SelectInput'

const components = {
  'string': {
    is: 'input',
    type: 'text'
  },
  'number': {
    is: 'input',
    type: 'number'
  },
  'email': {
    is: 'input',
    type: 'email'
  },
  'checkbox': {
    is: 'boolean-component'
  },
  'text': {
    is: 'text-component'
  },
  'image': {
    is: 'image-component'
  },
  'select': {
    is: 'select-component'
  }
}

export default {
  components: {
    'image-component': ImageInput,
    'text-component': TextInput,
    'select-component': SelectInput,
    'boolean-component': BooleanInput
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
      if ('extra' in field) {
        this.$set(component, 'extra', field.extra)
      }
      return component
    },
    update (identifier, value) {
      this.$set(this.instance, identifier, value)
      this.$emit('input')
    }
  }
}
</script>

<style lang="scss" scoped>
@import '@/modules/inputs.scss';
@import '@/modules/buttons.scss';

.edit {
  .field {
    border-bottom: 1px solid #eee;
    display: inline-flex;
    box-sizing: border-box;
    width: 100%;
    padding: 5px;

    .label {
      margin: auto;
      width: 10%;
    }
    .input {
      width: 90%;
    }

    @media screen and (max-width: 1600px){
      .label {
        width: 15%;
      }
      .input {
        width: 85%;
      }
    }
    @media screen and (max-width: 1000px) {
      .label {
        width: 20%;
      }
      .input {
        width: 80%;
      }
    }
    @media screen and (max-width: 800px) {
      flex-direction: column;
      .label {
        margin: auto auto 5px auto;
        width: 100%;
      }
      .input {
        width: 100%;
      }
    }
  }
}
</style>
