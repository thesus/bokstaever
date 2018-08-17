<template>
  <div class="image-select">
    <div class="current-image" v-if="image">
      <img :src="image.thumbnail">
    </div>
    <span class="multiple" v-if="extra.multiple">{{ imageCount }} {{ imageCount|pluralize('Image') }} selected</span>
    <button type="button" class="btn btn-default" @click="showModal = true">
      Select Image
    </button>
    <modal-component v-if="showModal" @close="showModal = false">
      <image-component @selected="selectImage" :value="value" :multiple="extra['multiple']"/>
    </modal-component>
  </div>
</template>

<script>
import ImageSelect from '@/components/ImageSelect'
import Modal from '@/components/Modal'
import { pluralize } from '@/filters/Text'

export default {
  filters: {
    'pluralize': pluralize
  },
  components: {
    'modal-component': Modal,
    'image-component': ImageSelect
  },
  props: {
      'value': {
        required: false
      },
      'extra': {
        type: Object,
        default: () => {
          return {
            multiple: false
          }
        }
      }
  },
  data () {
    return {
      image: null,
      showModal: false,
      count: 0
    }
  },
  mounted () {
    this.getImage()
  },
  computed: {
    imageCount () {
      if (Array.isArray(this.value)) {
        return this.value.length
      } else if (this.extra.multiple) {
        return this.count
      }
    }
  },
  methods: {
    async getImage (value=this.value) {
      if (value !== undefined && !(Array.isArray(value))) {
        this.$set(
          this,
          'image',
          await this.$api.get(`/images/${value}/`, true)
        )
      }
    },
    selectImage (value) {
      this.$emit(
        'input',
        { target: { value: value } }
      )
      if (this.value === undefined) {
        this.getImage(value)
        this.count = Array.isArray(value) ? value.length : undefined
      }
      this.showModal = false
    }
  },
  watch: {
    value () {
      this.getImage()
    }
  }
}
</script>

<style lang="scss" scoped>
@import '@/modules/buttons.scss';

.image-select {
    display: flex;

    .btn {
      margin: auto 0 auto 0;
    }
}

.multiple {
  margin: 5px 5px 5px 0px;
}

.current-image {
  height: 150px;
  width: 150px;
  margin-right: 8px;
  img {
      height: 100%;
      width: 100%;
      object-fit: cover;
  }
}
</style>
