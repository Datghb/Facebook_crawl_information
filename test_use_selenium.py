from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from time import sleep

# Khởi tạo trình duyệt
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
browser.get("http://facebook.com")
sleep(5)

# Đăng nhập
txtUser = browser.find_element(By.ID, "email")
txtUser.send_keys("bhuh082@gmail.com")
sleep(3)
txtPass = browser.find_element(By.ID, "pass")
txtPass.send_keys("24012004444")
sleep(3)
txtPass.send_keys(Keys.ENTER)
sleep(5)

# Mở nhóm Facebook
browser.get("https://www.facebook.com/groups/233986561026635")
sleep(5)

# Lấy các bài viết trong nhóm
posts = browser.find_elements(By.CSS_SELECTOR, "div.html-div")
sleep(5)
if posts:
    for post in posts:
        try:
            # Tìm theo XPath chính xác cho tên người đăng trong bài viết
            author_name = post.find_element(By.XPATH, ".//span[@class='html-span' and text()]")
            print(f"Tên người đăng: {author_name.text}")
        except Exception as e:
            print("Không tìm thấy tên người đăng trong bài viết.")
else:
    print("Không tìm thấy bài đăng.")


sleep(15)
# Đóng trình duyệt sau khi lấy xong thông tin
browser.quit()