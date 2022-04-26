<template>
  <div>
    <h2 class="text-center">New Institution</h2>
        <b-container>
      <hr>
<!-- Name -->
      <b-row>
        <b-col b-col>
            <strong>Name &emsp;</strong>
            <b-form-input v-model="name" maxlength="255"/>
        </b-col>
<!-- Type -->
        <b-col b-col>
            <strong>Type &emsp;</strong>
            <b-form-input v-model="type" maxlength="255"/>
        </b-col>
      </b-row>
      <br>
<!-- Visibility -->
        <b-row>
        <b-col b-col>
            <strong>Visibility &emsp;</strong>
            <b-form-input v-model="visibility" maxlength="255"/>
        </b-col>
<!-- Year -->
        <b-col b-col>
            <strong>Year &emsp;</strong>
            <b-form-input v-model="year" maxlength="255"/>
        </b-col>
<!-- Place -->
        <b-col b-col>
            <strong>Place &emsp;</strong>
            <b-form-input v-model="place" maxlength="255"/>
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
      <b-button variant="success" @click="submit()">Create</b-button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'InsertInstitution',
  props : ['id'],
  data () {
    return {
      name: '',
      type: '',
      visibility: '',
      year: '',
      place : '',
      notes : ''
    }
  },
  methods: {
    async submit() {
      try {
        this.error = false;
        const data = {name:this.name,
                      year:this.year,
                      type:this.type,
                      visibility:this.visibility,
                      place:this.place,
                      notes:this.notes};
        const header = { 'Content-Type': 'application/json' };
        this.loading=true;
        const response = await this.$http.post('http://'+this.$store.state.address+'/api/v1/institution/', data, header);
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
