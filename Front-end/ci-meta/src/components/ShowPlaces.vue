<template>
  <b-container>
    <b-card
            border-variant="default"
            header="Places"
            header-border-variant="default"
            header-text-variant="bold"
            align="center"
            >
      <b-row>
        <b-col>
          Sent from : {{from}}
        </b-col>
        <b-col>
          Sent to : {{to}}
        </b-col>
      </b-row>
    </b-card>
  </b-container>
</template>

<script>
export default {
  components: {},
  name: 'ShowPlaces',
  props : {docId : 0},
  data () {
    return {
      toId : '',
      fromId : '',
      to: '',
      from : '',
      description: '',
    }
  },
  async mounted(){
    try {
      const header = { 'Content-Type': 'application/json' };
      const response = await this.$http.get('http://'+this.$store.state.address+'/api/v1/position/', header);
      if (response.status==200){
        response.data.result.forEach((position, index) => {
          if(response.data.ids[index][0]==this.docId){
            if(position.type=="to")
              this.to=position.place.city;
            if(position.type=="from")
              this.from=position.place.city;
          }
        });
      }
    }
    catch (e) {
      this.loading = false;
      console.log(e);
      this.error = true;
    }
  },
  methods : {
  }
}
</script>