#! /usr/bin/python3
# coding= utf-8

import json


class Read_Json(object):
    def __init__(self, filename):
        self.filepath = "e:/python2/测试/data/" + filename


    def read_json(self):
        with open(self.filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
            # print(data)
            return data


# path = Read_Json("meeting_list.json").read_json()
# with open("e:/python2/测试/data/token.txt", "r") as f:
#     token = f.read()
# token = path.get("headers").setdefault("token", token)
# arr = []
# for data in path.values():
#     arr.append((
#         path.get("url"),
#         path.get("data"),
#         path.get("headers")
#     ))
# print(arr)


# if __name__ == '__main__':
#     datas = Read_Json("login.json").read_json()
#     arr = []
#     for data in datas.values():
#         arr.append((data.get("url"),
#                     data.get("mobile"),
#                     data.get("password"),
#                     data.get("code"),
#                     data.get("msg")))
#         print(arr)
# #



"""
   # url = "https://vzhapi.tamiyun.com/robotadmin/tm/admin/meeting/c2mGetAllMeeting"
        # data = {
        #     "createEndTime": "",
        #     "createStartTime": "",
        #     "curPage": 1,
        #     "employeeId": 22,
        #     "endTime": "",
        #     "feeType": "null",
        #     "isVzh": -1,
        #     "pageSize": 10,
        #     "rocessId": "null",
        #     "startTime": ""}
        # headers = {
        #     "Content-Type": "application/json",
        #     "token": "f7b8affca1e54dbd960e7ec9a3bd2ead",
        #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like"
        #                   " Gecko) Chrome/76.0.3809.100 Safari/537.36"
        #             }
"""
#
# ,
#              "logon_02":
#           {"url":"https://vzhapi.tamiyun.com/robotadmin/tm/admin/employee/login",
#                   "mobile":"18612260408",
#                  "password":"",
#                   "msg": "输入参数错误!",
#                   "code": 400}