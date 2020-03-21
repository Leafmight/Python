# with the build in dict cursor
import datetime
import pymysql
cnx = pymysql.connect(user='dev', password='ax2',host='127.0.0.1',port=3307,db='test') 

cursor = cnx.cursor(pymysql.cursors.DictCursor) 

query = ("SELECT firstname, lastname, startdate, enddate, salary FROM pythondemo")

cursor.execute(query)
cursor.fetchall()