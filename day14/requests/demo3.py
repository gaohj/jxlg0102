
#免费代理
#西刺代理
#快代理

import urllib.request
import random
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
}

#http://www.jsons.cn/useragent/
ua_list = [
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv,2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)",
    "Mozilla/5.0 (hp-tablet; Linux; hpwOS/3.0.0; U; en-US) AppleWebKit/534.6 (KHTML, like Gecko) wOSBrowser/233.70 Safari/534.6 TouchPad/1.0"
]
ip_list = [
    {'http':'http://180.118.128.199'},
    {'http':'http://180.104.63.120'},
    {'http':'http://58.22.204.62'},
    {'http':'http://114.215.139.19'},
]

url = "http://www.qfedu.com"
#这是代理
proxy = random.choice(ip_list)
proxy_handler = urllib.request.ProxyHandler(proxies=proxy) #使用代理
openser = urllib.request.build_opener() #创建打开服务器
req = urllib.request.Request(url=url,headers=headers)
req.add_header("User-Agent",random.choice(ua_list))
print(req.get_header('User-agent'))
response =openser.open(req)
#print(response.read().decode('utf-8'))