import pickle
class ChatMsg:
    def __init__(self,from_user_id,to_user_id,content):
        self.from_user_id = from_user_id
        self.to_user_id = to_user_id
        self.content = content

class BindMsg:
    def __init__(self,user_id):
        self.user_id = user_id

if __name__ == '__main__':
    import pickle
    msg = ChatMsg(110,999,'你好，小麦')
    dump_ = pickle.dumps(msg)
    print(dump_)
    load_ = pickle.loads(dump_)
    print(type(load_),load_.from_user_id,load_.to_user_id,load_.content)