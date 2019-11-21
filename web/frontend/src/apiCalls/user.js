import axios from 'axios';
const BASE_URL_USER = process.env.VUE_APP_BASEURL+'/api/user/';

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
export function attemptUserCreate(userName,firstName,surname,age,gender,email){
    var data = {username:userName,
                firstname:firstName,
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