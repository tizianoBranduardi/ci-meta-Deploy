<template>
  <div>
    <div v-if="!this.$store.state.logged">
      <Login />
    </div>
    <div v-if="this.$store.state.logged">
      <insert-document />
    </div>
  </div>
</template>

<script>
import Login from '@/components/Login.vue';
import InsertDocument from '../components/InsertDocument.vue';

export default {
  components: {
    Login,
    InsertDocument,
  },
};
</script>
