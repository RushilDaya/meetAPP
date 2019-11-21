<template>
  <div id="app">
    <b-navbar id="navbar">
      <template slot="brand">
        <navbar-item>
          <img id="brandImage"
            src="./assets/brand.svg"
            alt="MeetApp"
          >
        </navbar-item>
      </template>
       <template slot="start">
            <b-navbar-item href="#">
                Home
            </b-navbar-item>
            <b-navbar-item href="#">
                Profile
            </b-navbar-item>
        </template>
        <template slot="end">
            <b-navbar-item tag="div">
                <div class="buttons">
                    <a v-if="!$auth.isAuthenticated" @click="login" class="button is-light">
                        Log in
                    </a>
                    <a v-if="$auth.isAuthenticated" @click="logout" class="button is-light">
                        Log Out
                    </a>
                </div>                
            </b-navbar-item>
        </template>
    </b-navbar>
    <section class="hero is-primary is-fullheight">
      <router-view></router-view>
    </section>
  </div>
</template>

<script>
import * as userAPI from './apiCalls/user.js'

export default {
  name: 'app',
  data (){
    return {
      apiMessage:''
    }
  },
  components: {
  },
  methods: {
    // Log the user in
    login() {
      this.$auth.loginWithRedirect()
    },
    // Log the user out
    logout() {
      this.$auth.logout({
        returnTo: window.location.origin
      });
    }
  },
  computed:{
    authState: function(){
        return this.$auth.isAuthenticated
    }, 
    userData: function(){
       return this.$auth.user
    }
  },
  watch: {
    userData: function(){
        if (this.authState == true){
            userAPI.emailExists(this.userData.email)
              .then(emailData =>{
                if (emailData['exists']==false){
                  this.$router.push({name:'createProfile',params:{email:emailData['email']}})
                }
                else{
                  this.$router.push({name:'home'})
                }
              })
            
        }
    }
  },
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
#navbar {
  padding: 20px;
}
#brandImage {
  height: 50px;
}
</style>
