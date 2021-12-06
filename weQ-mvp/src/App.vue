<template>
  <v-app>   



  
    <!-- 내용영역에 라우터 페이지 렌더링 --> 
   <v-main>

      <!-- 페이지 장면전환 효과 넣기 -->
      <v-slide-x-transition mode="out-in"> 
       
        <router-view ></router-view>
      </v-slide-x-transition>
   </v-main>  


          <div class="shadow">
          <v-bottom-navigation elevation=0  fixed > 

            <v-btn class="my-btn" color="#fff" v-for="nav in botNav" :key="nav"  :to="'/'+currentUrl+'/'+nav.id"  > 
          

              <p class="kor">{{nav.kor}}</p>
              <p class="eng">{{nav.eng}}</p>
            </v-btn>

          </v-bottom-navigation> 
          </div>
       
     
     <div v-if="loading" style="position:absolute; width: 100%; height:100%; top:0; left:0; z-index:10000; background-color:white">
            <div style="margin-left: auto; margin-right: auto">
                <v-img :src="loadingImg" style="margin-top:40%">
                </v-img>
            </div>
        </div>
  </v-app>
 
</template>    
<script>
import {db} from './views/fb' 

export default { 
      props: ['storeName'],    

  data: () => {
    return { 
       botNav : [],  
       loading: true, 
       loadingImg:'',
       currentUrl: '',

    }
  },
  mounted() {
            setTimeout(() => {
                this.loading = false
            }, 2000)
        },
  methods: { 
       scrollToTop() {
                window.scrollTo(0,0);
           },
      getParams(){
      this.currentUrl = window.location.pathname.split('/')[1]
    },

     getBotNav(){   
       db.collection('stores').doc(window.location.pathname.split('/')[1]).collection('info').get().then((snapShot) => {    
          snapShot.forEach((doc) => {
              for(let i = 0; i<doc.data().botNavEng.length; i++){  
                   this.botNav.push({ 
                 eng: doc.data().botNavEng[i], 
                 kor: doc.data().botNavKorean[i] ,
                 id: doc.data().pgId[i]
            })
              }
          })
      })

    },   
    getLoadingPgImg(){  
      db.collection('master').doc('loadingPg').get().then((snapShot) => { 
       this.loadingImg = snapShot.data().img;
      })
    }

  },
  created(){
    this.scrollToTop();
    this.getBotNav();
    this.getParams();
    this.getLoadingPgImg();
  }
  
}
</script>