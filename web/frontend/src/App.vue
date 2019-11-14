<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <HelloWorld msg="Welcome  Your YAA Vue.js App:"/>
    <p>{{apiMessage}}</p>
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'
import axios from 'axios'

export default {
  name: 'app',
  data (){
    return {
      apiMessage:''
    }
  },
  components: {
    HelloWorld
  },
  beforeMount(){
    axios.get(process.env.VUE_APP_BASEURL)
    .then(response =>{
      this.apiMessage = response.data
    })
    .catch(e => {
      this.apiMessage = e
    })
    window.console.log(process.env)
    
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
