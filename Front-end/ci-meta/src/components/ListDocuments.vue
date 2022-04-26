<template>
  <div>
    <b-container>
      <hr>
      <b-row>
        <b-col>
          <div class="text-center">
            <b-button-group class="mx-1">
              <b-button v-if="page>0" @click="page = page-1, loadPage()" variant="primary">&laquo;</b-button>
              <b-button v-else>&laquo;</b-button>
              <b-button disabled>Page {{page+1}}</b-button>
              <b-button v-if="ids.length==pageSize" @click="page = page+1, loadPage()" variant="primary">&raquo;</b-button>
              <b-button v-else>&raquo;</b-button>
            </b-button-group>
          </div>
          </b-col>
      </b-row>
      <hr>
    </b-container>

    <p v-show="!show">Loading...</p>
    <b-table-simple v-show="show">
      <b-thead>
        <b-tr>
          <b-th>Id</b-th>
          <b-th>Type</b-th>
          <b-th>Date</b-th>
          <b-th></b-th>
          <b-th>Incipit</b-th>
          <b-th>Note</b-th>
        </b-tr>
      </b-thead>
      
      <b-tr v-for="(doc, index) in docs" :key="doc" v-show="!doc.is_deleted">
        <b-td>
          <b-button variant="link" @click="showDocs(ids[index])">
            {{doc.collection}} {{doc.folder}} - {{doc.folder_number}}
          </b-button>
        </b-td>
        <b-td>{{doc.type}}</b-td>
        <b-td>{{doc.gregorian_date}}</b-td>
        <b-td></b-td>
        <b-td>{{doc.incipit}}</b-td>
        <b-td>{{doc.note}}</b-td>
      </b-tr>

    </b-table-simple>
  </div>
</template>

<script>
import ShowDocuments from './ShowDocuments.vue';
export default {
  components: { ShowDocuments },
  name: 'ListDocuments',
  data () {
    return {
      ids :[],
      docs:[],
      show: false,
      showDoc : false,
      page : 0,
      pageSize : 20,
    }
  },
    async mounted() {
      try {
        this.error = false;
        const header = { 'Content-Type': 'application/json' };
        //(page:0,page_size:10,filters:!((col:is_deleted,opr:eq,value:False)))
        const response = await this.$http.get('http://'+this.$store.state.address+'/api/v1/document/?q=(page:'+this.page+',page_size:'+this.pageSize+',filters:!((col:is_deleted,opr:eq,value:False)))', header);
        console.log(response.data.count);
        if (response.data.count>=1){
          this.show=true;
          this.ids=response.data.ids;
          this.docs=response.data.result;
        }
      }
      catch (e) {
        this.loading = false;
        console.log(e);
        this.error = true;
      }
        
    },
    methods : {
      showDocs(id) {
        this.$router.push({name: 'Show Documents', params: {id: id}});
      },
      async loadPage() {
        try {
        this.error = false;
        const header = { 'Content-Type': 'application/json' };
        const response = await this.$http.get('http://'+this.$store.state.address+'/api/v1/document/?q=(page:'+this.page+',page_size:'+this.pageSize+')', header);
        console.log(response.data.count);
        if (response.data.count>=1){
          this.show=true;
          this.ids=response.data.ids;
          this.docs=response.data.result;
          }
        }
        catch (e) {
          this.loading = false;
          console.log(e);
          this.error = true;
        } 
      },
    }
};
</script>
