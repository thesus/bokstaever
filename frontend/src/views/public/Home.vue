<template>
  <div class="home">
    <div class="post" v-for="post in posts.results">
      <router-link :to="{ name: 'detail', params: { id: post.id, slug: post.slug }}">
        <span class="image" :style="{ 'background-image': 'url(' + $mediaRoot + post.image + ')' }"> </span>
        <div class="post-content" lang="en">
            <div class="post-text">
              <h2>{{ posts.headline }}</h2>
              <p>{{ post.text | truncatechars(400) }}</p>
              <div class="post-footer">
                  {{ post.published }} →
              </div>
          </div>
        </div>
      </router-link>
    </div>
    <pagination-component :count="posts.pages"/>
  </div>
</template>

<script>
import Pagination from '@/components/Pagination'
import { truncatechars } from '@/filters/Text.js'

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
      posts: {},
    }
  },
  mounted () {
    this.getPosts()
  },
  computed: {
    currentPage () {
      return parseInt(this.$route.query.page) || 1
    }
  },
  methods: {
    async getPosts () {
      this.$set(
        this,
        'posts',
        await this.$api.getByPage('/posts/', 5, this.currentPage)
      )
    }
  },
  watch: {
    currentPage () {
      this.getPosts()
    }
  }
}
</script>

<style lang="scss" slot-scoped>
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
