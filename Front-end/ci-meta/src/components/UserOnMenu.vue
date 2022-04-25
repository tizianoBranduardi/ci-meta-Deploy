<template>
  <b-nav style="margin : 0px 10px 0px 10px" v-if="this.$store.state.logged">
    <strong>Welcome {{this.$store.state.username}}</strong>&emsp; 
    <a href="http://172.20.27.81:8080/back-end/login/" target="_blank" rel="noopener noreferrer">Account settings</a>&emsp;
    <a @click="logout()" href="">Logout</a>
  </b-nav>
  <!-- <b-nav style="margin : 0px 10px 0px 10px" v-else>
    <router-link to="/login">Login</router-link>
  </b-nav> -->
</template>

<script>
export default {
  name: 'UserOnMenu',
  methods: {
    logout() {
      this.$store.commit('logout');
    }
  }
};
</script>
