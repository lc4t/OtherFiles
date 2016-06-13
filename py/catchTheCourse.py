#! /usr/bin/python3
# -*- coding:UTF-8 -*-

import requests
from bs4 import BeautifulSoup
import lxml
import re
import time
from optparse import OptionParser

from urllib.parse import urlencode

__TYPE__ = 'A'

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


    def uestcVisitExam(self, NEXT = True):   # set upselect
        self.examManagerBaseURL = 'http://eams.uestc.edu.cn'
        self.examTypes = {}
        loginer = self.request.get(url = self.examManagerBaseURL + '/eams/home!submenus.action', headers = self.uestcHeader)
        soup = BeautifulSoup(loginer.text, 'lxml')
        print ('exam/ ==>')
        for i, types in enumerate(soup.select('a[mytitle]')):
            print (i, types['mytitle'])
            self.examTypes[i] = types['href']

        if (NEXT):
            select = int((input('select one, input number:')))
            self.uestcGetSelectType(select)

    def uestcGetSelectType(self, upselect = -1, NEXT = True):    # set select
        print ('uestcGetSelectType ==>')
        if (upselect < 0 or upselect >= len(self.examTypes)):
            print ('error input, back')
            self.uestcVisitExam()
            return


        self.tablerTypes = {}
        tabler = self.request.get(url = self.examManagerBaseURL + self.examTypes[upselect], headers = self.uestcHeader)
        soup = BeautifulSoup(tabler.text, 'lxml')
        for i, types in enumerate(soup.select('a[mytitle]')):
            print (i, types['mytitle'])
            self.tablerTypes[i] = types['href']

        if (NEXT):
            select = int((input('select one, input number:')))
            self.uestcTablerSelectType(select, upselect)


    def uestcTablerSelectType(self, select, upselect, NEXT = True):    # handle point here
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

        html = self.request.get(url = self.examManagerBaseURL + self.tablerTypes[select], headers = self.uestcHeader)
        if (NEXT):
            if (upselect == 0):
                if (select == 9):
                    self.uestcChooseCourseType(html.text)
                else:
                    print ('select error')
                    self.uestcVisitExam()
                    return
            else:
                print ('upselect error')
                self.uestcVisitExam()
                return
        else:
            return html.text
        return

    def uestcChooseCourseType(self, html, NEXT = True):
        # baseURL is http://eams.uestc.edu.cn/eams/, add /eams/ to choosecourseTypes
        self.choosecourseTypes = {}
        print ('uestcChooseCourse ==>')
        soup = BeautifulSoup(html,'lxml')
        if(re.findall(r'第 1 轮', soup.get_text())):
            for i, types in enumerate(soup.select('a[target=stdElectDiv]')):
                cType = re.findall(r'(\w)平台',types.parent.h2.get_text())[0]
                print (cType + ' 平台')
                print (types.parent.select('div')[0].div.get_text().strip('\n').replace('\t',''))

                self.choosecourseTypes[cType] = '/eams/' + types['href']

            if (NEXT):
                select = input('select one, input A or B:').upper()
                html = self.request.get(url = self.examManagerBaseURL + self.choosecourseTypes[select], headers = self.uestcHeader)
                self.uestcChooseCourse1(select, html.text)
            else:
                select = __TYPE__
                html = self.request.get(url = self.examManagerBaseURL + self.choosecourseTypes[select], headers = self.uestcHeader)
                self.uestcChooseCourse1(select, html.text)
                return html.text
            return
        elif(re.findall(r'第 2 轮', soup.get_text())): # not test
            for i, types in enumerate(soup.select('a[target=stdElectDiv]')):
                cType = re.findall(r'(\w)平台',types.parent.h2.get_text())[0]
                print (cType + ' 平台')
                print (types.parent.select('div')[0].div.get_text().strip('\n').replace('\t',''))

                self.choosecourseTypes[cType] = '/eams/' + types['href']


            if (NEXT):
                select = input('select one, input A or B:').upper()
                html = self.request.get(url = self.examManagerBaseURL + self.choosecourseTypes[select], headers = self.uestcHeader)
                self.uestcChooseCourse2(select, html.text)
            else:
                select = __TYPE__
                html = self.request.get(url = self.examManagerBaseURL + self.choosecourseTypes[select], headers = self.uestcHeader)
                return html.text
            return

        elif(re.findall(r'第 3 轮', soup.get_text())): # not test
            for i, types in enumerate(soup.select('a[target=stdElectDiv]')):
                cType = re.findall(r'(\w)平台',types.parent.h2.get_text())[0]
                print (cType + ' 平台')
                print (types.parent.select('div')[0].div.get_text().strip('\n').replace('\t',''))
                self.choosecourseTypes[cType] = '/eams/' + types['href']

            if (NEXT):
                select = input('select one, input A or B:').upper()
                html = self.request.get(url = self.examManagerBaseURL + self.choosecourseTypes[select], headers = self.uestcHeader)
                self.uestcChooseCourse3(select, html.text)
            else:
                select = __TYPE__
                html = self.request.get(url = self.examManagerBaseURL + self.choosecourseTypes[select], headers = self.uestcHeader)
                return html.text
            return
        else:
            print (soup)
            print ('not support')

    def uestcChooseCourse1(self, select, html, NEXT = True):
        soup = BeautifulSoup(html, 'lxml')
        for links in soup.select('script[src^=/eams/stdElectCourse!]'):
            if (re.findall(r'data\.action', links['src'])):  # data
                self.dataURL = links['src']
            elif (re.findall(r'queryStdCount\.action', links['src'])):
                self.queryStdCountURL = links['src']
        self.catchCourseURL = self.queryStdCountURL.replace('queryStdCount.action', 'batchOperator.action')
        # dataJson = self.request.get(self.examManagerBaseURL + dataURL).text
        # stdCountJson = self.request.get(self.examManagerBaseURL + queryStdCountURL).text
        # print (dataJson)
        # print ('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
        # print (stdCountJson)

    def uestcChooseCourse2(self, select, html, NEXT = True):
        soup = BeautifulSoup(html, 'lxml')
        for links in soup.select('script[src^=/eams/stdElectCourse!]'):
            if (re.findall(r'data\.action', links['src'])):  # data
                self.dataURL = links['src']
            elif (re.findall(r'queryStdCount\.action', links['src'])):
                self.queryStdCountURL = links['src']
        self.catchCourseURL = self.queryStdCountURL.replace('queryStdCount.action', 'batchOperator.action')
        # dataJson = self.request.get(self.examManagerBaseURL + dataURL).text
        # stdCountJson = self.request.get(self.examManagerBaseURL + queryStdCountURL).text
        # print (dataJson)
        # print ('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
        # print (stdCountJson)

    def uestcChooseCourse3(self, select, html, NEXT = True):
        soup = BeautifulSoup(html, 'lxml')
        for links in soup.select('script[src^=/eams/stdElectCourse!]'):
            if (re.findall(r'data\.action', links['src'])):  # data
                self.dataURL = links['src']
            elif (re.findall(r'queryStdCount\.action', links['src'])):
                self.queryStdCountURL = links['src']

        # /eams/stdElectCourse!data.action?profileId=654
        self.catchCourseURL = self.queryStdCountURL.replace('queryStdCount.action', 'batchOperator.action')
        # dataJson = self.request.get(self.examManagerBaseURL + dataURL).text
        # stdCountJson = self.request.get(self.examManagerBaseURL + queryStdCountURL).text
        # print (dataJson)
        # print ('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
        # print (stdCountJson)

    def uestcCatchCourse(self, courseCode = 0, value = 0, thread = 20, action = True):
        # operator0:258929:false

        # virtualCashCost258929:12
        # operator0:258929:true:0
        # 258929 252344 252382
        i = 0
        needLogin = True
        while(True):
            if (needLogin):
                self.uestcVisitExam(NEXT = False)
                self.uestcGetSelectType(upselect = 0, NEXT = False)
                self.uestcChooseCourseType(self.uestcTablerSelectType(select = 9, upselect = 0, NEXT = False), NEXT = False)
            if (courseCode == 0 or courseCode == None):
                courseCode = input('coursecode:')
                courseCode = courseCode.split(' ')
            for code in courseCode:
                if (action):
                    # print ('try catch' + str(code))
                    postData = urlencode(
                        {
                            'virtualCashCost'+str(code): value,
                            'operator0':str(code) + ':true:0'
                        }).encode(encoding='UTF8')
                else:
                    # print ('un catch' + str(code))
                    postData = urlencode(
                        {
                            'operator0':str(code) + ':false'
                        }).encode(encoding='UTF8')
                # print (postData)
                ans = self.request.post(url = self.examManagerBaseURL + self.catchCourseURL, data = postData, headers = self.uestcHeader)
                date = ans.headers['Date']
                soup = BeautifulSoup(ans.text, 'lxml')
                message = soup.div.get_text().replace('\n','').replace('\t','')
                # print (str(i) + ':' + str(date) + ':' + str(message))
                if (i % 50 == 1):
                    print ()
                    print (i, end = ' ')
                    print (date)
                    print (message)
                i += 1
                if (re.findall(r'This session has been expired', message)):
                    needLogin = True
                    print (message)
                    break
                elif(re.findall(r'失败', message)):
                    print ('0', end = '')
                elif(re.findall(r'成功', message)):
                    print (message)
                    courseCode.remove(code)
                else:
                    print ('0', end = '')
                needLogin = False




