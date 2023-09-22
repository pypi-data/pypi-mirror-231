from database import Database
from prefect_gcp.secret_manager import GcpSecret
import psycopg2.extras as extras
import pandas as pd
from prefect.filesystems import GCS

gcs_block = GCS.load("bohr-prefect")

host = GcpSecret.load("research-host").read_secret().decode('utf-8')
user = GcpSecret.load("research-user").read_secret().decode('utf-8')
pwd = GcpSecret.load("research-pwd").read_secret().decode('utf-8')
port = GcpSecret.load("research-port").read_secret().decode('utf-8')
db= GcpSecret.load("research-db").read_secret().decode('utf-8')


db = Database(user,pwd,host,port,db,multiple=True)

# sql="select * from clients.peak_period"
# df = db.get_sql(sql)
# df.to_csv('pp.csv')
# print(df)

df = pd.read_csv('pp.csv', index_col=0)
df=df.head(7)
del(df['id'])
print(df)

onConflict='ON CONFLICT ON CONSTRAINT key_test_table DO NOTHING'
onConflict='ON CONFLICT ON CONSTRAINT key_test_table DO UPDATE SET pp1=excluded.pp1,pp2=excluded.pp2,country=excluded.country'
db.insert('clients.test_table',df,onConflict=onConflict)

sql="select * from clients.test_table"
df = db.get_sql(sql)
print(df)