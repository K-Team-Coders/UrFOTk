import { createRouter, createWebHashHistory } from "vue-router";

const routes = [
  {
    path: "/",
    name: "PersonDataBase",

    component: () => import("../views/PersonDatabase.vue"),
  },
  {
    path: "/document_scan",
    name: "DocumentsScan",
    props(route) {
      return { text: route.query.text };
    },

    component: () => import("../views/DocumentsScan.vue"),
  },
  {
    path: "/users/:id",
    name: "UserDetails",

    component: () => import("../views/Users.vue"),
  },
  {
    path: "/error",
    name: "NotFound",
    component: () => import("../components/ErrorPage.vue"),
    props: true,
  },
];

const router = createRouter({
  history: createWebHashHistory(),
  routes,
});

export default router;
