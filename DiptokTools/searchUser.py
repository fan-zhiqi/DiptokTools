# # -*- coding: utf-8 -*-
#
# from django.shortcuts import render
# from django.views.decorators.csrf import csrf_exempt
# import pymysql
#
#
# conn = pymysql.connect(host="193.112.224.186",port=3306, user="root", password="Wwzaixian2019.", db="flo")
# cur = conn.cursor()
#
# # 接收POST请求数据
#
# result={}
# @csrf_exempt
# def search_user(request):
#     global telephone,useID,code,result
#     if request.POST:
#         mobile =request.POST.get('q')
#
#         if mobile:
#             userSql = "select subject_id,user_id,subject_code FROM user_account WHERE subject_id like  %s" % (mobile)
#             cur.execute(userSql)
#             result = cur.fetchall()
#         else:
#             result= '手机号码为空'
#
#     return render(request, "search_user.html",{'result': result})


pass
