<template>
  <b-container>
    <b-row>
      <b-col class="text-center">
        <h2 v-show="!editPerson & !newPerson">Persons</h2>
      </b-col>
    </b-row>
    <b-row>
      <b-col v-show="!editPerson & !newPerson">
        <div class="text-center">
          <p class="h4 mb-2">
            <b-icon icon="plus-circle" variant="primary" size="lg">
            </b-icon>
            <b-button style="text-decoration: none;" variant="link" @click="newPerson=!newPerson, error=false">Add New</b-button>
          </p>
          <div v-show="error" class="error">
            <br>
            <strong>Error - The person already exists or has been deleted</strong>
          </div>
        </div>
      </b-col>
      <b-col v-show="editPerson || newPerson">
        <b-button variant="link" @click="editPerson=false, newPerson=false">Back to list</b-button>
      </b-col>
    </b-row>
    <b-row v-if="newPerson">
      <insert-person />
    </b-row>
    <b-row v-if="editPerson">
        <show-persons :id="this.id"/>
    </b-row>
    <b-row v-show="!editPerson & !newPerson">
        <b-col>
          <hr>
          <div class="text-center">
            <b-button-group class="mx-1">
              <b-button @click="letter='a', refresh()" variant="link">a</b-button>
              <b-button @click="letter='b', refresh()" variant="link">b</b-button>
              <b-button @click="letter='c', refresh()" variant="link">c</b-button>
              <b-button @click="letter='d', refresh()" variant="link">d</b-button>
              <b-button @click="letter='e', refresh()" variant="link">e</b-button>
              <b-button @click="letter='f', refresh()" variant="link">f</b-button>
              <b-button @click="letter='g', refresh()" variant="link">g</b-button>
              <b-button @click="letter='h', refresh()" variant="link">h</b-button>
              <b-button @click="letter='i', refresh()" variant="link">i</b-button>
              <b-button @click="letter='j', refresh()" variant="link">j</b-button>
              <b-button @click="letter='k', refresh()" variant="link">k</b-button>
              <b-button @click="letter='l', refresh()" variant="link">l</b-button>
              <b-button @click="letter='m', refresh()" variant="link">m</b-button>
              <b-button @click="letter='n', refresh()" variant="link">n</b-button>
              <b-button @click="letter='o', refresh()" variant="link">o</b-button>
              <b-button @click="letter='p', refresh()" variant="link">p</b-button>
              <b-button @click="letter='q', refresh()" variant="link">q</b-button>
              <b-button @click="letter='r', refresh()" variant="link">r</b-button>
              <b-button @click="letter='s', refresh()" variant="link">s</b-button>
              <b-button @click="letter='t', refresh()" variant="link">t</b-button>
              <b-button @click="letter='u', refresh()" variant="link">u</b-button>
              <b-button @click="letter='v', refresh()" variant="link">v</b-button>
              <b-button @click="letter='w', refresh()" variant="link">w</b-button>
              <b-button @click="letter='x', refresh()" variant="link">x</b-button>
              <b-button @click="letter='y', refresh()" variant="link">y</b-button>
              <b-button @click="letter='z', refresh()" variant="link">z</b-button>
            </b-button-group>
          </div>
          <hr>
          </b-col>
      </b-row>
    <div v-for="(person, index) in persons" :key="person" v-show="!editPerson & !newPerson">
      <div v-if="!person.is_deleted">
      <b-row v-if="!editPerson">
        <b-col cols=5>
          <strong>Name : </strong>{{person.name}}
        </b-col>
        <b-col cols=6>
          <strong>Latin name : </strong>{{person.name_latin}}
        </b-col>
        <b-col>
          <b-button variant="link" size="sm" @click="id=ids[index], editPerson=true, refresh()">
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
import ShowPersons from './ShowPersons.vue';
import InsertPerson from './InsertPerson.vue'
export default {
  components: { ShowPersons, InsertPerson },
  name: 'ListPersons',
  data () {
    return {
      letter: '',
      id: 0,
      ids :[],
      persons:[],
      editPerson: false,
      newPerson : false,
      error: false,
    }
  },
    async mounted() {
      try {
        const header = { 'Content-Type': 'application/json' };
        const response = await this.$http.get('http://'+this.$store.state.address+'/api/v1/person/?q=(filters:!((col:name,opr:sw,value:a)))', header);
        if (response.data.count>=1){
          this.ids=response.data.ids;
          this.persons=response.data.result;
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
        const response = await this.$http.get('http://'+this.$store.state.address+'/api/v1/person/?q=(filters:!((col:name,opr:sw,value:'+this.letter+')))', header);
        if (response.data.count>=1){
          this.ids=response.data.ids;
          this.persons=response.data.result;
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
        this.editPerson=false;
        this.newPerson=false;
        this.refresh();
      }
    }
};
</script>

<style>

</style>