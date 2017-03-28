# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from . import models
from spider.shuapiao import shua
# Create your views here.

def index(request):
    # return HttpResponse('Hello world!')
    articles = models.Article.objects.all()     #get(pk=1)
    return render(request,'index.html',{'articles':articles})

def article_page(request,article_id):
    article = models.Article.objects.get(pk=article_id)
    return render(request,'article_page.html',{'article':article})

def edit_page(request,article_id):
    if str(article_id) =='0':
        return render(request,'edit_page.html')
    article = models.Article.objects.get(pk=article_id)
    return render(request,'edit_page.html',{'article':article})

def edit_action(request):
    title = request.POST.get('title','TITLTE')
    content = request.POST.get('content','CONTENT')
    article_id = request.POST.get('article_id','0')

    if article_id =='0':
       models.Article.objects.create(title=title,content= content)
       articles = models.Article.objects.all()
       return render(request,'index.html',{'articles':articles})

    article = models.Article.objects.get(pk=article_id)
    article.title = title
    article.content = content
    article.save()
    return render(request,'article_page.html',{'article':article})

def train(request):
    return render(request,'train.html')

# 查询余票
def query_action(request):
    from_station = request.GET.get('from_station').encode("utf-8")
    to_station = request.GET.get('to_station').encode("utf-8")
    train_date = request.GET.get('train_date').encode("utf-8")

    if from_station!= None and to_station != None and train_date != None :
        ticket_list = shua.serchTicket(from_station,to_station,train_date)
        return HttpResponse(ticket_list)
    else:
        return HttpResponse("")

# 检查车站名称是否正确
def station_action(request):
    flag = "0"
    #  将Unicode 转化为 str
    station_name = request.GET.get('station_name').encode("utf-8")
    # 0表示输入车站有误
    station_dict = shua.station_list
    try:
        print station_dict[station_name]
        flag = "1"
    except KeyError, e:
        flag = "0"
    return HttpResponse(flag)










