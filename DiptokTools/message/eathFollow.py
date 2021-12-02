import random
import re

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from DiptokTools.message.followOther import follow, followEFS, EFSfollow
from DiptokTools.message.login import userId

result = ''
res3 = ''
followUserId3 = ''
@csrf_exempt
def follow2(request):
    global result,res3,followUserId3,res4,followUserId4,mobile,followMobile
    if request.POST:
        mobile = request.POST.get('w')
        followMobile = request.POST.get('w2')
        if re.match(r"^1[356789]\d{9}$", mobile):


            if re.match(r"^1[356789]\d{9}$",followMobile):

                try:
                    follow(mobile, followMobile)
                    follow(followMobile, mobile)
                    result = mobile +'、'+ followMobile+'相互关注成功'
                except Exception as e:
                    result = e
            else:
                result = '请输入好友正确的手机号码'
        else:
            result = '请输入你的正确手机号码'
    return render(request,'eathFollow.html',{"eathFollowRlt":result})


@csrf_exempt
def follow3(request):
    global result,res3,followUserId3,res4,followUserId4,mobile,followMobile
    if request.POST:
        mobile = request.POST.get('w')
        followMobile = request.POST.get('w2')
        if re.match(r"^1[356789]\d{9}$", mobile):
            if re.match(r"^1[356789]\d{9}$",followMobile):
                try:
                    followEFS(mobile, followMobile)
                    EFSfollow(followMobile, mobile)
                    result = mobile +'、'+ followMobile+'相互关注成功'
                except Exception as e:
                    result = e
            else:
                result = '请输入好友正确的手机号码'
        else:
            result = '请输入你的正确手机号码'



    return render(request,'eathFollow1.html',{"eathFollowRlt":result})


def eath_follow(mobile):

    try:

        followMobile = str(random.randint(13600000000, 13699999999))
        follow(mobile, followMobile)
        follow(followMobile, mobile)

        result = mobile + '、' + followMobile + '相互关注成功'
    except Exception as e:
        result = e
    return result

