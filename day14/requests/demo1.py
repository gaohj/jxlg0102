from urllib import request

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
    "Cookie":"anonymid=juagdpiney0yg3; _r01_=1; jebe_key=af15eb55-de2a-49f2-8861-fe6e628d49ed%7C67510b08b897c5e3b50e55d3a235a53c%7C1554854833372%7C1%7C1554854833452; _de=28A69782AB906D4A677B8FA35C706602; depovince=JX; jebecookies=f717be86-3b22-44c7-bb53-1772c80f6704|||||; JSESSIONID=abcSZ2iDkTLWF-XzTRBUw; ick_login=d91148b0-4447-4f36-8698-7d1a2e04ad85; p=87ebfcfd49d72527485094e38c7647223; first_login_flag=1; ln_uact=gaohj5@163.com; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; t=4fa97bd8bac3358f1b27e688c016a4a13; societyguester=4fa97bd8bac3358f1b27e688c016a4a13; id=541197383; xnsid=6450f738; ver=7.0; loginfrom=null; jebe_key=af15eb55-de2a-49f2-8861-fe6e628d49ed%7C67510b08b897c5e3b50e55d3a235a53c%7C1561685071316%7C1%7C1561685071224; wp_fold=0"
}

url = "http://www.renren.com/541197383/profile"

req = request.Request(url,headers=headers)
response = request.urlopen(req)
# print(response.read().decode())

with open('renren.html','w') as fp:
    fp.write(response.read().decode('UTF-8'))