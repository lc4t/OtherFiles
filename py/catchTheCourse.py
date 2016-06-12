#! /usr/bin/python3
# -*- coding:UTF-8 -*-

import requests
from bs4 import BeautifulSoup
import lxml
import re
import time
from optparse import OptionParser

from urllib.parse import urlencode
class Login:
    def __init__(self):
        self.request = requests.Session()


    def uestc(self, loginURL, username = '', password = ''):

        captchaResponse = ''
        self.uestcHeader = {
                'Host': 'idas.uestc.edu.cn',
                'Proxy-Connection': 'keep-alive',
                'Cache-Control': 'max-age=0',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'Origin': 'http://idas.uestc.edu.cn',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Referer': 'http://idas.uestc.edu.cn/authserver/login?service=http://portal.uestc.edu.cn/index.portal',
                'Accept-Encoding': 'gzip, deflate',
                'Accept-Language': 'en-US,en;q=0.8',
        }
        checkURL = 'http://idas.uestc.edu.cn/authserver/needCaptcha.html?username=' + username + '&_=' + str(int(time.time() * 1000))

        loginer = self.request.get(url = loginURL, headers = self.uestcHeader)
        soup = BeautifulSoup(loginer.text, 'lxml')

        checker = self.request.get(url = checkURL, headers = self.uestcHeader)
        if (re.findall(r'true', checker.text)):
            open('captcha.jpg', 'wb').write(self.request.get(url = 'http://idas.uestc.edu.cn/authserver/captcha.html', headers = self.uestcHeader).content)
            captchaResponse = input('Please input the captha.jpg \'s code:')

        '''
        need to login:
            username=123
            password=123
            lt=LT-2529-DkdcaLcTkYiX0voxtUnVaT7drNZTMl1465744645549-24rb-cas
            dllt=userNamePasswordLogin
            execution=e3s1
            _eventId=submit
            rmShown=1
        '''
        lt = soup.select('input[name=lt]')[0]['value']
        dllt = soup.select('input[name=dllt]')[0]['value']
        execution = soup.select('input[name=execution]')[0]['value']
        _eventId = soup.select('input[name=_eventId]')[0]['value']
        rmShown = soup.select('input[name=rmShown]')[0]['value']


        if (captchaResponse):
            postData = urlencode(
                {
                    'username':username,
                    'password':password,
                    'lt':lt,
                    'dllt':dllt,
                    'execution':execution,
                    '_eventId':_eventId,
                    'rmShown':rmShown,
                    'captchaResponse': captchaResponse
                }).encode(encoding='UTF8')
        else:
            postData = urlencode(
                {
                    'username':username,
                    'password':password,
                    'lt':lt,
                    'dllt':dllt,
                    'execution':execution,
                    '_eventId':_eventId,
                    'rmShown':rmShown,
                }).encode(encoding='UTF8')

        loginer = self.request.post(url = loginURL, data = postData, headers = self.uestcHeader)
        loginer = self.request.get(url = loginer.url)
        if (loginer.url == loginURL):
            print ('username/password/captcha may wrong, please input again')
            exit(0)
        self.uestcVisitExam()

    def uestcVisitExam(self):   # set upselect
        self.examManagerBaseURL = 'http://eams.uestc.edu.cn'
        self.examTypes = {}
        loginer = self.request.get(url = self.examManagerBaseURL + '/eams/home!submenus.action', headers = self.uestcHeader)
        soup = BeautifulSoup(loginer.text, 'lxml')
        print ('exam/ ==>')
        for i, types in enumerate(soup.select('a[mytitle]')):
            print (i, types['mytitle'])
            self.examTypes[i] = types['href']
        select = int((input('select one, input number:')))
        self.uestcGetSelectType(select)

    def uestcGetSelectType(self, upselect = -1):    # set select
        print ('uestcGetSelectType ==>')
        if (upselect < 0 or upselect >= len(self.examTypes)):
            print ('error input, back')
            self.uestcVisitExam()
            return


        self.tablerTypes = {}
        tabler = self.request.get(url = self.examManagerBaseURL + self.examTypes[select])
        soup = BeautifulSoup(tabler.text, 'lxml')
        for i, types in enumerate(soup.select('a[mytitle]')):
            print (i, types['mytitle'])
            self.tablerTypes[i] = types['href']
        select = int((input('select one, input number:')))
        self.uestcTablerSelectType(select, upselect)


    def uestcTablerSelectType(self, select, upselect):    # handle point here
        print ('uestcTablerSelectType ==>')
        '''
            upselect
                0 课程管理
                1 我的信息
                2 辅修与双学位
            select
                0 我的计划
                1 文字评教
                2 学生评教
                3 成绩在线打印申请
                4 重修报名
                5 重修报名申请日志查询
                6 我的重修课表
                7 全校开课查询
                8 全校计划查询
                9 选    课
                10 我的选课日志
                11 我的课表
                12 我的成绩
                13 转专业-报名申请
                14 转方向-报名申请
                15 我的重修申请
                16 我的考试
                17 课程管理
                18 我的信息
                19 辅修与双学位
        '''
        if (select < 0 or select >= len(self.tablerTypes)):
            print ('error input, back')
            self.uestcVisitExam()
            return

        html = self.request.get(url = self.examManagerBaseURL + self.tablerTypes[select])
        if (upselect == 0):
            if (select == 9):
                self.uestcChooseCourse(html)

    def uestcChooseCourse(self, html):
        print ('uestcChooseCourse ==>')


def main():
    usage = "usage: %prog [options] arg"
    parser = OptionParser()
    parser.add_option('-u', '--username', help = 'Your username')
    parser.add_option('-p', '--password', help = 'Your password')
    parser.add_option('-s', '--school', help = 'uestc..')
    (options, args) = parser.parse_args()
    if (options.school == None):
        options.school = 'uestc'
    if (options.username == None or options.password == None):
        parser.print_help()
        exit(0)
    if (options.school == 'uestc'):
        crawler = Login()
        crawler.uestc('http://idas.uestc.edu.cn/authserver/login?service=http://portal.uestc.edu.cn/index.portal', options.username, options.password)
    else:
        print ('Not support, you can pull request to https://github.com/lc4t/Otherfile/py/catchTheCourse.py')
        exit(0)





if __name__ == '__main__':
    main()
