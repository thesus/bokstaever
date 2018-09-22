<template>
  <transition name="modal">
      <div class="modal-mask">
          <div class="modal-wrapper">
              <div class="modal-container">
                  <h3 v-if="title">{{ title }}</h3>
                  <div class="modal-content">
                      <slot></slot>
                  </div>
                  <span class="btn-modal" @click="$emit('close')" />
              </div>
          </div>
      </div>
  </transition>
</template>

<script>
export default {
  props: ['title']
}
</script>

<style lang="scss" scoped>
@import "@/modules/buttons.scss";

.modal-mask {
    position: fixed;
    z-index: 10000;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, .5);
    transition: opacity .3s;
    display: table;
}

.modal-wrapper {
    display: table-cell;
    vertical-align: middle;
}

.modal-container {
    @media screen and (min-width: 1200px) {
      max-width: 60vw;
    }

    width: auto;

    min-width: 100px;
    max-width: 90vw;

    background-color: #fff;
    margin: 0px auto;
    position: relative;

    overflow: hidden;

    h3 {
      padding: 8px 0 0 15px;
      min-height: 28px;
      width: calc(100% - 55px);
      margin: 0;
    }

    .modal-content {
        box-sizing: border-box;
        padding: 8px;
        width: 100%;

        min-height: 60px;
        max-height: 85vh;

        overflow-x: hidden;
        overflow-y: auto;
        border-top: solid 1px #eee;
    }

    .btn-modal {
        position: absolute;
        height: 36px;
        width: 44px;
        top: 0;
        right: 0;
        line-height: 0;
        display: block;
        text-indent: -9999px;
        background: #fff url(/dashboard/assets/svg/x.svg) 50% 50% / 15px 15px no-repeat;
        cursor: pointer;
    }
}

.modal-enter, .modal-leave-active {
    opacity: 0;
}

.modal-enter .modal-container,
.modal-leave-active .modal-container {
  transform: scale(1.1);
}
</style>
