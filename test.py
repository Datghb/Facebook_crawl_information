from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
browser.get("https://www.facebook.com/groups/327940020092140")
sleep(5)

# Chờ các post tải xong
# Chờ bài đăng xuất hiện
WebDriverWait(browser, 10).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.xu06os2 x1ok221b"))
)

# Lấy tất cả các bài post
posts = browser.find_elements(By.CSS_SELECTOR, "div.xu06os2 x1ok221b")

for post in posts:
    try:
        # Lấy thông tin
        author = post.find_element(By.CSS_SELECTOR, 'span.xt0psk2').text
        content = post.find_element(By.CSS_SELECTOR, 'div.x1iorvi4').text

        print(f"Tác giả: {author}")
        print(f"Nội dung: {content}")

    except Exception as e:
        print(f"Lỗi khi lấy dữ liệu: {e}")

