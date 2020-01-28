import requests

url='https://fanyi.qq.com/api/translate'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'}
formData={'source': 'auto',
          'target': 'en',
          'sourceText': '小麦',
          'qtv':'e214f134da29e5db',
          'qtk':'8bRKHYzrsoAUnvqY16czwxJZ3Olh79fw2vttU7cLBu/ffIZYmb9GXtSuZzZMqtnL7JhJsJyP81B9MWkjQcqwcOnC8IA3euWL+/XmlnlLk+tFAmAZUMwq0tqOm2kRoqLj8K/h4pB+G176BiFltB6xMA==',
         'sessionUuid':'translate_uuid1575274167266'
          }
response=requests.post(url,data=formData,headers=headers)
print(response.status_code)