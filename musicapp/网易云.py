# #!coding:utf-8
import time
import pymysql
import requests
import json
import cloudmusic
from lxml import etree
class Song():
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE',
            'Refer': 'http://music.163.com',
            'Host': 'music.163.com'
        }
    def get_song(self,id):
        respone = requests.get("http://music.163.com/api/song/detail/?id={}&ids=%5B{}%5D".format(id, id), headers=self.headers)
        # print(respone.json())
        print("http://music.163.com/api/song/detail/?id={}&ids=%5B{}%5D".format(id, id))
        song = respone.json()['songs']
        name = song[0]['name']
        artists = song[0]['artists'][0]['name']
        picUrl = song[0]['album']['blurPicUrl']
        album = song[0]['album']['name']
        song_information = {}
        # song_information['artists'] = artists
        song_information['name'] = artists+'-' +name
        song_information['pic'] = picUrl
        song_information['introduction'] = album
        # print('歌手', artists)
        # print("歌曲名称",name)
        # print('封面', picUrl)
        # print('专辑', album)
        return song_information
    def get_lyric(self,id):
        url = 'http://music.163.com/api/song/lyric?id=' + str(id) + '&lv=1&kv=1&tv=-1'
        res = requests.get(url, headers=self.headers)
        lyric = res.text
        json_obj = json.loads(lyric)
        lyric = json_obj['lrc']['lyric']
        return lyric
        # lyric = re.sub(r'[\d:.[\]]','', lyric)
    def get_id(self):
        idlist = []
        url = 'https://music.163.com/#/discover/toplist?id=19723756'
        respone = requests.get(url, headers=self.headers)
        html = etree.HTML(respone.text)
        #//*[@id="19544200921655452578680"]/td[2]/div/div/div/span/a
        #//*[@id="19538284221655452578680"]/td[2]/div/div/div/span/a
        #//*[@id="19452628401655452578680"]/td[2]/div/div/div/span/a
        #//*[@id="19531253531655452578680"]/td[2]/div/div/div/span/a
        id_list = html.xpath('//a/@href')
        print(id_list)
        for id in id_list:
            print(id.text)
            href = id.xpath('./@href')[0]
            music_id = href.split('=')[1]
            if "$" not in music_id:
                music_name = id.xpath('./text()')[0]
                idlist.append(music_id)
        return idlist
    def get_id2(self):
        id_list =[]
        playlist = cloudmusic.search('林俊杰')
        for music in playlist:
            print(music.id)
            id_list.append(music.id)
        return id_list
    def get_information(self):
        id_list = self.get_id2()
        sid=378
        # id2 = 36
        # n = 0
        # m = 1
        down_url = 'https://music.163.com/song/media/outer/url?id='
        for id in id_list:
            # if n % 30 == 0:
            #     m+=1
            #     print("m=",m)
            time.sleep(2)
            print(sid)
            song_information = self.get_song(id)
            song_information['lyric'] = self.get_lyric(id)
            song_information['id'] = sid
            song_information['url'] = down_url+id
            song_information['singer_id'] = 9
            # song_information['style'] = '原创榜'
            print(song_information)
            # song_list = {}
            # song_list['id'] = id2
            # song_list['song_id'] = int(sid)
            # song_list['song_list_id'] = m
            self.save(song_information,'song')
            # self.save(song_list, 'list_song')
            sid+=1
            # id2+=1
            # n+=1


    def save(self,data,table):
        # 打开数据库连接
        db = pymysql.connect(host="localhost", user="root", password="123456", db="music")
        # 使用 cursor() 方法创建一个游标对象
        cursor = db.cursor()
        # 列的字段
        keys = ', '.join(data.keys())
        # 行字段
        values = ', '.join(['%s'] * len(data))
        sql = 'INSERT INTO {table}({keys}) VALUES ({values})'.format(table=table, keys=keys, values=values)
        # # 将字段的value转化为元祖存入
        cursor.execute(sql, tuple(data.values()))
        db.commit()
if __name__=='__main__':
    songtest = Song()
    songtest.get_information()
    # 字典数据

#林允儿-小幸运
#夏日入侵企画-想去海边


##################################
# import requests
# from lxml import etree
# import os   #创建文件夹
# url='https://music.163.com/discover/toplist?id=3778678'
# head={
#      'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'
# }



