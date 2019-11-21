<template>
    <div>
        <h1> CREATE PROFILE </h1>

    </div>
</template>


<script>

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
          gender:''
      }
  },
  methods: {
  },
  mounted(){
      if (this.email == undefined){
          this.$router.push('home')
      }
  }
}
</script>