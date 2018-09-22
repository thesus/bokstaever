<template>
  <div class="image">
    <div class="image-list">
      <div v-if="images" v-for="image in images.results" class="thumbnail" :key="image.id">
        <img
         :src="image.thumbnail"
         :class="{ 'selected': isSelected(image.id) }"
         @click="selectImage(image)"
        >
      </div>
    </div>

    <div class="pagination">
      <button type="button" :disabled="!(page > 1)" @click="page -= 1" class="icon left" />
      <button type="button" :disabled="!(page < images.pages)" @click="page += 1" class="icon right" />
    </div>
    <div v-if="multiple || !required" class="footer-group">

      <span v-if="multiple && selected.length >= 1">
        {{ selected.length }} {{ selected.length | pluralize('Image') }} selected.
      </span>

      <input type="button" class="btn btn-default" v-if="multiple" :disabled="(selected.length < 1)" @click="selected = []" value="Clear">

      <input type="button" class="btn btn-default" v-if="!multiple && !required" @click="$emit('submit', null)" value="Clear">

      <input type="button" class="btn btn-default" v-if="multiple" :disabled="!required ? false : (selected.length < 1)" @click="$emit('submit', selected)" value="Select">
  </div>
</div>
</template>

<script>
import { Request } from '@/utils'
import { pluralize } from '@/filters/Text'

export default {
  filters: {
    'pluralize': pluralize
  },
  props: {
    'multiple': Boolean,
    'required': {
      type: Boolean,
      default: true
    },
    'limit': {
      type: Number,
      default: 15
    },
    'value': {
    }
  },
  data () {
    return {
      images: {},
      page: 1,
      selected: (Array.isArray(this.value)) ? this.value : []
    }
  },
  mounted () {
    this.getImages()
  },
  methods: {
    isSelected (id) {
      if (this.multiple) {
        return this.selected.includes(id)
      }
    },
    async getImages () {
      try {
        let request = new Request()
        this.$set(
          this,
          'images',
          await request.list('images', this.limit, this.page)
        )
      } catch (e) {} // Discard error
    },
    selectImage (image) {
      var id = image.id
      if (this.multiple) {
        if (this.selected.includes(id)) {
          let index = this.selected.indexOf(id)
          this.selected.splice(index, 1)
        } else {
          this.selected.push(id)
        }
      } else {
        this.$emit('submit', id)
      }
    }
  },
  watch: {
    page () {
      this.getImages()
    },
    value () {
      if (Array.isArray(this.value)) {
        this.selected = this.value
      }
    }
  }
}
</script>

<style lang="scss" scoped>
@import '@/modules/pagination.scss';
@import '@/modules/buttons.scss';
@import '@/modules/thumbnails.scss';
@import '@/modules/inputs.scss';

.selected {
    outline: 3px solid rgb(44, 70, 127);
}

.thumbnail {
  cursor: pointer;
}

.footer-group {
  float: right;
}
</style>
