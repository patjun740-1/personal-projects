import csv
import requests 
import re
from bs4 import BeautifulSoup 

url = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page="

filename = "DEC28_시가총액1-200.csv"
f = open(filename,"w",encoding="utf-8-sig", newline = "")
writer = csv.writer(f)

title = "N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE".split("\t")
# = ["N","종목명","현재가"...]
writer.writerow(title)

for page in range(1,5):
    res = requests.get(url+str(page))
    res.raise_for_status()
    soup = BeautifulSoup(res.text,"lxml")

    data_rows= soup.find("table", attrs={"class":"type_2"}).find("tbody").find_all("tr")
    for row in data_rows: 
        columns = row.find_all("td") 
        if len(columns)<=1:   #의미없는 데이터 :  공백란, 줄바꿈 등등  skip
            continue 
        price = row.find("td", attrs ={"class":"number"})  
        price = price.get_text()
        string = list(price) 
        for elem in string: 
            if elem ==",": 
                string.remove(elem) 
        price = ''.join(string)
        if int(price)>50000:
            continue
        data = [column.get_text().strip() for column in columns]
        # print(data) 
        writer.writerow(data)