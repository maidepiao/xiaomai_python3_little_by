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

