<template>
  <div>
    <input type="checkbox" class="menu-checkbox" id="menu">
    <nav class="navbar">
      <label class="menu-toggle" for="menu"><span>Menu</span></label>
      <div class="container">
        <ul>
          <li><router-link :to="{ name: 'home' }">Home</router-link></li>
          <li>
            <router-link v-if="isLoggedIn" :to="{ name: 'dashboard'}">
              Dashboard
            </router-link>
          </li>
          <li v-for="page in pages.results">
            <router-link :to="{ name: 'page', params: { slug: page.slug } }">{{ page.slug }}</router-link>
          <li>
            <router-link v-if="isLoggedIn" :to="{ name: 'logout'}">
              Logout
            </router-link>
          </li>
          <li>
            <router-link v-if="!isLoggedIn" :to="{ name: 'login'}">
              Login
            </router-link>
          </li>
        </ul>
      </div>
    </nav>
    <router-view/>
    <footer class="footer">
        <div class="container">
            <h3 class="title">{{ info.name }}</h3>
            <div class="contact">
                  <span class="contact-type">E-Mail</span>
                  <span class="contact"><a :href="'mailto:' + info.email">{{ info.email }}</a></span>
            </div>
            <div class="info">
                {{ info.info }}
            </div>
       </div>
   </footer>
  </div>
</template>

<script>
export default {
  data () {
    return {
      info: {},
      pages: {}
    }
  },
  mounted() {
    this.getInfo()
    this.getPages()
  },
  computed: {
    isLoggedIn () {
      return localStorage.getItem('jwt_token') ? true : false
    }
  },
  methods: {
    async getInfo() {
      this.$set(
        this,
        'info',
        await this.$api.get('/settings/')
      )
    },
    async getPages() {
      this.$set(
        this,
        'pages',
        await this.$api.get('/pages/')
      )
    }
  }
}
</script>

<style lang="scss" scoped>
.navbar {
    position: fixed;
    top: 0;
    left: 0;
    background: #fff;
    width: 220px;
    height: 100%;
    transform: translate3d(-220px, 0, 0);
    transition: transform .35s;
    z-index: 1000;
    // border-right: 1px solid #eee;
    // box-sizing: border-box;
    ul {
        list-style: none;
        padding: 0px 10px 0px 15px;
        li {
            text-transform: uppercase;
            letter-spacing: .2rem;
            line-height: 3rem;
            border-bottom: 1px solid #eee;
            a {
                text-decoration: none;
                color: #222;
                width: 100%;
                display: block;
            }
        }
    }
}

label.menu-toggle {
    // border-right: 1px solid #eee;
    // border-bottom: 1px solid #eee;
    // box-sizing: border-box;
    position: absolute;
    right: -60px;
    width: 60px;
    height: 60px;
    line-height: 0;
    display: block;
    text-indent: -9999px;
    background: #fff url(/assets/svg/menu.svg) 50% 50% / 25px 25px no-repeat;
    cursor: pointer;
}

.menu-checkbox {
    display: none;
}

.menu-checkbox:checked + .navbar {
    transform: translate3d(0, 0, 0);
}


.footer {
    display: block;
    background: #fdfdfd;
    border-top: 1px solid #eee;
    position: relative;
    margin-top: 25px;
    padding-bottom: 10px;

    .container {
        display: grid;
        column-gap: 40px;
        grid-template-areas:
          'header header header'
          'left right right';
        margin: auto;
        @media screen and (min-width: 1200px) {
            width: 40%;
        }
        @media screen and (min-width: 700px) and (max-width: 1200px){
            width: 70%;
        }
        @media screen and (max-width: 700px) {
            width: 90%;
        }

       .title {
           grid-area: header;
           color: #222;
           text-transform: lowercase;
       }

       .contact {
          grid-area: left;
          display: block;
          a {
            text-decoration: none;
            color: #0088cc;
          }
       }

       .info {
         grid-area: right;
         color: #828282;
       }
    }
}
</style>
