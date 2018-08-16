<template>
  <div id="app">
    <router-view />
  </div>
</template>

<style lang="scss">
$font-family-sans-serif:
  -apple-system,
  BlinkMacSystemFont,
  "Segoe UI",
  "Roboto",
  "Helvetica Neue", Arial, sans-serif,
  "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol" !default;


body {
    font-family: $font-family-sans-serif;
    background-color: #fdfdfd;
    margin: 0;
    color: rgb(60, 60, 60);
}

h1, h2, h3 {
  font-weight: 400;
}

.icon {
    outline: none;
    border: none;
    display: inline-block;
    width: 20px;
    height: 20px;

    &.left {
        background: transparent url(/assets/svg/arrow-left.svg) 0px 0px no-repeat;
        background-size: contain;
    }

    &.right {
        background: transparent url(/assets/svg/arrow-right.svg) 0px 0px no-repeat;
        background-size: contain;
    }

    &.menu {
      background: transparent url(/assets/svg/menu.svg) 0px 0px no-repeat;
      background-size: contain;
    }
}

</style>
