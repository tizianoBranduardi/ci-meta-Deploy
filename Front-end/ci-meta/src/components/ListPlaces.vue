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
          <p class="h4 mb-2">
            <b-icon icon="plus-circle" variant="primary" size="lg">
            </b-icon>
            <b-button variant="link" @click="newPlace=!newPlace, error=false">Add New</b-button>
          </p>
          <insert-place v-show="newPlace"/>
          <div v-show="error" class="error">
            <br>
            <strong>Error - The place already exists or has been deleted</strong>
          </div>
        </div>
      </b-col>
    </b-row>
    <br>
    <div v-for="(place, index) in places" :key="place">
      <div v-if="!place.is_deleted">

      <b-row v-if="edit[ids[index]]">
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
            <b-button size="sm" variant="success" @click="update(index, place.city, place.description), edit[ids[index]]=false"><b-icon icon="pencil-square" ></b-icon></b-button>&emsp;
            <b-button size="sm" variant="danger" @click="remove(index), edit[ids[index]]=false"><b-icon icon="trash" ></b-icon></b-button>
          </div>
        </b-col>
      </b-row>
      <b-row v-if="!edit[ids[index]]">
        <b-col cols=5>
          <strong>City : </strong>{{place.city}}
        </b-col>
        <b-col cols=6>
          <strong>Description : </strong>{{place.description}}
        </b-col>
        <b-col>
          <b-button variant="link" size="sm" @click="edit[ids[index]]=true, refresh()">
            <b-icon icon="pencil-square" ></b-icon>
          </b-button>
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
      edit: [],
      max: 0,
      error: false,
    }
  },
    async mounted() {
      try {
        const header = { 'Content-Type': 'application/json' };
        const response = await this.$http.get('http://'+this.$store.state.address+'/api/v1/place/', header);
        if (response.data.count>=1){
          this.max= Math.max(response.data.ids);
          this.edit = new Array(Math.max.apply(Math,response.data.ids)).fill(false);
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
      async update(index, city, description) {
        try {
          const id = this.ids[index];
          const header = { 'Content-Type': 'application/json' };
          const data = {'city': city, 'description' : description};
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
        this.newPlace=false;
        const header = { 'Content-Type': 'application/json' };
        const response = await this.$http.get('http://'+this.$store.state.address+'/api/v1/place/', header);
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
      showError(){
        this.error=true;
      },
      hideError(){
        this.error=false;
      }
    }
};
</script>

<style>

</style>