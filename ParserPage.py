__author__ = 'maru'
#coding=gb2312
import urllib2
import re
from BeautifulSoup import  BeautifulSoup
import mysql
import uuid



class ParserPage():

    def parserPage(self,url):

        try:
            html = urllib2.urlopen(url).read().decode("gb2312")
        except UnicodeDecodeError,e:
            print("UnicodeDecodeError:"+e)
            return
        except urllib2.URLError,e:
            print("URLError"+e)
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

        try:
            soup = BeautifulSoup(html,fromEncoding="gb2312")

            content = soup.find(color="#666666")

        except IndentationError,e:
            print(e)
        except AttributeError,e:
            print(e)

        return {
            "name": resName,
            "url": resURL,
            "leve1": resList[0],
            "leve2": resList[1],
            "time": content.contents[0]
        }

    def parserNews(self,url):
        try:
            html = urllib2.urlopen(url).read().decode("gb2312")
        except UnicodeDecodeError,e:
            print("UnicodeDecodeError:"+e)
            return
        except urllib2.URLError,e:
            print("URLError"+e)
            return

        try:
            soup = BeautifulSoup(html, fromEncoding="gb2312")
            db = mysql.Mysql()
            for content in soup.findAll(colspan='2'):
                title = content.find(target='_blank').string
                newURL = content.a["href"]
                time = content.find(color='#666666').string
                result = (title,time,newURL)
                db.insertNewsData(result)
                print(title)
        except IndentationError,e:
            print(e)
        except AttributeError,e:
            print(e)







# if __name__ == "__main__":
#     index = 21457
#     parser = ParserPage()
#     db = mysql.Mysql()
#     while index > 0:
#         try:
#             result = parser.parserPage(url="http://v8.ccut.edu.cn/article.php?/%s" % index)
#             name = result['name']
#             url = result['url']
#             leve1 = result['leve1']
#             leve2 = result['leve2']
#             time = result['time']
#             db.insertData(id=uuid.uuid1(),title=name,url=url,leve1=leve1,leve2=leve2,time=time)
#         except TypeError,e:
#             print("TypeError-----%s" % index)
#             continue
#         except Exception,e:
#             print("resultError-----%s" % index)
#             continue
#         finally:
#             index -= 1

    # while index < 2:
    #     parser.parserPage(url='http://v8.ccut.edu.cn/article.php?/21457')
    #     index += 1





