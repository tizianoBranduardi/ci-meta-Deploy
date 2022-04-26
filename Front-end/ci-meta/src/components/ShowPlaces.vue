<template>
  <b-container>
    <b-card
            border-variant="default"
            header="Places"
            header-border-variant="default"
            header-text-variant="bold"
            align="center"
            >
      <b-row v-show="!edit" class="text-center">
        <b-col cols=5>
          Sent from : <i>{{from}}</i>
        </b-col>
        <b-col cols=5>
          Sent to : <i>{{to}}</i>
        </b-col>
        <b-col cols=2>
          <b-button variant="link" size="sm" @click="edit = true">
                  <b-icon icon="pencil-square" ></b-icon>
          </b-button>
        </b-col>
      </b-row>

      <b-row v-show="edit" class="text-center">
        <b-col cols=5>
        Sent from&emsp;<b-form-select v-model="fromId" :options="places"/>
        </b-col>
        <b-col cols=5>
        Sent to&emsp;<b-form-select v-model="toId" :options="places"/>
        </b-col>
        <b-col>
          <b-button variant="primary" size="sm" @click="submit(), edit=false">Save
          </b-button>
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
      places : [],
      toId : '',
      fromId : '',
      positionToId: 0,
      positionFromId: 0,
      to: '-- missing --',
      from : '-- missing --',
      edit: false,
      description: '',
    }
  },
  async mounted(){
    try {
      const header = { 'Content-Type': 'application/json' };
      const response = await this.$http.get('http://'+this.$store.state.address+'/api/v1/position/', header);
      if (response.status==200){
        response.data.result.forEach((position, index) => {
          console.log(position.document.id);
          if(position.document.id==this.docId){
            if(position.type=="to"){
              this.to=position.place.city;
              this.positionToId=response.data.ids[index];
            }
            if(position.type=="from"){
              this.from=position.place.city;
              this.positionFromId=response.data.ids[index];
            }
          }
        });
        const response2 = await this.$http.get('http://'+this.$store.state.address+'/api/v1/place/?q=(filters:!((col:is_deleted,opr:eq,value:False),(col:is_validated,opr:eq,value:True)))', header);
        if (response2.status==200){
          this.places.push({value:0, text:'-- Empty --'})
          response2.data.result.forEach((place,index) => {
            this.places.push({value:response2.data.ids[index]+"-"+place.city, text:place.city});
          });
        }
      }
    }
    catch (e) {
      this.loading = false;
      console.log(e);
      this.error = true;
    }
  },
  methods : {
    async submit() {
      try {
        const header = { 'Content-Type': 'application/json' };
        // FROM
        if(this.positionFromId!=0 && this.fromId==0){ //STATO INIT : campo popolato  - - STATO FINALE : vuoto
          const deleteFrom = await this.$http.delete('http://'+this.$store.state.address+'/api/v1/position/'+this.positionFromId, header);
          this.from='-- missing --';
          this.positionFromId=0;
        }
        else if(this.positionFromId!=0 && this.fromId!=0){ //STATO INIT : campo popolato  - - STATO FINALE : campo popolato
          const dataFrom = {'appuser': this.$store.state.id, 'document': this.docId, 'place':parseInt(this.fromId.split("-")[0]), 'type':'from'}
          const responsePutFrom = await this.$http.put('http://'+this.$store.state.address+'/api/v1/position/'+this.positionFromId, dataFrom, header);
          this.from=this.fromId.split("-")[1];
        }
        else if (this.positionFromId==0 && this.fromId!=0){ //STATO INIT : vuoto  - - STATO FINALE : campo popolato
          const dataFrom = {'appuser': this.$store.state.id, 'document': this.docId, 'place':parseInt(this.fromId.split("-")[0]), 'type':'from'}
          const responsePostFrom = await this.$http.post('http://'+this.$store.state.address+'/api/v1/position/', dataFrom, header);
          this.from=this.fromId.split("-")[1];
        }
        //TO
        if(this.positionToId!=0 && this.toId==0){ //STATO INIT : campo popolato  - - STATO FINALE : vuoto
          const deleteTo = await this.$http.delete('http://'+this.$store.state.address+'/api/v1/position/'+this.positionToId, header);
          this.to='-- missing --';
          this.positionToId=0;
        }
        else if(this.positionToId!=0 && this.toId!=0){ //STATO INIT : campo popolato  - - STATO FINALE : campo popolato
          const dataTo = {'appuser': this.$store.state.id, 'document': this.docId, 'place':parseInt(this.toId.split("-")[0]), 'type':'to'}
          const responsePutTo = await this.$http.put('http://'+this.$store.state.address+'/api/v1/position/'+this.positionToId, dataTo, header);
          this.to=this.toId.split("-")[1];
        }
        else if (this.positionToId==0 && this.toId!=0){ //STATO INIT : vuoto  - - STATO FINALE : campo popolato
          const dataTo = {'appuser': this.$store.state.id, 'document': this.docId, 'place':parseInt(this.toId.split("-")[0]), 'type':'to'}
          const responsePostTo = await this.$http.post('http://'+this.$store.state.address+'/api/v1/position/', dataTo, header);
          this.to=this.toId.split("-")[1];
        }
        this.edit=false;
        
      }
      catch (e) {
        console.log(e);
      }
    },
  }
}
</script>
