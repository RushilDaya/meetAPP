<template>
    <div>
      <div v-if="state=='pending'">
        loading...
      </div>
      <div v-if="state=='failure'">
          <b-message size="is-medium is-warning">
                {{message}}
          </b-message>
      </div>
      <div v-if="state=='ready'">
            <section>
                    <b-field label="User Name">
                        <b-input v-model="userName"></b-input>
                    </b-field>
                </section>
                <section>
                    <b-field label="First Name">
                        <b-input v-model="userFirstName"></b-input>
                    </b-field>
                </section>
                <section>
                    <b-field label="Surname">
                        <b-input v-model="userSurname"></b-input>
                    </b-field>
                </section>
                <section>
                    <b-field label="Age">
                        <b-numberinput v-model="userAge" controls-rounded></b-numberinput>
                    </b-field>
                </section>
                <section>
                    <b-field label="Gender">
                        <div class="block">
                            <b-radio v-model="userGender"
                                name="Male"
                                native-value="M">
                                Male
                            </b-radio>
                            <b-radio v-model="userGender"
                                name="Female"
                                native-value="F">
                                Female
                            </b-radio>
                            <b-radio v-model="userGender"
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
      userName:'',
      userEmail:'',
      userFirstName:'',
      userLastName:'',
      userGender:'',
      userAge:0
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
        this.userName = userData.userName;
        this.userEmail = userData.userEmail;
        this.userFirstName = userData.userFirstName;
        this.userLastName = userData.userLastName;
        this.userGender = userData.userGender;
        this.userAge = userData.userAge;
        this.state = 'ready';
      }
    })

  }
}
</script>