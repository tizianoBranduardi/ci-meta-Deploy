<template>
  <b-container>
    <b-row>
      <b-col class="text-center">
        <h2 >Places</h2>
        <b-button variant="link" size="sm" @click="refresh()">refresh</b-button>
      </b-col>
    </b-row>
    <br>
    <div v-for="(place, index) in places" :key="place">
      <div v-if="!place.is_deleted">
      <b-row> 
        <b-col>
          <strong>Id : {{ids[index]}}</strong>
        </b-col>
        <b-col>
          <strong>City</strong> : <b-form-input type="text" v-model="place.city"/>
        </b-col>
        <b-col>
          <div class="text-inline">
          <strong>Description</strong> : <b-form-input type="text" v-model="place.description"/>
          </div>
        </b-col>
        <b-col>
          <div class="text-center">
            <br>
            <b-button variant="danger" @click="remove(index)">Delete</b-button>&emsp;
            <b-button variant="success" @click="update(index)">Update</b-button>
          </div>
        </b-col>
      </b-row>
      <br>
      <hr>
      </div>
    </div>
    <b-row>
      <b-col>
        <div class="text-center">
          <b-button variant="primary" @click="newPlace=!newPlace">Add New</b-button>
          <insert-place v-show="newPlace"/>
        </div>
      </b-col>
    </b-row>
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