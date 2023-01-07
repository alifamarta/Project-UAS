from model import daftar_nilai
from os import system

def input_nilai():
    system("cls")
    nama = input("Masukkan nama : ")
    nim = input("Masukkan NIM : ")
    tugas = int(input("Nilai Tugas : "))
    uts = int(input("Nilai UTS : "))
    uas = int(input("Nilai UAS : "))

    daftar_nilai.tambah_data(nama, nim, tugas, uts, uas)