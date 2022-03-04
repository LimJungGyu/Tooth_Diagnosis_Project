from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request
select = input("1= google ,2 =naver  : ")
search = input("search : ")

driver = webdriver.Chrome()
if select == "1":
        driver.get("https://www.google.co.kr/imghp?hl=ko&tab=wi&authuser=0&ogbl")
        elem = driver.find_element_by_name("q")
        elem.send_keys(search)
        elem.send_keys(Keys.RETURN)
if select == "2":
        base_url = 'https://search.naver.com/search.naver?where=image&section=image&query='
        end_url = '&res_fr=0&res_to=0&sm=tab_opt&color=&ccl=2' \
              '&nso=so%3Ar%2Ca%3Aall%2Cp%3Aall&recent=0&datetype=0&startdate=0&enddate=0&gif=0&optStr=&nso_open=1'
        driver.get(base_url+search+end_url)
      


SCROLL_PAUSE_TIME = 1
last_height = driver.execute_script("return document.body.scrollHeight")

while True:

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(SCROLL_PAUSE_TIME)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        try:
                driver.find_element_by_css_selector(".mye4qd").click()
        except:
                break
    last_height = new_height
if select == "1":
        images = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")

        count = 1
        for image in images:
                try:
                        image.click()
                        time.sleep(2)
                        imgUrl = driver.find_element_by_css_selector(".n3VNCb").get_attribute("src")
                        path = "D:\\images2\\"
                        urllib.request.urlretrieve(imgUrl,path+ search + str(count) + ".jpg")
                        print(count)
                        count = count + 1
                except:
                        continue
if select == "2":
        images = driver.find_elements_by_class_name("_image")
        count = 1
        for image in images:
                try:
                        image.click()
                        time.sleep(2)
                        imgUrl = driver.find_element_by_css_selector(".n3VNCb").get_attribute("src")
                        path = "D:\\images\\"
                        urllib.request.urlretrieve(imgUrl,path+ search + str(count) + ".jpg")
                        print(count)
                        count = count + 1
                        print(imgUrl)
                except:
                        continue

driver.close()