<template>
    <div>
      <div v-if="state==='pending'">
        loading...
      </div>
      <div v-if="state==='failure'">
          <b-message size="is-medium is-warning">
                {{message}}
          </b-message>
      </div>
      <div v-if="state==='ready'">
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
      </div>
    </div>
</template>

<script>
import * as userAPI from '../apiCalls/user.js';

export default {
  name: 'profile',
  data (){
    return {
      state : 'pending',
      message : '',
      username:'',
      email:'',
      firstname:'',
      lastname:'', 
      gender:'',
      age:0
    }
  },
  components: {
  },
  methods: {},
  computed:{},
  watch: {},
  mounted(){
    userAPI.getUserData(this.$auth.user.email)
    .then(userData =>{
      if (userData.success == false){
        this.state = 'failure';
        this.message = 'could not find user profile';
      }
      else {
        this.username = userData.username;
        this.email = userData.email;
        this.firstname = userData.firstname;
        this.lastname = userData.lastname;
        this.gender = userData.gender;
        this.age = userData.age;
        this.state = 'ready';
      }
    })

  }
}
</script>