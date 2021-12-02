import random
import re
import threading

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from DiptokTools.message.eathFollow import eath_follow
from DiptokTools.message.followOther import follow
from DiptokTools.threading.threadingPy import CreatThread


@csrf_exempt
def follow3(request):
    rlt = ''
    if request.POST:
        mobile = request.POST.get('e')
        if re.match(r"^1[356789]\d{9}$", mobile):
            n = 0
            while n < 10:
                followMobile = str(random.randint(13600000000, 13699999999))
                follow(mobile, followMobile)
                follow(followMobile, mobile)
                rlt += followMobile + '    '
                n += 1
            result = rlt + '相互关注成功'
        else:
            result = '请输入正确的手机号码'
    else:
        result = '请输入正确的手机号码'

    return render(request, 'eathTenFollow.html', {"rlt": result})

'''
  >> from itertools import combinations, permutations
>> permutations([1, 2, 3], 2)
<itertools.permutations at 0x7febfd880fc0>
                # 可迭代对象 
>> list(permutations([1, 2, 3], 2))   #排列
[(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)] 
>> list(combinations([1, 2, 3], 2))   #组合
[(1, 2), (1, 3), (2, 3)]
'''


@csrf_exempt
def follow4(request):
    if request.POST:
        mobile = request.POST.get('e')
        if re.match(r"^1[356789]\d{9}$", mobile):
            CreatThread('线程1',mobile).start_thread()
            CreatThread('线程2', mobile).start_thread()

    return render(request, 'eathTenFollow.html', {"rlt": result})

