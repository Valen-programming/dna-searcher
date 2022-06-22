import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: () => import('@/pages/home/HomePage.vue'),
  },
  
  {
    path: '/alignments',
    name: 'Alignments',
    component: () => import('@/pages/alignments/AlignmentsPage.vue'),
  },
  {
    path: '/sequences/add',
    name: 'AddNewSequence',
    component: () => import('@/pages/add_new_sequence/AddNewSequencePage.vue'),
  },
  {
    path: '/sequences/:id',
    name: 'EditSequence',
    component: () => import('@/pages/edit_sequence/EditSequencePage.vue'),
  },
  {
    path: '/categories',
    name: 'Categories',
    component: () => import('@/pages/categories/CategoriesPage.vue'),
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
})

export default router
