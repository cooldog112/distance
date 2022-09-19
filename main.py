import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd

browser = webdriver.Chrome()
df = pd.read_csv('data.csv', encoding='cp949')
url = 'https://map.naver.com/v5/directions'
browser.get(url)
df.insert(2, 'distance', '')

for i in range(len(df)):
    print(df['시작점'][i], df['도착점'][i])
    browser.implicitly_wait(3)
    browser.find_element(By.ID, 'directionStart0').clear()
    browser.find_element(By.ID, 'directionStart0').send_keys(df['시작점'][i])
    browser.implicitly_wait(3)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter')

    browser.implicitly_wait(3)
    browser.find_element(By.ID, 'directionGoal1').clear()
    browser.find_element(By.ID, 'directionGoal1').send_keys(df['도착점'][i])
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.press('enter')

    find_btn = browser.find_element(By.CSS_SELECTOR, '#container > shrinkable-layout > div > directions-layout > directions-result > div.main > div.search_area > directions-search > div.btn_box > button.btn.btn_direction')
    find_btn.click() # 길찾기 버튼 클릭
    time.sleep(2)
    distance = browser.find_element(By.XPATH, '//body/app[1]/layout[1]/div[3]/div[2]/shrinkable-layout[1]/div[1]/directions-layout[1]/directions-result[1]/div[1]/directions-summary-list[1]/directions-hover-scroll[1]/div[1]/ul[1]/li[1]/directions-summary-item-pubtransit[1]/div[1]/div[1]/strong[1]/readable-duration[1]/span[1]')

    print(distance.text)
    df['distance'][i] = distance.text

df.to_csv('result.csv', encoding='cp949')
