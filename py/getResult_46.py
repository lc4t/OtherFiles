# -*- coding:utf-8 -*-
__author__ = 'lc4t'

import requests
import xlwt
import xlrd
import re
from bs4 import BeautifulSoup

class QuerySuper:
    def __init__(self, ticket, name):
        self.ticket = str(ticket)
        self.name = name
    def getResult(self):
        #return , should be Overrided
        ''' interface output
        [姓名', '考试类别', '准考证号', '总分', '听力', '阅读', '写作与翻译']
        '''
        pass


class QueryChsi(QuerySuper):
    def getResult(self):
        try:
            url = 'http://www.chsi.com.cn/cet/query'
            headers = {
            'Host': 'www.chsi.com.cn',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36',
            'Referer': 'http://www.chsi.com.cn/cet/',
            }
            params = { 'zkzh':self.ticket,'xm':self.name }
            request = requests.get(url, params = params, headers = headers )#proxies = proxies)
            result = request.text
            html = BeautifulSoup(result,'lxml') 
            p = html.find_all(class_='cetTable')
            ans = p[0].get_text()
            ans =  (ans.replace(' ', '').replace('\n', '').replace('\t', '').replace('\r', '').replace('姓名：', ' ').replace('学校：',' ').replace('考试类别：',' ').replace('准考证号：',' ').replace('考试时间：',' ').replace('总分：',' ').replace('听力：',' ').replace('阅读：',' ').replace('写作与翻译：',' ')).split()
            result = [self.name, ans[2], self.ticket, ans[5], ans[6], ans[7], ans[8]]
            assert len(result) == 7
            return result
        except Exception as err:
            print (err, self.name, self.ticket, 'chsi')
            return ''

class QuerySushe(QuerySuper):
    def getResult(self):
        try:
            url = 'http://cet.99sushe.com/findscore'
            headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36',
            'Referer': 'http://cet.99sushe.com/',
            'Origin': 'http://cet.99sushe.com',
            }
            data = { 'id':self.ticket,'name':self.name.encode('GBK') }
            request = requests.post(url, data = data, headers = headers, cookies = {'score':''}, )#proxies = proxies)
            result = str(request.text).split(',')
            if (result[0] == '4'):
                result[0] = '四'
            elif (result[0] == '6'):
                result[0] = '六'
            else:
                pass

            result = [self.name, '英语'+ result[0] + '级', self.ticket, result[4], result[1], result[2], result[3]]
            assert len(result) == 7
            return result
        except Exception as err:
            print ('error:', err, self.name, self.ticket, 'sushe')
            return ''

class QueryFactory:
    def __init__(self, method, ticket, name):
        if (method == 'chsi'):
            self.query =  QueryChsi(ticket, name)
        elif (method == 'sushe'):
            self.query = QuerySushe(ticket, name)
        else:
            print ('No this method')
            exit(0)        
    
    def getResult(self):
        return self.query.getResult()



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
        data = f.readlines()    #get name,ticket for lines
        self.SaveAns_init()
        length = len(data)
        lastList = []
        for i in range(0, length, 1):
            data[i] = data[i].replace('\n','').split()

            queryResult = QueryFactory('sushe', data[i][0], data[i][1]).getResult()
            if (queryResult == ''):
                queryResult = QueryFactory('chsi', data[i][0], data[i][1]).getResult()
                if (queryResult == ''):
                    lastList.append(data[i])
                    continue


            ans = queryResult
            self.SaveAns(i + 1, ans[0], ans[1], ans[2], ans[3], ans[4], ans[5], ans[6])
            print (str(i + 1) + '/' + str(length) + str(queryResult))
        if (len(lastList) > 0):
            print ('----These are not got, please redo')
            for i in lastList:
                print (i[0], i[1])


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
    print (u'将信息保存到txt中,每一行包含信息依次为\r\n\r\n准考证号 姓名\r\n\r\n用至少一个空格隔开，可以从xls表格中复制出来')
    print(u'保存的文件名为test.txt 然后就可以再次运行了')
    q = CreateXLS('46_result.xls','Sheet1')
    q.Query('test.txt')



