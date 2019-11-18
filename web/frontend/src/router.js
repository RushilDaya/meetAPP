import Profile from "./components/Profile.vue";
import HomeComponent from './components/HomeComponent.vue';
import VueRouter from 'vue-router';

const router = new VueRouter({
  mode: 'history',
  routes: [
    // .. other routes and pages ..
    {
      path: "/",
      name: "home",
      component:HomeComponent
    },
    {
      path: "/profile",
      name: "profile",
      component: Profile
    }
  ]
});

export default router;