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
    k +=1 
    print(k)

    driver = webdriver.Chrome("./chromedriver_3")     
    driver.get(l)   
    time.sleep(4)  

    # 리뷰 버튼 누르기 
    review_btn = driver.find_element_by_link_text("리뷰")
    review_btn.click()  
    time.sleep(3) 

    # 평점순 누르기 
    order_btn = driver.find_element_by_link_text("평점순") 
    order_btn.click() 
    time.sleep(3) 

    worst_to_best = driver.find_element_by_link_text("평점높은순") 
    worst_to_best.click() 
    time.sleep(3)

    
    for i in range(5):  
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
            rating = s.find_element_by_class_name('_2tObC')    
            if int(rating.text) > 3: 
                break 
            ratings.append(rating.text)
            txt_list.append(text1.text)  
            # print(text1.text)
            name = driver.find_element_by_class_name('_3XamX') 
            names.append(name.text)    
            
            # print(len(txt_list))
            # print(len(names))   
            print(len(ratings)) 
            if (len(ratings) != len(txt_list)) and len(ratings) != len(names): 
                break
        except: 
            pass   
    
    driver.close()  
    
datas = pd.DataFrame({'name': names, 'review' : txt_list,'rating' : ratings})    
# print(datas) 
datas.to_csv('negativeReviews.csv', index = False, encoding='utf-8-sig') 
