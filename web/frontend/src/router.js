import Profile from "./components/Profile.vue";
import HomeComponent from './components/HomeComponent.vue';
import Management from './components/Management.vue';
import CreateProfile from './components/CreateProfile.vue';
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
    },
    {
      path: '/management',
      name: 'management',
      component: Management
    },
    {
      path: '/createProfile',
      name:'createProfile',
      component: CreateProfile,
      props: true
    }
  ]
});

export default router;
