from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import requests,json

from DiptokTools.message.login import loginApi


@csrf_exempt
def cancel(request):
    message = {}
    if request.POST:
        d1 =request.POST.get('q')

        '''
        loads()：将json数据转化成dict数据
        dumps()：将dict数据转化成json数据
        load()：读取json文件数据，转成dict数据
        dump()：将dict数据转化成json数据后写入json文件
        '''

        resp = loginApi(d1)
        loginResp =resp.get('code')
        if loginResp != 200:
            message['rlt'] =  '你输入的手机号码为%s手机号码不正确' % d1
        else:
            token = resp.get('data').get('token')  # [b'data']['token']
            token1 = 'Bearer ' + token

            cancelUrl = "http://193.112.224.186:8080/home/user/logoff/verifycode/validate"
            data1 = json.dumps({"areaCode":"86","phoneNumber":"13632422058","verificationCode":""})

            header = {
                'Content-Type': 'application/json',
                'Authorization': token1
            }

            res = requests.post(url=cancelUrl, data=data1, headers=header)
            print(res.json())
            resp1 = res.json().get('data')
            if resp1:
                cancelUrl = "http://193.112.224.186:8080/home/user/logoff"
                data1 = json.dumps({"areaCode":"86","mobile":"13632422058","temporaryCode":resp1})

                header = {
                    'Content-Type': 'application/json',
                    'Authorization': token1
                }
                res = requests.post(url=cancelUrl, data=data1, headers=header)
                cancelUrl = "http://193.112.224.186:8080/home/user/logoff/confirm"


                header = {
                    'Content-Type': 'application/json',
                    'Authorization': token1
                }
                res = requests.post(url=cancelUrl, headers=header)
                message['rlt'] = "注销成功"
            else:
                message['rlt'] = "注销成功"

    return render(request,"cancelUser.html",message)



