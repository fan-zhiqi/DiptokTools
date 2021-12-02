
import requests
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json

from DiptokTools.message.login import loginApi, userId, loginApiEFS, userIdEFS

result = ''

@csrf_exempt
def follow1(request):
    global result
    if request.POST:
        mobile = request.POST.get('q')
        followMobile = request.POST.get('q2')
        res = loginApi(mobile)
        followUserId1 = userId(followMobile)
        loginCode = res.get('code')
        if loginCode == 200:
            token1 = res.get('data').get('token')
            token =  'Bearer '+ token1
            url = 'http://193.112.224.186:8080/home/followers/add'
            header = {
                'Content-Type': 'application/json',
                'Authorization': token,
                'Accept':'*/*'
            }
            followData = json.dumps({
                "followUserId":followUserId1
            })
            res = requests.post(url=url,data=followData,headers=header)
            result = res.json()
        else:
            result = res.json().get('msg')
    return render(request,'follow.html',{"followRlt":result})


def follow(mobile,followMobile):
    res = loginApi(mobile)
    followUserId1 = userId(followMobile)
    loginCode = res.get('code')
    if loginCode == 200:
        token1 = res.get('data').get('token')
        token =  'Bearer '+ token1
        url = 'http://193.112.224.186:8080/home/followers/add'
        header = {
            'Content-Type': 'application/json',
            'Authorization': token,
            'Accept':'*/*'
        }
        followData = json.dumps({
            "followUserId":followUserId1
        })
        res = requests.post(url=url,data=followData,headers=header)
        result1 = res.json()
    else:
        result1 = res.json().get('msg')
    print(result1)

def EFSfollow(mobile,followMobile):
    res = loginApiEFS(mobile)
    followUserId1 = userId(followMobile)
    loginCode = res.get('code')
    if loginCode == 200:
        token1 = res.get('data').get('token')
        token =  'Bearer '+ token1
        url = 'http://193.112.224.186:8080/home/followers/add'
        header = {
            'Content-Type': 'application/json',
            'Authorization': token,
            'Accept':'*/*'
        }
        followData = json.dumps({
            "followUserId":followUserId1
        })
        res = requests.post(url=url,data=followData,headers=header)
        result1 = res.json()
    else:
        result1 = res.json().get('msg')
    print(result1)

def followEFS(mobile,followMobile):
    res = loginApi(mobile)
    followUserId1 = userIdEFS(followMobile)
    loginCode = res.get('code')
    if loginCode == 200:
        token1 = res.get('data').get('token')
        token =  'Bearer '+ token1
        url = 'http://193.112.224.186:8080/home/followers/add'
        header = {
            'Content-Type': 'application/json',
            'Authorization': token,
            'Accept':'*/*'
        }
        followData = json.dumps({
            "followUserId":followUserId1
        })
        res = requests.post(url=url,data=followData,headers=header)
        result1 = res.json()
    else:
        result1 = res.json().get('msg')
    print(result1)