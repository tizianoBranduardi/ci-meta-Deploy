<template>
  <div>
    <div class="text-center" v-if="!this.$store.state.logged">
        <h3>The Accademia del Cimento in Florence: tracing the roots of the European scientific enterprise</h3>
      <div>  
        <b-img center :src="images.cimento" fluid width="800"/>
      </div>
      <p>
        This project analyses for the first time in its entirety the extensive corpus of unpublished documents, descriptions of experiments and thousands of epistolary exchanges between members of the Cimento and scholars throughout Europe. 
        By looking at the sources in their entirety, it aims at systematically connecting the strictly experimental, theoretical and philosophical aspects of the Accademia with its intellectual history.
      </p>
      <login />
    </div>
    <b-tabs content-class="mt-3" fill v-else>
      <b-tab title="Documents" active>
        <b-container>
          <b-row>
            <b-col b-col>
              <div class="text-center">
                <p class="h4 mb-2"><b-icon icon="search" variant="primary" size="lg"></b-icon> 
                <router-link style="text-decoration: none;" to="/search"> Search</router-link>  
                </p>
              </div>
            </b-col>

            <b-col b-col>
              <div class="text-center">
                <p class="h4 mb-2"><b-icon icon="plus-circle" variant="primary" size="lg"></b-icon>
                <router-link style="text-decoration: none;" to="/documents"> New</router-link>
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
        <list-persons />
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
import ListPersons from './ListPersons.vue';
import Login from './Login.vue';

  export default {
    components: {
      ListDocuments,
      InsertImage,
      InsertImageHome,
      InsertPlace,
      ListPlaces,
      ListPersons,
      Login,
    },
    data() {
          return {
              images: {
                cimento: require('../../public/cimento.png')
              }
          }
      }
};

</script>

