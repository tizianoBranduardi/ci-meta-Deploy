<template>
  <div>
    <h2 class="text-center">{{name}}</h2>
    <div class="text-center">
      <i>Use the <b-icon icon="pencil-square" ></b-icon> button to edit the relative field. Press the <strong>Update</strong> button at the bottom to update the Person</i>
    </div>
    <b-container>
      <hr>
<!-- Name -->
      <b-row>
        <b-col b-col v-show="!editName">
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
<!-- Name Latin -->
        <b-col b-col>
          <p v-show="!editNameLatin">
            <strong>Latin Name &emsp;</strong>{{nameLatin}}
            <b-button variant="link" size="sm" @click="editNameLatin = true">
                <b-icon icon="pencil-square" ></b-icon>
            </b-button>
          </p>
          <div>
          <b-input-group class="mt-3" v-show="editNameLatin">
            <b-form-input v-model="nameLatin" maxlength="255" placeholder="Latin Name" />
            <b-input-group-append>
              <b-button variant="info" @click="editNameLatin=false">Update</b-button>
            </b-input-group-append>
          </b-input-group>
          </div>
        </b-col>
      </b-row>
<!-- Alias -->
      <b-row>
        <b-col b-col>
          <p v-show="!editAlias">
            <strong>Alias &emsp;</strong>{{alias}}
            <b-button variant="link" size="sm" @click="editAlias = true">
                <b-icon icon="pencil-square" ></b-icon>
            </b-button>
          </p>
          <div>
          <b-input-group class="mt-3" v-show="editAlias">
            <b-form-input v-model="alias" maxlength="255" placeholder="Alias" />
            <b-input-group-append>
              <b-button variant="info" @click="editAlias=false">Update</b-button>
            </b-input-group-append>
          </b-input-group>
          </div>
        </b-col>
<!-- Born -->
        <b-col b-col>
          <p v-show="!editBorn">
            <strong>Born &emsp;</strong>{{born}}
            <b-button variant="link" size="sm" @click="editBorn = true">
                <b-icon icon="pencil-square" ></b-icon>
            </b-button>
          </p>
          <div>
          <b-input-group class="mt-3" v-show="editBorn">
            <b-form-input v-model="born" maxlength="255" placeholder="Born" />
            <b-input-group-append>
              <b-button variant="info" @click="editBorn=false">Update</b-button>
            </b-input-group-append>
          </b-input-group>
          </div>
        </b-col>
<!-- Death -->
        <b-col b-col>
          <p v-show="!editDeath">
            <strong>Alias &emsp;</strong>{{death}}
            <b-button variant="link" size="sm" @click="editDeath = true">
                <b-icon icon="pencil-square" ></b-icon>
            </b-button>
          </p>
          <div>
          <b-input-group class="mt-3" v-show="editDeath">
            <b-form-input v-model="death" maxlength="255" placeholder="Death" />
            <b-input-group-append>
              <b-button variant="info" @click="editDeath=false">Update</b-button>
            </b-input-group-append>
          </b-input-group>
          </div>
        </b-col>
      </b-row>
<!-- Reference -->
      <b-row>
        <b-col b-col >
          <p v-show="!editReference">
            <strong>Reference &emsp;</strong>{{reference}}
            <b-button variant="link" size="sm" @click="editReference = true">
                <b-icon icon="pencil-square" ></b-icon>
            </b-button>
          </p>
          <div>
          <b-input-group class="mt-3" v-show="editReference">
            <b-form-input v-model="reference" maxlength="255" placeholder="Reference" />
            <b-input-group-append>
              <b-button variant="info" @click="editReference=false">Update</b-button>
            </b-input-group-append>
          </b-input-group>
          </div>
        </b-col>
      </b-row>
<!-- Wiki & Links -->
      <b-row>
        <b-col b-col >
          <p v-show="!editWiki">
            <strong>Wikidata &emsp;</strong>{{wikidata}}
            <b-button variant="link" size="sm" @click="editWiki = true">
                <b-icon icon="pencil-square" ></b-icon>
            </b-button>
          </p>
          <div>
          <b-input-group class="mt-3" v-show="editWiki">
            <b-form-input v-model="wikidata" maxlength="255" placeholder="Wikidata" />
            <b-input-group-append>
              <b-button variant="info" @click="editWiki=false">Update</b-button>
            </b-input-group-append>
          </b-input-group>
          </div>
        </b-col>
        <b-col b-col >
          <p v-show="!editLinks">
            <strong>Links &emsp;</strong><a :href="links" target="_blank">{{links}}</a>
            <b-button variant="link" size="sm" @click="editLinks = true">
                <b-icon icon="pencil-square" ></b-icon>
            </b-button>
          </p>
          <div>
          <b-input-group class="mt-3" v-show="editLinks">
            <b-form-input v-model="links" maxlength="255" placeholder="Links" />
            <b-input-group-append>
              <b-button variant="info" @click="editLinks=false">Update</b-button>
            </b-input-group-append>
          </b-input-group>
          </div>
        </b-col>
      </b-row>
      <hr>
      <show-edit-affiliation :personId="this.id" />
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
      <b-button variant="danger" @click="deletePerson()">Delete</b-button>&emsp;
      <b-button variant="success" @click="submit()">Update</b-button>
    </div>
  </div>
</template>

<script>
import ShowEditAffiliation from './ShowEditAffiliation.vue';

export default {
  components: { ShowEditAffiliation },
  name: 'ShowPersons',
  props : ['id'],
  data () {
    return {
      name: '',
      editName: false,
      nameLatin: '',
      editNameLatin: false,
      alias: '',
      editAlias: false,
      birth: '',
      editBirth : false,
      death : '',
      editDeath : false,
      reference : '',
      editReferecence : false,
      wikidata : '',
      editWiki : false,
      links : '',
      editLinks : false,
      notes : '',
      editNotes : false
    }
  },
  async mounted() {
    try {
      this.error = false;
      const header = { 'Content-Type': 'application/json' };
      const response = await this.$http.get('http://'+this.$store.state.address+'/api/v1/person/'+this.id, header);
      if (response.status==200){
        this.show=true;
        this.name=response.data.result.name;
        this.nameLatin=response.data.result.name_latin;
        this.alias=response.data.result.alias;
        this.birth=response.data.result.birth;
        this.death=response.data.result.death;
        this.reference=response.data.result.reference;
        this.wikidata=response.data.result.wikidata;
        this.links=response.data.result.links;
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
    async deletePerson() {
      try {
        const header = { 'Content-Type': 'application/json' };
        const data = {'is_deleted': 'true'}
        const response = await this.$http.put('http://'+this.$store.state.address+'/api/v1/person/'+this.id, data, header);
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
                      name_latin:this.nameLatin,
                      alias:this.alias,
                      birth:this.birth,
                      death:this.death,
                      reference:this.reference,
                      wikidata:this.wikidata,
                      links:this.links,
                      notes:this.notes};
        const header = { 'Content-Type': 'application/json' };
        this.loading=true;
        const response = await this.$http.put('http://'+this.$store.state.address+'/api/v1/person/'+this.id, data, header);
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
