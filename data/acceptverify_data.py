#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/1 16:03
# @Author  : 二部测试-陈兴川
# @File    : acceptverify_data.py
#@email    :chenxingchuan@chinasoftinc.com

class AcceptVerify_datas:
    containerno_data=[{'test_name':'用集装箱号查询','no':"blIV52717","check":"blIV52717"}]
    sta=[{'test_name':'只输入eta开始时间','etastart':"2019-07-01","etaend":"null"},
         {'test_name': '只输入eta结束时间', 'etastart': "null", "etaend": "2019-07-09"},
         {'test_name':'输入eta开始时间和结束时间','etastart':"2019-07-01","etaend":"2019-07-09"},
         {'test_name':'输入相同的eta开始时间和结束时间','etastart':"2019-07-08","etaend":"2019-07-08"}]
    etd=[{'test_name':'只输入etd开始时间','etdstart':"2019-06-01","etdend":"null"},
         {'test_name': '根据ETD 结束日期搜索数据', 'etdstart': "null", "etdend": "2019-06-30"},
         {'test_name': '输入相同etd开始时间和结束时间', 'etdstart': "2019-06-06", "etdend": "2019-06-06"},
         {'test_name':'输入etd开始时间和结束时间','etdstart':"2019-06-01","etdend":"2019-06-30"}]