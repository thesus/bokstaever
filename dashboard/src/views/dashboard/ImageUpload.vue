<template>

  <form enctype="multipart/form-data" v-on:submit.prevent="submitImages">
    <div class="image-upload">
      <label class="file-input">
        <span class="btn btn-default">Upload Images</span>
        <input
          type="file"
          multiple
          ref="upload"
          accept="image/*"
          @change="imageSelect">
      </label>
      <div class="image-list">
        <div class="thumbnail" v-for="image in images" v-if="images">
          <img :src="image.url" :class="{uploading: showProgress(image)}">
          <div
            class="progress"
            v-show="showProgress(image)"
            v-bind:style="{height: 'calc(' + image.progress + '% - 10px)'}">
          </div>
          <input type="text" v-model="image.title" :disabled="showProgress(image)">
        </div>
      </div>
    </div>
    <button class="btn btn-default btn-right" type="submit">Submit</button>
  </form>

</template>

<script>
export default {
  data() {
    return {
      'images': []
    }
  },
  methods: {
    showProgress: (image) => {
      return image.progress > 0 && image.progress < 100
    },
    imageSelect (event) {
      this.images = []
      let images = this.$refs.upload.files
      for (let i = 0; i < images.length; i++) {
        let name = images[i].name
        let title = name.substring(0, name.lastIndexOf('.'))

        this.images.push({
          'title': title,
          'file': images[i],
          'url': URL.createObjectURL(images[i]),
          'progress': 0
        })
      }
    },
    submitImages () {
      for (let image of this.images) {
        this.uploadImage(image)
      }
    },
    uploadImage (image) {
      image.progress = 0.1
      let formData = new FormData()
      formData.append('image', image.file)
      formData.append('title', image.title)

      this.$api.sendFile('/images/', formData, 'post', true, image)
    }
  }
}
</script>


<style lang="scss" scoped>
@import '@/modules/buttons.scss';
@import '@/modules/thumbnails.scss';
@import '@/modules/inputs.scss';

.uploading {
  filter: brightness(0.6) blur(0.8px);
}

.thumbnail {
  position: relative;
  margin-bottom: 30px;
}

.progress {
  position: absolute;
  width: 3px;
  height: 0%;
  background-color: #ccc;
  bottom: 5px;
  right: 5px;
  border-radius: 2px;
}
</style>
