class TVshow:
    def __init__(self,show):
        self.__show = show
    @property
    def show(self):
        return self.__show
tvshow = TVshow('红楼一梦')
print(tvshow.show)
tvshow.show = '江南'