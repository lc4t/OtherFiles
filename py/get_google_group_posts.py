#! /bin/python3
# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup as BS
import lxml
import requests
from optparse import OptionParser
from datetime import datetime
import json
def log(message):
    print ('%s: %s' % (str(datetime.now()), message))

class get_google_group_posts:
    def __init__(self, googlegroup_name, filename = None):
        posts_list = self.get_posts_list(googlegroup_name)
        for i in range(0, len(posts_list), 1):
            log('process: %d/%d' % (i + 1, len(posts_list)))
            posts_list[i] = self.add_subject_content(posts_list[i])
        self.output(posts_list, filename)

    def get_posts_list(self, googlegroup_name):
        posts_list = []
        leftURL = 'https://groups.google.com/forum/?_escaped_fragment_=forum/' + googlegroup_name #[1-100]
        for i in range(1, 999999, 100):
            offset = '[' + str(i) + '-' + str(i + 99) + ']'
            now_posts_list = BS(requests.get(leftURL + offset).text, 'lxml').findAll('tr')
            log('get ' + str(len(now_posts_list)) + ' from ' + leftURL + offset)
            if len(now_posts_list) <= 0:
                break
            for one in now_posts_list:
                subject = {}
                subject.update({'subject_href':one.select('.subject')[0].a['href']})
                subject.update({'subject_title':one.select('.subject')[0].a['title']})
                subject.update({'subject_author': one.select('.author')[0].text})
                subject.update({'last_post_date': one.select('.lastPostDate')[0].text})
                subject.update({'content': []})
                posts_list.append(subject)
        log('get ' + str(len(posts_list)) + ' posts')
        return posts_list

    def add_subject_content(self, subject):
        log('follow into: ' + subject['subject_href'])
        for one in BS(requests.get(subject['subject_href'].replace('https://groups.google.com/d/', 'https://groups.google.com/forum/?_escaped_fragment_=')).text, 'lxml').findAll('tr'):
            floor = {}
            if one.select('.subject') and one.select('.author') and one.select('.lastPostDate') and one.select('.snippet'):
                floor.update({'subject':one.select('.subject')[0].a['href']})
                floor.update({'title':one.select('.subject')[0].a['title']})
                floor.update({'author':one.select('.author')[0].text})
                floor.update({'last_post_date':one.select('.lastPostDate')[0].text})
                floor.update({'snippet':one.select('.snippet')[0].text})
                subject['content'].append(floor)
        log('done: ' + subject['subject_href'])
        return subject

    def output(self, jsons, filename = None):
        try:
            open(filename, 'w+').write(json.dumps({'get':jsons}, ensure_ascii=False))
            log('write file success, done')
        except Exception as e:
            print (jsons)
            log('cannot write to file because %s, print it done' % (str(e)))


def main():
    usage = "usage: %prog [options] arg"
    parser = OptionParser()
    parser.add_option('-g', '--groupname', help = 'groupname, like "homotopytypetheory"')
    parser.add_option('-o', '--output', help = 'output to file, if not set will print all:)')
    (options, args) = parser.parse_args()
    if (options.groupname == None):
        parser.print_help()
        exit(0)
    crawler = get_google_group_posts(options.groupname, options.output)

if __name__ == '__main__':
    main()
