from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
import pyautogui
from datetime import datetime
from discord_webhook import DiscordWebhook

sido = ""
junggoding = ""
schoolname = "학교 이름"
name = "이름"
birthday = "생년월일 (6자리)"

webhook = DiscordWebhook(url="Discord Webhook URL")

driver = webdriver.Chrome()
driver.get("https://hcs.eduro.go.kr/#/loginHome")
elem = driver.find_element(By.ID, "btnConfirm2").click()
elem = driver.find_element(By.CLASS_NAME, "searchBtn").click()
select = Select(driver.find_element(By.ID, "sidolabel")).select_by_index(sido)
select = Select(driver.find_element(By.ID, "crseScCode")).select_by_index(int(junggoding))
elem = driver.find_element(By.ID, "orgname")
elem.send_keys(schoolname)
elem.send_keys(Keys. RETURN)
time.sleep(0.1)
driver.find_element(By.CSS_SELECTOR, '#softBoardListLayer > div.layerContentsWrap > div.layerSchoolSelectWrap > ul > li > a > p > a').click()
driver.find_element(By.CLASS_NAME, "layerFullBtn").click()
driver.find_element(By.ID, "user_name_input").send_keys(name)
driver.find_element(By.ID, "birthday_input").send_keys(birthday)
elem = driver.find_element(By.CLASS_NAME, "keyboard-icon")
elem.click() # 키패드 로드
elem.click() # 작동 오류 방지를 위해 재로드
zero = pyautogui.locateCenterOnScreen("0.png")
one = pyautogui.locateCenterOnScreen("1.png")
two = pyautogui.locateCenterOnScreen("2.png")
three = pyautogui.locateCenterOnScreen("3.png")
four = pyautogui.locateCenterOnScreen("4.png")
five = pyautogui.locateCenterOnScreen("5.png")
six = pyautogui.locateCenterOnScreen("6.png")
seven = pyautogui.locateCenterOnScreen("7.png")
eight = pyautogui.locateCenterOnScreen("8.png")
nine = pyautogui.locateCenterOnScreen("9.png")
# 비밀번호 4자리 (엉어로)
pyautogui.click(one)
pyautogui.click(two)
pyautogui.click(three)
pyautogui.click(four)
########################
driver.find_element(By.ID, "btnConfirm").click()
time.sleep(1.8)
driver.find_element(By.CLASS_NAME, "survey-button").click()
time.sleep(1)
driver.find_element(By.ID, "survey_q1a1").click()
driver.find_element(By.ID, "survey_q2a3").click()
driver.find_element(By.ID, "survey_q3a1").click()
driver.find_element(By.ID, "btnConfirm").click()
time.sleep(0.5)
driver.save_screenshot("./result.png")
driver.close()
with open("./result.png", "rb") as f:
	webhook.add_file(f.read(), filename='result.png')
response = webhook.execute()