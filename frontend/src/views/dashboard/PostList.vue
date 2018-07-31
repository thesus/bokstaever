<template>
  <div>
    <table class="table table-list">
        <thead>
            <tr>
                <th>ID</th>
                <th>Date</th>
                <th>Headline</th>
                <th>Draft</th>
            </tr>
        </thead>
        <tbody>
            <tr
             v-for="post in posts.results"
             @click="$router.push({ name: 'post-edit', params: { id: post.id }})"
             class="posts">
                <td>{{ post.id }}</td>
                <td>{{ post.published }}</td>
                <td>{{ post.headline }}</td>
                <td>{{ post.draft }}</td>
            </tr>
        </tbody>
    </table>
    <pagination-component :count="posts.pages" />
    <router-link class="btn btn-default btn-right" :to="{name: 'post-create'}">New Post</router-link>
  </div>
</template>

<script>
import Pagination from '@/components/Pagination'

export default {
  components: {
    'pagination-component': Pagination
  },
  data () {
    return {
      posts: {}
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
        await this.$api.getByPage('/posts/', 8, this.currentPage, true)
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

<style lang="scss" scoped>
@import '@/modules/tables.scss';
@import '@/modules/buttons.scss';

.posts {
  cursor: pointer;
}
</style>
