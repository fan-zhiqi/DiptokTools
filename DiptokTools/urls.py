
from django.conf.urls import url
from DiptokTools import search, searchUser, userInfo, cancelUser, menu
from DiptokTools.message import login, followOther, eathFollow, eathTenFollow

urlpatterns = [
    url(r'^search_form/$', search.search_form),
    url(r'^search/$', search.search),
    # url(r'^search_user/$', searchUser.search_user),
    url(r'^userInfo/$', userInfo.form),
    url(r'^cancel/$',cancelUser.cancel),
    url(r'^meun/$',menu.menu),
    url(r'^searchUserInfo/$', userInfo.userInfo),
    # 关注，添加好友
    url(r'^login/$', login.login),
    url(r'^follow', followOther.follow1),
    url(r'^eathFollow/$', eathFollow.follow2),
    url(r'^eathFollow1/$', eathFollow.follow3),
    url(r'^eathTenFollow/$', eathTenFollow.follow3)

]
'''
regex: 正则表达式，与之匹配的 URL 会执行对应的第二个参数 view。

view: 用于执行与正则表达式匹配的 URL 请求。

kwargs: 视图使用的字典类型的参数。

name: 用来反向获取 URL。
'''
