import { createRouter, createWebHashHistory } from "vue-router";

const routes = [
  {
    path: "/person_database",
    name: "PersonDataBase",

    component: () => import("../views/PersonDatabase.vue"),
  },
  {
    path: "/",
    name: "DocumentsScan",
    props(route) {
      return {  text: route.query.text }},

    component: () => import("../views/DocumentsScan.vue"),
  }, 
  {
    path: "/notfound",
    name: "NotFound",
    component: () => import("../components/PageNotFound.vue"),
    props: true,
  },
];

const router = createRouter({
  history: createWebHashHistory(),
  routes,
});

export default router;
