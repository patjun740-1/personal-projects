<template>  
<!-- eslint-disable vue/no-use-v-if-with-v-for,vue/no-confusing-v-for-v-if -->

  <v-main>  
     <v-img  :src="mainPicUrl" height="20%"> 
     </v-img>
     <v-container class="mainInfo"> 
        <p class="mainTitle"> {{storeTitle}}</p> 
        <p class="mainDesc"> {{storeDesc}} </p> 
        <v-container class="hourBox">
        <p class="hours" v-for="e in storeHours" :key="e"> {{e}} </p>  
        </v-container> 
        
     </v-container> 

        
  

     <v-container class="homePg" >    
       <div v-for="divide in dividers" :key="divide">  
            <v-container class="horizontalScroll"  v-if="divide.id%3=== 0">   
              <p class="rec1Title">{{divide.name}}</p>
               <div class="scrolling-wrapper">    
            <v-container class="spacer">
            </v-container>
           
        <v-card class="homeMenu" elevation=0 v-for="menu in menus" :key="menu" v-if="menu.dividerId.indexOf(divide.id) !== -1" v-bind:to="currenturl+'/'+menu.name"> 
               
                <v-container class="imgimg">
                   <v-img  :src="menu.imgUrl"  width=120px height=125px> 
    
                </v-img> 
                </v-container>  
       
                
            <p class="menuTitle">{{menu.name}}</p>
            <p class="menuDesc">{{menu.description}}</p>
            </v-card> 
         
        </div>
       
            </v-container>
              <div class="sigCont" v-if="divide.id%3 === 1">
               <p class="rec2Title">{{divide.name}}</p>
              <div class="divsLine">
               <v-card flat class="sigMenu"  v-for="menu in menus" :key="menu" v-if="menu.dividerId.indexOf(divide.id) !== -1"  v-bind:to="currenturl+'/'+menu.name"> 
                <v-img class="sigImg" :src="menu.imgUrl"> </v-img>  
      
    
                <div class="sigTextCont">
                <p class="sigMenuName">
        
                  {{menu.name}}
                </p>
                <p class="sigMenuDesc">
                  {{menu.description}}
              
                </p>                          
                </div>
                      
               </v-card> 
              </div>
              </div>



            <v-container class="tempC" v-if="divide.id%3=== 2">
               <p class="rec1Title">{{divide.name}}</p>
                      <div class="scrolling-wrapper3">  
                         <v-card flat class="tempCCard"  v-for="menu in menus" :key="menu" v-if="menu.dividerId.indexOf(divide.id) !== -1"  v-bind:to="currenturl+'/'+menu.name"> 
                <v-img class="tempCImg" :src="menu.imgUrl"> </v-img>   
                
      
  
                <div class="tempCtextCont">
                <p class="tempCname">
        
                  {{menu.name}}
                </p>
                <p class="tempCdesc">
                  {{menu.description}}
              
                </p>                          
                </div>
                      
               </v-card> 
                      
                        
              
                  
                      </div>
            </v-container>


       </div>

       
 <v-container class="footerWhite"></v-container>
     </v-container>

   
 
       

  </v-main>

</template>
 
 <script> 
import {db, oStorage} from './fb'; 

export default {   
    props: ['storeName', 'themeId'],      
  
  data: () => { 
      return {
        mainPicUrl: '', 
        storeTitle: '', 
        storeDesc: '', 
        storeHours: '', 
        menus: {},
        dividers : [] , 
        placeHolder : [] ,    
        currenturl: '',
      }
    },
   
    methods: {
        
        getTitle(){  
            db.collection('stores').doc(this.storeName).collection('info').get().then((snapShot) => {  
                snapShot.forEach((doc) => {  
                    this.storeTitle = doc.data().title;  
                }) 
            }) 
        }, 
        
        getImgUrl() { 
            this.mainPicUrl = ''
        db.collection('stores').doc(this.storeName).collection('info').get().then((snapShot) => { 
          
             snapShot.forEach((doc) => {
                    this.mainPicUrl = doc.data().img
             })
        })
        }, 
        getDesc(){
            this.storeTitle = '' 
            db.collection('stores').doc(this.storeName).collection('info').get().then((snapShot) => { 
                snapShot.forEach((doc) => {
                    this.storeDesc = doc.data().description;
                })
            })
        },
        getHours(){
            this.storeTitle = '' 
            db.collection('stores').doc(this.storeName).collection('info').get().then((snapShot) => { 
                snapShot.forEach((doc) => {
                    this.storeHours = doc.data().businessHours;  
                   
                })
            })
        }, 
         getDivider(){ 
          this.dividers = []    
          db.collection('stores').doc(this.storeName).collection('info').get().then((snapShot) => { 
              snapShot.forEach((doc) => { 
                for (let i = 0 ; i < doc.data().divider.length; i ++){   
                  if(i>2){ 
                    this.dividers.push({
                     name : doc.data().divider[i] , 
                     id : 0,
                   }) 
                  }

                   this.dividers.push({
                     name : doc.data().divider[i] , 
                     id : i ,
                   })  
                }  
              })
          })
        },
         getAllMenu() {
            this.menus = []    
            db.collection('stores').doc(this.storeName).collection('allMenu').get().then((snapShot) => { 
              snapShot.forEach((doc) => {
                        this.menus.push({
                          name: doc.data().name, 
                            price: doc.data().displayPrice, 
                            dividerId: doc.data().dividerId ,
                            description: doc.data().description ,
                            imgUrl : doc.data().img,
                            id: doc.data().id
                        })
                        this.menus.sort((a, b) => a.id - b.id ); 
              })
            })  
         }, 
         getUrl() {
  
          this.currenturl = window.location.pathname
  
         }, 
       
    },   

    created() {
        this.getTitle(); 
        this.getImgUrl(); 
        this.getDesc(); 
        this.getHours();  
        this.getDivider(); 
        this.getAllMenu();  
        this.getUrl();
    
    }
}
</script>