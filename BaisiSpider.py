# http://www.budejie.com/video/ Spider v1.0
# Author: Jiawei Zhong

import urllib.request
import re
import os


isSinglePage = input("Are you downloading in single page ? (Y/N): ")
dirName = "budejie"


def getVideoSinglePage(i):
    print("Downloading video from page %s" % i)
    req = urllib.request.Request('http://www.budejie.com/video/%i' % i)
    req.add_header('User-Agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36')
    html = urllib.request.urlopen(req).read().decode('utf-8')
    reg = r'data-mp4="(.*?)"'

    for i in re.findall(reg, html):
        filename = i.split("/")[-1]
        print("Downloading video %s ..." % filename)
        urllib.request.urlretrieve(i, "budejie/%s" % filename)


if not os.path.exists(dirName):
    os.mkdir(dirName)
    print("Directory ", dirName,  " Created ")
else:
    print("Directory ", dirName,  " already exists")

if isSinglePage == "Y" or isSinglePage == "y":
    pageNum = input("Please input the page number you want to download: ")
    getVideoSinglePage(int(pageNum))
else:
    pageStart = input("Please input the page number you want to start: ")
    pageEnd = input("Please input the page number you want to end: ")
    for i in range(int(pageStart), int(pageEnd)):
        getVideoSinglePage(i)