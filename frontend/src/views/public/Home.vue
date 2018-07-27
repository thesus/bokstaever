<template>
  <div class="home">
    <div class="post" v-for="post in posts">
      <router-link :to="{ name: 'detail', params: { slug: post.slug, id: post.id }}">
        <span class="image" :style="{ 'background-image': 'url(' + mediaRoot + post.image + ')' }"> </span>
        <div class="post-content" lang="en">
            <div class="post-text">
              <h2>{{ post.headline }}</h2>
              <p>{{ post.text | truncatechars(400) }}</p>
              <div class="post-footer">
                  {{ post.published }} →
              </div>
          </div>
        </div>
      </router-link>
    </div>
    <pagination-component :count="getPages"/>
  </div>
</template>

<script>
import Pagination from '@/components/Pagination'
import { truncatechars } from '@/filters/Text.js'
// @ is an alias to /src

export default {
  components: {
    'pagination-component': Pagination
  },
  filters: {
    'truncatechars': truncatechars
  },
  name: 'home',
  data () {
    return {
      apiRoot: process.env.VUE_APP_API_ROOT,
      mediaRoot: process.env.VUE_APP_MEDIA_ROOT,
      postCount: null,
      posts: [],
    }
  },
  mounted () {
    this.getPosts()
  },
  computed: {
    getPages () {
      let perPage = 5
      return Math.ceil(this.postCount / perPage)
    },
    getOffset () {
      return ((this.currentPage * 5) - 5)
    },
    currentPage () {
      return this.$route.query.page ? parseInt(this.$route.query.page) : 1
    }
  },
  methods: {
    getPosts () {
      console.log('fetching...')
      this.$http({
        method: 'get',
        url: this.apiRoot + '/posts/?limit=5&offset=' + this.getOffset,
      }).then((response) => {
        let data = response.data
        this.$set(this, 'posts', data.results ? data.results : [])
        this.$set(this, 'postCount', data.count ? data.count : 0)
      })
    }
  },
  watch: {
    currentPage () {
      this.getPosts()
    }
  }
}
</script>

<style lang="scss" scoped>
.post {
    &:nth-child(even) {
      .image{
         float: right;
      }
      .post-content {
          float: left;
      }
    }
    &:nth-child(odd) {
      .post-content {
        float: right;
      }
      .image {
        float: left;
      }
    }
    .post-content, .image {
        width: calc(50% - 10px);
        @media screen and (min-width: 581px) {
            height: 100%;
        }
        @media screen and (max-width: 580px) {
            width: 100% !important;
        }
    }
    .post-content {
        @media screen and (max-width: 990px) {
            width: calc(65% - 10px);
        }
        @media screen and (max-width: 580px) {
            margin-bottom: 15px;
        }
        color: #212529;
        position: relative;
        .post-text {
            position: relative;
            @media screen and (min-width: 581px) {
                position: absolute;
                width: 100%;
                top: 30%;
                transform: translateY(-30%);
            }
            p {
                hyphens: auto;
                word-break: break-word;
                text-align: justify;
            }

            .post-footer {
                float: right;
            }
        }
    }
    .image {
        background-repeat: no-repeat;
        background-position: center;
        background-size: cover;
        @media screen and (max-width: 990px) {
            width: calc(35% - 10px);
        }
        @media screen and (max-width: 580px) {
            height: 300px;
        }
    }

    display: block;
    position: relative;
    @media screen and (min-width: 581px) {
        height: 300px;
    }
    width: 60%;
    @media screen and (max-width: 1300px) {
        width: 95%;
    }
    margin: auto auto 30px auto;
}
</style>
