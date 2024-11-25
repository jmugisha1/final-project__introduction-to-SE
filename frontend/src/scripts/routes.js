import { createRouter, createWebHistory } from "vue-router";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "index",
      component: () => import("../views/index.vue"),
    },
    {
      path: "/about",
      name: "about",
      component: () => import("../views/about.vue"),
    },
    {
      path: "/account/login",
      name: "login",
      component: () => import("../views/login.vue"),
    },
    {
      path: "/account/register",
      name: "regsiter",
      component: () => import("../views/register.vue"),
    },
    {
      path: "/shop",
      name: "shop",
      component: () => import("../views/shop.vue"),
    },
    {
      path: "/create",
      name: "create",
      component: () => import("../views/create.vue"),
    },
  ],
});

export default router;
