import requests

access_token = 'EAAUsKLCZBlSwBO6LZArq9uSsT81rbaVw9mhlWwZC4WpIs9pZBts9D2pfyJ9neiIWIWUP3ZB27g5g3eQfv4VM4ldirDGGtmeS3ZB53JtOxZBS5RTqu9IGIreloiuMQhRlk4quZA4080hOr96za8K5oWzO5cZBZAu8Nw4d1Nk1E1FTp54IV8hRzLzM00KFvR3rDu7HYtbZCVrEjcISyRLjWZAx3c754ZCZCFwyrFJ8vnfxY9h97htyDw6rXggUnT2TK2N5GBZBwZDZD'
group_id = '327940020092140'

url = f'https://graph.facebook.com/v22.0/{group_id}/feed?fields=message,created_time,from&access_token={access_token}'

response = requests.get(url)
data = response.json()
if 'data' in data:
    for post in data['data']:
        print('Tên người đăng:', post['from']['name'])
        print('Nội dung bài viết:', post.get('message', 'Không có nội dung'))
        print('Ngày đăng:', post['created_time'])
        print('-' * 30)
else:
    print('Lỗi:', data)
