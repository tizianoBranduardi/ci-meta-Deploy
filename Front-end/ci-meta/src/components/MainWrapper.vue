<template>
  <div>
  <p class="text-center" v-if="!this.$store.state.logged">
    Welcome into <strong>ci-meta</strong> the historical documents analysis application
    <br>
    Login to access the services
  </p>
  <b-tabs content-class="mt-3" v-else>
    <b-tab title="Documents" active>
      <b-container>
        <b-row>
          <b-col b-col>
            <div class="text-center">
              <p class="h4 mb-2"><b-icon icon="search" variant="primary" size="lg"></b-icon> 
              <router-link to="/search"> Search</router-link>  
              </p>
            </div>
          </b-col>

          <b-col b-col>
            <div class="text-center">
              <p class="h4 mb-2"><b-icon icon="plus-circle" variant="primary" size="lg"></b-icon>
              <router-link to="/documents"> New</router-link>
              </p>
            </div>
          </b-col>
        </b-row>
      </b-container>
      <list-documents />
    </b-tab>
    <b-tab title="Places" >
      <list-places />
    </b-tab>
    <b-tab title="Persons" >
    </b-tab>
    <b-tab title="Institutions" >
    </b-tab>
  </b-tabs>
</div>
</template>

<script>
import InsertImage from './InsertImage.vue';
import InsertImageHome from './InsertImageHome.vue';
import InsertPlace from './InsertPlace.vue';
import ListDocuments from './ListDocuments.vue';
import ListPlaces from './ListPlaces.vue';

  export default {
  components: {
    ListDocuments,
    InsertImage,
    InsertImageHome,
    InsertPlace,
    ListPlaces,
  },
};

</script>

