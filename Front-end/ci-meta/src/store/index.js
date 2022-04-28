import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);
export default new Vuex.Store({
  state: {
    token: '',
    username: '',
    address: '172.20.27.81:8080/back-end',
    logged: false,
    id : 0,
    documentType: [],
    language: [],
  },
  mutations: {
    login(state, payload) {
      state.token = 'Bearer ' + payload.token;
      state.username = payload.username;
      state.logged = true;
      state.address= payload.address;
    },
    id(state, id){
      state.id = id;
    },
    storeDocumentType(state, newType) {
      state.documentType.push({value: newType.toLowerCase(), text: newType.charAt(0).toUpperCase() + newType.slice(1)});
    },
    storeLanguage(state, newLanguage) {
      state.language.push({value: newLanguage.toLowerCase(), text: newLanguage.charAt(0).toUpperCase() + newLanguage.slice(1)});
    },
    async initData(state) {
      try {
        const header = { 'Content-Type': 'application/json' };
        const response = await this.$http.get('http://'+this.$store.state.address+'/api/v1/data/', header);
        if (response.data.count>=1){
          for( data in response.data.result) {
            //TODO : aggiornare i campi delle lingue e doc type
          }
        }
      }
      catch (e) {
        this.loading = false;
        console.log(e);
        this.error = true;
      }
    },
    logout(state) {
      state.token = '';
      state.username = '';
      state.logged = false;
    },
  },
});