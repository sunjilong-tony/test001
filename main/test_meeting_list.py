#! /usr/bin/python3
# coding= utf-8

import unittest
from web.meeting_list import Meeting_List
from tools.read_json import Read_Json
from parameterized import parameterized


def get_data():
    path = Read_Json("meeting_list.json").read_json()
    with open("e:/python2/测试/data/token.txt", "r") as f:
        token = f.read()
    path.get("headers").setdefault("token", token)
    arr = []
    for i in path.values():
        arr.append((
            path.get("url"),
            path.get("data"),
            path.get("headers")
        ))
    return arr


class Test_meeting_list(unittest.TestCase):
    @parameterized.expand(get_data())
    def test_list(self, url, data, headers):
        re = Meeting_List().meeting_list(url=url, data=data, headers=headers)
        self.assertEqual(300, re.status_code)

if __name__ == '__main__':
    unittest.main()
