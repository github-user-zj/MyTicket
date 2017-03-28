#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'Administrator'
__mtime__ = '2017/3/11'
   
"""
import requests
import json
import datetime

class Shuapiao():

    def __init__(self):
        pass

    # 访问外网方法
    def request(self, url):
        headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
        content = requests.get(url, headers=headers, verify=False)
        return content

    # 查询车票信息
    def getlist(self,from_station,to_station):
        #获取明天日期
        train_date = self.getAfterDate()
        url = 'https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date='+train_date + \
              '&leftTicketDTO.from_station='+from_station+'&leftTicketDTO.to_station='+to_station+'&purpose_codes=ADULT'
        html = self.request(url).content
        ticket_list = []
        try:
            dict_html = json.loads(html)['data']
            for i in dict_html:
                ticket = []
                queryLeft = i['queryLeftNewDTO']
                station_train_code = queryLeft['station_train_code'].encode('utf-8')
                swz_num = queryLeft['swz_num'].encode('utf-8')
                zy_num = queryLeft['zy_num'].encode('utf-8')
                ze_num = queryLeft['ze_num'].encode('utf-8')
                rw_num = queryLeft['rw_num'].encode('utf-8')
                rz_num = queryLeft['rz_num'].encode('utf-8')
                yw_num = queryLeft['yw_num'].encode('utf-8')
                yz_num = queryLeft['yz_num'].encode('utf-8')
                wz_num = queryLeft['wz_num'].encode('utf-8')
                # self.pandu(seat=swz_num,name = '商务座')
                # self.pandu(seat=zy_num,name='一等座')
                # self.pandu(seat=ze_num,name='二等座')
                # self.pandu(seat=rw_num, name='软卧')
                # self.pandu(seat=rz_num, name='软座')
                # self.pandu(seat=yw_num, name='硬卧')
                # self.pandu(seat=yz_num,name='硬座')
                # self.pandu(seat=wz_num,name='无座')
                # print '*'*50
                ticket_list.append({"station_train_code":station_train_code,"swz_num":swz_num,"zy_num": zy_num,
                                    "ze_num":ze_num,"rw_num":rw_num,"rz_num":rz_num,"yw_num":yw_num,"yz_num":yz_num,"wz_num":wz_num})
            # ret = mail('北京至上海的商务座有票了,抓紧抢票啊！！！www.12306.cn')
            # if ret:
            #     print("ok")  # 如果发送成功则会返回ok，稍等20秒左右就可以收到邮件
            # else:
            #     print("filed")  # 如果发送失败则会返回filed
            # print ticket_list


        except KeyError:
            print '未查询到数据！！！'
        # return json.dumps(ticket_list)
        return json.dumps(ticket_list)

    #if 判断的封装
    def pandu(self,seat,name):
        if seat != '无' and seat != '--':
            if seat == '有':
                print name+'有余票'
            else:
                print name+'还有余票%s 张' % seat


    # 获取车站对应简称
    def get_station_names(self):
        d1 = dict()
        url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js'
        html = self.request(url).content.replace('var station_names =\'','').replace('\';','')
        names = html.split('@')
        for i in names:
            jianchengs = i.split('|')
            # print jianchengs
            if len(jianchengs) > 1:
                # print jianchengs[0],jianchengs[1]
                d1[jianchengs[1]] = jianchengs[2]
        return d1

    #获取n天后的日期
    def getAfterDate(self,day=1):
        now = datetime.datetime.now()
        delta = datetime.timedelta(days=day)
        n_days = now + delta
        return n_days.strftime('%Y-%m-%d')

    def serchTicket(self,from_station,to_station):
        # from_station = raw_input("请输入出发地\n")
        # to_station = raw_input("请输入目的地\n")
        # from_station = "北京"
        # to_station = "厦门"
        d2 = self.get_station_names()
        try:
            # print(d2[from_station])
            # print(d2[to_station])
            from_station = d2[from_station]
            to_station = d2[to_station]
            return self.getlist(from_station=from_station,to_station=to_station)
        except KeyError, e:
            print '输入车站有误！！！'
#
# while True:
#     name = raw_input("请输入车站\n")
#     Shua = Shuapiao()
#     d2 = Shua.get_station_names()
#     try:
#         print(d2[name])
#     except KeyError, e:
#         print '输入车站有误'
shua = Shuapiao()
# lists = shua.serchTicket("北京","厦门")
# print lists