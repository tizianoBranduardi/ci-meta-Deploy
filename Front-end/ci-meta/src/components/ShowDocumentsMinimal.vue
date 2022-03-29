<template>
    <div>
      <h2 class="text-center">Document {{id}}</h2>
      <b-container>
        <hr>
        <b-row>
          <b-col b-col>
            <p>
              <strong>Document type &emsp;</strong>{{documentType}}
            </p>
          </b-col>

          <b-col b-col >
            <p>
              <strong>Date &emsp;</strong>{{date}}
            </p>
          </b-col>
        </b-row>

        <b-row>
          <b-col b-col >
            <p >
              <strong>Collection &emsp;</strong>{{collection}}
            </p>
          </b-col>
          <b-col b-col >
            <p>
              <strong>Folder &emsp;</strong>{{folder}}
            </p>
          </b-col>
          <b-col b-col >
            <p>
              <strong>Folder Number &emsp;</strong>{{folderNumber}}
            </p>
          </b-col>
          <b-col b-col >
            <p>
              <strong>Shelfmark &emsp;</strong>{{shelfmark}}
            </p>
          </b-col>
        </b-row>

        <hr>

        <b-row>
          <b-col b-col>
            <p>
              <strong>Incipit &emsp;</strong>{{incipit}}
            </p>
          </b-col>
        </b-row>
      </b-container>
  </div>
</template>

<script>
export default {
  name: 'ShowDocumentsMinimal',
  props : ['id'],
  data () {
    return {
      documentType: '',
      incipit: '',
      language: '',
      date: '',
      collection: '',
      folder: '',
      folderNumber: '',
      shelfmark: '',
    }
  },
  async mounted() {
    try {
      this.error = false;
      const header = { 'Content-Type': 'application/json' };
      const response = await this.$http.get('http://'+this.$store.state.address+'/api/v1/document/'+this.id, header);
      if (response.status==200){
        this.documentType=response.data.result.type;
        this.incipit=response.data.result.incipit;
        this.language=response.data.result.language;
        this.date=response.data.result.gregorian_date;
        this.collection=response.data.result.collection;
        this.folder=response.data.result.folder;
        this.folderNumber=response.data.result.folder_number;
        this.shelfmark=response.data.result.shelfmark;
      }
    }
    catch (e) {
      this.loading = false;
      console.log(e);
      this.error = true;
    } 
  },
  methods: {
  }
};
</script>
