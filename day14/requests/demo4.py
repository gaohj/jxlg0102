import requests
import json
import time

headers = {
    "User-Agent": "Mozilla/5.0 (hp-tablet; Linux; hpwOS/3.0.0; U; en-US) AppleWebKit/534.6 (KHTML, like Gecko) wOSBrowser/233.70 Safari/534.6 TouchPad/1.0",
}

#把下划线 o去掉就可以了
url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
# url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"

fw = input("请输入要翻译的英文单词")
timed = int(time.time() *1000)
data= {
        "i": fw,
        "from": "AUTO",
        "to": "AUTO",
        "smartresult": "dict",
        "client": "fanyideskweb",
        "salt": "15616915700465",
        "sign": "6d422c8b06f5bc15c1016c2474d2e994",
        "ts": "1561691570046",
        "bv": "3a019e7d0dda4bcd253903675f2209a5",
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "action	": "FY_BY_REALTIME",
}

response = requests.post(url,data=data,headers=headers)

dict = response.json()

print(dict['translateResult'][0][0]['tgt'])