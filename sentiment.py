from selenium import webdriver  
import time  
import pandas as pd 

browser = webdriver.Chrome("./chromedriver_3")     
browser.get('https://m.place.naver.com/my/feed')  
# tabs = browser.window_handles   
time.sleep(2)
browser.find_element_by_class_name('_2jKeGFDxcF._2iffd72snL').click()
time.sleep(4)  

for i in range(10):
    browser.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1.5)
browser.execute_script("window.scrollTo(0, 0);") 

all_reviews = browser.find_elements_by_class_name("_1hP2U5CcXO")  
all_link = [] 
all_names = [] 


for e in all_reviews: 

    all_link.append(e.find_element_by_class_name(f'_2jKeGFDxcF.BcOdLctfj_'))
    all_names.append(e.find_element_by_class_name("B8JgXoFczU").text) 
    

rating = [] 
reviewText = [] 
 
# datas = pd.DataFrame({'name': all_names, 'link': all_link,})  
# print(datas)    

i = 1 
for l in all_link: 
    i+=1  
    l.click()  
    time.sleep(3)   
    
  
url_list = []
for i in range(1, len(browser.window_handles)): 
    browser.switch_to_window(browser.window_handles[i])  
    if (browser.current_url in url_list): 
        continue
    url_list.append(browser.current_url)  
url_list.reverse() 

datas = pd.DataFrame({'link' : url_list,})   
# pd.unique(datas)
browser.close()

datas.to_csv('restaurantLinks1.csv', index = False, encoding='utf-8')



  

    # browser.back()  
    # browser.execute_script("window.scrollTo(0, 0);")
    
    # 리뷰페이지로 이동  
    # print(l)
    # browser.switch_to.window(browser.window_handles[1])
    # # print(browser.current_url)   
    # 리뷰페이지로 이동 
    # browser.find_element_by_xpath('//button[normalize-space()="리뷰"]').click()
    # elem = browser.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/div[3]/div/div/div/div/a[4]') 
    # elem.click() 
    # browser.switch_to.window(browser.window_handles[1])  
    # # print(browser.current_url)   

    # # # 리뷰가 모두 보이게 하단으로 스크롤링 
    # for j in range(5): 
    #     time.sleep(3)
    #     more_btn = browser.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/div[5]/div[4]/div[5]/div[2]') 
    #     more_btn.click()  
    #     time.sleep(0.5) 
    # browser.back()



    # if i ==5: 
    #     break
        
    # all_name = browser.find_elements_by_xpath('/html/body/div[3]/div[4]/div/div/div[1]/button/div/div[2]')
    # all_loca = browser.find_elements_by_xpath('/html/body/div[3]/div[4]/div/div/div[1]/button/div/div[1]/div[1]')

