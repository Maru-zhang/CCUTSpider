__author__ = 'Maru'
#coding=utf8
import urllib2
import json
import MySQLdb



host = '10.73.5.55'
port = 3306
user = 'root'
pwd = '312'

conn = MySQLdb.connect(host=host,user=user,passwd=pwd,db='yinner',port=port)
conn.set_character_set('utf8')
cur = conn.cursor()

api = 'http://api.peiyinxiu.com/v3.0/SourceDetail?appkey=3e8622117aee570a&v=4.2.38&sign=d76a36d732459ca7b014fc251211b2c5&uid=0&token=0&svuid=10261&coo_id=&fid=0&svid=976'
data = urllib2.urlopen(url=api).read().decode("utf-8")

d1 = json.loads(data)['data']

sql = 'insert into yinner.Matter values("%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s")' % (d1['audio_count'],d1['audio_id'],d1['audio_url'],d1['from'],d1['gender'],d1['img_url'],d1['srt_count'],d1['srt_id'],d1['srt_url'],d1['title'],d1['video_time'],d1['video_url'])


try:
    cur.execute(sql.encode('utf8'))
    conn.commit()
except MySQLdb.Error,e:
    print(e)
