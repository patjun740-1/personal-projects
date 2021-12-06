
<template>
    
    <v-main >   

 <div class="shadowTop">
     <v-container class="test">  
             
                     <v-btn  depressed plain left @click="hasHistory()">   <svg style="width:24px;height:24px" viewBox="0 0 24 24">
    <path fill="currentColor" d="M20,11V13H8L13.5,18.5L12.08,19.92L4.16,12L12.08,4.08L13.5,5.5L8,11H20Z" />
</svg>  </v-btn>


     </v-container>
      </div>
     <div class="titleHolder">
       <p class="testTitle" >{{theme}}</p> 
       </div>


                     <div class="backGroundVh" v-if="numItem < 9">

                        <v-container class="matchInside" >   
                            <v-card class="matchMenu" v-for="e in menus" :key="e" v-bind:to="currenturl+'/'+e.name"> 

                            <v-img class="menuImgHolder" :src="e.imgUrl"  aspect-ratio="1.236" :width="width" ></v-img>  
               
                             <p class="matchMenuTitle">{{e.name}}  </p>
                             <p class="matchMenuPrice">{{e.price}}  </p>
                            </v-card>
                         
                          
                        
                        </v-container>
                        </div>    

                    <div class="backGround" v-if="numItem > 8">
                                     
                            
                        <v-container class="matchInside" >   
                            <v-card class="matchMenu" v-for="e in menus" :key="e" v-bind:to="currenturl+'/'+e.name"> 
              
                            <v-img class="menuImgHolder" :src="e.imgUrl"></v-img>  
                
                             <p class="matchMenuTitle">{{e.name}}  </p>
                             <p class="matchMenuPrice">{{e.price}}  </p>
                            </v-card>
                       
                        
                        </v-container>
                        </div>  


        <!-- <v-container class="footer"></v-container> -->

    </v-main> 
</template> 
 
 <script>   
 import {db, oStorage} from './fb'; 


 export default {  
 
     data: () => {
         return {
             menus: [],
             currenturl: '', 
             theme: '', 
             numItem: 0, 
           
         }
     }, 

     methods: {
        getMenu() {  
            
            db.collection('stores').doc(this.$route.params.storeName).collection('allMenu').get().then((snapShot) => { 
                snapShot.forEach((doc) => {

                    if(doc.data().themeId.indexOf(parseInt(this.$route.params.themeId)) !== -1) {
                            this.menus.push({
                            name: doc.data().name, 
                                price: doc.data().displayPrice, 
                                dividerId: doc.data().dividerId ,
                                description: doc.data().description ,
                                imgUrl : doc.data().img,
                                id: doc.data().id
                            }) 
                            this.numItem +=1;
                            this.menus.sort((a, b) => a.id - b.id ); 
                    } 
             
                })
            })


         },  

         getTheme() { 
             db.collection('stores').doc(this.$route.params.storeName).collection('matching').doc('theme').collection('allThemes').get().then((snapShot) => {
                 snapShot.forEach((doc) => {
                     if (doc.data().themeId == this.$route.params.themeId) {
                         this.theme = doc.data().title  
                    
                         return
                     } 
               
                 })
             })

         },

         getUrl() {
             this.currenturl = window.location.pathname
         }, 
         hasHistory () { 
        if(window.history.length > 1) {
                 window.history.back()
            }
      
        },
     }, 
     created(){
         this.getMenu(); 
         this.getUrl(); 
         this.getTheme();
     }

 } 
 </script>



                   
                 