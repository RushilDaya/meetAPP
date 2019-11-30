<template>
    <div class="container" style="width:90%;padding:10%">
        <div class="hero is-light is-fullheight">
            <div class="container">
            <h1 class="title" style="color:black">
                Create Profile
            </h1>
            <h2 class="subtitle" style="color:black">
                {{email}}
            </h2>
            
            <b-message v-if="showErrorMessage" type="is-danger">
             {{errorMessage}}
            </b-message>

                <section>
                    <b-field label="User Name">
                        <b-input v-model="username"></b-input>
                    </b-field>
                </section>
                <section>
                    <b-field label="First Name">
                        <b-input v-model="firstname"></b-input>
                    </b-field>
                </section>
                <section>
                    <b-field label="Last Name">
                        <b-input v-model="lastname"></b-input>
                    </b-field>
                </section>
                <section>
                    <b-field label="Age">
                        <b-numberinput v-model="age" controls-rounded></b-numberinput>
                    </b-field>
                </section>
                <section>
                    <b-field label="Gender">
                        <div class="block">
                            <b-radio v-model="gender"
                                name="Male"
                                native-value="M">
                                Male
                            </b-radio>
                            <b-radio v-model="gender"
                                name="Female"
                                native-value="F">
                                Female
                            </b-radio>
                            <b-radio v-model="gender"
                                name="Other"
                                native-value="O">
                                Other
                            </b-radio>
                        </div>
                    </b-field>
                </section>
                <section>
                    <div class="buttons">
                        <b-button :disabled="invalidData" @click="attemptUserCreate()" type="is-primary">Create</b-button>
                    </div>
                </section>
            </div>
        </div>
    </div>
</template>


<script>
import * as userAPI from '../apiCalls/user.js';

export default {
  name: 'CreateProfile',
  props: {
    email: String
  },
  data(){
      return {
          username:'',
          firstname:'',
          lastname:'',
          age:21,
          gender:'M',
          errorMessage :''
      }
  },
  methods: {
      attemptUserCreate(){
          userAPI.attemptUserCreate(this.$http, this.username,this.firstname,this.lastname,this.age,this.gender,this.email)
          .then(response=>{
              if (response.success === true){
                  this.$router.push('home')
              }
              else {
                  this.errorMessage = response.reason
              }
          })
      }

  },
  computed:{
      showErrorMessage: function(){
          if (this.errorMessage == ''){
              return false
          }
          return true
      },
      invalidFirstName: function(){
          if (this.firstname == ''){
              return true
          }
          if (this.firstname.indexOf(' ') !== -1){
              return true
          }
          return false
      },
      invalidLastName: function(){
          if (this.lastname == ''){
              return true
          }
          if (this.lastname.indexOf(' ') !== -1){
              return true
          }
          return false
      },
      invalidUserName: function(){
          if (this.username == ''){
              return true
          }
          if (this.username.indexOf(' ') !== -1){
              return true
          }
          return false
      },
      invalidData: function(){
          return this.invalidFirstName || this.invalidLastName || this.invalidUserName
      }
  },
  mounted(){
      if (this.email == undefined){
          this.$router.push('home')
      }
  }
}
</script>