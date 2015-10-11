__author__ = 'maru'
#coding=gb2312
import urllib2
import re

def parserPage(url):
    
    try:
        html = urllib2.urlopen(url).read().decode("gb2312")
    except UnicodeDecodeError,e:
        return
    except UnicodeDecodeError,e:
        return

    patName = re.compile(r'<font class=bigfont><b>(.*)</b>')
    patURL = re.compile(r'href="(.*\.rmvb|.*\.mp4)"')
    patList = re.compile(r'<a href="http://v8\.ccut\.edu\.cn/sort\.php\?/\d*">(.*?)</a>')

    try:
        resName = re.findall(patName,html)[0]
        resURL = re.findall(patURL,html)[0]
        resList = re.findall(patList,html)
    except IndexError,e:
        return

    print("Name:" + resName)
    print("URL:" + resURL)
    for tag in resList:
        print("tag:" + tag)


if __name__ == "__main__":
    index = 130
    while index < 1000: 
        parserPage("http://v8.ccut.edu.cn/article.php?/%s" % index)
        index = index + 1
	print index
