import psycopg2
from conf import user,dbname,password,host

connection=psycopg2.connect(
    host=host,
    dbname=dbname,
    user=user,
    password=password
)
cursor=connection.cursor()
print("hello word")
connection.close()