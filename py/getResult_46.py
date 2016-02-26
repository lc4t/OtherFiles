# -*- coding:utf-8 -*-
__author__ = 'lc4t'

import requests
import urllib.request
import urllib.parse
import http.cookiejar
import xlwt
import xlrd
import re
from bs4 import BeautifulSoup



class Query:
    def __init__(self):
        pass
    def Chsi(self, ticket, name):
        ticket = str(ticket)
        name = urllib.parse.quote(name)
        url = 'http://www.chsi.com.cn/cet/query?zkzh='+ticket+'&xm='+name
        headers = {
        'Host': 'www.chsi.com.cn',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36',
        'Referer': 'http://www.chsi.com.cn/cet/',
        }
        
        request = urllib.request.Request(url,headers=headers)
        # request.set_proxy(host = '127.0.0.1:10801', type = 'http')
        result = urllib.request.urlopen(request, )
        html = BeautifulSoup(result.read()) 
        p = html.find_all(class_='cetTable')
        ans = p[0].get_text()
        return ans.replace(' ','').replace('\n','').replace('\t','').replace('\r','').replace('姓名：',' ').replace('学校：',' ').replace('考试类别：',' ').replace('准考证号：',' ').replace('考试时间：',' ').replace('总分：',' ').replace('听力：',' ').replace('阅读：',' ').replace('写作与翻译：',' ')
    def Sushe(self, ticket, name):
        ticket = str(ticket)
        # proxies = {
        #     'http': 'http://127.0.0.1:8080',
        # }
        headers = {
        # 'Host': 'www.chsi.com.cn',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36',
        'Referer': 'http://cet.99sushe.com/',
        'Origin': 'http://cet.99sushe.com',
        }
        request = requests.post('http://cet.99sushe.com/findscore',data = { 'id':ticket,'name':name.encode('GBK') }, headers = headers, cookies = {'score':''}, )#proxies = proxies)
        result = str(request.text).split(',')
        return ([name, result[0] + '级', ticket, result[4], result[1], result[2], result[3]])

class CreateXLS:
    def __init__(self, fileName, sheetName):
        self.fileName = fileName
        self.workBook = xlwt.Workbook(encoding = 'utf-8')
        self.workSheet = self.workBook.add_sheet(sheetName)
    def Copy(self,inputFile):
        data = xlrd.open_workbook(inputFile)
        table = data.sheets()[0]
        nrows = table.nrows
        ncols = table.ncols
        for i in range(0,nrows,1):
            for j in range(0,ncols,1):
                # print (table.cell(i,j).value)
                self.workSheet.write(i,j,table.cell(i,j).value)
                self.Save()

    def Copy4Query(self):
        data = xlrd.open_workbook(fromFile)
        table = data.sheets()[0]
        nrows = table.nrows
        ncols = table.ncols
        ticket = 0
        name = 0
        for i in range(0,ncols,1):
            print (table.cell(0,i).value)
            if (table.cell(0,i).value == u'准考证'):
                ticket = i
            if (table.cell(0,i).value == u'姓名'):
                name = i
        for i in range(0,nrows,1):
            self.workSheet.write(i,ticket,table.cell(i,ticket).value)
            self.workSheet.write(i,name,table.cell(i,name).value)
            self.Save()

    def Query(self,inputFile):
        f = open(inputFile,'r')
        data = f.readlines()
        q = Query()
        function = 'sushe'
        dataAns = []
        self.SaveAns_init()
        length = len(data)
        if (function == 'chsi'):
            for i in range(0,length,1):
                data[i] = data[i].replace('\n','').split()
                dataAns.append(q.Chsi(data[i][0],data[i][1]))
                ans = dataAns[i].split()
                self.SaveAns(i + 1,ans[0],ans[1],ans[2],ans[3],ans[4],ans[5],ans[6],ans[7],ans[8],data[i][2],data[i][3],data[i][4],data[i][5],)
                print (str(i+1)+'/'+str(length)+dataAns[i])
        elif (function == 'sushe'):
            for i in range(0,length,1):
                data[i] = data[i].replace('\n','').split()
                dataAns.append(q.Sushe(data[i][0],data[i][1]))
                ans = dataAns[i]
                self.SaveAns(i + 1, ans[0], ans[1], ans[2], ans[3], ans[4], ans[5], ans[6])
                print (str(i+1)+'/'+str(length)+str(dataAns[i]))
        else:
            exit(0)

    def SaveAns_init(self):
        self.workSheet.write(0,0,u'姓名')
        self.workSheet.write(0,1,u'考试类别')
        self.workSheet.write(0,2,u'准考证号')
        self.workSheet.write(0,3,u'总分')
        self.workSheet.write(0,4,u'听力')
        self.workSheet.write(0,5,u'阅读')
        self.workSheet.write(0,6,u'写作与翻译')
        self.Save()
    def SaveAns(self,index,name,exam,ticket,total,listenNumber,readNumber,writeNumber):
        self.workSheet.write(index,0,name)
        self.workSheet.write(index,1,exam)
        self.workSheet.write(index,2,ticket)
        self.workSheet.write(index,3,total)
        self.workSheet.write(index,4,listenNumber)
        self.workSheet.write(index,5,readNumber)
        self.workSheet.write(index,6,writeNumber)
        self.Save()
    def Save(self):
        self.workBook.save(self.fileName)
    def Write(self,row,column,value):
        self.workSheet.write(row,column,value)
        self.Save()



if __name__ == '__main__':
    q = CreateXLS('46_result.xls','Sheet1')
    q.Query('test.txt')
    # try:
    #     q = CreateXLS('46_result.xls','Sheet1')
    #     q.Query('test.txt')
    # except:
    #     print (u'将信息保存到txt中,每一行包含信息依次为\n准考证号 姓名 学院 年级 班级号 学号\n用至少一个空格隔开，可以从xls表格中复制出来')
    #     print(u'保存的文件名为test.txt 然后就可以再次运行了')
    #     print(u'如果上面都OK,还是报错的话,可能是需要验证码0.0')



