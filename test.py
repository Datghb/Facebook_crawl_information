import requests

access_token = 'YOUR_ACCESS_TOKEN'
group_id = 'YOUR_GROUP_ID'

url = f'https://graph.facebook.com/v19.0/{group_id}/feed?fields=message,created_time,from&access_token={access_token}'

response = requests.get(url)
data = response.json()

for post in data['data']:
    print('Tên người đăng:', post['from']['name'])
    print('Nội dung bài viết:', post.get('message', 'Không có nội dung'))
    print('Ngày đăng:', post['created_time'])
    print('-' * 30)
