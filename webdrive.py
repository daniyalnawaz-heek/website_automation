from selenium import webdriver
import time
import pyautogui
path="D:/Downloads/chromedriver_win32/chromedriver.exe"
driver=webdriver.Chrome(executable_path=path)
driver.get("http://google.com")
driver.maximize_window()
driver.get("https://www.zara.com/in/en/man-new-in-l711.html")
pyautogui.press("enter")
search=driver.find_element_by_class_name("search-box")
search.click()
time.sleep(5)
pyautogui.typewrite("bomber jacket")
time.sleep(5)
pyautogui.press("enter")









