
<template>
<!-- eslint-disable vue/no-use-v-if-with-v-for,vue/no-confusing-v-for-v-if -->

    <v-main >   

 

        <v-container class="storyPg" height=90px elevation=0>  

            <p class="PgMainTitle">
                전체메뉴
            </p> 
        </v-container>
  
        
 
            <v-tabs height="40px" >  
                   <v-tab v-for="elem in categoryTab" :key="elem">  
                       <p class="tabsTxt" > {{elem.tabName}}  </p>
                   </v-tab>    
                   <v-tab-item v-for="pg in categoryTab" :key="pg"> 
                
                           <div class="backGroundVh" v-if="pg.pgSize < 10"> 
                            
                       <v-container class="matchInside">   
                           <v-card class="cardTest" v-for="p in menuAll" :key="p" v-bind:to="currenturl+'/'+p.name" v-if="p.tabId === pg.tabId">
                             <v-img class="menuImg" :src="p.imgUrl"   ></v-img> 
                             <p class="menuItemTitle">{{p.name}} </p>
                             <p class="menuItemPrice"> {{p.price}}</p>
            
                            </v-card> 
                           
           

                       </v-container>  
                           </div>


                    <div class="backGround" v-if="pg.pgSize >9">
                       <v-container class="matchInside">   
                           <v-card class="cardTest" v-for="p in menuAll" :key="p" v-bind:to="currenturl+'/'+p.name" v-if="p.tabId === pg.tabId">
                             <v-img class="menuImg" :src="p.imgUrl"></v-img> 
                             <p class="menuItemTitle">{{p.name}} </p>
                             <p class="menuItemPrice"> {{p.price}}</p>
            
                            </v-card> 

           

                       </v-container> 
                         
                           </div>
                        
                   </v-tab-item>  
                 
            </v-tabs>    
  

             <div class="footer"> </div>
                
                      
        
      
       
    </v-main> 
</template> 

<script>
import {oStorage, db} from './fb';  

export default {
    data: () =>{
        return {
            categoryTab : [],    
            menuAll: [], 
            popupOpen: false,  
            currenturl : '', 

        
  
           
        }
    }, 
methods: {
     async readFromFB() {
        db.collection('stores').doc(this.$route.params.storeName).collection('menuCategory').get().then((snapShot) => { 
             snapShot.forEach((doc) => {
                 this.categoryTab.push({
                     tabName : doc.data().name, 
                     tabId : doc.data().tabId, 
                     pgSize : doc.data().size,
                 })  
             }) 
    
        }) 
  
    },       

    async  getMenu() {  
            
            db.collection('stores').doc(this.$route.params.storeName).collection('allMenu').get().then((snapShot) => { 
                snapShot.forEach((doc) => {
                            this.menuAll.push({ 
                                name: doc.data().name, 
                                price: doc.data().displayPrice, 
                                id: doc.data().id,
                                description: doc.data().description ,
                                imgUrl : doc.data().img ,
                                tabId: doc.data().tabId ,
                            })
                            this.menuAll.sort((a, b) => a.id - b.id ); 
                })
            })
         }, 

    async getCurrent() {
        this.currenturl = window.location.pathname 
    },   
 
}, 
created(){
    this.readFromFB();  
    this.getMenu();    
    this.getCurrent();
  
}, 

}
</script> 
