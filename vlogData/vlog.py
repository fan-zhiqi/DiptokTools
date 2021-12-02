import json

import requests
from vlogData.connetMySQL import read_data

from vlogData.login import login

dataId = read_data()
list(dataId)


class VlogStatus:
    def update_status(self):
        for i in dataId:
            url = "http://193.112.224.186:8888/api/sys/moments/updateStatus"
            data =json.dumps({"id":i,"auditStatus":1,"failReason":""})
            header={"Content-Type": "application/json;charset=UTF-8"}
            # Cookie: JSESSIONID=A6mdYJpiMJuwBlUq9W4rk6xJEwDQpgljR56CD51i; Admin-Token=1
            session = requests.Session()
            res= login().session(session)
            # print(res.json())
            resp= session.post(url,data=data,headers=header)
            print(resp.json())

if __name__ == '__main__':
    VlogStatus().update_status()