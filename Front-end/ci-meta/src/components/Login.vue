<template>
  <div class="d-flex align-items-center justify-content-center">

    <b-card
    title="Login"
    style="max-width: 40rem;"
    class="text-center"
    border-variant="warning"
    >
      <b-form inline v-if="!this.$store.state.logged">
        <b-container>
          <b-row>
            <b-col>
              <b-input-group prepend="Username" class="mb-2 mr-sm-2 mb-sm-0">
                <b-form-input v-model="uname"></b-form-input>
              </b-input-group>
            </b-col>
            <b-col>
              <b-input-group prepend="Password" class="mb-2 mr-sm-2 mb-sm-0">
                <b-form-input v-model="pw" type="password"></b-form-input>
              </b-input-group>
            </b-col>
          </b-row>
        </b-container>
        <br>
        <b-button v-on:click.prevent="login()" variant="primary">Login</b-button>
        <br>
        <div class="text-center" style="margin-top: 20px;" v-if="loading">
          <b-spinner variant="primary"></b-spinner>
        </div>
        <div class="text-center" style="margin-top: 20px;" v-if="error">
          Error! Please check your credentials and retry
        </div>
      </b-form>
    </b-card>
    
  </div>
</template>

<script>
  export default {
    name: 'Login',
    data() {
      return {
        loading: false,
        logged: false,
        error: false,
        uname: '',
        pw: '',
        address: '172.20.27.81:8080/back-end',
        timeout: false,
        docker: false,
      };
    },
    methods: {
      async login() {
        try {
          this.error = false;
          const data = { username: this.uname, password: this.pw, provider: 'db' };
          const headers = { 'Content-Type': 'application/json' };
          this.loading=true;
          const response = await this.$http.post('http://'+this.address+'/api/v1/security/login', data, headers);
          if (response.statusText!='OK'){
            this.loading=false;
            this.error=true;
          }
          else {
            this.loading=false;
            this.logged = true;
            this.$http.defaults.headers.common['Authorization'] ='Bearer '+response.data.access_token;
            this.$store.commit('login', {username: this.uname, token: response.data.access_token, address: this.address});
            this.findId();
            this.loadConfiguration();
            this.$router.push({ name: 'Home'});
          }
        }
        catch (e) {
          console.log(e);
          this.error = true;
          this.loading= false;
        }
      },
      async findId() {
        try{
          const headers = { 'Content-Type': 'application/json' };
          const response = await this.$http.get('http://'+this.address+'/api/v1/appuser/', headers);
          response.data.result.forEach((user, index) => {
            if(user.username==this.uname){
              this.$store.commit('id', response.data.ids[index]);
              }
            });
        }
        catch (e){
          console.log(e);
        }
      },
      async loadConfiguration(){
        try{
          const headers = { 'Content-Type': 'application/json' };
          const response = await this.$http.get('http://'+this.address+'/api/v1/configuration/', headers);
          response.data.result.forEach((element, index) => {
            if(element.key=='language'){
              this.$store.commit('storeLanguage', element.value);
            }
            if(element.key=='docType'){
              this.$store.commit('storeDocumentType', element.value);
            }
            });
        }
        catch (e){
          console.log(e);
        }
      }
    },
  };
</script>