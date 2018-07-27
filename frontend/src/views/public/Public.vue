<template>
  <div>
    <input type="checkbox" class="menu-checkbox" id="menu">
    <nav class="navbar">
      <label class="menu-toggle" for="menu"><span>Menu</span></label>
      <div class="container">
        <ul>
          <li><router-link :to="{ name: 'home' }">Home</router-link></li>
          <li><router-link :to="{ name: 'dashboard'}">Dashboard</router-link></li>
          <li><a href="/impressum">Impressum</a></li>
          <li><a href="/accounts/login">Login</a></li>
        </ul>
      </div>
    </nav>
    <router-view/>
  </div>
</template>

<style lang="scss" scoped>
.navbar {
    position: absolute;
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
</style>
