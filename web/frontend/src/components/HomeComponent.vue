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
export default {
  name: 'HomeComponent',
  props: {
    msg: String
  },
  methods: {
  }
}
</script>

