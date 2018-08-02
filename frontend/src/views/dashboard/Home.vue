<template>
  <div>
    <notifications/>
    <button @click="sendMessage">Send Message</button>
  </div>
</template>

<script>
export default {
  methods: {
    sendMessage () {
      this.$notify({
        type: 'danger',
        title: 'Achtung',
        text: 'Ein Fehler beim Speichern ist aufgetreten! Sie müssen nun aufhören die Anwendung zu benutzen.'
      })
    }
  }
}
</script>
