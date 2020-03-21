
import datetime
import pymysql

cnx = pymysql.connect(user='dev', password='ax2',host='127.0.0.1',port=3307,db='test')  

cursor = cnx.cursor()

query = ("SELECT firstname, lastname, startdate, enddate, salary FROM movieDB")


cursor.execute(query)

for (firstname, lastname, startdate, enddate, salary) in cursor:
  print("{} {} hired from {} to {} is paid: {} DKR pr month".format(firstname, lastname, startdate, enddate, salary))

cursor.close()
cnx.close()
