
import datetime
import pymysql

cnx = pymysql.connect(user='dev', password='ax2',host='127.0.0.1',port=3307,db='startcode_test')  

cursor = cnx.cursor()

query = ("SELECT info, name, year FROM movieDB")


cursor.execute(query)

for (info, name, year) in cursor:
  print("info {} name {} year {}".format(info, name, year))

cursor.close()
cnx.close()
