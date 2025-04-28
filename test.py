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
browser.get("https://www.facebook.com/groups/233986561026635")
sleep(5)

# Chờ các post tải xong
WebDriverWait(browser, 10).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div[role="article"]'))
)

posts = browser.find_elements(By.CSS_SELECTOR, 'div[role="article"]')

for post in posts:
    try:
        # Lấy thông tin
        author = post.find_element(By.CSS_SELECTOR, 'span.x1lliihq').text
        content = post.find_element(By.CSS_SELECTOR, 'div.x1iorvi4').text
        time = post.find_element(By.CSS_SELECTOR, 'span.x4k7w5x').get_attribute('aria-label')
        reactions = post.find_element(By.CSS_SELECTOR, 'span.x1e558r4').text

        print(f"Tác giả: {author}")
        print(f"Nội dung: {content}")
        print(f"Thời gian: {time}")
        print(f"Cảm xúc: {reactions}\n")

    except Exception as e:
        print(f"Lỗi khi lấy dữ liệu: {e}")