import Profile from "./components/Profile.vue";
import VueRouter from 'vue-router';

const router = new VueRouter({
  mode: 'history',
  routes: [
    // .. other routes and pages ..

    // NEW - add the route to the /profile component
    {
      path: "/profile",
      name: "profile",
      component: Profile
    }
  ]
});

export default router;