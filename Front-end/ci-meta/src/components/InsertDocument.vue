<template>
  <div> 
    <b-container v-show="!success">
      <b-container>
        <h3 class="text-center">Create new Document</h3>
        <br>
        <b-row>
          <b-overlay :show="insertDocType" :opacity="1">
            <div style="display-inline">
              <b-col class="text-cente">
                <strong>Document type &emsp;</strong>
                <b-form-select size="sm" v-model="documentType" :options="this.$store.state.documentType"/>
              </b-col>
            </div>
          </b-overlay>
        </b-row>
      </b-container>
      <br>

      <b-container>
        <b-row>
          <b-col>
            <strong>Publication </strong>
            <b-form-input type="text" v-model="publication" />
          </b-col>
          <b-col>
            <strong>Archive </strong>
            <b-form-input type="text" v-model="archive" />
          </b-col>
        </b-row>
        <b-row >
          <b-col>
          <br>
          </b-col>
        </b-row>
        <b-row>
          <b-col>
            <strong>Collection &emsp;</strong>
            <b-form-input type="text" v-model="collection" />
          </b-col>
          <b-col>
            <strong>Folder &emsp;</strong>
            <b-form-input type="text" v-model="folder" />
          </b-col>
          <b-col>
            <strong>Folder Number &emsp;</strong>
            <b-form-input type="text" v-model="folderNumber" />
          </b-col>
          <b-col><strong>Shelfmark &emsp;</strong>
          <b-form-input type="text" v-model="shelfmark" /></b-col>
        </b-row>
      </b-container>
      <hr>
      <b-container>
        <b-row>
          <b-col>
            <b-input-group class="mt-3" style="display-inline">
              <strong>Title &emsp;</strong>
              <b-form-input v-model="title" maxlength="255" placeholder="" />
            </b-input-group>
          </b-col>
          <b-col>
            <b-input-group class="mt-3" style="display-inline">
              <strong>Incipit &emsp;</strong>
              <b-form-input v-model="incipit" maxlength="255" placeholder="" />
            </b-input-group>
          </b-col>
        </b-row>
      </b-container>
      <br>
      
      <b-container>
        <b-row>
          <b-col>
            <strong>Transcription &emsp;</strong>
            <b-form-textarea
              id="textarea"
              v-model="transcription"
              placeholder=""
              rows="8"
              max-rows="10"
            ></b-form-textarea>
          </b-col>
        </b-row>
      </b-container>
      <br>
      <b-container>
        <b-row>
          <b-col>
                <strong>Document language &emsp;</strong>
                <b-form-select size="sm" v-model="language" :options="this.$store.state.language"/>
              </b-col>
          <b-col>
            <strong>Date &emsp;</strong>
            <input type="date" v-model="date" placeholder="YYYY-MM-DD" required pattern="\d{4}-\d{2}-\d{2}">
      
            <b-form-checkbox size="sm" :v-model="isDateDeduced">The date has been deduced?</b-form-checkbox>
          </b-col>
          <b-col lg="2">
          </b-col>
        </b-row>
      </b-container>
      <br>

      <b-container>
        <b-row>
          <b-col style="display-inline">
            <strong>Note &emsp;</strong>
            <b-form-textarea
              id="note"
              v-model="note"
              placeholder=""
              rows="3"
              max-rows="6"
            ></b-form-textarea>
          </b-col>
        </b-row>
      </b-container>
      <br>
      <hr>
    
      <div class="text-center">
        <b-button v-show="!loading" @click.prevent="submit()">Submit</b-button>
        <b-spinner v-show="loading" variant="primary"></b-spinner>
        <p v-show="error">The request handler returned an error. Check the server logs for more info.</p>
        <p v-show="success">Success! {{this.toastText}}</p>
      </div>
    </b-container>

    <b-container v-show="!success">
      <b-row>
        <b-col class="text-center">
          <p v-show="success">Success! {{this.toastText}}</p>
          <hr>
          <h3>Insert images - places - persons</h3>
          <br>
        </b-col>
      </b-row>
      <b-row>
        <b-col>
          <insert-image :id="docId" ref="images" />
        </b-col>
        <b-col style="display-inline">
          <b-card
            border-variant="default"
            header="Places"
            header-border-variant="default"
            header-text-variant="default"
            align="center"
            >
            <b-row>
              Sent from<br><b-form-select size="sm" v-model="placeFrom" :options="places"/><br>
            </b-row>
            <b-row>
              Sent to<br><b-form-select size="sm" v-model="placeTo" :options="places"/><br>
            </b-row>
            Or<b-button variant="link" @click="createPlace=!createPlace">create a new place</b-button>
            <insert-place v-show="createPlace"/>
          </b-card>
        </b-col>
      </b-row>
      <b-row>
        <div class="text-center">
          <hr>
          <b-button v-show="!loading" @click.prevent="secondSubmit()">Submit</b-button>
        </div>
      </b-row>
    </b-container>

  </div>
