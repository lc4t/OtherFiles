import requests
from urllib.parse import urlparse
import re

r = requests.Session()
print('visit: http://www.baidu.com')
step1 = r.get('http://www.baidu.com/', allow_redirects=False)
if 'www.baidu.com/img' in step1.text:
    print('had logined')
    exit()
url = step1.headers['Location']
print('Location: ' + url)
step2 = r.get(url, allow_redirects=False)
url = step2.headers['Location']
print('Location: ' + url)
step3 = r.get(url, allow_redirects=False)
domain = urlparse(url).netloc
url = 'http://' + domain + '/' + step3.headers['Location']
print('Location: ' + url)
step4 = r.get(url, allow_redirects=False)
data = {
# http://10.20.164.2:9997/login
    'username': '2014060102018',
    'password': '',
}
url = re.findall('<form\saction="(.*?)"', step4.text)[0]
step5 = r.post(url, data=data)
domain = urlparse(step5.url).netloc
target = re.findall('window.location.href="(.*?)"',step5.text)[0]
url = 'http://' + domain + target

while(1):
    print('Location: ' + url)
    step6 = r.get(url, allow_redirects=False)
    if target in step6.text:
        continue
    else:
        break
url = re.findall('window.location.href="(.*?)";', step6.text)[0]
print('Location: ' + url)
step7 = r.get(url)

if 'Successfully signed in' in step7.text:
    print('success sign in, please visit %s' % (step7.request.url))


# 222.197.165.114:8080
