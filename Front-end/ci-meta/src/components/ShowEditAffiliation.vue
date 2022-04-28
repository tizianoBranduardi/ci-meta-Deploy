<template>
  <b-container>
    <b-card
            border-variant="default"
            header="Affiliation to Institutions"
            header-border-variant="default"
            header-text-variant="bold"
            align="center"
            >
      <div v-for="(affiliation, index) in affiliations" :key="affiliation">
        <b-row v-show="!edit" class="text-center">
          <b-col cols=6>
            Institution : <i>{{affiliation.institution.name}}</i>
          </b-col>
          <b-col cols=2>
            From : <i>{{affiliation.from_date}}</i>
          </b-col>
          <b-col cols=2>
            To : <i>{{affiliation.to_date}}</i>
          </b-col>
          <!-- <b-col>
            <b-button variant="link" size="sm" @click="deleteAffiliation(index)">
                    <b-icon icon="pencil-square" ></b-icon>
            </b-button>
          </b-col> -->
          <b-col cols=2>
            <b-button variant="link" size="sm" @click="edit = true">
                    <b-icon icon="pencil-square" ></b-icon>
            </b-button>
          </b-col>
        </b-row>
      </div>
      <b-row>
        <b-col>
          <br>
          <b-button variant="link" size="sm" @click="newAffiliation = !newAffiliation">
                  <b-icon icon="plus-circle" ></b-icon>Add new affiliation
          </b-button>
          <br><br>
        </b-col>
      </b-row>

      <b-row v-show="edit" class="text-center">
        <b-col cols=5>
        Sent from&emsp;<b-form-select v-model="fromId" :options="institutions"/>
        </b-col>
        <b-col cols=5>
        Sent to&emsp;<b-form-select v-model="toId" :options="institutions"/>
        </b-col>
        <b-col>
          <b-button variant="primary" size="sm" @click="submit(), edit=false">Save
          </b-button>
        </b-col>
      </b-row>

      <b-row v-show="newAffiliation" class="text-center">
        <b-col cols=6>
          Institution<br><b-form-select v-model="newInstitution" :options="institutions"/>
        </b-col>
        <b-col cols=2>
          From&emsp;<b-form-input v-model="newFrom" />
        </b-col>
        <b-col cols=2>
          To&emsp;<b-form-input v-model="newTo" />
        </b-col>
        <b-col>
          <br>
          <b-button variant="primary" size="sm" @click="addAffiliation()">Save
          </b-button>
        </b-col>
      </b-row>
      <b-row v-show="error" class="text-center">
        <b-col>
          <b>Error! Check the input [From & To date fields must be only numbers]</b>
        </b-col>
      </b-row>

    </b-card>
  </b-container>
</template>

