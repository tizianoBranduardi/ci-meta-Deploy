<template>
  <b-container>
    <b-row>
      <b-col class="text-center">
        <h2 >Places</h2>
      </b-col>
    </b-row>
    <b-row>
      <b-col>
        <div class="text-center">
          <b-button variant="link" size="sm" @click="refresh()">refresh</b-button>
          <p class="h4 mb-2">
            <b-icon icon="plus-circle" variant="primary" size="lg">
            </b-icon>
            <b-button variant="link" @click="newPlace=!newPlace">Add New</b-button>
          </p>
          <insert-place v-show="newPlace"/>
        </div>
      </b-col>
    </b-row>
    <br>
    <div v-for="(place, index) in places" :key="place">
      <div v-if="!place.is_deleted">
      <b-row> 
        <b-col>
          <b-input-group prepend="City">
            <b-form-input type="text" v-model="place.city"/>
          </b-input-group>
        </b-col>
        <b-col>
          <b-input-group prepend="Description">
            <b-form-input type="text" v-model="place.description"/>
          </b-input-group>
        </b-col>
        <b-col cols="12" md="auto">
          <div class="text-center">
            <b-button size="sm" variant="success" @click="update(index)">Update</b-button>&emsp;
            <b-button size="sm" variant="danger" @click="remove(index)">Delete</b-button>
          </div>
        </b-col>
      </b-row>
      <hr>
      </div>
    </div>
  </b-container>
</template>

<script>
import InsertPlace from './InsertPlace.vue';
export default {
  components: { InsertPlace },
  name: 'ListPlaces',
  data () {
    return {
      ids :[],
      places:[],
      newPlace : false,
    }
  },
    async mounted() {
      try {
        const header = { 'Content-Type': 'application/json' };
        const response = await this.$http.get('http://'+this.$store.state.address+'/api/v1/place/', header);
        console.log(response.data.count);
        if (response.data.count>=1){
          this.show=true;
          this.ids=response.data.ids;
          this.places=response.data.result;
        }
      }
      catch (e) {
        this.loading = false;
        console.log(e);
        this.error = true;
      }
        
    },
    methods : {
      async remove(index) {
        try {
          const id = this.ids[index];
          const header = { 'Content-Type': 'application/json' };
          const data = {'is_deleted': 'true'};
          const response = await this.$http.put('http://'+this.$store.state.address+'/api/v1/place/'+id, data, header);
          if (response.status==200)
            this.refresh();
        }
      catch (e) {
        console.log(e);
        this.error = true;
        }
      },
      async refresh(){
        try {
        const header = { 'Content-Type': 'application/json' };
        const response = await this.$http.get('http://'+this.$store.state.address+'/api/v1/place/', header);
        console.log(response.data.count);
        if (response.data.count>=1){
          this.ids=response.data.ids;
          this.places=response.data.result;
        }
      }
      catch (e) {
        this.loading = false;
        console.log(e);
        this.error = true;
        }
      },
      async loadPage() {
        try {
        const header = { 'Content-Type': 'application/json' };
        const response = await this.$http.get('http://'+this.$store.state.address+'/api/v1/document/?q=(page:'+this.page+',page_size:'+this.pageSize+')', header);
        console.log(response.data.count);
        if (response.data.count>=1){
          this.show=true;
          this.ids=response.data.ids;
          this.docs=response.data.result;
          }
        }
        catch (e) {
          this.loading = false;
          console.log(e);
          this.error = true;
        } 
      },
    }
};
</script>

<style>

</style>