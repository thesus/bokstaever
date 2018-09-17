<template>
  <form @submit.prevent="$emit('update', instance)">
    <div class="edit">
      <div class="field" v-for="field in fields">
        <div class="label">{{ field.name }}</div>
        <div class="input">
          <component
          v-bind="getComponentData(field)"
          @input="instance[field.identifier] = $event.target.value" >
          </component>
        </div>
      </div>
    </div>
    <button class="btn btn-default btn-right" :class="{'success': $store.getters.isSucceded('send')}" type="submit">
      Submit
      <span v-if="$store.getters.isLoading('send')" class="icon loading inline inverse" />
      <span v-if="$store.getters.isSucceded('send')" class="icon check" />
    </button>
  </form>
</template>

<script>
import ImageInput from '@/components/inputs/ImageInput'
import TextInput from '@/components/inputs/TextInput'
import SelectInput from '@/components/inputs/SelectInput'

const components = {
  'string': {
    is: 'input',
    type: 'text'
  },
  'email': {
    is: 'input',
    type: 'email'
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
    'select-component': SelectInput
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
    }
  }
}
</script>

<style lang="scss" scoped>
@import '@/modules/inputs.scss';
@import '@/modules/buttons.scss';

.icon.check {
  height: 12px;
  width: 12px;
  margin-left: 3px;
}

.success, .success:hover {
  background-color: rgba(7, 112, 33, 0.9) !important;
}

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
