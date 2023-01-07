from tabulate import tabulate
from model.daftar_nilai import mahasiswa
from os import system

def cetak_daftar_nilai():
    system("cls")
    headers = ["No","Nama","NIM","Tugas","UTS","UAS","Nilai Akhir"]
    print(tabulate([mahasiswa[i] for i in mahasiswa], headers=headers,showindex="always",tablefmt="fancy_grid"))

def cetak_hasil_pencarian(nama):
    headers = ["Nama","NIM","Tugas","UTS","UAS","Nilai Akhir"]
    print(tabulate([mahasiswa[nama]], headers=headers,tablefmt="fancy_grid"))
    print("DATA DITEMUKAN")