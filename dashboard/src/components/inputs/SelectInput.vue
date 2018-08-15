<template>
  <div>
    <multiselect v-model="choice" track-by="name" label="name" placeholder="Select type" :options="getOptions" :searchable="false" :allow-empty="false">
      <template slot="singleLabel" slot-scope="{ option }">{{ option.name }}</template>
    </multiselect>
  </div>
</template>

<script>
import Multiselect from 'vue-multiselect'

var getChoice = (value, extra) => {
  if (extra && value) {
    return [{
        value: value,
        name: extra.filter(i => i[0] === value)[0][1]
      }]
    }
  }

export default {
    components: { Multiselect },
    props: ['value', 'extra'],
    data () {
      return {
        choice: getChoice(this.value, this.extra)
      }
    },
    computed: {
      getOptions () {
        let data = []
        for (let i of this.extra) {
          data.push({
              'value': i[0],
              'name': i[1]
          })
        }
        return data
      }
    },
    watch: {
      value () {
        this.choice = getChoice(this.value, this.extra)
      },
      choice () {
        if (this.choice && this.choice.value) {
          this.$emit(
            'input',
            { target: { value: this.choice.value }}
          )
        }
      }
    }
}
</script>

<style src="vue-multiselect/dist/vue-multiselect.min.css"></style>

<style lang="scss" scoped>

</style>
