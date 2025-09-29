import psycopg2

conn=psycopg2.connect(
    database="mydb",
    password="root",
    user="postgres",
    host="localhost"
)

print("database connected")

cur=conn.cursor()
cur.execute("select name from student where class='class 10';")
print(cur.fetchall())