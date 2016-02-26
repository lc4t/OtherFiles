# -*- coding:utf-8 -*-
__author__ = 'lc4t'

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
        url = 'http://cet.99sushe.com/findscore'
        headers = {
        # 'Host': 'www.chsi.com.cn',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36',
        'Referer': 'http://cet.99sushe.com/',
        'Origin': 'http://cet.99sushe.com',
        }
        request = urllib.request.Request(url,headers=headers)
        result = urllib.request.urlopen(request).read()
        print (result)
        exit(0)

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
        dataAns = []
        self.SaveAns_init()
        length = len(data)
        for i in range(0,length,1):
            data[i] = data[i].replace('\n','').split()
            dataAns.append(q.Chsi(data[i][0],data[i][1]))
            ans = dataAns[i].split()
            self.SaveAns(i + 1,ans[0],ans[1],ans[2],ans[3],ans[4],ans[5],ans[6],ans[7],ans[8],data[i][2],data[i][3],data[i][4],data[i][5],)
            print (str(i+1)+'/'+str(length)+dataAns[i])
    def SaveAns_init(self):
        self.workSheet.write(0,0,u'姓名')
        self.workSheet.write(0,1,'学校')
        self.workSheet.write(0,2,u'考试类别')
        self.workSheet.write(0,3,u'准考证号')
        self.workSheet.write(0,4,u'考试时间')
        self.workSheet.write(0,5,u'总分')
        self.workSheet.write(0,6,u'听力')
        self.workSheet.write(0,7,u'阅读')
        self.workSheet.write(0,8,u'写作与翻译')
        self.workSheet.write(0,9,u'学院')
        self.workSheet.write(0,10,u'年级')
        self.workSheet.write(0,11,u'班级')
        self.workSheet.write(0,12,u'学号')
        self.Save()
    def SaveAns(self,index,name,school,exam,ticket,data,total,number1,number2,number3,college,grade,classN,stuCode):
        self.workSheet.write(index,0,name)
        self.workSheet.write(index,1,school)
        self.workSheet.write(index,2,exam)
        self.workSheet.write(index,3,ticket)
        self.workSheet.write(index,4,data)
        self.workSheet.write(index,5,total)
        self.workSheet.write(index,6,number1)
        self.workSheet.write(index,7,number2)
        self.workSheet.write(index,8,number3)
        self.workSheet.write(index,9,college)
        self.workSheet.write(index,10,grade)
        self.workSheet.write(index,11,classN)
        self.workSheet.write(index,12,stuCode)
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



