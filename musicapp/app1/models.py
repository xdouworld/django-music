from django.db import models

# Create your models here.


class Admin(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True,verbose_name='用户名')
    password = models.CharField(max_length=255, blank=True, null=True,verbose_name='密码')

    class Meta:
        managed = False
        db_table = 'admin'
        verbose_name = '管理员'
        verbose_name_plural = '管理员'


class Collect(models.Model):
    user_id = models.IntegerField(blank=True, null=True,verbose_name='用户名')
    type = models.IntegerField(blank=True, null=True,verbose_name='类型')
    song_id = models.IntegerField(blank=True, null=True,verbose_name='歌曲id')
    song_list_id = models.IntegerField(blank=True, null=True,verbose_name='歌单id')
    create_time = models.DateTimeField(blank=True, null=True,verbose_name='创建时间')

    class Meta:
        managed = False
        db_table = 'collect'
        verbose_name = '用户收藏'
        verbose_name_plural = '用户收藏'

class Comment(models.Model):
    user_id = models.IntegerField(blank=True, null=True,verbose_name='评论id')
    type = models.IntegerField(blank=True, null=True,verbose_name='类型')
    song_id = models.IntegerField(blank=True, null=True,verbose_name='歌曲id')
    song_list_id = models.IntegerField(blank=True, null=True,verbose_name='歌单id')
    content = models.CharField(max_length=255, blank=True, null=True,verbose_name='评论内容')
    create_time = models.DateTimeField(blank=True, null=True,verbose_name='创建时间')
    up = models.IntegerField(blank=True, null=True,verbose_name='点赞数')

    class Meta:
        managed = False
        db_table = 'comment'
        verbose_name = '用户评论'
        verbose_name_plural = '用户评论'

class Consumer(models.Model):
    username = models.CharField(max_length=255, blank=True, null=True,verbose_name='用户名')
    password = models.CharField(max_length=255, blank=True, null=True,verbose_name='密码')
    sex = models.IntegerField(blank=True, null=True,verbose_name='性别')
    phone_num = models.CharField(max_length=15, blank=True, null=True,verbose_name='手机号码')
    email = models.CharField(max_length=30, blank=True, null=True,verbose_name='电子邮箱')
    birth = models.DateTimeField(blank=True, null=True,verbose_name='生日')
    introduction = models.CharField(max_length=255, blank=True, null=True,verbose_name='简介')
    location = models.CharField(max_length=255, blank=True, null=True,verbose_name='地区')
    avator = models.CharField(max_length=255, blank=True, null=True,verbose_name='头像')
    create_time = models.DateTimeField(blank=True, null=True,verbose_name='创建时间')
    update_time = models.DateTimeField(blank=True, null=True,verbose_name='上传时间')

    class Meta:
        managed = False
        db_table = 'consumer'
        verbose_name = '用户信息'
        verbose_name_plural = '用户信息'

class ListSong(models.Model):
    song_id = models.IntegerField(blank=True, null=True,verbose_name='歌曲id')
    song_list_id = models.IntegerField(blank=True, null=True,verbose_name="歌单id")

    class Meta:
        managed = False
        db_table = 'list_song'
        verbose_name = '歌单'
        verbose_name_plural = '歌单'

class Rank(models.Model):
    song_list_id = models.IntegerField(verbose_name='歌单id')
    consumer_id = models.IntegerField(verbose_name='用户id')
    score = models.IntegerField(blank=True, null=True,verbose_name='评分')

    class Meta:
        managed = False
        db_table = 'rank'
        unique_together = (('song_list_id', 'consumer_id'),)
        verbose_name = '评分'
        verbose_name_plural = '评分'

class Singer(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True,verbose_name="姓名")
    sex = models.IntegerField(blank=True, null=True,verbose_name="性别")
    pic = models.CharField(max_length=255, blank=True, null=True,verbose_name="照片")
    birth = models.DateTimeField(blank=True, null=True,verbose_name="生日")
    location = models.CharField(max_length=255, blank=True, null=True,verbose_name="地区")
    introduction = models.CharField(max_length=255, blank=True, null=True,verbose_name="简介")

    class Meta:
        managed = False
        db_table = 'singer'
        verbose_name = '歌手信息'
        verbose_name_plural = '歌手信息'

class Song(models.Model):
    singer_id = models.IntegerField(blank=True, null=True,verbose_name='歌手id')
    name = models.CharField(max_length=255, blank=True, null=True,verbose_name='姓名')
    introduction = models.CharField(max_length=255, blank=True, null=True,verbose_name='简介')
    create_time = models.DateTimeField(blank=True, null=True,verbose_name="创建时间")
    update_time = models.DateTimeField(blank=True, null=True,verbose_name="上传时间")
    pic = models.CharField(max_length=255, blank=True, null=True,verbose_name="头像地址")
    lyric = models.TextField(blank=True, null=True,verbose_name="歌词")
    url = models.CharField(max_length=255, blank=True, null=True,verbose_name='歌曲链接')
    class Meta:
        managed = False
        db_table = 'song'
        verbose_name = '歌曲信息'
        verbose_name_plural = '歌曲信息'

class SongList(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True,verbose_name="标题")
    pic = models.CharField(max_length=255, blank=True, null=True,verbose_name='图片链接')
    introduction = models.TextField(blank=True, null=True,verbose_name='简介')
    style = models.CharField(max_length=255, blank=True, null=True,verbose_name='风格')

    class Meta:
        managed = False
        db_table = 'song_list'
        verbose_name = '歌单信息'
        verbose_name_plural = '歌单信息'
class ranking(models.Model):
    singer_id = models.IntegerField(blank=True, null=True,verbose_name='歌手id')
    name = models.CharField(max_length=255, blank=True, null=True,verbose_name='姓名')
    introduction = models.CharField(max_length=255, blank=True, null=True,verbose_name='简介')
    create_time = models.DateTimeField(blank=True, null=True,verbose_name="创建时间")
    update_time = models.DateTimeField(blank=True, null=True,verbose_name="上传时间")
    pic = models.CharField(max_length=255, blank=True, null=True,verbose_name="头像地址")
    lyric = models.TextField(blank=True, null=True,verbose_name="歌词")
    url = models.CharField(max_length=255, blank=True, null=True,verbose_name='歌曲链接')
    style = models.CharField(max_length=255, blank=True, null=True, verbose_name='风格')
    class Meta:
        managed = False
        db_table = 'ranking'
        verbose_name = '排行榜信息'
        verbose_name_plural = '排行榜信息'