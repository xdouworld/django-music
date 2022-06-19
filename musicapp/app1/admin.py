from django.contrib import admin
from .models import *
# Register your models here.
from django.apps import apps

admin.site.site_header = '音乐管理后台'  # 设置header
admin.site.site_title = '音乐管理后台'  # 设置title
admin.site.index_title = '音乐管理后台'
models = apps.get_models()
@admin.register(Admin)
class admintmodel(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
@admin.register(Collect)
class Collectmodel(admin.ModelAdmin):
    list_display = ['user_id','song_id','song_list_id','create_time']
    search_fields = ['user_id','song_id','song_list_id','create_time']
@admin.register(Comment)
class Commentmodel(admin.ModelAdmin):
    list_display = ['user_id','song_id','song_list_id','content','create_time']
    search_fields = ['user_id','song_id','song_list_id','content','create_time']
@admin.register(Consumer)
class Consumermodel(admin.ModelAdmin):
    list_display = ['username','password','sex','phone_num','create_time']
    search_fields = ['username','password','sex','phone_num','create_time']
@admin.register(Singer)
class Singermodel(admin.ModelAdmin):
    list_display = ['name','sex','location','birth']
    search_fields = ['name','sex','location','birth']
@admin.register(ListSong)
class ListSongmodel(admin.ModelAdmin):
    list_display = ['song_id','song_list_id']
    search_fields = ['song_id','song_list_id']
@admin.register(Rank)
class Rankmodel(admin.ModelAdmin):
    list_display = ['song_list_id','consumer_id','score']
    search_fields = ['song_list_id','consumer_id','score']
@admin.register(Song)
class Songmodel(admin.ModelAdmin):
    list_display = ['singer_id','name','update_time','url']
    search_fields = ['singer_id','name','update_time','url']
@admin.register(SongList)
class SongListmodel(admin.ModelAdmin):
    list_display = ['title','style']
    search_fields = ['title','style']
@admin.register(ranking)
class rankingmodel(admin.ModelAdmin):
    list_display = ['id','name','update_time','url']
    search_fields = ['id','name','update_time','url']
for model in models:
    try :
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass