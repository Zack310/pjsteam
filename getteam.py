import requests
import pprint

i = 1

for i in range(255):
    r = requests.get('https://pubgleague.dmm.com/team/profile/' + i)

    print(r.text)
    
    ytxt = r.text
    w = open(i + '.html', 'w', encoding='utf-8')
    w.write(ytxt)
    i += 1

w.closed



# import pandas as pd
# from selenium import webdriver
# import time
# import os
# from datetime import datetime

# now = datetime.now()
# str_now = now.strftime('%Y%m%d')
# desktop_path = "D:/GoogleDrive/Stock_Alerts/Data/"
# laptop_path = "C:\project\pjsteam\html\"
# data_path = desktop_path

# daily_dir_path = data_path + str_now
# if not os.path.exists(daily_dir_path):
#     os.makedirs(daily_dir_path)

# options = webdriver.ChromeOptions()
# preferences = {'download.default_directory': daily_dir_path, 'safebrowsing.enabled': 'false'}
# options.add_experimental_option("prefs", preferences)
# #処理は出来ているがadsenseの表示が出来ないためにエラーメッセージが帰ってきている
# #options.add_argument('--headless')
# driver = webdriver.Chrome("C:/Users/zack/dev/python/driver/chromedriver.exe", chrome_options=options)

# i = 0
# with open('D:/GoogleDrive/Stock_Alerts/Data/TSE1st_code201812.csv', encoding='utf-8') as f:
#     for row in f:
#         #ヘッダー部分を読み込まないようにする
#         if i == 0:
#             i += 1
#             continue
#         else:
#             #i件まで取り込む 全件2105
#             if i == 2105:
#                 break
#             else:
#                 try:
#                     row_sorce = row.rstrip().split(',')
#                     stock_code = row_sorce[1]
#                     url = "https://kabuoji3.com/stock/" + stock_code + "/2019/"

#                     driver.get(url)
#                     driver.implicitly_wait(5)
#                     html = driver.page_source
#                     tables = pd.read_html(html)

#                     tables[0].to_csv(daily_dir_path + "/daily_" + stock_code + ".csv")
#                     i +=1

#                 except Exception as identifier:
#                 # logging error to the error_kenkunflag.csv
#                     with open('D:/GoogleDrive/Stock_Alerts/error_get_price.csv', "a", encoding='utf-8') as logf:
#                         logf.write(str(stock_code) + ' : ' + str(identifier) + '\n')
#                         print("Error:{}".format(stock_code))
#                     continue

#                 time.sleep(10)


# driver.quit()
