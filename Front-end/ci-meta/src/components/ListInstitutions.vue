<template>
  <b-container>
    <b-row>
      <b-col class="text-center">
        <h2 v-show="!editInstitution & !newInstitution">Institutions</h2>
      </b-col>
    </b-row>
    <b-row>
      <b-col v-show="!editInstitution & !newInstitution">
        <div class="text-center">
          <p class="h4 mb-2">
            <b-icon icon="plus-circle" variant="primary" size="lg">
            </b-icon>
            <b-button variant="link" @click="newInstitution=!newInstitution, error=false">Add New</b-button>
          </p>
          <div v-show="error" class="error">
            <br>
            <strong>Error - The institution already exists or has been deleted</strong>
          </div>
        </div>
      </b-col>
      <b-col v-show="editInstitution || newInstitution">
        <b-button variant="link" @click="editInstitution=false, newInstitution=false">Back to list</b-button>
      </b-col>
    </b-row>
    <b-row v-if="newInstitution">
      <insert-institution />
    </b-row>
    <b-row v-if="editInstitution">
        <show-institution :id="this.id"/>
    </b-row>

    <div v-for="(institution, index) in institutions" :key="institution" v-show="!editInstitution & !newInstitution">
      <div v-if="!institution.is_deleted">
      <b-row v-if="!editInstitution">
        <b-col cols=4>
          <strong>Name : </strong>{{institution.name}}
        </b-col>
        <b-col>
          <strong>Type : </strong>{{institution.type}}
        </b-col>
        <b-col>
          <strong>Year : </strong>{{institution.year}}
        </b-col>
        <b-col>
          <strong>Place : </strong>{{institution.place}}
        </b-col>
        <b-col>
          <b-button variant="link" size="sm" @click="id=ids[index], editInstitution=true, refresh()">
            <b-icon icon="search" ></b-icon>
          </b-button>
        </b-col>
      </b-row>
      <hr>
      </div>
    </div>
  </b-container>
</template>

<script>
import ShowInstitution from './ShowInstitution.vue';
import InsertInstitution from './InsertInstitution.vue'
export default {
  components: { ShowInstitution, InsertInstitution },
  name: 'ListPersons',
  data () {
    return {
      letter: '',
      id: 0,
      ids :[],
      institutions:[],
      editInstitution: false,
      newInstitution : false,
      error: false,
    }
  },
    async mounted() {
      try {
        const header = { 'Content-Type': 'application/json' };
        const response = await this.$http.get('http://'+this.$store.state.address+'/api/v1/institution/', header);
        if (response.data.count>=1){
          this.ids=response.data.ids;
          this.institutions=response.data.result;
        }
      }
      catch (e) {
        this.loading = false;
        console.log(e);
        this.error = true;
      }
        
    },
    methods : {
      async refresh(){
        try {
        const header = { 'Content-Type': 'application/json' };
        const response = await this.$http.get('http://'+this.$store.state.address+'/api/v1/institution/', header);
        if (response.data.count>=1){
          this.ids=response.data.ids;
          this.institutions=response.data.result;
          }
        }
        catch (e) {
          this.loading = false;
          console.log(e);
          this.error = true;
        }
      },
      showError(){
        this.error=true;
        setTimeout(() => this.error = false, 5000);
      },
      hideError(){
        this.error=false;
      },
      exitEdit(){
        this.editInstitution=false;
        this.newInstitution=false;
        this.refresh();
      }
    }
};
</script>

<style>

</style>