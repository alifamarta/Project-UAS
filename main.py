from model import daftar_nilai
from view import input_nilai,view_nilai

while True:
    print("\n")
    print("\n")
    ask = input("[1] TAMBAH DATA \n[2] LIHAT DATA \n[3] UBAH DATA \n[4] CARI DATA \n[5] HAPUS DATA \n[6] KELUAR \nPILIH OPSI = ")

    if ask == '1':
        input_nilai.input_nilai()
    
    elif ask == '2':
        view_nilai.cetak_daftar_nilai()

    elif ask == '3':
        daftar_nilai.ubah_data()
    
    elif ask == '4':
        daftar_nilai.cari_data()

    elif ask == '5':
        daftar_nilai.hapus_data()
    
    elif ask == '6':
        print("TERIMA KASIH SUDAH MENGGUNAKAN PROGRAM INI")
        print("\n")
        print("        ALIF NUR FATHLII AMARTA")
        print("\n")
        print("                TI.22.A3")
        print("\n")
        exit()