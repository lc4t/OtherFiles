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

    def __init__(self):
        gevent.monkey.patch_all()

    def login(self, session=None):
        if not session:
            print('在选课页面中刷新并复制Request Headers的cookie')
            cookie = input('Give me cookie [xx=xx; ...]: ')
        else:
            cookie = 'JSESSIONID=%s' % session
        q = {k:v for k,v in re.findall(r'([^=]*)=([^;]*);{0,1}\s{0,1}', cookie)}
        self.r.cookies = cookiejar_from_dict(q)
        print(q)
        test = self.r.get('http://eams.uestc.edu.cn/eams/stdElectCourse.action').text
        if '进入选课>>>>' in test:
            return True
        elif '未到选课时间' in test:
            log('未到选课时间')
            # exit()
            return False
        else:
            log('Error login')
            exit()
            return False

    def set_thread(self, thread):
        self.thread = thread
        log('set thread %d', thread)


    def select(self, li_str=None):
        if not li_str:
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
        else:
            try:
                _ = li_str.split(',')
                for i in _:
                    temp = i.split(':')
                    self.aims.append((int(temp[0]), int(temp[1])))
            except IndexError:
                print('input error, split with space')
            except ValueError:
                print('input id nums, only INT')

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
            except IndexError as e:
                try:
                    result = etree.HTML(html).xpath('//h2/text()')[0]
                except IndexError as e2:
                    log('[Thread %s] start %d-%d error: %s' % (thread_id, s_id, c_id, str(e2)))
                    log(html)
                    result = html
            except Exception as e:
                log('[Thread %s] start %d-%d error: %s' % (thread_id, s_id, c_id, str(e)))
                log(html)
                result = html

            result = result.replace('\t', '').replace('\n', '')
            if '失败：' in result:
                log('[Thread %s] start %d-%d result: %s' % (thread_id, s_id, c_id, result))
                continue
            elif '成功' in result:
                log('[Thread %s] start %d-%d result: %s' % (thread_id, s_id, c_id, result))
                self.aims.remove((s_id, c_id))
                break
            elif '在未到选课时间' in result:
                log('[Thread %s] start %d-%d result: %s' % (thread_id, s_id, c_id, result))
                continue
            else:
                log('[Thread %s] start %d-%d result: %s' % (thread_id, s_id, c_id, result))
                continue



    def run(self):
        _ = self.aims
        threads = []
        total = 1
        for ids in _:
            for i in range(self.thread):
                threads.append(gevent.spawn(self.task, str(i) + '/' + str(total), ids[0], ids[1]))
                total += 1
        gevent.joinall(threads)

if __name__ == '__main__':
    catch = Catch()
    parser = OptionParser()
    parser.add_option('-t', '--thread',
                      help="thread per task")
    parser.add_option('-l', '--list',
                      help="s1:c1,s2:c2,...")
    parser.add_option('-s', '--session',
                      help="value")

    (options, args) = parser.parse_args()
    if options.thread is not None:
        catch.set_thread(int(options.thread))
    if options.session is not None:
        catch.login(options.session)
    else:
        catch.login()
    if options.list is not None:
        catch.select(options.list)
    else:
        catch.select()

    catch.run()
