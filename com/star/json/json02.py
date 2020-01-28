import json

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