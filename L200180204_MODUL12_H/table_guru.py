import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="sekolah"
)

cursor = mydb.cursor()

query = """
CREATE TABLE guruu
(
    nig INT(10),
    nama VARCHAR(100),
    alamat VARCHAR(100)
)
"""

cursor.execute(query)

print("Table guruu sukses dibuat")
