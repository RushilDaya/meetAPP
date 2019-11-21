import axios from 'axios';
const BASE_URL_GENERAL = process.env.VUE_APP_BASEURL+'/api/general/';

export function initDB(){
    axios.post(BASE_URL_GENERAL+'init')
    .then(response=>{
        return response.data
    })
    .catch(error =>{
        error;
        return 'sad'
    })
}

