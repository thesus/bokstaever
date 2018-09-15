<template>

  <form enctype="multipart/form-data" v-on:submit.prevent="submitImages">
    <notifications />
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
          <img
            :src="image.url"
            :class="{
              uploading: showProgress(image),
              success: image.success,
              failure: (image.success === false)
            }"
          >
          <div
            class="progress"
            v-show="showProgress(image)"
            v-bind:style="{height: 'calc(' + image.progress + '% - 10px)'}">
          </div>
          <input type="text" v-model="image.title" :disabled="showProgress(image) || image.success">
        </div>
      </div>
    </div>
    <button class="btn btn-default btn-right" type="submit">Submit</button>
  </form>

</template>

<script>
export default {
  data () {
    return {
      'images': {}
    }
  },
  methods: {
    showProgress (image) {
      return image.progress > 0 && !(image.success != null)
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
        this.$set(image, 'success', (!image.success ? null : true))

        if (image.success === null) {
          this.uploadImage(image)
        }
      }
    },
    async uploadImage (image) {
      this.$set(image, 'progress', 0.1)

      let formData = new FormData()
      formData.append('image', image.file)
      formData.append('title', image.title)

      try {
        let request = await this.$api.sendFile(
          '/images/',
          formData,
          'post',
          true,
          image
        )

        if (request) {
          this.$set(image, 'success', true)
        }
      } catch (error) {
        this.$set(image, 'success', false)

        if (error.response && error.response.data && error.response.data.title) {
          this.$notify({
            type: 'danger',
            title: 'An Error occurred!',
            text: image.title + ' : ' + error.response.data.title[0] +
                  ' Change the title and try again!'
          })
        } else {
          this.$notify({
            type: 'danger',
            title: 'Error!',
            text: 'Unknown error occurred!',
            timeout: 5000
          })
        }
      }
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

.success, .failure {
  box-sizing: border-box;
}

.success {
  border: 5px solid green;
}

.failure {
  border: 5px solid red;
}

.thumbnail {
  position: relative;
  margin-bottom: 42px;
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
