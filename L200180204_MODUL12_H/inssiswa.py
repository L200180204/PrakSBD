import mysql.connector
 
con = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="sekolah"
)
 
cur = con.cursor()
sql = "INSERT INTO siswa (nis, nama, alamat) VALUES (%s, %s, %s)"
values = [
  ("200500002", "Septian", "Jl. Garuda III/32 RT.005/02"),
  ("200500003", "Amalia", "Jl. Ciak RT.004/01 No.18"),
  ("200500004", "Neymar", "Gg. Subur Ujung No.12 RT.012/015"),
  ("200500005", "Vito", "Jl. Kampung Melayu Kecil III/14 RT.001/09")
]
 
for val in values:
  cur.execute(sql, val)
  con.commit()
 
print("{} data berhasil ditambahkan".format(len(values)))
