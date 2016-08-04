from bs4 import BeautifulSoup
import lxml
import re
import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder
from urllib.parse import urlencode


class Bitcoin:
    def __init__(self, username = None, password = None, cookies = None):
        self.r = requests.Session()
        self.proxies = {
            "http": "127.0.0.1:10801",
            "https": "127.0.0.1:10802",
            }
        self.headers = {
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding':'gzip, deflate, br',
            'Accept-Language':'en-US,en;q=0.8',
            'Cache-Control':'max-age=0',
            'Connection':'keep-alive',
            'Content-Type':'application/x-www-form-urlencoded',
            'Host':'bitcointalk.org',
            'Origin':'https://bitcointalk.org',
            'Referer':'https://bitcointalk.org/index.php?action=login2',
            'Upgrade-Insecure-Requests':'1',
            'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.82 Safari/537.36',
            'X-Forwarded-For':'127.0.0.1',
            }


        print ('username:%s' % username)
        print ('try login')
        if (cookies):
            self.headers.update({'Cookie':cookies})
            html = self.r.get('https://bitcointalk.org/index.php', headers = self.headers, proxies = self.proxies).text
        else:
            post_data = urlencode({
                'user' : username,
                'passwrd' : password,
                'cookielength' : '43200',
                'hash_passwrd' : 'false'
                }).encode('utf8')
            self.r.get('https://bitcointalk.org/index.php', headers = self.headers, proxies = self.proxies).cookies
            self.r.post('https://bitcointalk.org/index.php?action=login2', data = post_data, headers = self.headers, proxies = self.proxies, allow_redirects=False).headers
            html = self.r.get('https://bitcointalk.org/index.php', headers = self.headers, proxies = self.proxies).text
            
        # print (html)
        if len(re.findall('logout', html)) >= 1:
            print ('Login success')
        else:
            raise ValueError('username or password not match')
    
    def set_topic(self, topic):
        html = self.r.get('https://bitcointalk.org/index.php?topic=' + str(topic), headers = self.headers, proxies = self.proxies).text
        reply = re.findall('<a href="(https://bitcointalk\.org/index\.php\?action=post;topic=[\d\.]+;num_replies=\d+)"', html)
        if len(reply) > 0:
            return reply[0]

    def post_reply(self, url, content):
        headers = self.headers

        soup = BeautifulSoup(self.r.get(url, headers = self.headers, proxies = self.proxies).text, 'lxml')
        post_url = soup.select('#postmodify')[0]['action']

        multipart_data = MultipartEncoder(
        fields = {
                'topic' : soup.findAll('input',{'name': 'topic'})[0]['value'],
                'subject': soup.findAll('input',{'name': 'subject'})[0]['value'],
                'icons': soup.findAll('select', {'name':'icon'})[0].findAll('option', {'selected':'selected'})[0]['value'],
                'message': content,
                'notify': soup.findAll('input',{'name': 'notify'})[0]['value'],
                'do_watch': soup.findAll('input',{'name': 'do_watch'})[0]['value'],
                'do_watch': soup.findAll('input',{'name': 'do_watch', 'checked': 'checked'})[0]['value'],
                'goback': soup.findAll('input',{'name': 'goback'})[0]['value'],
                'post': soup.findAll('input',{'name': 'post'})[0]['value'], 
                'num_replies': soup.findAll('input',{'name': 'num_replies'})[0]['value'],
                'additional_options': soup.findAll('input',{'name': 'additional_options'})[0]['value'],
                'sc': soup.findAll('input',{'name': 'sc'})[0]['value'],
                'seqnum': soup.findAll('input',{'name': 'seqnum'})[0]['value'],
                }
        )
        headers.update({'content-type': multipart_data.content_type})
        self.r.post(post_url, headers = headers, data = multipart_data, proxies = self.proxies)
        print ('post done')


from optparse import OptionParser
import time


def main():
    usage = "usage: %prog [options] arg"
    parser = OptionParser()
    parser.add_option('-u', '--username', help = 'Your username')
    parser.add_option('-p', '--password', help = 'Your password')
    parser.add_option('-c', '--cookies', help = 'Your cookies   "PHPSESSID=xxx; SMFCookie129=aaa"')
    parser.add_option('-t', '--topicid', help = 'target topic id')
    parser.add_option('-s', '--content', help = 'content for you post')
    parser.add_option('-o', '--times', help = 'post again every this second')
    (options, args) = parser.parse_args()

    if (options.cookies == None and (options.username == None and options.password == None)):
        parser.print_help()
    elif (options.topicid == None or options.content == None):
        parser.print_help()
    else:
        bitcoin = Bitcoin(username = options.username, password = options.password, cookies = options.cookies)
        reply_url = bitcoin.set_topic(options.topicid)
        if (options.times):
            while (True):
                time.sleep(int(options.times))
                bitcoin.post_reply(url = reply_url, content = options.content)
        else:
            bitcoin.post_reply(url = reply_url, content = options.content)
        
    exit(0)

if __name__ == '__main__':
    main()