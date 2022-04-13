<template>
  <div>

    <div class="d-flex align-items-center justify-content-center" v-if="!submit">
        <b-card
          title="Search Document"
          style="max-width: 80rem;"
          class="text-center"
          border-variant="warning"
          >
          <b-form inline >
            <label class="sr-only">Insert one or many values to search for</label>
            <b-input-group class="mb-2 mr-sm-2 mb-sm-0">
              <b-form-input v-model="collection" placeholder="Collection"></b-form-input>&emsp;
              <b-form-input v-model="folder" placeholder="Folder"></b-form-input>&emsp;
              <b-form-input v-model="folder_number" placeholder="Folder Number"></b-form-input>&emsp;
              <b-form-input v-model="shelfmark" placeholder="Shelfmark"></b-form-input>
            </b-input-group>
            <br>
            <b-input-group class="mb-2 mr-sm-2 mb-sm-0">
              <b-form-input v-model="content" placeholder="Document Content"></b-form-input>
            </b-input-group>
            <br>
            <b-button v-on:click.prevent="search(), submit_search=true" variant="primary">Search</b-button>
            <br>
            <div class="text-center" style="margin-top: 20px;" v-if="loading">
            <b-spinner variant="primary"></b-spinner>
            </div>
          </b-form>
        </b-card>
    </div>

    <div style="margin: 10px 10px 10px 10px" v-if="submit_search & !submit & !loading">
      <h3>Found {{this.results}} documents</h3>
      <br>
      <b-table-simple>
        <b-thead>
          <b-tr>
            <b-th>Doc Id</b-th>
            <b-th>Doc Type</b-th>
            <b-th>Date</b-th>
            <b-th></b-th>
            <b-th>Incipit</b-th>
          </b-tr>
        </b-thead>
        
        <b-tr v-for="(doc, index) in docs" :key="doc">
          <b-td>
            <b-button variant="link" @click="id=ids[index], submit=true">
              {{doc.collection}} {{doc.folder}} {{doc.folder_number}} {{doc.shelfmark}}
            </b-button>
          </b-td>
          <b-td>{{doc.type}}</b-td>
          <b-td>{{doc.gregorian_date}}</b-td>
          <b-td></b-td>
          <b-td>{{doc.incipit}}</b-td>
        </b-tr>
      </b-table-simple>
    </div>

    <div v-if="submit">
      <b-button variant="link" @click="submit = false">Back to selection</b-button>
      <br>
      <ShowDocuments :id="id" />
    </div>

  </div>
</template>

<script>
import ShowDocuments from './ShowDocuments.vue'
export default {
  components: { ShowDocuments },
  name: 'SearchDocuments',
  data () {
    return {
      id : 0,
      collection: '',
      folder: '',
      folder_number: '',
      shelfmark: '',
      content: '',
      results: 0,
      ids :[],
      docs:[],
      loading: false,
      submit: false,
      submit_search: false,
      }
    },
  methods: {
    async search() {
      this.loading=true;
      try {
        const header = { 'Content-Type': 'application/json' };
        let rison= '?q=(filters:!(';
        let modified=false;
        if(this.collection!='') {
          rison=rison+'(col:collection,opr:ct,value:\''+this.collection+'\')';
          modified=true;
        }
        if(this.folder!='') {
          if(modified) rison=rison+',';
          rison=rison+'(col:folder,opr:ct,value:\''+this.folder+'\')';
          modified=true;
        }
        if(this.folder_number!='') {
          if(modified) rison=rison+',';
          rison=rison+'(col:folder_number,opr:ct,value:\''+this.folder_number+'\')';
          modified=true;
        }
        if(this.shelfmark!='') {
          if(modified) rison=rison+',';
          rison=rison+'(col:shelfmark,opr:ct,value:\''+this.shelfmark+'\')';
          modified=true;
        }
        if(this.content!='') {
          if(modified) rison=rison+',';
          rison=rison+'(col:transcription,opr:ct,value:\''+this.content+'\')';
          modified=true;
        }
        rison=rison+'))';
        // /?q=(filters:!((col:collection,opr:ct,value:'Fr'),(col:folder,opr:ct,value:'13'),(col:folder_number,opr:ct,value:'11r-34r'),(col:shelfmark,opr:ct,value:'11r-34r')))
        const response = await this.$http.get('http://'+this.$store.state.address+'/api/v1/document/'+rison, header);
        if (response.status==200){
          this.loading=false;
          this.results=response.data.count;
          this.ids=response.data.ids;
          this.docs=response.data.result;
        }
      }
      catch (e) {
        console.log(e);
      }
    }
  }
}
</script>

<style>

</style>