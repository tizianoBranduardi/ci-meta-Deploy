<template>
  <div>
    <h2 class="text-center">{{name}}</h2>
    <div class="text-center">
      <i>Use the <b-icon icon="pencil-square" ></b-icon> button to edit the relative field. Press the <strong>Update</strong> button at the bottom to update the Institution</i>
    </div>
    <b-container>
      <hr>
<!-- Name -->
      <b-row>
        <b-col b-col cols=5 v-show="!editName">
            <strong>Name &emsp;</strong>{{name}}
            <b-button variant="link" size="sm" @click="editName = true">
                <b-icon icon="pencil-square" ></b-icon>
            </b-button>
        </b-col>
        <b-col v-show="editName">
          <b-input-group class="mt-3" >
            <b-form-input v-model="name" maxlength="255" placeholder="Name" />
            <b-input-group-append>
              <b-button variant="info" @click="editName=false">Update</b-button>
            </b-input-group-append>
          </b-input-group>
        </b-col>
<!-- Type -->
        <b-col b-col>
          <p v-show="!editType">
            <strong>Type &emsp;</strong>{{type}}
            <b-button variant="link" size="sm" @click="editType = true">
                <b-icon icon="pencil-square" ></b-icon>
            </b-button>
          </p>
          <div>
          <b-input-group class="mt-3" v-show="editType">
            <b-form-input v-model="type" maxlength="255" placeholder="Type" />
            <b-input-group-append>
              <b-button variant="info" @click="editType=false">Update</b-button>
            </b-input-group-append>
          </b-input-group>
          </div>
        </b-col>
<!-- Visibility -->
        <b-col b-col>
          <p v-show="!editVisibility">
            <strong>Visibility &emsp;</strong>{{visibility}}
            <b-button variant="link" size="sm" @click="editVisibility = true">
                <b-icon icon="pencil-square" ></b-icon>
            </b-button>
          </p>
          <div>
          <b-input-group class="mt-3" v-show="editVisibility">
            <b-form-input v-model="visibility" maxlength="255" placeholder="Visibility" />
            <b-input-group-append>
              <b-button variant="info" @click="editVisibility=false">Update</b-button>
            </b-input-group-append>
          </b-input-group>
          </div>
        </b-col>
      </b-row>
      <br>
<!-- Year -->
      <b-row>
        <b-col b-col>
          <p v-show="!editYear">
            <strong>Year &emsp;</strong>{{year}}
            <b-button variant="link" size="sm" @click="editYear = true">
                <b-icon icon="pencil-square" ></b-icon>
            </b-button>
          </p>
          <div>
          <b-input-group class="mt-3" v-show="editYear">
            <b-form-input v-model="year" maxlength="255" placeholder="Year" />
            <b-input-group-append>
              <b-button variant="info" @click="editYear=false">Update</b-button>
            </b-input-group-append>
          </b-input-group>
          </div>
        </b-col>
<!-- Place -->
        <b-col b-col>
          <p v-show="!editPlace">
            <strong>Place &emsp;</strong>{{place}}
            <b-button variant="link" size="sm" @click="editPlace = true">
                <b-icon icon="pencil-square" ></b-icon>
            </b-button>
          </p>
          <div>
          <b-input-group class="mt-3" v-show="editPlace">
            <b-form-input v-model="place" maxlength="255" placeholder="Place" />
            <b-input-group-append>
              <b-button variant="info" @click="editPlace=false">Update</b-button>
            </b-input-group-append>
          </b-input-group>
          </div>
        </b-col>
      </b-row>
      <br>
<!-- Note -->
      <b-row>
        <b-col>
          <p>
            <strong>Note &emsp;</strong>
          </p>
          <div>
          <b-input-group class="mt-3">
            <b-form-input v-model="notes" maxlength="255" />
          </b-input-group>
          </div>
          <br>
        </b-col>
      </b-row>
    </b-container>
      <br>
    <div class="text-center">
      <b-button variant="danger" @click="deleteInstitution()">Delete</b-button>&emsp;
      <b-button variant="success" @click="submit()">Update</b-button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ShowInstitution',
  props : ['id'],
  data () {
    return {
      name: '',
      editName: false,
      type: '',
      editType: false,
      year: '',
      editYear: false,
      visibility: '',
      editVisibility : false,
      place : '',
      editPlace : false,
      notes : '',
      editNotes : false
    }
  },
  async mounted() {
    try {
      this.error = false;
      const header = { 'Content-Type': 'application/json' };
      const response = await this.$http.get('http://'+this.$store.state.address+'/api/v1/institution/'+this.id, header);
      if (response.status==200){
        this.show=true;
        this.name=response.data.result.name;
        this.type=response.data.result.type;
        this.visibility=response.data.result.visibility;
        this.year=response.data.result.year;
        this.place=response.data.result.place;
        this.notes=response.data.result.notes;
      }
    }
    catch (e) {
      this.loading = false;
      console.log(e);
      this.error = true;
    } 
  },
  methods: {
    async deleteInstitution() {
      try {
        const header = { 'Content-Type': 'application/json' };
        const response = await this.$http.delete('http://'+this.$store.state.address+'/api/v1/institution/'+this.id, header);
        if (response.status==200)
          this.$parent.exitEdit();
      }
      catch (e) {
        console.log(e);
      }
    },
    async submit() {
      try {
        this.error = false;
        const data = {name:this.name,
                      visibility:this.visibility,
                      type:this.type,
                      year:this.year,
                      place:this.place,
                      notes:this.notes};
        const header = { 'Content-Type': 'application/json' };
        this.loading=true;
        const response = await this.$http.put('http://'+this.$store.state.address+'/api/v1/institution/'+this.id, data, header);
        if (response.status==200){
          this.$parent.exitEdit();
          }
        }
        catch (e) {
          console.log(e);
          this.$parent.exitEdit();
        }
      }
    }
};
</script>
