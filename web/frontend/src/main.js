import Vue from 'vue'
import App from './App.vue'
import router from './router'
import Buefy from 'buefy'
import 'buefy/dist/buefy.css'

// Import the Auth0 configuration
import { domain, clientId } from "../auth_config.json";

// Import the plugin here
import { Auth0Plugin } from "./auth";

import axios from "axios";
Vue.prototype.$http = axios

// Install the authentication plugin here
Vue.use(Auth0Plugin, {
  domain,
  clientId,
  onRedirectCallback: appState => {
    router.push(
      appState && appState.targetUrl
        ? appState.targetUrl
        : window.location.pathname
    );
  }
});

import VueRouter from 'vue-router'

Vue.use(VueRouter)
Vue.use(Buefy)

Vue.config.productionTip = false;
Vue.config.devtools = true;


new Vue({
  render: h => h(App),
  router
}).$mount('#app')
