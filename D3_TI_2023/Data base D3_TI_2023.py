#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import mysql.connector

dataBase = mysql.connector.connect(
    host ="localhost",
    user ="root",
    passwd =""
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE D3_TI_2023")


# In[ ]:


import mysql.connector

dataBase = mysql.connector.connect(
    host ="localhost",
    user ="root",
    passwd ="",
    database = "D3_TI_2023"
)

cursorObject = dataBase.cursor()

studentRecord = """CREATE TABLE Mata_Kuliah (
                    Kode_MK VARCHAR(10) PRIMARY KEY,
                    Nama_MK VARCHAR(50),
                    Waktu DATE,
                    Ruangan VARCHAR(10)
                    );
                    CREATE TABLE Mahasiswa (
                    NIM VARCHAR(10) PRIMARY KEY,
                    Nama VARCHAR(30),
                    Alamat VARCHAR(255),
                    Mata_Kuliah_Ikut VARCHAR(10),
                    FOREIGN KEY (Mata_Kuliah_Ikut) REFERENCES Mata_Kuliah(Kode_MK)
                    );
                    CREATE TABLE DOSEN (
                    NIP VARCHAR(20) PRIMARY KEY,
                    Nama_Dosen VARCHAR(50),
                    Mata_Kuliah_Ajar VARCHAR(10),
                    FOREIGN KEY (Mata_Kuliah_Ajar) REFERENCES Mata_Kuliah(Kode_MK)
                    );"""

cursorObject.execute(studentRecord)

dataBase.close()


# In[ ]:


import mysql.connector

dataBase = mysql.connector.connect(
    host ="localhost",
    user ="root",
    passwd ="",
    database = "D3_TI_2023"
)

cursorObject = dataBase.cursor()

sql = "INSERT INTO Mata_Kuliah (Kode_MK, Nama_MK, Waktu, Ruangan)VALUES (%s, %s, %s, %s)"
val = [('MK_001', 'Basis Data', '2023-04-10 08:00:00', 'L1R1'),
        ('MK_002', 'Algoritma', '2023-04-11 13:00:00', 'L1R2'),
        ('MK_003', 'Mikrokontroler', '2023-04-12 10:00:00', 'L1R3'),
        ('MK_004', 'Cloud computing', '2023-04-13 15:00:00', 'L2R1'),
        ('MK_005', 'kewirausahaan', '2023-04-14 08:00:00', 'L2R2')
      ]

cursorObject.executemany(sql, val)
dataBase.commit()

dataBase.close()


# In[ ]:


import mysql.connector

dataBase = mysql.connector.connect(
    host ="localhost",
    user ="root",
    passwd ="",
    database = "D3_TI_2023"
)

cursorObject = dataBase.cursor()

sql = "INSERT INTO Mahasiswa (NIM, Nama, Alamat, Mata_Kuliah_Ikut)VALUES (%s, %s, %s, %s)"
val = [('1111001', 'Deswinta Faadhilah', 'Magetan', 'MK_001'),
        ('1111002', 'Diana Lathifa', 'Mejayan', 'MK_001'),
        ('1111003', 'Azzahra Kareena', 'Pilangkenceng', 'MK_003'),
        ('1111004', 'Bimo Adji', 'Madiun', 'MK_002'),
        ('1111005', 'Fernando Djaka', 'Saradan', 'MK_004')
      ]

cursorObject.executemany(sql, val)
dataBase.commit()

dataBase.close()


# In[1]:


import mysql.connector

dataBase = mysql.connector.connect(
    host ="localhost",
    user ="root",
    passwd ="",
    database = "D3_TI_2023"
)

cursorObject = dataBase.cursor()

sql = "INSERT INTO Dosen (NIP, Nama_Dosen, Mata_Kuliah_Ajar)VALUES (%s, %s, %s)"
val = [('1122001', 'Masbahah S.Pd M.Pd', 'MK_001'),
        ('1122002', 'Yusuf Fadlila S.Kom M.Kom', 'MK_002'),
        ('1122003', 'Fendi Aji Purnomo S.Si M.Eg', 'MK_003'),
        ('1122004', 'Nur Azizul S.kom M.Kom', 'MK_004'),
        ('1122005', 'Darmawan S.kom M.Kom', 'MK_005')
      ]

cursorObject.executemany(sql, val)
dataBase.commit()

dataBase.close()


# In[2]:


import mysql.connector

dataBase= mysql.connector.connect(
    host = 'localhost',
    user= 'root',
    password = '',
    database = "D3_TI_2023"
)

cursorObject = dataBase.cursor()

# Query untuk menampilkan data mata kuliah yang diikuti oleh mahasiswa beserta dosen yang mengajar
query = "SELECT Mahasiswa.NIM, Mahasiswa.Nama AS Nama_Mahasiswa, Mata_Kuliah.Nama_MK AS Mata_Kuliah, Dosen.Nama_Dosen          FROM Mahasiswa          INNER JOIN Mata_Kuliah ON Mahasiswa.Mata_Kuliah_Ikut = Mata_Kuliah.Kode_MK          INNER JOIN Dosen ON Dosen.Mata_Kuliah_Ajar = Dosen.Mata_Kuliah_Ajar"

# Mengeksekusi query
cursorObject.execute(query)

# Menampilkan data
for data in cursorObject.fetchall():
    print("NIM        : ", data[0])
    print("Mahasiswa  : ", data[1])
    print("Mata Kuliah: ", data[2])
    print("Dosen      : ", data[3])
    print()
    
# Menutup koneksi ke database
db.close()


# In[ ]:




