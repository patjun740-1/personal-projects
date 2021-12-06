<template>
      <v-main >
    <v-container class="storyPg">  
      <p class="PgMainTitle">  
        주문하기
      </p>
    </v-container>  
    <div class="orderPg" > 
        <v-container class="orderTextBox">
            <p class="orderTitle">주문하기 버튼을 눌러 메뉴를 주문해주세요</p> 
            
            <p class="orderText">주문하기 버튼을 누르면 매점의 카카오톡 채널로 연결됩니다. 
                채널을 추가한 뒤 사장님께 카톡으로 주문하려는 메뉴를 
                전달해주세요!   향후 서비스 업데이트 후에는 어플을 통해 
                직접 주문하실 수 있습니다 :) </p>  

        <v-btn class="orderBtn"  color="#345161" :href="kakaoUrl">   
        <p class="btnText">주문하기 
        
        </p>
       </v-btn> 
        </v-container>
    </div> 

      </v-main>
</template> 
<script>   

import {db} from './fb';

export default {
        
    data: () => {
        return { 
            kakaoUrl: '',
        }
    }, 
 
    methods: {
        async getKakao(){
            this.kakaoUrl = '' 
            db.collection('stores').doc(this.$route.params.storeName).collection('info').get().then((snapShot) => {   
                snapShot.forEach((doc) =>{
                    this.kakaoUrl = doc.data().kakao 
                })
              
            })

        }, 
    }, 
    created(){
        this.getKakao();
    }

}
</script>