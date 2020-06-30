import mysql.connector
 
con = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="sekolah"
)
 
cur = con.cursor()
sql = "INSERT INTO pelajaran (kode, nama, pengajar) VALUES (%s, %s, %s)"
values = [
  ("22", "Biologi", "Sartono"),
  ("33", "Matematika", "Isbani"),
  ("44", "Sejarah", "Sugeng Riyadi"),
  ("21", "Bahasa Inggris", "Nur Hidayat")
]
 
for val in values:
  cur.execute(sql, val)
  con.commit()
 
print("{} data berhasil ditambahkan".format(len(values)))
