<template>
  <div class="image">
    <div class="image-list">
      <div v-if="images" v-for="image in images.results" class="thumbnail">
        <img
         :src="$mediaRoot + image.thumbnail"
         :class="{ 'selected': isSelected(image.id) }"
         @click="selectImage(image)"
        >
      </div>
    </div>

    <div class="pagination">
      <button :disabled="!(page > 1)" @click="page -= 1" class="icon left" />
      <button :disabled="!(page < images.pages)" @click="page += 1" class="icon right" />
    </div>
    <span v-if="multiple && selected.length >= 1">
      {{ selected.length }} {{ selected.length | pluralize('Image') }} selected.
    </span>
    <div v-if="multiple" class="btn-group">
      <button class="btn btn-default" :disabled="selected.length < 1" @click="selected = []">Clear</button>
      <button class="btn btn-default" :disabled="selected.length < 1" @click="$emit('selected', selected)">Select</button>
  </div>
</div>
</template>

<script>
import { pluralize } from '@/filters/Text'

export default {
  filters: {
    'pluralize': pluralize
  },
  props: {
    'multiple': Boolean,
    'limit': {
      type: Number,
      default: 15
    }
  },
  data () {
    return {
      images: {},
      page: 1,
      selected: [],
    }
  },
  mounted () {
    this.getImages()
  },
  methods: {
    isSelected (id) {
      if (this.$props.multiple) {
        return this.selected.includes(id)
      }
    },
    async getImages () {
      this.$set(
        this,
        'images',
        await this.$api.getByPage('/images/', this.limit, this.page, true)
      )
    },
    selectImage (image) {
      var id = image.id
      if (this.$props.multiple) {
        if (this.selected.includes(id)) {
          let index = this.selected.indexOf(id)
          this.selected.splice(index, 1)
        } else {
          this.selected.push(id)
        }
      } else {
        this.$emit('selected', image)
      }
    }
  },
  watch: {
    page () {
      this.getImages()
    }
  }
}
</script>

<style lang="scss" scoped>
@import '@/modules/pagination.scss';
@import '@/modules/buttons.scss';

$preview-size: 200px;

.image-list {
    display: grid;
    grid-template-columns: repeat(auto-fill, 200px);
    grid-gap: 10px;
    justify-content: space-between;
    width: 100%;
    .thumbnail {
        width: $preview-size;
        height: $preview-size;
    }
}

img {
    height: 100%;
    width: 100%;
    object-fit: cover;
}

.selected {
    outline: 3px solid rgb(44, 70, 127);
}

.btn-group {
  float: right;
  margin-right: 85px;
}
</style>
