import re

import requests

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json


resp = ''
@csrf_exempt
def login(request):
    global resp
    if request.POST:
        mobile = request.POST.get('q')
        if mobile:
            if re.match(r"^1[356789]\d{9}$",mobile):
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
                    "phoneNumber": mobile
                })
                header = {'Content-Type': 'application/json'}
                res = requests.post(url, data=data, headers=header)
                resp = res.json()
            else:
                resp = '手机号码不正确'
        else:
            resp = '手机号码为空'
    return render(request,'login.html',{'loginRlt':resp})

def loginApi(mobile):
    global resp
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
        "phoneNumber": mobile
    })
    header = {'Content-Type': 'application/json'}
    res = requests.post(url, data=data, headers=header)
    resp = res.json()
    return resp

def loginApiEFS(mobile):
    global resp
    url = 'http://193.112.224.186:8080/login/mobile/verifycode'
    data = json.dumps({
        "areaCode": "853",
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
        "phoneNumber": mobile
    })
    header = {'Content-Type': 'application/json'}
    res = requests.post(url, data=data, headers=header)
    resp = res.json()
    return resp

def userIdEFS(telephone):
    res = loginApiEFS(telephone)
    followUserId = res.get('data').get('userId')
    return followUserId

def userId(telephone):
    res = loginApi(telephone)
    followUserId = res.get('data').get('userId')
    print(followUserId)
    return followUserId