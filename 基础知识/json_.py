#coding=utf-8
import json

信息 = dict(姓名='小麦',年龄=25)
print(信息)
json_str = json.dumps(信息)
print(type(json_str),json_str)
信息 = json.loads(json_str)
print(type(信息),信息['姓名'])


#json:{...}        python:dict
#json:[...]        python:list
#json:"..."        python:str
#json:10.05        python:int float
#json:true/false   python:True/False
#json:null         python:None

class Animal:
    def __init__(self,nick_name,legs):
        self.nick_name = nick_name
        self.legs = legs

bird = Animal('polly',2)
try:
    json.dumps(bird)
except TypeError as e:
    print('json序列化出错了',e)

def Animal2Dict(animal):
    return {'nick_name':animal.nick_name,
            'legs':animal.legs}
print(json.dumps(bird,default=Animal2Dict))

print(bird.__dict__)

bird_json = json.dumps(bird,default= lambda obj:obj.__dict__)
bird = json.loads(bird_json)
print(type(bird))

def Dict2Animal(animal):
    return Animal(animal['nick_name'],animal['legs'])

bird = json.loads(bird_json,object_hook=Dict2Animal)
print(type(bird))

信息 = {'姓名':'小麦'}
with open ('D:/信息.txt','w') as file:
    json.dump(信息,file,ensure_ascii=False)
with open ('D:/信息.txt','r') as file:
    信息 = json.load(file)
    print(信息)