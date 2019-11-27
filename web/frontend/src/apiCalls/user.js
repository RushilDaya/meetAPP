import axios from 'axios';
const BASE_URL_USER = process.env.VUE_APP_BASEURL+'/api/user/';

//TODO: add api level error handling
//TODO: add user verification on server using tokens

// this call can be reduced to a single one with getUserData
export function emailExists(userEmail){
    return axios.get(BASE_URL_USER+`email/${userEmail}`)
    .then(response=>{
        return response.data
    })
    .catch(error =>{
        error;
        return 'sad'
    })
}
export function attemptUserCreate(username,firstname,surname,age,gender,email){
    var data = {username:username,
                firstname:firstname,
                surname:surname,
                age:age,
                gender:gender,
                email:email}
    return axios.post(BASE_URL_USER+'create',data)
    .then(response=>{
        return response.data
    })
    .catch(error =>{
        error;
        return 'sad'
    })
}

export function getUserData(email){
    return axios.get(BASE_URL_USER+`${email}`)
    .then(response =>{
        return response.data
    })
    .catch(error=>{
        error;
        return 'sad'
    })
}