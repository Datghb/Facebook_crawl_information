from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
browser.get("http://facebook.com")
sleep(5)
# 2a. Điền thông tin vào ô user và pass

txtUser = browser.find_element(By.ID, "email")
txtUser.send_keys("bhuh082@gmail.com")  # <---  Điền username thật của các bạn vào đây
sleep(3)
txtPass = browser.find_element(By.ID, "pass")
txtPass.send_keys("24012004444")
sleep(3)
txtPass.send_keys(Keys.ENTER)
sleep(50)
browser.quit()

# 4. Đóng trình duyệt
browser.close()

#

# # 2b. Submit form
#
# txtPass.send_keys(Keys.ENTER)
