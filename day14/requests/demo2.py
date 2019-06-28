from urllib import request
import http.cookiejar
import urllib.parse

cookie = http.cookiejar.CookieJar() #用来管理cookie 创建对象

#创建处理器对象
handle = urllib.request.HTTPCookieProcessor(cookie)

#根据处理器对象 创建打卡对象

opener = urllib.request.build_opener(handle)

post_url = "https://passport.weibo.cn/signin/login"

data = {
    "username":"17701256561",
    "password":"lizhibin666",
    "savestate":1,
    "r":"https://weibo.cn/?luicode=10000011&lfid=102803",
    "ec":0,
    "pagerefer":"https://weibo.cn/pub/",
    "entry":"mweibo",
    "wentry":"",
    "loginfrom":"",
    "client_id":"",
    "code":"",
    "qq":"",
    "mainpageflag":1,
    "hff":"",
    "hfp":""
}

data = urllib.parse.urlencode(data).encode('utf-8')
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
    "Origin": "https://passport.weibo.cn",
    "Accept": "*/*",
    "Content-Type": "application/x-www-form-urlencoded",
    "Connection": "keep-alive",
    "Host": "passport.weibo.cn",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Referer": "https://passport.weibo.cn/signin/login?entry=mweibo&r=https%3A%2F%2Fweibo.cn%2F%3Fluicode%3D10000011%26lfid%3D102803&backTitle=%CE%A2%B2%A9&vt="
}



req = urllib.request.Request(post_url,headers=headers,data=data)
response = opener.open(req) #保存登录以后的cookie信息

# print(response.read().decode('gb2312'))

url = "https://m.weibo.cn/profile/6388179289"

headers1 = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
}


reqs1 = urllib.request.Request(post_url,headers=headers1)

responses = opener.open(reqs1)

print(responses.read().decode('gb2312'))

