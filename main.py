import psycopg2
from conf import user,dbname,password,host

connection=psycopg2.connect(
    host=host,
    dbname=dbname,
    user=user,
    password=password
)
cursor=connection.cursor()
cursor.execute("SELECT * FROM book;")
versions = cursor.fetchall()
for version in versions:
    print("Результат запроса", version)
cursor.close()
connection.close()