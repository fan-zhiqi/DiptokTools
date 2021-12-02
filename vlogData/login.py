import requests


class login():
    def session(self,session):
        url="http://193.112.224.186:8888/api/login"
        data = "username=admin&password=123456&submit=Login"
        header = {"Content-Type": "application/x-www-form-urlencoded"}
        # Cookie: sidebarStatus=0
        my_session = session.post(url,data=data,headers=header)
        return my_session


if __name__ == '__main__':
    a=login().session(session=requests.Session())
    print(a)