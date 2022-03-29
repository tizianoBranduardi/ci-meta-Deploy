<template>
  <b-card
    border-variant="default"
    header="Images"
    header-border-variant="default"
    header-text-variant="default"
    align="center"
    >
    <b-row>
      <b-col>
        <b-carousel
        id="carousel"
        v-model="slide"
        :interval="10000"
        controls
        indicators
        background="#ababab"
        >
          <div v-for="(url, index) in imgUrl" v-bind:key="url">
            <b-carousel-slide v-bind:img-src="url.data">
              <div class="display-inline">
                <b-form-input size="sm" type="text" v-model="url.title" placeholder="Title" />
                <b-form-input size="sm" type="text" v-model="url.description" placeholder="Description" />
                <b-button v-on:click="deleteImage(index)" size="sm" text="delete" variant="primary">Delete</b-button>
              </div>
            </b-carousel-slide>
          </div>
        </b-carousel>
      </b-col>
    </b-row>
    <b-row no-gutters>
      <b-col>
        <b-card-body title="Insert image">
          <input
            type="file"
            @change="onFileChange"
            placeholder="Choose an image"
          >
        </b-card-body>
      </b-col>
    </b-row>
  </b-card>
</template>

<script>
  export default {
    name: 'InsertImage',
    props : { id:0 },
    data () {
      return {
        insertImage : true,
        imgUrl : [],
        imgIndex : [{}],
        encodedImg : '',
      }
    },
    async mounted() {
    try {
      this.error = false;
      const header = { 'Content-Type': 'application/json' };
      const response = await this.$http.get('http://'+this.$store.state.address+'/api/v1/image/', header);
      if (response.status==200){
        response.data.result.forEach((image, index) => {
          if(image.document.id==this.id){
            this.imgUrl.push({data : image.data, title : image.title, description : image.description});
            this.imgIndex.push(response.data.ids[index]);
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
      deleteImage(index) {
        this.imgUrl.splice(index,1);
      },
      onFileChange(e) {
        const file = e.target.files[0];
        this.encodeImage(file);
      },
      encodeImage(fileObject){
        const reader = new FileReader();
        reader.onloadend = ((e) => {
          this.imgUrl.push({data : e.target.result, title : '', description : ''});
        });
        reader.readAsDataURL(fileObject);
      },
      async post(img){
        try {
          const data = { data : img.data,
                      title : img.title,
                      description : img.description,
                      document: this.id };
          const header = { 'Content-Type': 'application/json' };
          const response = await this.$http.post('http://'+this.$store.state.address+'/api/v1/image/', data, header);
          if (response.statusText=='CREATED'){
            console.log("OK");
          }
        }
        catch (e) {
          this.loading = false;
          console.log(e);
          this.error = true;
        }
      },
      async delete(img){
        try {
          const header = { 'Content-Type': 'application/json' };
          const response = await this.$http.delete('http://'+this.$store.state.address+'/api/v1/image/'+img, header);
        }
        catch (e) {
          this.loading = false;
          console.log(e);
          this.error = true;
        }
      },
      async submit() {
        if(this.imgUrl.length>0)
          this.imgUrl.forEach(img => this.post(img));
        if(this.imgIndex.length>0)
          this.imgIndex.forEach(index => this.delete(index));
      }
    }
  };
</script>
