__author__ = 'maru'
import urllib2
import re

def parserPage(url):
    html = urllib2.urlopen(url).read().decode("gb2312")

    patName = re.compile(r'<font class=bigfont><b>(.*)</b>')
    patURL = re.compile(r'href="(.*\.rmvb|.*\.mp4)"')
    patList = re.compile(r'<a href="http://v8\.ccut\.edu\.cn/sort\.php\?/\d*">(.*?)</a>')

    resName = re.findall(patName,html)[0]
    resURL = re.findall(patURL,html)[0]
    resList = re.findall(patList,html)

    print("Name:" + resName)
    print("URL:" + resURL)
    for tag in resList:
        print("tag:" + tag)


if __name__ == "__main__":
    parserPage("http://v8.ccut.edu.cn/article.php?/21300")