<script>
export default {
  components: {},
  name: 'ShowEditAffiliation',
  props : {personId : 0},
  data () {
    return {
      institutions : [],
      affiliations : [],
      newAffiliation : '',
      newInstitution : '',
      newFrom : '',
      newTo : '',
      toId : '',
      fromId : '',
      positionToId: 0,
      positionFromId: 0,
      to: '-- missing --',
      from : '-- missing --',
      edit: false,
      description: '',
      error: false,
    }
  },
  async mounted(){
    try {
      const header = { 'Content-Type': 'application/json' };
      const response = await this.$http.get('http://'+this.$store.state.address+'/api/v1/affiliation/', header);
      if (response.status==200){
        response.data.result.forEach((affiliation, index) => {
          if(affiliation.person.id==this.personId){
              this.affiliations.push(affiliation);
          }
        });
        const response2 = await this.$http.get('http://'+this.$store.state.address+'/api/v1/institution/', header);
        if (response2.status==200){
          this.institutions.push({value:0, text:'-- Empty --'})
          response2.data.result.forEach((institution,index) => {
            this.institutions.push({value:response2.data.ids[index]+"-"+institution.name, text:institution.name});
          });
        }
      }
    }
    catch (e) {
      console.log(e);
    }
  },
  methods : {
    async addAffiliation(){
      this.error=false;
      try {
        const header = { 'Content-Type': 'application/json' };
        const data = {'person': this.personId, 'institution':parseInt(this.newInstitution.split("-")[0]), 'from_date': parseInt(this.newFrom), 'to_date': parseInt(this.newTo)};
        const response = await this.$http.post('http://'+this.$store.state.address+'/api/v1/affiliation/', data, header);
        if(response.status==201){
          this.newAffiliation=false;
          this.reload();
        }
        else {
          this.error=true;
        }
      }
      catch (e) {
        this.error=true;
        console.log(e);
      }      
    }, 
    async reload(){
      try {
        const header = { 'Content-Type': 'application/json' };
        const response = await this.$http.get('http://'+this.$store.state.address+'/api/v1/affiliation/', header);
        if (response.status==200){
          this.affiliations=[];
          response.data.result.forEach((affiliation, index) => {
            if(affiliation.person.id==this.personId){
                this.affiliations.push(affiliation);
            }
          });
        }
      }
      catch (e) {
        console.log(e);
      }
    }
    // async submit() {
    //   try {
    //     const header = { 'Content-Type': 'application/json' };
    //     // FROM
    //     if(this.positionFromId!=0 && this.fromId==0){ //STATO INIT : campo popolato  - - STATO FINALE : vuoto
    //       const deleteFrom = await this.$http.delete('http://'+this.$store.state.address+'/api/v1/position/'+this.positionFromId, header);
    //       this.from='-- missing --';
    //       this.positionFromId=0;
    //     }
    //     else if(this.positionFromId!=0 && this.fromId!=0){ //STATO INIT : campo popolato  - - STATO FINALE : campo popolato
    //       const dataFrom = {'appuser': this.$store.state.id, 'document': this.docId, 'place':parseInt(this.fromId.split("-")[0]), 'type':'from'}
    //       const responsePutFrom = await this.$http.put('http://'+this.$store.state.address+'/api/v1/position/'+this.positionFromId, dataFrom, header);
    //       this.from=this.fromId.split("-")[1];
    //     }
    //     else if (this.positionFromId==0 && this.fromId!=0){ //STATO INIT : vuoto  - - STATO FINALE : campo popolato
    //       const dataFrom = {'appuser': this.$store.state.id, 'document': this.docId, 'place':parseInt(this.fromId.split("-")[0]), 'type':'from'}
    //       const responsePostFrom = await this.$http.post('http://'+this.$store.state.address+'/api/v1/position/', dataFrom, header);
    //       this.from=this.fromId.split("-")[1];
    //     }
    //     //TO
    //     if(this.positionToId!=0 && this.toId==0){ //STATO INIT : campo popolato  - - STATO FINALE : vuoto
    //       const deleteTo = await this.$http.delete('http://'+this.$store.state.address+'/api/v1/position/'+this.positionToId, header);
    //       this.to='-- missing --';
    //       this.positionToId=0;
    //     }
    //     else if(this.positionToId!=0 && this.toId!=0){ //STATO INIT : campo popolato  - - STATO FINALE : campo popolato
    //       const dataTo = {'appuser': this.$store.state.id, 'document': this.docId, 'place':parseInt(this.toId.split("-")[0]), 'type':'to'}
    //       const responsePutTo = await this.$http.put('http://'+this.$store.state.address+'/api/v1/position/'+this.positionToId, dataTo, header);
    //       this.to=this.toId.split("-")[1];
    //     }
    //     else if (this.positionToId==0 && this.toId!=0){ //STATO INIT : vuoto  - - STATO FINALE : campo popolato
    //       const dataTo = {'appuser': this.$store.state.id, 'document': this.docId, 'place':parseInt(this.toId.split("-")[0]), 'type':'to'}
    //       const responsePostTo = await this.$http.post('http://'+this.$store.state.address+'/api/v1/position/', dataTo, header);
    //       this.to=this.toId.split("-")[1];
    //     }
    //     this.edit=false;
        
    //   }
    //   catch (e) {
    //     console.log(e);
    //   }
    // },
  }
}
</script>
