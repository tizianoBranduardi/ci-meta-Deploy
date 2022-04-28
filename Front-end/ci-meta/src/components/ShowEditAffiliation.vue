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
          <b-col cols=4>
            Institution : <i>{{affiliation.institution.name}}</i>
          </b-col>
          <b-col cols=3>
            From : <i>{{affiliation.from_date}}</i>
          </b-col>
          <b-col cols=3>
            To : <i>{{affiliation.to_date}}</i>
          </b-col>
          <b-col cols=2>
            <b-button variant="link" size="sm" @click="edit=!edit, error=false, editInstitution=affiliation.institution.id, editFrom=affiliation.from_date, editTo=affiliation.from_date, editIndex=index">
                    <b-icon icon="pencil-square" ></b-icon>
            </b-button>
          </b-col>
        </b-row>
      </div>
      <b-row>
        <b-col>
          <br>
          <b-button variant="link" size="sm" @click="newAffiliation = !newAffiliation, error=false">
                  <b-icon icon="plus-circle" ></b-icon>Add new affiliation
          </b-button>
          <br><br>
        </b-col>
      </b-row>

      <b-row v-show="edit" class="text-center">
        <b-col cols=4>
          Institution<b-form-select v-model="editInstitution" :options="institutions"/>
        </b-col>
        <b-col cols=3>
          From&emsp;<b-form-input v-model="editFrom" />
        </b-col>
        <b-col cols=3>
          To&emsp;<b-form-input v-model="editTo" />
        </b-col>
        <b-col cols=1>
          <br>
          <b-button variant="success" size="sm" @click="submit()">
                  <b-icon icon="check2-square" ></b-icon>
          </b-button>
        </b-col>
        <b-col cols=1>
          <br>
          <b-button variant="danger" size="sm" @click="deleteAffiliation()">
                  <b-icon icon="trash" ></b-icon>
          </b-button>
        </b-col>
      </b-row>

      <b-row v-show="newAffiliation" class="text-center">
        <b-col cols=4>
          Institution<br><b-form-select v-model="newInstitution" :options="institutions"/>
        </b-col>
        <b-col cols=3>
          From&emsp;<b-form-input v-model="newFrom" />
        </b-col>
        <b-col cols=3>
          To&emsp;<b-form-input v-model="newTo" />
        </b-col>
        <b-col>
          <br>
          <b-button variant="primary" size="sm" @click="addAffiliation()">
            <b-icon icon="check2-square" ></b-icon>
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
      ids: [],
      newAffiliation : '',
      newInstitution : '',
      newFrom : '',
      newTo : '',
      editInstitution : '',
      editFrom : '',
      editTo : '',
      editIndex : 0,
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
        this.ids=response.data.ids;
        response.data.result.forEach((affiliation, index) => {
          if(affiliation.person.id==this.personId){
              this.affiliations.push(affiliation);
          }
        });
        const response2 = await this.$http.get('http://'+this.$store.state.address+'/api/v1/institution/', header);
        if (response2.status==200){
          response2.data.result.forEach((institution,index) => {
            this.institutions.push({value:response2.data.ids[index], text:institution.name});
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
        const data = {'person': this.personId, 'institution':parseInt(this.newInstitution), 'from_date': parseInt(this.newFrom), 'to_date': parseInt(this.newTo)};
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
          this.ids=response.data.ids;
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
    },
    async submit() {
      this.error=false;
      try {
        const header = { 'Content-Type': 'application/json' };
        const data = {'person': this.personId, 'institution':parseInt(this.editInstitution), 'from_date': parseInt(this.editFrom), 'to_date': parseInt(this.editTo)};
        const response = await this.$http.put('http://'+this.$store.state.address+'/api/v1/affiliation/'+this.ids[this.editIndex], data, header);
        if(response.status==200){
          this.reload();
          this.edit=false;
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
    async deleteAffiliation() {
      this.error=false;
      try {
        const header = { 'Content-Type': 'application/json' };
        const response = await this.$http.delete('http://'+this.$store.state.address+'/api/v1/affiliation/'+this.ids[this.editIndex], header);
        if(response.status==200){
          this.reload();
          this.edit=false;
        }
        else {
          this.error=true;
        }
      }
      catch (e) {
        this.error=true;
        console.log(e);
      }      
    }
  }
}
</script>
