# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index/', views.index),
    url(r'^article/(?P<article_id>[0-9]+)$',views.article_page,name='article_page'),
    url(r'^edit/(?P<article_id>[0-9]+)$',views.edit_page,name='edit_page'),
    url(r'^edit/action$',views.edit_action,name='edit_action'),
    url(r'^train/', views.train),
    # 查询余票
    url(r'^query/action$',views.query_action,name='query_action'),
    # 查询输入车站是否正确
    url(r'^station/action$',views.station_action,name='station_action'),
]
