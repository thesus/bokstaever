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
        background: transparent url(/dashboard/assets/svg/arrow-left.svg) 0px 0px no-repeat;
        background-size: contain;
    }

    &.right {
        background: transparent url(/dashboard/assets/svg/arrow-right.svg) 0px 0px no-repeat;
        background-size: contain;
    }

    &.menu {
      background: transparent url(/dashboard/assets/svg/menu.svg) 0px 0px no-repeat;
      background-size: contain;
    }

    &.check {
      background: transparent url(/dashboard/assets/svg/check.svg) 0px 0px no-repeat;
      background-size: contain;
    }

    &.loading {
        display: block;
        border: 4px solid transparent;
        border-top: 4px solid rgb(44, 70, 127);
        border-radius: 50%;
        width: 30px;
        height: 30px;
        animation: spin 2s linear infinite;

        &.inline {
          display: inline-block;
          border-width: 2px;
          height: 10px;
          width: 10px;
        }

        &.inverse {
          border-color: transparent;
          border-top-color: white;
        }
    }
    @keyframes spin {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
}

</style>
