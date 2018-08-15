<template>
  <div class="dashboard">
    <div class="navbar-toggle-container">
      <span type="checkbox" class="navbar-toggle icon menu" @click="open = !open" />
    </div>
    <nav class="navbar">
      <div class="container">
        <transition name="menu">
          <ul v-if="isCollapsed" :class="{  notransition: shouldCollapse }">
            <li><a href="/">Home</a></li>
            <li><router-link :to="{ name: 'dashboard' }">Dashboard</router-link></li>
            <li><router-link :to="{ name: 'post-list' }">Posts</router-link></li>
            <li><router-link :to="{ name: 'page-list' }">Pages</router-link></li>
            <li><router-link :to="{ name: 'image-list' }">Images</router-link></li>
            <li><router-link :to="{ name: 'settings-edit' }">Settings</router-link></li>
            <li><router-link :to="{ name: 'logout' }">Logout</router-link></li>
          </ul>
        </transition>
      </div>
    </nav>
    <div class="content">
      <router-view/>
    </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      open: false,
      width: null
    }
  },
  computed: {
    shouldCollapse () {
      return this.width >= 800
    },
    isCollapsed () {
      return this.shouldCollapse ? true : this.open
    }
  },
  mounted () {
    this.$nextTick(function() {
      window.addEventListener('resize', this.getWidth)
    })

    this.getWidth()
  },
  beforeDestroy () {
    window.removeEventListener('resize', this.getWidth)
  },
  methods: {
    getWidth () {
      this.width = document.documentElement.clientWidth
    }
  }
}
</script>

<style lang="scss" scoped>
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

.dashboard {
  margin-top: 10px;
}

.navbar-toggle-container {
  width: 100%;
  height: 33px;
  @media screen and (min-width: 800px) {
    display: none;
  }
}

.navbar-toggle {
    cursor: pointer;
    margin: 5px 25px 0px 0px;
    float: right;
    @media screen and (min-width: 800px) {
      display: none
    }
}

.navbar {
    width: 100%;
    background: #fff;
    margin: 0px 0px 10px 0px;

    .container {
        width: 100%;
        margin: 0;
    }

    ul {
        border-top: 1px solid #eee;
        border-bottom: 1px solid #eee;
        list-style: none;
        margin: 0px;
        padding: 0;
        display: flex;
        justify-content: center;
        @media screen and (max-width: 799px) {
            flex-flow: column;
            padding-left: 8px;
        }
        @media screen and (min-width: 800px) {
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
            line-height: 4rem;
            height: 4rem;
            a {
                text-decoration: none;
                color: #222;
                width: 100%;
                display: block;
                margin: 0;
                padding: 0;
            }
            @media screen and (max-width: 799px) {
                &:not(:last-child) {
                    border-bottom: 1px solid #eee;
                }
            }
        }
    }
}

.content {
  padding: 8px;
}
</style>
