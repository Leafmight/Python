import datetime
import pymysql

cnx = pymysql.connect(user='dev', password='ax2',host='127.0.0.1',port=3307,db='startcode_test')  

cursor = cnx.cursor()

query = ("SELECT id, info, name, year FROM movieDB")

# hire_start = datetime.date(1960, 1, 1)
# # hire_end = datetime.date(2004, 12, 31)

cursor.execute(query

for (id, info, name, year) in cursor:
  print("{} {} hired from {} to {} is paid: {} DKR pr month".format(firstname, lastname, startdate, enddate, salary))

cursor.close()
cnx.close()