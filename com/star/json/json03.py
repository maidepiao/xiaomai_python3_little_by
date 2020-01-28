import json

信息 = {'姓名':'小麦'}
with open ('D:/信息.txt','w') as file:
    json.dump(信息,file,ensure_ascii=False)
with open ('D:/信息.txt','r') as file:
    信息 = json.load(file)
    print(信息)
