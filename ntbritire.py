
import pandas as pd
import numpy as np
from time import sleep
from selenium.webdriver import Chrome, ChromeOptions
from webdriver_manager.chrome  import ChromeDriverManager
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
sns.set()
 
def read():
    
    driver_path = ChromeDriverManager().install()
    driver = Chrome(driver_path)
       
    #NTBのページから任意引退選手を抽出
    #2019～2021年分まで繰り返し
    
    #初期値
    year = 2019
    r_2019=[]
    r_2020=[]
    r_2021=[]
    
    for year in range(2019, 2022) :
        url = f'https://npb.jp/announcement/{year}/pn_retired.html'
        driver.get(url)
        
    
        #任意引退選手名をクリック
        #1行目をセット
        
        i = 1
        while True:
            try:
                element = driver.find_element_by_xpath(f'//*[@id="layout"]/div/div/section/div/table/tbody/tr[{i}]/td[2]/a')
                sleep(3)
                element.click()
                sleep(3)
                
                #任意引退選手の生年月日を抽出
                a = driver.find_elements_by_tag_name('td')
            
                #print(a[2].text)
                #文字列を生年月日のみ抽出
                birth = a[2].text
                birth_1 = birth[0:4]
                
                #生年月日から年齢を算出
                birth_2 = int(birth_1)
                birth_3 = year - birth_2
                #リストに追加
                
                if year == 2019 :
                    r_2019.append(birth_3)
                    
                if year == 2020 :
                    r_2020.append(birth_3)
                
                if year == 2021 :
                    r_2021.append(birth_3)
                
                print(r_2019)
                print(r_2020)
                print(r_2021)
                
                i = i + 1 
                driver.back()
                sleep(6)
            except:
              break
        
        #前ページに戻る
        driver.back()
    
    #1年分終了すると次年度へ
    
    #1元配置分散分析
       
    result = stats.f_oneway(r_2019, r_2020, r_2021)  
    print("F値", result.statistic) 
    print("P値", result.pvalue)
          
read()