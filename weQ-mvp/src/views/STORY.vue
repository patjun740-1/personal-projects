<template>
  <v-main>
        <div class="shadowTop">
    <v-container class="storyPg">  
      <p class="PgMainTitle">  
        스토리
      </p>
    </v-container> 
          </div>

       <v-img class="storyMainImg" :src="storyPicUrl">
       </v-img>
     

  <v-container class="stories">
    <v-card class="storyCard" elevation="0" v-for="st in storiesList" :key="st">   
       <p class="storyNum">{{st.id}}</p>
      <p class="storyTitle">{{st.title}}</p> 
      <p class="storySubTitle">{{st.subTitle}}</p>  
  
      <v-img :src=st.img style="height:200px; margin-top:12px; margin-bottom:12px;"></v-img>  

      <p class="storyBody">
        {{st.body}}
      </p>
    </v-card>
 
  </v-container>

  <v-container class="footerWhite"></v-container>
  
  
  
  </v-main> 

</template>  




<script> 
import {oStorage, db} from './fb';  

export default { 

    data: () => {
        return { 
            storiesList: [],   
            storyPicUrl: '',
            imgList: [],
  
        }
    },  
 

    methods: {
      async getStory(){ 
      db.collection('stores').doc(this.$route.params.storeName).collection('info').doc('information').collection('stories').get().then((snapShot) => {
            snapShot.forEach((doc) =>{
             
                 this.storiesList.push({
                title: doc.data().title, 
                subTitle: doc.data().subTitle, 
                id: doc.data().id,  
                body: doc.data().body, 
                img: doc.data().img
              })
              this.storiesList.sort((a, b) => a.id - b.id ); 
            }) 
        })


      }, 
      async getImgUrl() { 
            this.storyPicUrl = '' 
    
            
        db.collection('stores').doc(this.$route.params.storeName).collection('info').get().then((snapShot) => { 
                
             snapShot.forEach((doc) => {
                    this.storyPicUrl = doc.data().storyMainPic 
             })
        })
        },  
},

    created(){ 
      this.getStory();
      this.getImgUrl();

    }
}
</script>
 