import psycopg2

conn=psycopg2.connect(
    database="mydb",
    user="postgres",
    password="root",
    host="localhost"
)
print("database connected successfully!")
cursor=conn.cursor()

cursor.execute("DROP TABLE IF EXISTS school")
cursor.execute('''create table school(id int primary key,
               name varchar(20),class_name varchar(20),fees int)''')
conn.commit()

data=[
    (1,'john','first',5000),
    (2,'jenny','second',6000),
    (3,'jake','third',7000),
    (4,'james','fourth',8000)
]

cursor.executemany('insert into school values(%s,%s,%s,%s)',data)
print("data inserted successfully!")

conn.commit()
cursor.close()

