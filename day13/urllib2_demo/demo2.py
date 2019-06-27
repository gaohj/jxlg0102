#encoding:utf-8

import urllib2

headers ={

   "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134",
}
url = "http://www.baidu.com"

#创建请求对象
res = urllib2.Request(url,headers=headers)

print(res.get_full_url()) #获取完整的url
print(res.get_method()) #获取客户端请求的方法
print(res.get_header("User-Agent")) #获取浏览器的名称
print(res.get_host()) #获取host名称
print(res.get_type()) #获取协议的名称

res.add_header("Connection","keep-alive")
print(res.get_header("Connection"))