</template>

<script>
import InsertPlace from './InsertPlace.vue';
import InsertImage from './InsertImage.vue';
export default ({
    name: 'insertDocument',
    components: { InsertImage, InsertPlace },
    data(){
      return{
        documentType: '',
        incipit: '',
        transcription: '',
        language: '',
        date: '', // Year - Month - Day
        isDateDeduced: false,
        collection: '',
        folder: '',
        folderNumber: '',
        shelfmark: '',
        note: '',
        publication: '',
        archive: '',
        title: '',
        insertDocType: false,
        newDocumentType: '',
        insertLanguage: false,
        newLanguage: '',
        error: false,
        loading: false,
        toastText: '',
        success: false,
        docId: 0,
        places: [],
        placeFrom: '',
        placeTo: '',
        createPlace : false,
      }
    },
    async mounted(){
      try {
          const header = { 'Content-Type': 'application/json' };
          const response = await this.$http.get('http://'+this.$store.state.address+'/api/v1/place/', header);
          if (response.status==200){
            response.data.result.forEach((place,index) => {
              if(!place.is_deleted && place.is_validated)
                this.places.push({value:response.data.ids[index], text:place.city})
            });
          }
        }
        catch (e) {
          this.loading = false;
          console.log(e);
          this.error = true;
        }
    },
    methods: {
      async submit() {
        try {
          this.error = false;
          if(this.date=='')
            this.date=null;
          const data = { type: this.documentType,
                        incipit: this.incipit,
                        transcription: this.transcription,
                        note: this.note,
                        language: this.language,
                        gregorian_date : this.date,
                        collection : this.collection,
                        shelfmark: this.shelfmark,
                        folder: this.folder,
                        folder_number: this.folderNumber,
                        is_date_deduced: this.isDateDeduced,
                        publication: this.publication,
                        archive: this.archive,
                        };
          const header = { 'Content-Type': 'application/json' };
          this.loading=true;
          const response = await this.$http.post('http://'+this.$store.state.address+'/api/v1/document/', data, header);
          console.log(response);
          if (response.statusText=='CREATED'){
            this.toastText='New document info: \n ID : '+response.data.id;
            this.docId=response.data.id;
            this.success=true;
            this.loading=false;
          }
        }
        catch (e) {
          this.loading = false;
          console.log(e);
          this.error = true;
        }
      },
      async secondSubmit(){
        this.$refs.images.submit();
        try {
          const data = { place: this.placeFrom,
                        appuser: this.$store.state.id,
                        document: this.docId,
                        type: 'from'
                        };
          const header = { 'Content-Type': 'application/json' };
          const response = await this.$http.post('http://'+this.$store.state.address+'/api/v1/position/', data, header);
          if (response.statusText=='CREATED'){
            const data = { place: this.placeTo,
                        appuser: this.$store.state.id,
                        document: this.docId,
                        type: 'to'
                        };
            const header = { 'Content-Type': 'application/json' };
            const response = await this.$http.post('http://'+this.$store.state.address+'/api/v1/position/', data, header);
            if (response.statusText=='CREATED'){
              this.$router.push({ name: 'Home'});
            }
          }
        }
        catch (e) {
          console.log(e);
        }
      }
    },
})
</script>
