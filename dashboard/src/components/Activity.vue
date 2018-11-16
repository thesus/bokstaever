<template>
  <div class="activity">
    <div class="map">
      <div class="year" v-for="(year, key) in values" :key="key">
        <div class="description">{{ key }}</div>
        <div class="months">
          <svg
            class="month"
            v-for="month in year"
            :key="month[0]"
            height="10"
            width="10"
            :style="{ 'opacity': getOpacity(month[1]) }"
            @click="setInfo(month[1])"
          >
            <rect
              x="0"
              y="0"
              width="10"
              height="10"
              :style="{ 'fill': (month[1] != 0) ? 'green' : 'black'}"
            />
          </svg>
        </div>
      </div>
    </div>
    <div class="information" v-if="info">
      {{ info }} entries were created.
    </div>
  </div>
</template>

<script>
export default {
  props: ['values'],
  data () {
    return {
      info: null
    }
  },
  methods: {
    getOpacity (value) {
      if (value === 0) {
        return 0.1
      } else if (value === 1) {
        return 0.4
      } else if (value < 3) {
        return 0.7
      } else {
        return 1
      }
    },
    setInfo (value) {
      this.$set(this, 'info', value)
    }
  }
}
</script>

<style lang="scss" scoped>
.map {
  display: flex;
  justify-content: center;
  @media screen and (min-width: 700px) {
    flex-flow: wrap;
  }
}

.year {
  margin: 10px;
  .description {
    text-align: center;
  }
}

.months {
  @media screen and (max-width: 700px) {
    width: 90px;
  }
  @media screen and (max-width: 400px) {
    width: 70px;
  }
}

.month {
  @media screen and (min-width: 700px) {
    &:not(:first-child):not(:last-child) {
      margin-left: 2px;
      margin-right: 2px;
    }
    &:first-child {
      margin-right: 2px;
    }
    &:last-child {
      margin-left: 2px;
    }
  }
  @media screen and (max-width: 700px) {
    margin: 3px;
  }
  cursor: pointer;
}

.information {
  display: block;
}
</style>
