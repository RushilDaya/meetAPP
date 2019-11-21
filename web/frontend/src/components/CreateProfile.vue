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
                <section>
                    <b-field label="User Name">
                        <b-input v-model="userName"></b-input>
                    </b-field>
                </section>
                <section>
                    <b-field label="First Name">
                        <b-input v-model="firstName"></b-input>
                    </b-field>
                </section>
                <section>
                    <b-field label="Surname">
                        <b-input v-model="surname"></b-input>
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
          userName:'',
          firstName:'',
          surname:'',
          age:21,
          gender:'M'
      }
  },
  methods: {
      attemptUserCreate(){
          userAPI.attemptUserCreate(this.userName,this.firstName,this.surname,this.age,this.gender,this.email)
      }
  },
  computed:{
      invalidFirstName: function(){
          if (this.firstName == ''){
              return true
          }
          if (this.firstName.indexOf(' ') !== -1){
              return true
          }
          return false
      },
      invalidSurname: function(){
          if (this.surname == ''){
              return true
          }
          if (this.surname.indexOf(' ') !== -1){
              return true
          }
          return false
      },
      invalidUserName: function(){
          if (this.userName == ''){
              return true
          }
          if (this.userName.indexOf(' ') !== -1){
              return true
          }
          return false
      },
      invalidData: function(){
          return this.invalidFirstName || this.invalidSurname || this.invalidUserName
      }
  },
  mounted(){
      if (this.email == undefined){
          this.$router.push('home')
      }
  }
}
</script>