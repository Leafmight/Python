import datetime
import pymysql

cnx = pymysql.connect(user='dev', password='ax2',host='127.0.0.1',port=3307,db='test')  

cursor = cnx.cursor()

query = ("SELECT firstname, lastname, startdate, enddate, salary FROM pythondemo WHERE startdate BETWEEN %s AND %s")

hire_start = datetime.date(1960, 1, 1)
hire_end = datetime.date(2004, 12, 31)

cursor.execute(query, (hire_start, hire_end))

for (firstname, lastname, startdate, enddate, salary) in cursor:
    print("{} {} hired from {} to {} is paid: {} DKR pr month".format(firstname, lastname, startdate, enddate, salary))

cursor.close()
cnx.close()

# insert, update, delete
from __future__ import print_function

from decimal import Decimal
from datetime import datetime, date, timedelta

# Connect with the MySQL Server
cnx = pymysql.connect(user='dev', password='ax2',host='127.0.0.1',port=3307,db='test')  
cursor = cnx.cursor()

curA = cnx.cursor()
curB = cnx.cursor()

# Query to get employees who joined in a period defined by two dates
query = ("SELECT id, salary FROM pythondemo WHERE enddate IS NULL")

# UPDATE and INSERT statements for the old and new salary
update_old_salary = (
  "UPDATE pythondemo SET salary = %s "
  "WHERE id = %s")

# Select the employees getting a raise (all that are still employed)
curA.execute(query)

# Iterate through the result of curA
for (id, salary) in curA:
  # Update the old and insert the new salary
  new_salary = int(round(Decimal(salary) * Decimal('1.15')))
  curB.execute(update_old_salary, (new_salary, id))
  # Commit the changes
  cnx.commit()
cursor.close()
curA.close()
curB.close()
cnx.close()