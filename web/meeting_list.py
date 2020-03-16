#! /usr/bin/python3
# coding= utf-8

import requests



class Meeting_List(object):


    def meeting_list(self, url, data, headers):
        return requests.post(url=url, json=data, headers=headers)

    """
    url = "https://vzhapi.tamiyun.com/robotadmin/tm/admin/meeting/c2mGetAllMeeting"
    data= {
        "createEndTime": "",
        "createStartTime": "",
        "curPage": 1,
        "employeeId": 22,
        "endTime": "",
        "feeType": "null",
        "isVzh": -1,
        "pageSize": 10,
        "rocessId": "null",
        "startTime": ""
        }
    """
