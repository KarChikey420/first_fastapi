import psycopg2

conn=psycopg2.connect(
    host="localhost",
    user="postgres",
    database="mydb",
    password="root"
)
print("Database connected successfully")
cur=conn.cursor()

cur.execute("select * from student")
print(cur.fetchall())