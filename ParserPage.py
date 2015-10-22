__author__ = 'maru'
#coding=gb2312
import urllib2
import re
import mysql


class ParserPage():

    def parserPage(self,url):

        try:
            html = urllib2.urlopen(url).read().decode("GB2312")
        except UnicodeDecodeError,e:
            return
        except urllib2.URLError,e:
            print(e)
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

        return {
            "name": resName,
            "url": resURL,
            "leve1": resList[0],
            "leve2": resList[1]
        }


if __name__ == "__main__":
    index = 1
    parser = ParserPage()
    db = mysql.Mysql()
    while index < 200:
        result = parser.parserPage(url="http://v8.ccut.edu.cn/article.php?/%s" % index)
        print(result['name'])
        # name = result['name'].encode("gb2312").decode("gb2312")
        # url = result['url'].encode("gb2312").decode("gb2312")
        # leve1 = result['leve1'].encode("gb2312").decode("gb2312")
        # leve2 = result['leve2'].encode("gb2312").decode("gb2312")
        db.insertData(id=index,title="好人".encode('gb2312'),url=result['url'],leve1=result['url'],leve2=result['url'])
        index += 1

