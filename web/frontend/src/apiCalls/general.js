const BASE_URL_GENERAL = process.env.VUE_APP_BASEURL+'/api/general/';

export function initDB(http){
    http.post(BASE_URL_GENERAL+'init')
    .then(response=>{
        return response.data
    })
    .catch(error =>{
        error;
        return 'sad'
    })
}

