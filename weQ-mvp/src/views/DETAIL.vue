<template>  
<v-main>

             <v-container class="test">  

               <v-btn  depressed plain left @click="hasHistory()">  
                    <svg style="width:24px;height:24px" viewBox="0 0 24 24">
                             <path fill="currentColor" d="M20,11V13H8L13.5,18.5L12.08,19.92L4.16,12L12.08,4.08L13.5,5.5L8,11H20Z" />
                    </svg>  
            </v-btn>
        

     </v-container>
          
     
    <v-container class="detailPg" v-for="m in menu" :key="m">

                     <v-img   :src="m.imgUrl" width="100%" height="500px;" contain></v-img>  
                     <v-container class="detailText">
               

                          <p class="detailTitle"> {{m.name}} </p>

                           <p class="detailDesc">  {{m.description}} </p> 

                            <p class="detailPrice">{{m.price}} </p>
                     </v-container>
                 

    </v-container> 
    <v-container class="chartHolder" >
       <v-img  :src="chart" height="400px" contain></v-img>  
    </v-container> 
     <v-container class="footerWhite"> 
     </v-container>
    
    
</v-main>
</template>  


<script>
import {oStorage, db} from './fb';  

export default {
    
    
    data: () => { 
        return {
            menu: [],
            chart: ''
        }

    },  

    methods: { 
        getMenu() { 
            this.menu = [] 
            db.collection('stores').doc(this.$route.params.storeName).collection('allMenu').get().then((snapShot) => {  
                var found = false  
           

                snapShot.forEach((doc) => {  
                        if(!found){
                        if(doc.data().name == this.$route.params.name) {
                                found = true
                                this.chart = doc.data().chart

                    
  
                            this.menu.push({
                                name: doc.data().name, 
                                price: doc.data().displayPrice, 
                                description: doc.data().description ,
                                imgUrl : doc.data().detailImg ,  

                            })   
                            this.menu.sort((a, b) => a.name - b.name );      
                                    
                    
                
                    }

                }
                        

            }) 
        })
    }, 

    hasHistory () { 
        if(window.history.length > 1) {
                 window.history.back()
            }
        }, 
    }, 

    created() {
        this.getMenu();
       
        
    }

}
</script>
