<template>
  <b-container>
    <b-row v-if="!select">
      <b-col>
        <div class="d-flex align-items-center justify-content-center" v-if="!submit">
          <b-card
              v-if="!submit"
              title="Search"
              style="max-width: 20rem;"
              class="text-center"
              border-variant="warning"
            >
            <b-form inline >
              <label class="sr-only" for="inline-form-input-id">Id</label>
              <b-input-group class="mb-2 mr-sm-2 mb-sm-0">
              <b-form-input v-model="id" id="inline-form-input-id" placeholder="id"></b-form-input>
              </b-input-group>
              <br>
              <b-button v-on:click.prevent="submit= true" variant="primary">Search</b-button>
              <br>
            </b-form>
          </b-card>
        </div>
        <div v-else>
          <b-button variant="link" @click="submit = false">Back to search</b-button>
          <br>
          <show-documents-minimal :id="id" />
          <br>
          <div class="text-center">
            <b-button v-on:click.prevent="select= true" variant="primary">Select</b-button>
          </div>
        </div>
      </b-col>
    </b-row>
    <b-row v-if="select">
      <b-button variant="link" @click="select=false, submit=false">Back to search</b-button>
      <insert-image :id="id" ref="images"/>
      <b-button v-on:click="upload()" variant="primary">Upload</b-button>
    </b-row>
  </b-container>
</template>

<script>
import InsertImage from './InsertImage.vue';
import ShowDocumentsMinimal from './ShowDocumentsMinimal.vue';
export default {
  components: { ShowDocumentsMinimal, InsertImage },
  name: 'InsertImageHome',
  data () {
    return {
      id : 0,
      submit: false,
      select : false,
    }
  },
  methods : {
    upload() {
      this.$refs.images.submit();
      this.select=false;
      this.submit=false;
      this.id=0;
    },
  }
};

</script>

<style>

</style>