#coding=utf-8
import requests
resp = requests.get('https://tool.lu/')
resp.encoding = 'utf-8'
#print(resp.status_code,resp.encoding,resp.text)

import json
resp = requests.post('https://tool.lu/encdec/ajax.html',data={'code': '我是小麦','operate': 'base64_encode'})
print(resp.url,resp.status_code,resp.text)
dict_text = json.loads(resp.text)
print(dict_text['text'])
