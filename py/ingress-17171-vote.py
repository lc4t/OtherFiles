# -*- coding:utf-8 -*-
import json
import requests
import time
import random

MIN = 10
MAX = 1000

count = 0
citys = input('输入你要投票的城市，用空格隔开:')
print(citys)
need = int(input('刷多少次?:'))
citys = citys.split()
data = {}
for i in citys:
    data.update({
                'citys[]'.encode().decode('utf-8'): i.encode().decode('utf-8')
                })

while 1:
    ip = '%d.%d.%d.%d' % (random.randint(1, 255),
                          random.randint(1, 255),
                          random.randint(1, 255),
                          random.randint(1, 255))
    ua = 'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/%d.0.%d.%d Safari/537.36' % (random.randint(52, 55), random.randint(0, 9999), random.randint(0, 99))
    headers = {
        'X-Forwarded-For': ip,
        'User-Agent': ua, #'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36'
    }
    r = requests.Session()
    r.get('http://mdc.17173.com/futureAct', headers=headers)
    test = r.post('http://mdc.17173.com/futureAct/vote', data=data,
                  headers=headers)
    status = json.loads(test.text)['success']
    print('[%d] ip:%s %s' % (count, ip, status))
    if status:
        count += 1
        t = random.randint(MIN, MAX)
        print('sleep %d second' % t)
        time.sleep(t)

    if count == need:
        print('done')
        exit(0)
