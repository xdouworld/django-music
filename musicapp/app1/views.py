from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import *
from django.db.models import Q
import json
# Create your views here.
@csrf_exempt
def login(request):
    if request.method == 'POST':
        print('1111')
        postBody = request.body
        persion = {
            'status': '200',
            'error': 0,
            'code': 1
        }
        # persion_str = json.dumps(persion)
        # response = HttpResponse(persion_str,content_type='application/json')
        response = JsonResponse(persion,safe=False)
        return response
@csrf_exempt
def get_songList(request):
    if request.method == 'POST' or request.method == 'GET':
        songlist = SongList.objects.filter().values()
        a= list(songlist)
        # persion_str = json.dumps(persion)
        # response = HttpResponse(persion_str,content_type='application/json')
        response = JsonResponse(a,safe=False)
        return response
@csrf_exempt
def get_singer(request):
    if request.method == 'POST' or request.method == 'GET':
        singerlist = Singer.objects.filter().values()
        # persion_str = json.dumps(persion)
        # response = HttpResponse(persion_str,content_type='application/json')
        response = JsonResponse(list(singerlist),safe=False)
        return response
@csrf_exempt
def get_detail(request):
    if request.method == 'POST' or request.method == 'GET':
        singerId = request.GET['singerId']
        print(singerId)
        songlist = Song.objects.filter(singer_id=singerId).values()
        # persion_str = json.dumps(persion)
        # response = HttpResponse(persion_str,content_type='application/json')
        response = JsonResponse(list(songlist),safe=False)
        return response
@csrf_exempt
def get_listsong(request):
    if request.method == 'POST' or request.method == 'GET':
        songListId = request.GET['songListId']
        print(songListId)
        songlist = ListSong.objects.filter(song_list_id=int(songListId)).values()
        # persion_str = json.dumps(persion)
        # response = HttpResponse(persion_str,content_type='application/json')
        response = JsonResponse(list(songlist),safe=False)
        return response
@csrf_exempt
def get_song(request):
    if request.method == 'POST' or request.method == 'GET':
        songId = request.GET['songId']
        song = Song.objects.filter(id=int(songId)).values()
        # persion_str = json.dumps(persion)
        # response = HttpResponse(persion_str,content_type='application/json')
        response = JsonResponse(list(song)[0],safe=False)
        return response
@csrf_exempt
def get_comment(request):
    if request.method == 'POST' or request.method == 'GET':
        songId = request.GET['songListId']
        print(songId)
        song = Comment.objects.filter(song_list_id=int(songId)).values()
        # persion_str = json.dumps(persion)
        # response = HttpResponse(persion_str,content_type='application/json')
        response = JsonResponse(list(song),safe=False)
        return response
@csrf_exempt
def get_consumer(request):
    if request.method == 'POST' or request.method == 'GET':
        Id = request.GET['id']
        song = Consumer.objects.filter(id=int(Id)).values()
        response = JsonResponse(list(song)[0],safe=False)
        return response
@csrf_exempt
def get_rank(request):
    if request.method == 'POST' or request.method == 'GET':
        Id = request.GET['songListId']
        song = Rank.objects.filter(song_list_id=int(Id)).values()
        score = 0
        for i in song:
            score+=i['score']
        response = JsonResponse(score,safe=False)
        return response
@csrf_exempt
def consumer_login(request):
    if request.method == 'POST' or request.method == 'GET':
        con = dict(request.POST)
        username = con['username'][0]
        password = con['password'][0]
        print(con['password'][0])
        consumer = Consumer.objects.filter(username=str(username),password=str(password)).values()
        res = {}
        if consumer:
            res['userMsg'] = list(consumer)[0]
            res['code'] = 1
            print(res)
        else:
            res['code'] = 2
        response = JsonResponse(res,safe=False)
        return response
@csrf_exempt
def consumer_add(request):
    if request.method == 'POST' or request.method == 'GET':
        con = dict(request.POST)
        for key, value in con.items():
            con[key] = value[0]
        print(con)
        msginfo = Consumer.objects.create(**con)
        msginfo.save()
        res = {}
        res['code'] = 1
        response = JsonResponse(res,safe=False)
        return response
@csrf_exempt
def get_likeStyle(request):
    if request.method == 'POST' or request.method == 'GET':
        style = request.GET['style']
        res = SongList.objects.filter(style=str(style)).values()
        response = JsonResponse(list(res),safe=False)
        return response
@csrf_exempt
def get_singerOfSex(request):
    if request.method == 'POST' or request.method == 'GET':
        sex = request.GET['sex']
        res = Singer.objects.filter(sex=str(sex)).values()
        response = JsonResponse(list(res),safe=False)
        return response
@csrf_exempt
def collectOfUserId(request):
    if request.method == 'POST' or request.method == 'GET':
        userId = request.GET['userId']
        res = Collect.objects.filter(user_id=int(userId)).values()
        response = JsonResponse(list(res),safe=False)
        return response
@csrf_exempt
def comment_add(request):
    if request.method == 'POST' or request.method == 'GET':
        con = dict(request.POST)
        for key, value in con.items():
            con[key] = value[0]
        print(con)
        con1 = {}
        con1['song_list_id'] = con['songListId']
        con1['user_id'] = con['userId']
        con1['content'] = con['content']
        con1['type'] = con['type']
        msginfo = Comment.objects.create(**con1)
        msginfo.save()
        res = {}
        res['code'] = 1
        response = JsonResponse(res,safe=False)
        return response
@csrf_exempt
def get_ranking(request):
    if request.method == 'POST' or request.method == 'GET':
        style = request.GET['style']
        song = ranking.objects.filter(style=(style)).values()
        # persion_str = json.dumps(persion)
        # response = HttpResponse(persion_str,content_type='application/json')
        response = JsonResponse(list(song), safe=False)
        return response
@csrf_exempt
def get_likeSongOfName(request):
    if request.method == 'POST' or request.method == 'GET':
        songName = request.GET['songName']
        song = ranking.objects.filter(Q(name__istartswith=songName)|Q(name__iendswith=songName)).values()
        song1 = Song.objects.filter(Q(name__istartswith=songName)|Q(name__iendswith=songName)).values()
        print(song)
        quer = list(song)+list(song1)  # 不排序
        response = JsonResponse(quer, safe=False)
        return response