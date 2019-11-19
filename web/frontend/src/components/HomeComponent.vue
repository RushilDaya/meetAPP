<template>
  <div>
    <div v-if="$auth.loading">
        <b-loading :is-full-page="true"></b-loading>
    </div>
    <div v-if="!$auth.loading">
        <container v-if="!$auth.isAuthenticated" style="padding:50px">
            <b-message size="is-medium is-warning">
                Please login to continue
            </b-message>
        </container>
        <div v-else>
        </div>
    </div>
  </div>
</template>

<script>
import * as userAPI from '../apiCalls/user.js'

export default {
  name: 'HomeComponent',
  props: {
    msg: String
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
            .then(emailData=>{
              window.console.log(emailData)
            })
        }
    }
  },
  methods: {
  }
}
</script>

