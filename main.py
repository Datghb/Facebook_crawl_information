import json
import os
import logging
from facebook_scraper import get_posts

# Tạo thư mục nếu chưa có
os.makedirs("data", exist_ok=True)
os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename="logs/crawl.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def crawl_user_posts(source_name, pages=1):
    logging.info(f"Đang crawl từ nhóm công khai: {source_name}")
    posts = []
    try:
        # Crawl từ group công khai
        for post in get_posts(group=source_name, pages=pages):
            posts.append({
                "user": post.get("username"),  # tên người đăng
                "text": post.get("text")       # nội dung bài viết
            })
    except Exception as e:
        logging.error(f"Lỗi: {e}")
        return []

    # Lưu dữ liệu vào file
    save_posts(posts, f"data/{source_name}_posts.json")
    logging.info(f"Đã lưu {len(posts)} bài viết")

# Lưu các bài viết vào file JSON
def save_posts(posts, filename):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(posts, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    crawl_user_posts("AKKO VN Community", pages=10)  # Thay "zingnews" bằng tên nhóm công khai bạn muốn crawl
