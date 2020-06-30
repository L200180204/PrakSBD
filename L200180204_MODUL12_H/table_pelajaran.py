import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="sekolah"
)

cursor = mydb.cursor()

query = """
CREATE TABLE pelajaran
(
    kode INT(10),
    nama VARCHAR(100),
    pengajar VARCHAR(100)
)
"""

cursor.execute(query)

print("Table pelajaran sukses dibuat")
