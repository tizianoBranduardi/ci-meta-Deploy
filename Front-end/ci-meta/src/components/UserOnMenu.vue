<template>
  <b-nav style="margin : 0px 10px 0px 10px" v-if="this.$store.state.logged">
    <strong>Welcome {{this.$store.state.username}}</strong>&emsp; 
    <a @click="logout()" href="">Logout</a>&emsp; 
    <a href="http://172.20.27.81:8080/back-end/login/">Account settings</a>
  </b-nav>
  <b-nav style="margin : 0px 10px 0px 10px" v-else>
    <router-link to="/login">Login</router-link>
  </b-nav>
</template>

<script>
export default {
  name: 'UserOnMenu',
  methods: {
    logout() {
      this.$store.commit('logout');
      this.$router.push({ name: 'Home'});
    }
  }
};
</script>
