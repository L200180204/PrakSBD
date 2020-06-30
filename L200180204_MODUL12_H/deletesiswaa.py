import tkinter as tk
import tkinter.messagebox
from tkinter import*
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="sekolah"
    )

c=db.cursor()

class delete_siswa:
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        self.frame.grid()
        
        self.e_delete = Label(self.frame, text="Pilih nis")
        self.e_delete.grid(row=2, column=0, columnspan=2, pady=10, padx=10)
        self.e_nis = Entry(self.frame, width=30)
        self.e_nis.grid(row=4, column=0, columnspan=2, pady=10, padx=10)
        self.b_delete = Button(self.frame, text="Hapus", command=self.delete)
        self.b_delete.grid(row=6, column=0, columnspan=2, pady=10, padx=10)

    def delete(self):
        c=db.cursor()
        e1=self.e_id.get()
        sql = "DELETE FROM siswa WHERE nis=%s"
        val=(e1, )
        c.execute(sql, val)
        db.commit()
        messagebox.showinfo("", "Data Berhasil Dihapus")
        
