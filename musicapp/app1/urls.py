# 引入views.py
from . import views
# 引入path
from django.urls import path

# 正在部署的应用的名称
app_name = 'app01'

urlpatterns = [
    # path函数将url映射到视图
    path('admin/login/status', views.login, name='login'),
    path('songList/allSongList', views.get_songList, name='songlist'),
    path('singer/allSinger', views.get_singer, name='singer'),
    path('song/singer/detail', views.get_detail, name='singer_listdetail'),
    path('listSong/detail', views.get_listsong, name='listsong_detail'),
    path('song/detail', views.get_song, name='song_detail'),
    path('comment/commentOfSongListId', views.get_comment, name='comment_detail'),
    path('consumer/selectByPrimaryKey', views.get_consumer, name='consumer_detail'),
    path('rank', views.get_rank, name='rank_detail'),
    path('consumer/login', views.consumer_login, name='consumer_login'),
    path('consumer/add', views.consumer_add, name='consumer_add'),
    path('songList/likeStyle', views.get_likeStyle, name='get_likeStyle'),
    path('singer/singerOfSex', views.get_singerOfSex, name='get_likeStyle'),
    path('collect/collectOfUserId', views.collectOfUserId, name='collectOfUserId'),
    path('comment/add', views.comment_add, name='comment_add'),
    path('ranking', views.get_ranking, name='get_ranking'),
    path('song/likeSongOfName', views.get_likeSongOfName, name='likeSongOfName'),

]