#! /usr/bin/python3
#-*- coding:utf-8 -*-

from optparse import OptionParser
from openpyxl import load_workbook
import requests
import lxml
import re
from bs4 import BeautifulSoup as bs
from datetime import datetime
def log(text):
    print ("[%s] %s" % (str(datetime.now()), text))

def download(url, filename, filepath):
    log('visit: %s' % (url))
    html = requests.get(url)
    if html.status_code != 200:
        log('%s return %d, failed' % (filename, html.status_code))
        return False
    else:
        open(filepath + '/' + filename, 'wb').write(html.content)
        log('%s ok..' % (filename))
        return True

def xlsx_handler(input_file, output_file, filename, url, prefix, postfix):
    log('loading %s...' % (input_file))
    xlsx = load_workbook(filename = input_file, data_only=True)['46']
    log('loadding %s success' % (input_file))
    filename = filename.split(',')

    row = 1
    while True:
        try:
            one_filename = ''.join([str(xlsx[cell].value) for cell in [i + str(row) for i in filename]]) + str(postfix)
        except TypeError as e:
            log('row:%d is None, exit' % (row))
            exit(0)
        one_url = prefix + '/' + xlsx[url+str(row)].value
        download(one_url, one_filename, output_file)
        row += 1

def info_handle(start, output_file, prefix):
    i = start - 1
    while True:
        i += 1
        one = bs(requests.get('%s%d' % (prefix, i)).content.decode('gb18030'), 'lxml')
        try: 
            if one.img['src']:
                print ('%d,%s' % (i, one.img['src']), end='')
                open(output_file,'a').write('%d,%s,' % (i, one.img['src']))
        except TypeError as e:
            log('%d %s' % (i, str(e)))
            continue
        table = one.findAll('table')[0]  
        for tr in table.findAll('tr'):
            for td in tr.findAll('td'):
                text = td.get_text().replace(' ', '').replace('\n', '').replace('\r','').replace('的个人资料', '')
                if re.findall('学生信息',text):
                    continue  
                elif text == '返回列表':
                    continue
                elif text == '用户':
                    continue
                elif text == '密码':
                    continue
                elif text == '姓名':
                    continue
                elif text == '性别':
                    continue
                elif text == '学号':
                    continue
                elif text == '班级':
                    continue
                elif text == '证件类型':
                    continue
                elif text == '证件号码':
                    continue
                elif text == '学历':
                    continue
                elif text == '专业':
                    continue
                elif text == '所在学院':
                    continue
                elif text == '照片名称':
                    continue
                elif text == '入学年份':
                    continue
                elif re.findall('操作',text):
                    continue
                elif text == '删除修改':
                    continue
                elif text == '照片名称':
                    continue
                elif text == '':
                    continue
                elif text == '\n':
                    continue
                elif text == ' ':
                    continue
                elif text == b'\xc2\xa0'.decode():
                    pass
                elif text == b'\xe3\x80\x80'.decode():
                    pass
                else: 
                    print (text, end=',')
                    open(output_file,'a').write(text + ',')

        print ('')
        open(output_file,'a').write('\n')
        # exit(0)
def main():
    usage = "usage: %prog [options] arg"
    parser = OptionParser()
    parser.add_option('-m', '--method', help='info(start, output, prefix) OR pic(input, output, filename, url, prefix, postfix)')
    parser.add_option('-o', '--output', help='output dir path')
    parser.add_option('-i', '--input', help='input file path')
    parser.add_option('-f', '--filename', help='filename ROWs up char, split with \',\'')
    parser.add_option('-u', '--url', help='url ROW up char')
    parser.add_option('-p', '--prefix', help='prefix+url is final url')
    parser.add_option('-e', '--postfix', help='filename+postfix is final to save')
    parser.add_option('-s', '--start', help='start offset')
    (options, args) = parser.parse_args()
    if options.method == 'pic':
        if options.output == None:
            parser.print_help()
            log('No output path')
            exit()
        elif options.input == None:
            parser.print_help()
            log('No inpput file')
            exit()
        elif options.filename == None:
            parser.print_help()
            log('No filemane search row')
            exit()
        elif options.url == None:
            parser.print_help()
            log('No url search row')
            exit()
        elif options.prefix == None:
            parser.print_help()
            log('No prefix')
            exit()
        elif options.postfix == None:
            log('No postfix type string,default None')
        else:
            xlsx_handler(options.input, options.output, options.filename, options.url, options.prefix, options.postfix)
    elif options.method == 'info':
        if options.output == None:
            parser.print_help()
            log('No output path')
            exit()
        elif options.start == None:
            parser.print_help()
            log('Need start offset')
            exit()
        elif options.prefix == None:
            parser.print_help()
            log('No prefix')
            exit()
        else:
            info_handle(int(options.start), options.output, options.prefix)
    else:
        parser.print_help()
        exit()

if __name__ == '__main__':
    main()