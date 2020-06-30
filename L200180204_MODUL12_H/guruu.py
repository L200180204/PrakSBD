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

class guru:
    def __init__(self, master):
        self.master = master
        self.master.title("Database Guruu")
        self.master.geometry('300x300')
        self.frame = Frame(self.master)
        self.frame.grid()

        title = Label(self.frame, text="Database Guru", font=('Times', 16, 'bold'))
        l_nama = Label(self.frame, text="Nama", font=('Times', 12))
        l_nis = Label(self.frame, text="NIg", font=('Times', 12))
        l_alamat = Label(self.frame, text="Alamat", font=('Times', 12))
        
        title.grid(row=0, columnspan=4, pady=10)
        l_id.grid(row=1, column=0, sticky=W, padx=3)
        l_nama.grid(row=2, column=0, sticky=W, padx=3)
        l_nim.grid(row=3, column=0, sticky=W, padx=3)
        l_alamat.grid(row=4, column=0, sticky=W, padx=3)
        
        
        #Entry dan posisi
        self.e_id = Entry(self.frame, width=30)
        self.e_nama = Entry(self.frame, width=30)
        self.e_nim = Entry(self.frame, width=30)
        self.e_alamat = Entry(self.frame, width=30)
        
        self.e_id.grid(row=1, column=1, sticky=W, padx=10)
        self.e_nama.grid(row=2, column=1, sticky=W, padx=10)
        self.e_nim.grid(row=3, column=1, sticky=W, padx=10)
        self.e_alamat.grid(row=4, column=1, sticky=W, padx=10)

        #Button dan posisi
        b_insert = Button(self.frame, text="Insert", command=self.insert_data)
        b_update = Button(self.frame, text="Update", command=self.update_data)
        b_show = Button(self.frame, text="Show", command=self.show_data)

        b_insert.grid(row=5, column=0, pady=10, ipadx=10)
        b_update.grid(row=5, column=1, pady=10, ipadx=10)
        b_show.grid(row=7, column=1, pady=10, ipadx=10)
        
    def insert_data(self):
        c = db.cursor()
        sql =f"INSERT INTO siswa (`nama`,`nig`, `alamat`)VALUES('{self.e_nama.get()}','{self.e_nis.get()}', '{self.e_alamat.get()}')"         
        c.execute(sql)
        db.commit()
        messagebox.showinfo("","Entry Data Berhasil")
    
    def update_data(self):
        c = db.cursor()
        e1=self.e_nama.get()
        e2=self.e_nig.get()
        e3=self.e_alamat.get()
        sql =f"UPDATE guruu SET nama=%s, nig=%s WHERE alamat=%s"
        val = (e1,e2,e3,e4)
        c.execute(sql,val)
        db.commit()
        messagebox.showinfo("","Update Data Berhasil")

    def show_data(self):
        show = Tk()
        show.title("Data Guru")
        Label(show, text="Nama").grid(row=0, column=1, sticky=W)
        Label(show, text="NIG").grid(row=0, column=2, sticky=W)
        Label(show, text="Alamat").grid(row=0, column=3, sticky=W)
        

        
        sql="select*from guruu"
        c.execute(sql)
        Member = c.fetchall()

        for i in range(len(guruu)):
            for j in range(len(guruu[i])):
                teks=Entry(show)
                teks.grid(row=i+1,column=j)
                teks.insert(END,data[i][j])

            
