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
    <a class="btn btn-default btn-right" href="/dashboard/post/edit/">New Post</a>
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
table {
    &.table {
        width: 100%;
        border-collapse: collapse;

        th, td {
            text-align: left;
            padding: 10px;
            border-left: 0;
            border-right: 0;
            border-bottom: 1px solid #ddd;
        }

        .posts {
            cursor: pointer;
        }

        &.table-list {
            tbody tr {
                &:hover {
                    background-color: #f5f5f5
                }
            }
        }
    }
}
</style>
