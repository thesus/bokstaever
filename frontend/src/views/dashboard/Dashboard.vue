<template>
  <div>
    <nav class="navbar">
      <div class="container">
        <ul>
            <li><router-link to="/">Home</router-link></li>
            <li><router-link to="/dashboard">Dashboard</router-link></li>
            <li><router-link to="/dashboard/post/list/1">Posts</router-link></li>
            <li><router-link to="/dashboard/images/list/1">Images</router-link></li>
            <li><router-link to="/dashboard/settings/edit">Settings</router-link></li>
        </ul>
      </div>
    </nav>
    <router-view/>
  </div>
</template>

<script>

</script>

<style lang="scss" scoped>

.navbar {
    display: block;
    width: calc(100% - 16px);
    background: #fff;
    border-top: 1px solid #eee;
    border-bottom: 1px solid #eee;
    margin: 8px 8px 10px 8px;

    .container {
        width: 100%;
        margin: 0;
    }

    ul {
        list-style: none;
        margin: 0px 5px 0px 10px;
        padding: 0;
        display: flex;
        justify-content: center;
        @media screen and (max-width: 700px) {
            flex-flow: column;
        }
        @media screen and (min-width: 701px) {
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
            @media screen and (max-width: 700px) {
                &:not(:last-child) {
                    border-bottom: 1px solid #eee;
                }
            }
        }
    }
}
</style>
