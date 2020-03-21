# dataframe to table
import pandas as pd 
import pymysql
from sqlalchemy import create_engine #sqlalchemy helped convert strings to dates seamlessly

#cnx = pymysql.connect(user='dev', password='ax2',host='127.0.0.1',port=3307,db='test') 
con_str = 'mysql+pymysql://dev:ax2@localhost:3307/test'
engine = create_engine(con_str)

df = pd.DataFrame({'make' : ['vw,audi,citroen'],
                  'model':['up','a6','c3'],
                  'year':['2018,2011,2019'],
                  'price':['123000','85000','143000']})
#df = df.applymap(str)
df.to_sql('cars',con=engine, if_exists='append', index = False)
print(df.dtypes)