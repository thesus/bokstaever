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
              uploading: showProgress(image.id),
              success: (imageSuccess(image.id) === true),
              failure: (imageSuccess(image.id) === false)
            }"
          >
          <div
            class="progress"
            v-show="showProgress(image.id)"
            v-bind:style="{height: 'calc(' + $store.getters.getProgress(image.id) + '% - 10px)'}"
          >
          </div>
          <input
            type="text"
            v-model="image.title"
            :disabled="showProgress(image.id) || imageSuccess(image.id)"
          >
        </div>
      </div>
    </div>
    <button class="btn btn-default btn-right" type="submit">Submit</button>
  </form>

</template>

<script>
import { Request } from '@/utils'

export default {
  data () {
    return {
      'images': []
    }
  },
  methods: {
    imageSuccess (id) {
      if (this.$store.getters.requestExists(id) && !this.$store.getters.isLoading(id)) {
        return this.$store.getters.isSucceded(id)
      } else {
        return null
      }
    },
    showProgress (id) {
      let progress = this.$store.getters.getProgress(id) || 0
      return progress > 0 && this.$store.getters.isLoading(id)
    },
    imageSelect (event) {
      this.$store.dispatch('reset')

      this.images = []
      let images = this.$refs.upload.files
      let i = 0

      for (let image of images) {
        let name = image.name
        let title = name.substring(0, name.lastIndexOf('.'))

        this.images.push({
          'title': title,
          'file': image,
          'url': URL.createObjectURL(image),
          'id': 'image_' + i
        })

        i++
      }
    },
    submitImages () {
      for (let image of this.images) {
        if (this.imageSuccess(image.id) !== true) {
           this.uploadImage(image)
        }
      }
    },
    async uploadImage (image) {
      let data = new FormData()
      data.append('image', image.file)
      data.append('title', image.title)
      try {
        let request = new Request(image.id)

        await request.upload(
          'images',
          undefined,
          data,
          image.id
        )
      } catch (error) {
        if (error.response && error.response.data && error.response.data.title) {
          this.$notify({
            type: 'danger',
            title: 'An Error occurred!',
            text: image.title + ' : ' + error.response.data.title[0] +
                  ' Change the title and try again!',
            timeout: 5000
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
