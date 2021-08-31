import sqlite3

conn = sqlite3.connect("c:/kivy/app/fdb.db")
cursor = conn.cursor()

cursor.execute("INSERT INTO db_makan(nom, prenom, age)VALUES('alex', 'ch', 18)")
conn.commit()

cursor.execute("SELECT * FROM db_makan")
print(cursor.fetchall())
conn.close 