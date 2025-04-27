import os
import json
import logging
import re

from facebook_scraper import get_posts, set_cookies
from utils import save_posts

# Tạo thư mục nếu chưa có
os.makedirs("data", exist_ok=True)
os.makedirs("logs", exist_ok=True)

# Cấu hình log
logging.basicConfig(
    filename="logs/crawl.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def load_cookies():
    with open("C:\Users\nguye\PycharmProjects\Facebook_crawler_project\cookies.txt", "r") as f:
        cookie_str = f.read().replace("\n", "")
        set_cookies(cookie_str)
        logging.info("Đã cài đặt cookie đăng nhập")


# Hàm tách tên từ link
def extract_name_from_url(url):
    match = re.search(r"facebook\.com/(groups/)?([^/?]+)", url)
    if match:
        is_group = bool(match.group(1))
        name = match.group(2)
        return name, is_group
    else:
        raise ValueError("Link Facebook không hợp lệ.")


# Crawl bài viết
def crawl_posts(source_name, is_group=False, pages=2):
    logging.info(f"Bắt đầu crawl {'group' if is_group else 'page'}: {source_name}")
    posts = []
    try:
        for post in get_posts(group=source_name if is_group else None, page=source_name if not is_group else None,
                              pages=pages):
            posts.append({
                "text": post.get("text"),
                "time": str(post.get("time")),
                "likes": post.get("likes"),
                "comments": post.get("comments"),
                "shares": post.get("shares"),
                "post_url": post.get("post_url")
            })
    except Exception as e:
        logging.error(f"Lỗi khi crawl: {e}")
        return []

    save_posts(posts, f"data/{source_name}_posts.json")
    logging.info(f"Đã lưu {len(posts)} bài viết vào data/{source_name}_posts.json")


# Chạy
if __name__ == "__main__":
    try:
        load_cookies()  # Tải cookies từ file
        url = input("https://www.facebook.com/groups/binhdanhocai").strip()
        source_name, is_group = extract_name_from_url(url)
        crawl_posts(source_name, is_group=is_group, pages=2)
    except Exception as e:
        logging.error(f"Lỗi: {e}")
        print(f"Lỗi: {e}")
