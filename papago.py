from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(options=options)

url = "https://papago.naver.com"
driver.get(url)

time.sleep(1)

trans = input("번역할 내용: ")
print(trans)
driver.find_element_by_css_selector("textarea#txtSource").send_keys(trans)
driver.find_element_by_css_selector("button#btnTranslate").click()

time.sleep(1)

result = driver.find_element_by_css_selector("div#txtTarget").text
print('결과: ', result)

time.sleep(1)
driver.close()