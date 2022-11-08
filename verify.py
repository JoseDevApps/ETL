import pandas as pd
import numpy as np
from sqlalchemy import create_engine, MetaData, Table
# input
path = './'
filename = 'temp_T.csv'
fn = path + '/' + filename
Host = 'localhost'
Port = '4000'
User = 'postgres'
Password = 'cperv_db_solar'
DBName = 'cperv'
TableName = ''
# Process
engine = create_engine('postgresql://'+User+':'+Password+'@'+Host+':'+Port+'/'+DBName)
connection = engine.connect()
print(engine)
metadata_obj = MetaData()
table_name = 'data_oruro'
census = Table('data_oruro', metadata_obj, autoload=True, autoload_with=engine)
print(census.columns.keys())
# result_q = [elem for elem in result]
# print(result_q)
# print(result)
# for elem in result:
#     print(elem)

dr = pd.read_csv('./ResumeData.csv')
df = pd.read_csv(fn,index_col=0, parse_dates=True)
print(df.info())
# print(df)
pd.io.sql.get_schema(df, name = 'data_oruro',)
df.head(0).to_sql(name='data_oruro', con=engine, if_exists='replace')
