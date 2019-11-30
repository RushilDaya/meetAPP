const BASE_URL_USER = process.env.VUE_APP_BASEURL+'/api/user/';

//TODO: add api level error handling
//TODO: add user verification on server using tokens

// this call can be reduced to a single one with getUserData
export function emailExists(http,userEmail){
    return http.get(BASE_URL_USER+`email/${userEmail}`)
    .then(response=>{
        return response.data
    })
    .catch(error =>{
        error;
        return 'sad'
    })
}
export function attemptUserCreate(http,username,firstname,lastname,age,gender,email){
    var data = {username:username,
                firstname:firstname,
                lastname:lastname,
                age:age,
                gender:gender,
                email:email}
    return http.post(BASE_URL_USER+'create',data)
    .then(response=>{
        return response.data
    })
    .catch(error =>{
        return error;
    })
}

export function attemptUserUpdate(http,email,username,firstname,lastname,age,gender){
    var data = {username:username,
        firstname:firstname,
        lastname:lastname,
        age:age,
        gender:gender,
        email:email}
    return http.put(BASE_URL_USER+`${email}`,data)
    .then(response=>{
        return response.data
    })
    .catch(error=>{
        return error;
    })
}

export function getUserData(http,  email){
    return http.get(BASE_URL_USER+`${email}`)
    .then(response =>{
        return response.data
    })
    .catch(error=>{
        error;
        return 'sad'
    })
}