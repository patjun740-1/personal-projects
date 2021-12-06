<template>
<!-- eslint-disable vue/no-use-v-if-with-v-for,vue/no-confusing-v-for-v-if -->

    <v-main>
          <v-container class="storyPg" >  
      <p class="PgMainTitle">  
        내 취향의 메뉴 찾기 
      </p>
    </v-container> 

      <div class="matchingPg" > 
        
        <v-container class="matchingRec" v-for="div in dividers" :key="div">
        <p class="matchingTitle">{{div.title}}</p>
        <p class="matchingDesc"> {{div.expl}} </p>
          <div class="scrolling-wrapper2">   
            <v-container class="spacer"></v-container>
            <v-card  class="matchingCard" v-for="theme in allTheme" :key="theme" v-if="div.id === theme.divId" v-bind:to="currenturl+'/'+theme.id" >    
               


              <v-container class="picHolderMatch"> 
                <v-img :src="theme.img">
              </v-img> 
              </v-container> 

              <div class="matchTxtBox">

              <p class="matchCardTitle">{{theme.title}}</p> 
              <p class="matchCardSub">{{theme.description}}</p>   
            
              
              </div>
      

    
            </v-card>
            
         


</div>  
        </v-container> 

      </div>
   
    </v-main>

</template> 

// <script> 
import {db, oStorage} from './fb'



export default { 
    data: () => {
        return { 
            dividers:[],   
            allTheme: [], 
            currenturl: '', 



        }
    }, 

    methods: {
      async getDividers(){ 
        db.collection('stores').doc(this.$route.params.storeName).collection('matching').get().then((snapShot) => {
          snapShot.forEach((doc) => {  
            for (let i=0; i<doc.data().divs.length; i++){
              this.dividers.push({
                title: doc.data().divs[i], 
                expl : doc.data().divExplain[i] ,
                id: i
              })
            }
          })
        })
      }, 
      
      async getData(){
          db.collection('stores').doc(this.$route.params.storeName).collection('matching').doc('theme').collection('allThemes').get().then((snapShot) => {
            snapShot.forEach((doc) => {
              // console.log(doc.data().title)
              //  var gsRef = oStorage.refFromURL(doc.data().img); 
              //         gsRef.getDownloadURL().then((url) => {
                          this.allTheme.push({ 
                            title: doc.data().title, 
                            description: doc.data().description, 
                            img : doc.data().img, 
                            divId: doc.data().divId,  
                            id : doc.data().themeId, 
                            ranking: doc.data().ranking
                           })
                             this.allTheme.sort((a, b) => a.id - b.id ); 
                            

                    // })
                
            })
          })
      }, 

      getUrl() {
          this.currenturl = window.location.pathname 
          // console.log(this.currenturl)
      },  
    },


    created(){
      this.getDividers();
      this.getData();
      this.getUrl();
    }
    
}
</script>
