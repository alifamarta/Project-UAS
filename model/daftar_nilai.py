from tabulate import tabulate
from os import system

mahasiswa = {}

#fungsi tambah data
def tambah_data(nama,nim,tugas,uts,uas):
    akhir = (tugas * (30/100)) + (uts * (35/100)) + (uas * (35/100))
    mahasiswa[nama] = nama, nim, tugas, uts, uas, akhir

#fungsi ubah data
def ubah_data():
    system("cls")
    nama = input("Masukkan nama : ")
    if nama in mahasiswa.keys():
        from view.input_nilai import input_nilai
        input_nilai()
    else:
        print("DATA TIDAK DITEMUKAN")

#fungsi mencari data
def cari_data():
    system("cls")
    nama = input("Masukkan nama : ")
    if nama in mahasiswa.keys():
        from view.view_nilai import cetak_hasil_pencarian
        cetak_hasil_pencarian(nama)
        
    else:
        print("DATA TIDAK DITEMUKAN")
#fungsi menghapus data
def hapus_data():
    system("cls")
    nama = input("Masukkan nama : ")
    if nama in mahasiswa.keys():
        del mahasiswa[nama]

    else:
        print("DATA TIDAK DITEMUKAN")