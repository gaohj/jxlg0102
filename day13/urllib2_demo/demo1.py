#encoding:utf-8

import urllib2

url = "http://www.baidu.com"
#1.请求的url
#2.为none 说明这个是get请求
#timeout 超时时间
res =urllib2.urlopen(url,data=None)

# print(res)
# print(res.read()) #返回所有的内容
# print(res.readline()) #获取行  <html>
# print(res.readlines()) # 列表 放所有的行
# print(res.getcode()) #获取客户端请求的状态
# print(res.geturl())

print(res.read().decode('utf-8'))