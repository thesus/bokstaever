<template>
  <transition name="modal">
      <div class="modal-mask">
          <div class="modal-wrapper">
              <div class="modal-container">
                  <div class="modal-content">
                      <slot></slot>
                  </div>
                  <button class="btn btn-default btn-modal" @click="$emit('close')">Close</button>
              </div>
          </div>
      </div>
  </transition>
</template>

<script>
export default {}
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
    transition: opacity .3s ease;
    display: table;
}

.modal-wrapper {
    display: table-cell;
    vertical-align: middle;
}

.modal-container {
    width: 50%;
    height: 70%;
    background-color: #fff;
    margin: 0px auto;
    position: relative;
    overflow: hidden;
    .modal-content {
        box-sizing: border-box;
        padding: 8px;
        width: 100%;
        height: calc(100% - 65px);
        overflow-x: hidden;
        overflow-y: auto;
    }

    .btn-modal {
        position: absolute;
        bottom: 8px;
        right: 8px;
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
