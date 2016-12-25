import gevent
import requests
from requests.utils import dict_from_cookiejar, cookiejar_from_dict
import gevent.monkey
import re
from datetime import datetime
from optparse import OptionParser
from lxml import etree


def log(text):
    print('[%s] %s' % (str(datetime.now()), text))


class Catch:
    headers = {

    }
    r = requests.Session()
    thread = 3
    aims = []

    def login(self):
        print('在选课页面中刷新并复制Request Headers的cookie')
        cookie = input('Give me cookie [xx=xx; ...]: ')
        q = {k:v for k,v in re.findall(r'([^=]*)=([^;]*);{0,1}\s{0,1}', cookie)}
        self.r.cookies = cookiejar_from_dict(q)
        print(q)
        test = self.r.get('http://eams.uestc.edu.cn/eams/stdElectCourse.action').text
        if '进入选课>>>>' in test:
            return True
        else:
            log('Error login')
            exit()
            return False
        # open('test.html', 'w').write(test)

    def set_thread(self, thread):
        self.thread = thread
        log('set thread %d', thread)


    def select(self):
        print('接下来输入选课平台（id 课程号）数据对，以空行结束')
        print('id就是网址?electionProfile.id=815后面的815， 课程号即?lesson.id=276731后的数字')
        print('例如 (815 275115) 表示选择A1600720.26科学技术史')
        i = 1
        while(1):
            _ = input('%d:' % i)
            if _ == '':
                break
            try:
                _ = _.split()
                self.aims.append((int(_[0]), int(_[1])))
            except IndexError:
                print('input error, split with space')
                continue
            except ValueError:
                print('input id nums, only INT')
                continue

    def task(self, thread_id, s_id, c_id):
        if len(self.aims) == 0:
            return

        url = 'http://eams.uestc.edu.cn/eams/stdElectCourse!batchOperator.action?profileId=%d' % s_id
        data = {
            'operator0': '%d:true:0' % c_id,
        }
        while(1):
            log('[Thread %s] start %d-%d' % (thread_id, s_id, c_id))
            html = self.r.post(url, data=data).text
            try:
                result = etree.HTML(html).xpath('//table/tr/td/div/text()')[0]
                result = result.replace('\t', '').replace('\n', '')
                if '失败：' in result:
                    log('[Thread %s] start %d-%d result: %s' % (thread_id, s_id, c_id, result))
                    # log('' % result)
                    continue
                elif '成功' in result:
                    log('[Thread %s] start %d-%d result: %s' % (thread_id, s_id, c_id, result))
                    self.aims.remove((s_id, c_id))
                    break
                else:
                    log('[Thread %s] start %d-%d result: %s' % (thread_id, s_id, c_id, result))
                    continue
            except IndexError as e:
                log('[Thread %s] start %d-%d error: %s' % (thread_id, s_id, c_id, str(e)))
                log(html)


    def run(self):
        _ = self.aims
        threads = []
        total = 1
        for ids in _:
            for i in range(self.thread):
                threads.append(gevent.spawn(self.task, str(i) + '/' + str(total), ids[0], ids[1]))
            # threads += [gevent.spawn(self.task, str(i) + '/' + str(total), ids[0], ids[1]) for i in range(self.thread)]
                total += 1
        gevent.joinall(threads)

if __name__ == '__main__':
    gevent.monkey.patch_all()
    catch = Catch()
    parser = OptionParser()
    parser.add_option('-t', '--thread',
                      help="thread per task")
    (options, args) = parser.parse_args()
    if options.thread is not None:
        catch.set_thread(int(options.thread))
    catch.login()
    catch.select()
    catch.run()
