# -*- coding: utf-8 -*-
"""
The program is used to download papers in batch.
The input data is BibTex file.
The program has two search methods:
1. search according to the title of the paper
2. search according to the DOI number of the paper
September 2022/02/15 python 3.6
"""

#pip3 install lxml  pip3 install requests

import time
import re
import requests
from lxml import etree
import sys
import os
import csv

file_path = "/Users/wht/Nutstore Files/.symlinks/坚果云/python/pythonProject/citexs1.csv"
save_path = "/Users/wht/Nutstore Files/.symlinks/坚果云/python/pythonProject/down/"


def read_csv(file_path):
    """
    读取CSV文件并返回论文信息。
    """
    papers = []
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            papers.append({
                'title': row['Title'],
                'author': row['Authors'],
                'year': row['Journal'],
                'doi': row['DOI']
            })
    return papers
print(papers)

def search_paper(artName):
    """
    Search papers
    ---------------
    Input: the name of paper
    ---------------
    Output: search results (if "" is not returned, otherwise PDF link is returned)
    """
    url = 'https://sci-hub.ru'
    # url = 'https://click.endnote.com/'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0',
               'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
               'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
               'Accept-Encoding': 'gzip, deflate, br',
               'Content-Type': 'application/x-www-form-urlencoded',
               'Content-Length': '123',
               'Origin': 'https://sci-hub.ru',
               'Connection': 'keep-alive',
               'Upgrade-Insecure-Requests': '1'}
    data = {'sci-hub-plugin-check': '',
            'request': artName}
    res = requests.post(url, headers=headers, data=data)
    html = res.text
    tree = etree.HTML(html)
    try:
        url = tree.xpath("//*[@id='buttons']/button/@onclick")
        url_d = 'https://sci-hub.ru'
        downUrl_out = url_d + url[0].split("'")[1]
        #https://sci-hub.ru/10.1007/s00122-015-2575-0
    except:
        return None
    return downUrl_out


def download_paper(downUrl_in):
    """
    Download the paper according to the paper link
    ----------------------
    Input: paper link
    ----------------------
    Output: PDF binary files
    """
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0',
               'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
               'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
               'Accept-Encoding': 'gzip, deflate, br',
               'Connection': 'keep-alive',
               'Upgrade-Insecure-Requests': '1'}
    res = requests.get(downUrl_in, headers=headers)
    return res.content

if __name__ == '__main__':
    file_path = "/Users/wht/Nutstore Files/.symlinks/坚果云/python/pythonProject/citexs1.csv"
    save_path = "/Users/wht/Nutstore Files/.symlinks/坚果云/python/pythonProject/down/"
    if not os.path.exists(save_path):
        os.makedirs(save_path)

        # Set search method, 1 for DOI, 2 for Title
    find_way = 2
    papers = read_csv(file_path)
    print("CSV contains {} papers".format(len(papers)))

    download_code = []
    for idx, paper in enumerate(papers):
        search_key = paper['doi'] if find_way == 1 else paper['title']
        print('No.{} Searching for: {}'.format(idx + 1, search_key))
        down_url = search_paper(search_key)
        if down_url is None:
            print('No.{} Not found!'.format(idx + 1))
            download_code.append(idx + 1)
        else:
            print('No.{} Paper link:{}'.format(idx + 1, down_url))
            print('Downloading...')
            pdf = download_paper(down_url)
            paper_name = "{}_{}".format(paper['author'].split(";")[0], paper['year'])
            with open('{}{}.pdf'.format(save_path, paper_name), 'wb') as f:
                f.write(pdf)
            print('---Download complete---')
        time.sleep(0.8)

    print("The papers not found are Nos.:{}".format(download_code))
    # Optionally, print titles of not found papers
    for idx in download_code:
        print("No.{}: {}".format(idx, papers[idx - 1]['title']))