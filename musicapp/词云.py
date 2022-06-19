import jieba
import wordcloud
import pymysql

db = pymysql.connect(host="localhost", user="root", password="123456", db="music")
# 使用 cursor() 方法创建一个游标对象
cursor = db.cursor()
#3编写sql
# sql = 'SELECT * FROM future.member WHERE MobilePhone = 18876153542 '
sql = "select name,introduction from ranking where style='飙升榜' "
#4.执行sql
cursor.execute(sql)
#5.查看结果
# result = cursor.fetchone() #用于返回单条数据
results = cursor.fetchall() #用于返回多条数据
print(results[0])
with open('test.txt','w',encoding="utf-8")as f:
    for i in results:
        for ii in i:
            f.write(ii+'\n')
# 读取文本
with open("test.txt",encoding="utf-8") as f:
    s = f.read()
print(s)
ls = jieba.lcut(s) # 生成分词列表
text = ' '.join(ls) # 连接成字符串


stopwords = ["的","是","了"] # 去掉不需要显示的词

wc = wordcloud.WordCloud(font_path="msyh.ttc",
                         width = 1000,
                         height = 700,
                         background_color='white',
                         max_words=100,stopwords=s)
# msyh.ttc电脑本地字体，写可以写成绝对路径
wc.generate(text) # 加载词云文本
wc.to_file("飙升榜.png") # 保存词云文件