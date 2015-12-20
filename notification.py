#encoding: utf-8

import MySQLdb
from pprint import pprint

host = "localhost"
user = "root"
passwd = "1qazxsw2"
port = 3306
database = "ssc"

conn=MySQLdb.connect(host=host,user=user,passwd=passwd,db=database,port=port,charset='utf8')

cur=conn.cursor()
statement = "select * from cqssc;"
print cur.execute(statement)
result = cur.fetchone()
pprint(result)
result = cur.fetchone()
pprint(result)
cur.close()
conn.commit()

