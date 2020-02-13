import requests,json,time,os,re

class LOLHeroSpider:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Mobile Safari/537.36'
        }
        self.hero_list_url = 'https://game.gtimg.cn/images/lol/act/img/js/heroList/hero_list.js'
        self.hero_url = 'https://game.gtimg.cn/images/lol/act/img/js/hero/{}.js'
        self.base_path = os.path.join('d:'+os.path.sep,'英雄联盟')

    def send_get(self,url):
        try:
            resp = requests.get(url,headers = self.headers)
            assert resp.status_code == 200,'{}请求失败'.format(url)
            return resp
        except Exception as e:
            print(e)
            return None

    def start(self):
        #获取英雄列表
        resp = self.send_get(self.hero_list_url)
        if resp:
            hero_list_text = resp.text
            hero_list_dict = json.loads(hero_list_text)
            self.process_heroes(**hero_list_dict)
        else:
            print('英雄列表为空,请检查获取URL:{}'.format(self.hero_list_url))

    def process_heroes(self,**hero_list_dict):
        # 获取英雄详细信息
        for hero in hero_list_dict['hero']:
            hero_info_url = self.hero_url.format(hero['heroId'])
            resp= self.send_get(hero_info_url)
            if resp:
                hero_info_dict = json.loads(resp.text)
                self.process_hero(**hero_info_dict)
            else:
                print('获取英雄:{}失败,请检查获取URL:{}'.format(hero['name'],self.hero_list_url))

    def process_hero(self,**hero_info_dict):
        hero = hero_info_dict['hero']
        skins = hero_info_dict['skins']
        for skin in skins:
            # 获取图片内容
            if skin['mainImg']:
                skin_content = self.send_get(skin['mainImg']).content
                hero_image_name = '{}.jpg'.format(skin['name'])
                hero_image_dir = os.path.join(self.base_path, hero['name'] + hero['title'])
                self.save_image(hero_image_dir,hero_image_name,skin_content)
        print('hero:{},skins:{}张,处理完成'.format(hero['name'],len(skins)))
        time.sleep(1)

    @staticmethod
    def save_image(image_dir,image_name,image_content):
        if not os.path.exists(image_dir):
            os.makedirs(image_dir)
        try:
            hero_image_path = os.path.join(image_dir,re.sub(r'[/|?]','',image_name))
            with open(hero_image_path, 'wb') as image:
                image.write(image_content)
        except Exception as e:
            print('{}保存失败,错误原因:{}'.format(hero_image_path,e))


if __name__ == '__main__':
    LOLHeroSpider().start()



