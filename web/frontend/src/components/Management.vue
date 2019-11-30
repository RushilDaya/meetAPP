<template>
  <div>
    <p> Manangement console </p>
    <button @click='initDB()'> re-initDB </button>
  </div>
</template>

<script>
import * as generalAPI from '../apiCalls/general.js'

export default {
  name: 'Management',
  props: {
  },
  methods: {
      initDB (){
          generalAPI.initDB(this.$http)
      }

  }
}
</script>