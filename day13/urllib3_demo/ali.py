import urllib.parse
import json
from urllib import request
headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
}

url = "https://job.alibaba.com/zhaopin/socialPositionList/doList.json"

for i in  range(1,10):
    params = {
        "pageSize": 10,
        't': '0.1439500693318494',
        'pageIndex':i
    }
    data = urllib.parse.urlencode(params).encode()

    req = urllib.request.Request(url,headers=headers,data=data)

    response = urllib.request.urlopen(req)
    content = response.read().decode()
    print(content)

    data_dict = json.loads(content)

    job_list = data_dict['returnValue']['datas']

    for job in job_list:
        degree = job.get('degree')
        departmentName = job.get('departmentName')
        firstCategory = job.get('firstCategory')
        description = job.get('description')
        workExperience = job.get('workExperience')

        with open('ali.txt', 'a+', encoding='utf-8') as fp:
            fp.write(str((degree, departmentName, firstCategory,description,workExperience)) + "\n")
            fp.flush()  # 不回车我也会往里写数据

