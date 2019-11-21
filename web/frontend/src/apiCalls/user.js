import axios from 'axios';
const BASE_URL_USER = process.env.VUE_APP_BASEURL+'/api/user/';

export function emailExists(userEmail){
    window.console.log(userEmail);
    axios.get(BASE_URL_USER+`email/${userEmail}`)
    .then(response=>{
        return response.data
    })
    .catch(error =>{
        error;
        return 'sad'
    })
}

