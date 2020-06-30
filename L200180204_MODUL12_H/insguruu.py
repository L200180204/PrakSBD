import mysql.connector
 
con = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="sekolah"
)
 
cur = con.cursor()
sql = "INSERT INTO guruu (nig, nama, alamat) VALUES (%s, %s, %s)"
values = [
  ("200501", "Sugeng Riyadi", "Jl. Mendungan III/32 RT.005/02"),
  ("200502", "Sartono", "Jl. Hj.Muslich RT.004/01 No.18"),
  ("200503", "Nur Hidayat", "Gg. Subur Ujung No.12 RT.012/015"),
  ("200504", "Isbani", "Jl. Kampung Blimbing III/14 RT.001/09")
]
 
for val in values:
  cur.execute(sql, val)
  con.commit()
 
print("{} data berhasil ditambahkan".format(len(values)))
