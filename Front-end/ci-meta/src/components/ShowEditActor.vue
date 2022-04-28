<template>
  <b-container>
    <b-card
            border-variant="default"
            header="Persons"
            header-border-variant="default"
            header-text-variant="bold"
            align="center"
            >
      <b-row v-show="!edit" class="text-center">
        <b-col cols=5>
          <b>Sender</b> : <i>{{from}}</i>
        </b-col>
        <b-col cols=5>
          <b>Recipient</b> : <i>{{to}}</i>
        </b-col>
        <b-col cols=2>
          <b-button variant="link" size="sm" @click="edit = true">
                  <b-icon icon="pencil-square" ></b-icon>
          </b-button>
        </b-col>
      </b-row>

      <b-row v-show="edit" class="text-center">
        <b-col cols=2>
          <br>
          <b-form-group description="Name's first letter">
            <b-form-input type="text" :formatter="loadPersons()" v-model="letterSender"/>
          </b-form-group>
        </b-col>
        <b-col>
        Sender
          <vue-single-select v-model="fromId" :options="persons" option-label="text" />
        </b-col>
        <b-col>
        Recipient
        <vue-single-select v-model="toId" :options="persons" option-label="text" />
        </b-col>
        <b-col cols=2>
          <br>
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
  name: 'ShowEditActor',
  props : {docId : 0},
  data () {
    return {
      persons : [{value:0, text:'-- Empty --'}],
      toId : '',
      fromId : '',
      actorToId: 0,
      actorFromId: 0,
      to: '-- missing --',
      from : '-- missing --',
      edit: false,
      description: '',
      letterSender: '',
      oldLetter: '',
    }
  },
  async mounted(){
    try {
      const header = { 'Content-Type': 'application/json' };
      const response = await this.$http.get('http://'+this.$store.state.address+'/api/v1/actor/', header);
      if (response.status==200){
        response.data.result.forEach((actor, index) => {
          if(actor.document.id==this.docId){
            if(actor.role=="recipient"){
              this.to=actor.person.name;
              this.actorToId=response.data.ids[index];
            }
            if(actor.role=="sender"){
              this.from=actor.person.name;
              this.actorFromId=response.data.ids[index];
            }
          }
        });
      }
    }
    catch (e) {
      console.log(e);
      this.error = true;
    }
  },
  methods : {
    async loadPersons(){
      if(this.oldLetter!=this.letterSender && this.letterSender!=''){
        this.oldLetter=this.letterSender;
        try{
          const header = { 'Content-Type': 'application/json' };
          const response2 = await this.$http.get('http://'+this.$store.state.address+'/api/v1/person/?q=(filters:!((col:is_deleted,opr:eq,value:False),(col:name,opr:sw,value:'+this.letterSender+')))', header);
          if (response2.status==200){
            this.persons=[];
            this.persons.push({value:0, text:'-- Empty --'})
            response2.data.result.forEach((person,index) => {
              this.persons.push({value:response2.data.ids[index]+"-"+person.name, text:person.name});
              //this.persons.push(person.name);
            });
          }
        }
        catch (e) {
          console.log(e);
        }
      }
    },
    async submit() {
      try {
        const header = { 'Content-Type': 'application/json' };
        // FROM
        if(this.actorFromId!=0 && parseInt(this.fromId.value)==0){ //STATO INIT : campo popolato  - - STATO FINALE : vuoto
          const deleteFrom = await this.$http.delete('http://'+this.$store.state.address+'/api/v1/actor/'+this.actorFromId, header);
          this.from='-- missing --';
          this.actorFromId=0;
        }
        if(this.actorFromId!=0 && parseInt(this.fromId.value)!=0){ //STATO INIT : campo popolato  - - STATO FINALE : campo popolato
          const dataFrom = {'appuser': this.$store.state.id, 'document': this.docId, 'person':parseInt(this.fromId.value.split("-")[0]), 'role':'sender'}
          const responsePutFrom = await this.$http.put('http://'+this.$store.state.address+'/api/v1/actor/'+this.actorFromId, dataFrom, header);
          this.from=this.fromId.value.split("-")[1];
        }
        if (this.actorFromId==0 && parseInt(this.fromId.value)!=0){ //STATO INIT : vuoto  - - STATO FINALE : campo popolato
          const dataFrom = {'appuser': this.$store.state.id, 'document': this.docId, 'person':parseInt(this.fromId.value.split("-")[0]), 'role':'sender'}
          const responsePostFrom = await this.$http.post('http://'+this.$store.state.address+'/api/v1/actor/', dataFrom, header);
          this.from=this.fromId.value.split("-")[1];
        }
        //TO
        if(this.actorToId!=0 && parseInt(this.toId.value)==0){ //STATO INIT : campo popolato  - - STATO FINALE : vuoto
          const deleteTo = await this.$http.delete('http://'+this.$store.state.address+'/api/v1/actor/'+this.actorToId, header);
          this.to='-- missing --';
          this.actorToId=0;
        }
        if(this.actorToId!=0 && parseInt(this.toId.value)!=0){ //STATO INIT : campo popolato  - - STATO FINALE : campo popolato
          const dataTo = {'appuser': this.$store.state.id, 'document': this.docId, 'person':parseInt(this.toId.value.split("-")[0]), 'role':'recipient'}
          const responsePutTo = await this.$http.put('http://'+this.$store.state.address+'/api/v1/actor/'+this.actorToId, dataTo, header);
          this.to=this.toId.value.split("-")[1];
        }
        if (this.actorToId==0 && parseInt(this.toId.value)!=0){ //STATO INIT : vuoto  - - STATO FINALE : campo popolato
          const dataTo = {'appuser': this.$store.state.id, 'document': this.docId, 'person':parseInt(this.toId.value.split("-")[0]), 'role':'recipient'}
          const responsePostTo = await this.$http.post('http://'+this.$store.state.address+'/api/v1/actor/', dataTo, header);
          this.to=this.toId.value.split("-")[1];
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
