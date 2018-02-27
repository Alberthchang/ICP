#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:57.0) Gecko/20100101 Firefox/57.0'
}


def main():
    start = time.time()
    for page in range(1, 3, 1):
        now = time.time()
        url = 'http://www.icpcha.net/newlist.php?page=' + str(page)
        print('Url : %s   elapse %ds' % (url, int(now - start)))
        try:
            resp = requests.get(url, timeout=5)
            content = resp.content.decode('utf-8')

            soup = BeautifulSoup(content, 'lxml')
            data = soup.select('body > div.wrap > table.seo > tr')

            with open('test.txt', 'a+') as fw:
                for line in data[1:-1]:
                    td_list = line.find_all('td')
                    unit = td_list[0].text.strip()
                    kind = td_list[1].text.strip()
                    icp = td_list[2].text.strip()
                    site_name = td_list[3].text.strip()
                    site_url = td_list[4].text.strip()
                    pass_time = td_list[5].text.strip()
                    icp_info = unit + ' | ' + kind + ' | ' + icp + ' | ' + site_name + ' | ' + site_url + ' | ' + pass_time

                    fw.write(icp_info + '\n')

            time.sleep(5)
        except:
            pass


if __name__ == '__main__':
    main()