def main():
    usage = "usage: %prog [options] arg"
    parser = OptionParser()
    parser.add_option('-u', '--username', help = 'Your username')
    parser.add_option('-p', '--password', help = 'Your password')
    parser.add_option('-s', '--school', help = 'uestc..')
    parser.add_option('-f', '--function', help = '[1]: catch course [2] normal..')
    parser.add_option('-o', '--others', help = 'give functions params,[1] is ok')
    (options, args) = parser.parse_args()
    if (options.school == None):
        options.school = 'uestc'
    if (options.username == None or options.password == None):
        parser.print_help()
        exit(0)
    if (options.school == 'uestc'):
        if (options.function == None or options.function == '2'):
            crawler = Login()
            crawler.uestc('http://idas.uestc.edu.cn/authserver/login?service=http://portal.uestc.edu.cn/index.portal', options.username, options.password)
            crawler.uestcVisitExam()
        elif (options.function == '1'):
            crawler = Login()
            crawler.uestc('http://idas.uestc.edu.cn/authserver/login?service=http://portal.uestc.edu.cn/index.portal', options.username, options.password)
            crawler.uestcCatchCourse(action = options.others)
    else:
        print ('Not support school, you can pull request to https://github.com/lc4t/Otherfile/py/catchTheCourse.py')
        exit(0)





if __name__ == '__main__':
    main()
