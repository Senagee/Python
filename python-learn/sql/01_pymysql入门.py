from pymysql import Connection

conn = Connection(
    host="localhost",
    port=3306,
    user="root",
    password="abc123"
)

print(conn.get_server_info())
conn.close()