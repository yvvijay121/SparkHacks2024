import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: () => import('../views/HomeView.vue')
    },
    {
      path: '/drug_list',
      name: 'drug_list',
      component: () => import('../views/DrugListView.vue')
    },
    // {
    //   path:"/stats",
    //   name: "stats",
    //   component: () => import('../views/StatsView.vue')
    // },
    // {
    //   path:"/drug/:id",
    //   name: "detail",
    //   component: () => import('../views/DrugDetailView.vue')
    // },
    // {
    //   path:"/drug/:id/edit",
    //   name: "edit",
    //   component: () => import('../views/DrugEditView.vue')
    // },
    // {
    //   path:"/drug/add",
    //   name: "add",
    //   component: () => import('../views/DrugAddView.vue')
    // },
    {
      path:"/user_select",
      name: "user_select",
      component: () => import('../views/UserSelectView.vue')
    },
    {
      path:"/med_line",
      name: "med_line",
      component: () => import('../views/MedLineView.vue')
    }
  ]
})

export default router
