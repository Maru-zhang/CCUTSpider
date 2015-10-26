__author__ = 'Maru'
#coding=gb2312
import MySQLdb

class Mysql:

    host = 'localhost'
    port = 3306
    user = 'root'
    pwd = ''

    def __init__(self):
        self.conn = MySQLdb.connect(host=self.host,user=self.user,passwd=self.pwd,db='sy_video',port=self.port,charset='gb2312')
        self.conn.set_character_set('gb2312')
        self.cur = self.conn.cursor()


    def queryAllData(self):
        try:
            sql = 'select * from FreeVideo'
            self.cur.execute(sql)
        except MySQLdb.Error,e:
            print "Mysql Error %d: %s" % (e.args[0], e.args[1])

    def insertData(self,id,title,url,leve1,leve2):
        try:
            sql = 'insert into FreeVideo values(%d,"%s","%s","%s","%s")' % (id,title,url,leve1,leve2)
            print(sql)
            self.cur.execute(sql)
            self.conn.commit()
        except MySQLdb.Error,e:
            print "Mysql Error %d: %s" % (e.args[0], e.args[1])


