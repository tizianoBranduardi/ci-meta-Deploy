<template>
  <div>
    <h2 class="text-center">New Person</h2>
    <b-container>
      <hr>
<!-- Name -->
      <b-row>
        <b-col b-col>
            <strong>Name </strong>
            <b-form-input v-model="name" maxlength="255" />
        </b-col>
<!-- Name Latin -->
        <b-col b-col>
            <strong>Latin Name </strong>
            <b-form-input v-model="nameLatin" maxlength="255"/>
        </b-col>
      </b-row>
<!-- Alias -->
      <b-row>
        <b-col b-col>
            <strong>Alias </strong>
            <b-form-input v-model="alias" maxlength="255"/>
        </b-col>
<!-- Born -->
        <b-col b-col>
            <strong>Born </strong>
            <b-form-input v-model="born" maxlength="255"/>
        </b-col>
<!-- Death -->
        <b-col b-col>
            <strong>Alias </strong>
            <b-form-input v-model="death" maxlength="255"/>
        </b-col>
      </b-row>
<!-- Reference -->
      <b-row>
        <b-col b-col >
            <strong>Reference</strong>
            <b-form-input v-model="reference" maxlength="255"/>
        </b-col>
      </b-row>
<!-- Wiki & Links -->
      <b-row>
        <b-col b-col>
            <strong>Wikidata</strong>
            <b-form-input v-model="wikidata" maxlength="255"/>
        </b-col>
        <b-col b-col >
            <strong>Links</strong>
            <b-form-input v-model="links" maxlength="255"/>
        </b-col>
      </b-row>
      <hr>
      <show-edit-affiliation :personId="this.id" />
      <br>
<!-- Note -->
      <b-row>
        <b-col>
            <strong>Note </strong>
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
      <b-button variant="success" @click="submit()">Create</b-button>
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
      nameLatin: '',
      alias: '',
      birth: '',
      death : '',
      reference : '',
      wikidata : '',
      links : '',
      notes : ''
    }
  },
  methods: {
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
        const response = await this.$http.post('http://'+this.$store.state.address+'/api/v1/person/', data, header);
        if (response.statusText=='CREATED'){
          this.$parent.exitEdit();
          }
        }
        catch (e) {
          console.log(e);
          this.$parent.showError();
          this.$parent.exitEdit();
        }
      }
    }
};
</script>
