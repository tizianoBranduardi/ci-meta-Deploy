<template>
  <div>
    <b-container>
      <h3 class="text-center">New Place</h3>
      <b-row>
        <b-col>
          <strong>City &emsp;</strong>
          <b-form-input type="text" v-model="city" />
        </b-col>
        <b-col>
          <strong>Description &emsp;</strong>
          <b-form-input type="text" v-model="description" />
        </b-col>
        <!-- <b-col>
          <b-form-checkbox size="md" :v-model="isValidated">It has been validated?</b-form-checkbox>
        </b-col> -->
      </b-row>
      <b-row>
        <b-col>
          <div class="text-center">
            <br>
            <b-button @click.prevent="submit()">Submit</b-button>
          </div>
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
export default {
components: {},
  name: 'InsertPlace',
  data () {
    return {
      city : '',
      description: '',
    }
  },
  methods : {
    async submit(){
      try {
        this.$parent.hideError();
        const data = {city : this.city,
                      description : this.description,
                      is_deleted : false,
                      is_validated : true};
        const header = { 'Content-Type': 'application/json' };
        const response = await this.$http.post('http://'+this.$store.state.address+'/api/v1/place/', data, header);
        if (response.statusText=='CREATED'){
            this.$parent.refresh();
          }
        }
        catch (e) {
          console.log(e);
          this.$parent.showError();
        }
    }
  }
}
</script>

<style>

</style>