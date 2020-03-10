<template>
  <nav class="navbar">
    <div class="navbar-toggle-container">
      <span class="navbar-toggle icon menu" @click="open = !open" />
    </div>
    <div class="container">
      <transition name="menu">
        <ul
          v-show="isCollapsed"
          :class="{ notransition: shouldCollapse }"
          @click="open = false"
        >
          <li><a href="/">Home</a></li>
          <li><router-link :to="{ name: 'dashboard' }">Dashboard</router-link></li>
          <li><router-link :to="{ name: 'post-list' }">Posts</router-link></li>
          <li><router-link :to="{ name: 'page-list' }">Pages</router-link></li>
          <li><router-link :to="{ name: 'image-list' }">Images</router-link></li>
          <li><router-link :to="{ name: 'gallery-list' }">Galleries</router-link></li>
          <li><router-link :to="{ name: 'logout' }">Logout</router-link></li>
        </ul>
      </transition>
    </div>
  </nav>
</template>

<script>
export default {
  data () {
    return {
      width: 0,
      open: false
    }
  },
  computed: {
    shouldCollapse () {
      return this.width >= 980
    },
    isCollapsed () {
      return this.shouldCollapse ? true : this.open
    }
  },
  mounted () {
    this.$nextTick(() => {
      window.addEventListener('resize', this.setWidth)
    })
    this.setWidth()
  },
  beforeDestroy () {
    window.removeEventListener('resize', this.setWidth)
  },
  methods: {
    setWidth () {
      this.width = document.documentElement.clientWidth
    }
  }
}
</script>

<style lang="scss" scoped>
$should_collapse: 980px;

.menu-enter-active, .menu-leave-active {
  transition: opacity .2s;
}
.menu-enter, .menu-leave-to {
  opacity: 0;
}
.menu-enter-to, .menu-leave {
  opacity: 1;
}

.notransition {
  transition: none !important;
}

.navbar-toggle-container {
  width: 100%;
  height: 50px;
  @media screen and (min-width: $should_collapse) {
    display: none;
  }
}

.navbar-toggle {
    cursor: pointer;
    margin: 15px 25px 15px 0px;
    float: right;
    @media screen and (min-width: $should_collapse) {
      display: none
    }
}

.navbar {
    width: 100%;
    background: rgb(34, 34, 34);
    margin: 0px 0px 10px 0px;

    .container {
        width: 100%;
        margin: 0;
    }

    ul {
        border-top: 1px solid #ccc;
        border-bottom: 1px solid #ccc;
        list-style: none;
        margin: 0px;
        padding: 0;
        display: flex;
        justify-content: center;
        @media screen and (max-width: $should_collapse - 1px) {
            flex-flow: column;
            padding: 0px 4px 0px 4px;
        }
        @media screen and (min-width: $should_collapse) {
            li:not(:first-child):not(:last-child){
                margin-left: 16px;
                margin-right: 16px;
            }
            li:first-child {
                margin-right: 16px;
            }
            li:last-child {
                margin-left: 16px;
            }
        }
        li {
            text-transform: uppercase;
            letter-spacing: .2rem;
            position: relative;
            line-height: 3rem;
            height: 3rem;
            a {
                text-decoration: none;
                color: #ccc;
                width: 100%;
                display: block;
                margin: 0;
                padding: 0;
            }
            @media screen and (max-width: $should_collapse - 1px) {
                padding-left: 4px;
                &:not(:last-child) {
                    border-bottom: 1px solid #ccc;
                }
            }
        }
    }
}
</style>
