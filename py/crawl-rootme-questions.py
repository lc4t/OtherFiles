from bs4 import BeautifulSoup as bs
import lxml
import re
import requests


if __name__ == '__main__':
    _ = requests
    main_list = ['App-Script', 'App-System', 'Cracking', 'Cryptanalysis',
                    'Forensic', 'Network', 'Programming', 'Realist',
                    'Web-Client', 'Steganography', 'Web-Server']

    for main_page in main_list:
        url = 'https://www.root-me.org/en/Challenges/%s/' % (main_page)
        getter = _.get(url)
        # print(html)
        html = bs(getter.text, 'lxml')
        # print(soup.prettify())
        count = int(re.findall('\s(\d+)\sChallenges', html.prettify())[0])
        print('#### %s(%d Challenges)' % (main_page, count))
        print()
        print('|No | Name | Points | Difficulty|')
        print('|-|-|-|-|')
        cnt = 0
        for tr in html.tbody.find_all('tr'):
            cnt += 1
            href = url + tr.a['href']
            title = tr.a.text
            points = int(tr.find_all('td')[3].text)
            diffculty = tr.find_all('td')[4].a['title'].split(':')[0].strip()
            print('|%d | [%s](%s)  | %d  | %s|' % (cnt, title, href, points, diffculty))

        print()
        print()
