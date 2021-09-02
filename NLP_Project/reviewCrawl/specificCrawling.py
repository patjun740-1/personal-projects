from selenium import webdriver  
import time  
import pandas as pd   


linkCSV = pd.read_csv('restaurantLinks1.csv', encoding='utf-8')  
link_list = linkCSV['link'].to_list()

data =[] 
names = []
txt_list = [] 
ratings = []
# i = 1
k = 0
for l in link_list:      
    

    driver = webdriver.Chrome("./chromedriver_3")     
    driver.get(l)   
    time.sleep(4)  

    # 리뷰 버튼 누르기 
    review_btn = driver.find_element_by_link_text("리뷰")
    review_btn.click()  
    time.sleep(3)

    # 리뷰 200개 안돼는 곳 빼기
    number_btn = driver.find_element_by_class_name("place_section_count")  
    print(number_btn.text) 
    k+=1  
    print(k)
    if int(number_btn.text) < 200: 
        driver.close()
        continue
    
    for i in range(100):
        # 더보기 버튼 누르기  
        try:
            more_btn = driver.find_element_by_link_text("더보기") 
            more_btn.click()  
            time.sleep(1.5)
        except:
           pass
    
    slots = driver.find_elements_by_class_name('_2Cv-r ') 
    # counter = 0 
    for s in slots:    
        # counter +=1
        try:
            text1 = s.find_element_by_class_name('WoYOw')  
            txt_list.append(text1.text)  
            # print(text1.text)
            name = driver.find_element_by_class_name('_3XamX') 
            names.append(name.text)    
            rating = s.find_element_by_class_name('_2tObC')    
            ratings.append(rating.text)
            # print(len(txt_list))
            # print(len(names))   
            # print(ratings)
        except: 
            pass   
      

    # break 

    driver.close()

 

datas = pd.DataFrame({'name': names, 'review' : txt_list,'rating' : ratings})    
# print(datas)
datas.to_csv('reviews.csv', index = False, encoding='utf-8-sig') 

    # # 리뷰 텍스트 가져오기 
    # txt_list = driver.find_elements_by_class_name('WoYOw')
    # time.sleep(3)  
    # print(len(txt_list))
    # for txt in txt_list:  
        
    
    # time.sleep(3)
    # # # 별점 가져오기  
    # rating = driver.find_elements_by_class_name('_2tObC')   
    # # print(len(rating))
    # for rate in rating: 
    #     ratings.append(rate.text)  
    
    # print(txt_list1)
    # print(ratings)
    # if i ==1: 
    #     break 
    # i +=1 
    # driver.close()

