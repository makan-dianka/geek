from mysql import connector

Host, User, Pwd, Db = 'localhost', 'root', '', 'gf'

gf = connector.connect(host=Host, user=User, password=Pwd, database=Db)
conn = gf.cursor()

command = "SHOW TABLES;"
conn.execute(command)

tables = conn.fetchall()

print(tables)