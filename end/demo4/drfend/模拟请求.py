# Charlie
# date:2020/3/4 14:28
# file_name:模拟请求
import requests

for i in range(100):
    res = requests.get('http://127.0.0.1:8000/api/v1/categorys/')
    print(res.json())
    print('当前次数',i)
