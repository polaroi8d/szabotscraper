#!/usr/bin/env python

from __future__ import print_function
from bs4 import BeautifulSoup
import argparse
import mechanize
import sys
reload(sys)
sys.setdefaultencoding('utf-8')  # use utf-8 encoding

URL = 'http://www.math.u-szeged.hu/~szbtmsz/kalkulus/quiz.php'


def argument_parse():
    parser = argparse.ArgumentParser(description="SzaboT Scrapper 1.0")
    parser.add_argument("eha", action="store", nargs="?", default="ABCDEFG.SZE", help="type your EHA code (required)")
    args = parser.parse_args()

    return args

def parse_table(soup):
    data = []
    table = soup.find('table')
    table_body = soup.find('tbody')
    rows = table_body.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols if ele])
    return data

def main():
    br = mechanize.Browser()
    br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US;      rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
    br.open(URL)
    br._factory.is_html = True

    def select_form(form):
        return form.attrs.get('action', None) == 'quiz.php'

    br.select_form(predicate=select_form)
    args = argument_parse()

    br.form.set_all_readonly(False)
    br.form['eha'] = args.eha
    br.submit()

    response = br.response()
    soup = BeautifulSoup(response, 'html5lib')

    data = parse_table(soup)

    sum_points = 0
    cnt = 0
    for i in range(len(data)):
        if cnt == 11:  # stop after 11th test
            break
        if data[i][1] != '-':
            sum_points += int(data[i][1])

        cnt += 1
        print(*data[i], sep='')

    print('Total points: %d' % (sum_points))


if __name__ == "__main__":
    main()
