#! /usr/bin/python3
# coding= utf-8
import requests


class Web_Login(object):


    def web_login_post(self, url, mobile, password):
        data = {"mobile": mobile,
                "passWord": password}
        headers = {"Content-Type": "application/json",
                   "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like"
                   " Gecko) Chrome/76.0.3809.100 Safari/537.36"}
        return requests.post(url=url, json=data, headers=headers)