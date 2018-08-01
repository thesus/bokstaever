<template>
  <div class="image-select">
    <div class="current-image" v-if="image">
      <img :src="image.thumbnail">
    </div>
    <button class="btn btn-default" @click="showModal = true">
      Select Image
    </button>
    <modal-component v-if="showModal" @close="showModal = false">
      <image-component @selected="selectImage"/>
    </modal-component>
  </div>
</template>

<script>
import ImageSelect from '@/components/ImageSelect'
import Modal from '@/components/Modal'

export default {
  components: {
    'modal-component': Modal,
    'image-component': ImageSelect
  },
  props: [
      'value'
  ],
  data () {
    return {
      image: null,
      showModal: false
    }
  },
  mounted () {
    this.getImage()
  },
  methods: {
    async getImage () {
      if (this.value !== undefined) {
        this.$set(
          this,
          'image',
          await this.$api.get(`/images/${this.value}/`, true)
        )
      }
    },
    selectImage (value) {
      this.$emit(
        'input',
        { target: { value: value } }
      )
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
