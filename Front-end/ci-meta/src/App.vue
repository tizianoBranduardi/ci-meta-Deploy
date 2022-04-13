<template>
  <div id="app">
    <b-navbar toggleable="small" type="dark" variant="dark" fixed="top" sticky>
      <b-navbar-brand to="/" style="margin : 0px 10px 0px 10px">Ci-Meta</b-navbar-brand>
      <UserOnMenu />
    </b-navbar>
    <div style="margin: 10px 10px 10px 10px">
      <router-view/>
    </div>
  </div>
</template>

<script>
import UserOnMenu from './components/UserOnMenu.vue';

export default {
  components: {
    UserOnMenu,
  },
};
</script>

<style scoped>
 .navbar.navbar-dark.bg-dark{
    background-color: rgb(240, 109, 3)!important;
 }
</style>
