import requests

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
import re

@csrf_exempt
def login(phone):
    url = 'http://193.112.224.186:8080/login/mobile/verifycode'
    data = json.dumps({
        "areaCode": "86",
        "userDeviceInfo": {
            "deviceId": "B2C892BC-AF6A-4C33-9142-49016BE48887",
            "brand": "apple",
            "model": "iPhone 7 Plus",
            "screenHeight": 736,
            "screenWidth": 414,
            "operationSystem": "14.4.2",
            "language": "cn"
        },
        "loginType": 1,
        "verificationCode": "7519",
        "phoneNumber": phone
    })
    header = {'Content-Type': 'application/json'}
    res = requests.post(url, data=data, headers=header)

    return res

def form(request):
    return render(request,'userInfo.html')



result = ''
@csrf_exempt
def userInfo(request):
    global result
    if request.GET:
        mobile = request.GET.get('q')
        if mobile:
            if re.match(r"^1[356789]\d{9}$",mobile):
                res = login(mobile)
                loginCode = res.json().get('code')

                if loginCode == 200:
                    token =  'Bearer '+ res.json().get('data').get('token')
                    url = 'http://193.112.224.186:8080/home'
                    header = {
                        'Content-Type': 'application/json',
                        'Authorization': token,
                        'Accept':'*/*'
                    }
                    res = requests.get(url,headers=header)
                    result = res.json()
                else:
                    result = res.json().get('msg')
                    return result
            else:
                result = '手机号码错误'
        else:
            result = '手机号码为空'

    return render(request,'userInfo.html',{"usrMessage":result})


