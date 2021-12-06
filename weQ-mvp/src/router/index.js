import Vue from 'vue'
import VueRouter from 'vue-router'
import HOME from '../views/HOME.vue' 
import COCKTAIL from '../views/COCKTAIL.vue'
import MENU from '../views/MENU.vue' 
import ORDER from '../views/ORDER.vue' 
import STORY from '../views/STORY.vue'
import {db} from '../views/fb' 
// import { TabsPlugin } from 'bootstrap-vue'

// console.log("HIHI")





Vue.use(VueRouter)
 

// console.log(storeList)< 
// <v-for="store in lst" :key="store"> 
// const routerLst = []
// for(let i = 0; i<lst.length; i++){ 
  
const routes = [ 
  
  {
    path: '/:storeName/0',
    name: 'Home',  
    props: true, 
    // console.log
    // component: Home
    // component: app  
    component: HOME
    

  },
  {
    path: '/:storeName/1',
    name: 'story',
    props: true,
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: STORY
  }, 
  {
    path: '/:storeName/3',
    name: 'menu',
    props: true,
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component:MENU
  }, 
  {
    path: '/:storeName/2',
    name: 'cocktail',
    props: true,
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: COCKTAIL
  }, 
  {
    path: '/:storeName/4',
    name: 'order',
    props: true,
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: ORDER
  },  
  {
    path: '/:storeName/2/:themeId',
    name: 'cocktailInside',
    props: true,
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: function () {
      return import(/* webpackChunkName: "about" */ '../views/MATCH.vue')
    }
  }, 
  {
    path: '/:storeName/3/:name',
    name: 'detailPgfromMenu',
    props: true,   
    // showBotNav: false


    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: function () {
      return import(/* webpackChunkName: "about" */ '../views/DETAIL.vue')
    }
  },  
  {
    path: '/:storeName/0/:name',
    name: 'detailPgFromHome',
    props: true,   
    // showBotNav: false


    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: function () {
      return import(/* webpackChunkName: "about" */ '../views/DETAIL.vue')
    }
  }, 
  {
    path: '/:storeName/2/:themeId/:name',
    name: 'deatilPgFromInside',
    props: true,   
    // showBotNav: false


    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: function () { 

      return import(/* webpackChunkName: "about" */ '../views/DETAIL.vue')
    
    }
  },  
] 

// db.collection('stores').doc(window.location.pathname.split('/')[1]).collection('info').get().then((snapShot) => {    


//   snapShot.forEach((doc) => {    
//       if (doc.data().botNavEng.indexOf('COCKTAIL') != -1){ 
//         routes.push({ 
//           path:'/:storeName/'
//           name:'specialRoute'
//         })

//       } 

  
    
//   })


// }) 



const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
  scrollBehavior (to, from, savedPosition) {
    return { x: 0, y: 0 }
  }
  
})

export default router
