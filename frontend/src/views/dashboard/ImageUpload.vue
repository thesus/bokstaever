<template>
  <form enctype="multipart/form-data" v-on:submit.prevent="submitImages">
    <table class="table">
      <tr>
        <td>Images</td>
        <td>
          <input
            type="file"
            multiple
            ref="upload"
            accept="image/*"
            @change="imageSelect">
        </td>
      </tr>
    </table>
    <div class="preview-container">
      <div class="preview" v-for="image in images" v-if="images">
        <div class="image-preview">
          <img :src="image.url" :class="{uploading: showProgress(image)}">
          <div
            class="progress"
            v-show="showProgress(image)"
            v-bind:style="{height: 'calc(' + image.progress + '% - 10px)'}">
          </div>
        </div>
        <input type="text" v-model="image.title" :disabled="showProgress(image)">
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

$preview-size: 200px;

input[type=text], input[type=email] {
    border-radius: 0;
    border: 1px solid #ccc;
    width: calc(100% - 5px);
}

.preview-container {
    display: flex;
    width: calc(100vw - 16px);
    flex-flow: row wrap;
    justify-content: flex-start;
    align-content: space-between;
    .preview {
        width: $preview-size;
        margin: 5px;
        .image-preview {
            width: $preview-size;
            height: $preview-size;
            margin-bottom: 2px;
            position: relative;
            img {
                height: 100%;
                width: 100%;
                object-fit: cover;
                &.uploading {
                    filter: brightness(0.6) blur(0.8px);
                }
            }
            .progress {
                position: absolute;
                width: 2px;
                height: 0%;
                background-color: #ccc;
                bottom: 5px;
                right: 5px;
                border-radius: 2px;
            }
        }
    }
}
</style>
