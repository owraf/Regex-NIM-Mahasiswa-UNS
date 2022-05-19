import pandas as pd
import re

def InputDataMahasiswa():
    #mendefinisikan sebagai datamahasiswauns
    def datamahasiswauns ():
        #input data mahasiswa
        nama_mhs = input('Silakan Masukkan Nama Lengkap Anda : ').upper()
        nim_mhs = input('Silakan Masukkan NIM Anda : ').upper()

        #membuat pola untuk NIM 
        nim_pattern = re.compile(r'(\w{1})(\d{2})(\d{2})(\d{3})')
        results = re.search(nim_pattern,nim_mhs)
        #mengelompokkan data (fakultas dan program studi) berdasarkan kode dalam NIM
        while True:
            if results.group(1) in ['M','m']:
                fakultas = 'FMIPA'
                while True:
                    if results.group(2) in '01':
                        prodi = 'S1 MATEMATIKA'
                        break
                    elif results.group(2) in '02':
                        prodi = 'S1 FISIKA'
                        break
                    elif results.group(2) in '03':
                        prodi = 'S1 KIMIA'
                        break
                    elif results.group(2) in '04':
                        prodi = 'S1 BIOLOGI'
                        break
                    elif results.group(2) in '05':
                        prodi = 'S1 INFORMATIKA'
                        break
                    elif results.group(2) in '06':
                        prodi = 'S1 FARMASI'
                        break
                    elif results.group(2) in '07':
                        prodi = 'S1 STATISTIKA'
                        break
                    elif results.group(2) in '08':
                        prodi = 'S1 ILMU LINGKUNGAN'
                        break
                    else:
                        print('Kode prodi anda salah, Silakan masukkan kembali')
                        break
                break
            elif results.group(1) in ['F','f']:
                fakultas = 'FEB'
                while True:
                    if results.group(2) in '01':
                        prodi = 'S1 MANAJEMEN'
                        break
                    elif results.group(2) in '02':
                        prodi = 'S1 AKUNTANSI'
                        break
                    elif results.group(2) in '03':
                        prodi = 'S1 EKONOMI PEMBANGUNAN'
                        break
                    else:
                        print('Kode prodi anda salah, Silakan masukkan kembali')
                        break
                break
            elif results.group(1) in ['C','c']:
                fakultas = 'FSRD'
                while True:
                    if results.group(2) in '01':
                        prodi = 'S1 SENI RUPA MUNRI'
                        break
                    elif results.group(2) in '02':
                        prodi = 'S1 DESAIN KOMUNIKASI VISUAL'
                        break
                    elif results.group(2) in '03':
                        prodi = 'S1 DESAIN INTERIOR'
                        break
                    elif results.group(2) in '04':
                        prodi = 'S1 KRIYA SENI'
                        break
                    else:
                        print('Kode prodi anda salah, Silakan masukkan kembali')
                        break
                break
            elif results.group(1) in ['D','d']:
                fakultas = 'FISIP'
                while True:
                    if results.group(2) in '01':
                        prodi = 'S1 ILMU ADMINISTRASI NEGARA'
                        break
                    elif results.group(2) in '02':
                        prodi = 'S1 ILMU KOMUNIKASI'
                        break
                    elif results.group(2) in '03':
                        prodi = 'S1 SOSIOLOGI'
                        break
                    elif results.group(2) in '04':
                        prodi = 'S1 HUBUNGAN INTERNASIONAL'
                        break
                    else:
                        print('Kode prodi anda salah, Silakan masukkan kembali')
                        break
                break
            elif results.group(1) in ['E','e']:
                fakultas = 'FH'
                while True:
                    if results.group(2) in '01':
                        prodi = 'S1 ILMU HUKUM'
                        break
                    else:
                        print('Kode prodi anda salah, Silakan masukkan kembali')
                        break
                break
            elif results.group(1) in ['G','g','R','r']:
                fakultas = 'FK'
                while True:
                    if results.group(2) in '01':
                        prodi = 'S1 KEDOKTERAN'
                        break
                    elif results.group(2) in '02':
                        prodi = 'S1 PSIKOLOGI'
                        break
                    else:
                        print('Kode prodi anda salah, Silakan masukkan kembali')
                        break
                break
            elif results.group(1) in ['H','h']:
                fakultas = 'FP'
                while True:
                    if results.group(2) in '01':
                        prodi = 'S1  AGROTEKNOLOGI'
                        break
                    elif results.group(2) in '02':
                        prodi = 'S1 AGRIBISNIS'
                        break
                    elif results.group(2) in '03':
                        prodi = 'S1 PENYULUHAN DAN KOMUNIKASI PERTANIAN'
                        break
                    elif results.group(2) in '04':
                        prodi = 'S1 PETERNAKAN'
                        break
                    elif results.group(2) in '05':
                        prodi = 'S1 ILMU DAN TEKNOLOGI PANGAN'
                        break
                    elif results.group(2) in '06':
                        prodi = 'S1 ILMU TANAH'
                        break
                    elif results.group(2) in '07':
                        prodi = 'S1 PENGELOLAAN HUTAN'
                        break
                    else:
                        print('Kode prodi anda salah, Silakan masukkan kembali')
                        break
                break
            elif results.group(1) in ['I','i']:
                fakultas = 'FT'
                while True:
                    if results.group(2) in '01':
                        prodi = 'S1 TEKNIK SIPIL'
                        break
                    elif results.group(2) in '02':
                        prodi = 'S1 ARSITEKTUR'
                        break
                    elif results.group(2) in '03':
                        prodi = 'S1 TEKNIK INDUSTRI'
                        break
                    elif results.group(2) in '04':
                        prodi = 'S1 TEKNIK Mesin'
                        break
                    elif results.group(2) in '05':
                        prodi = 'S1 TEKNIK KIMIA'
                        break
                    elif results.group(2) in '06':
                        prodi = 'S1 PERENCANAAN WILAYAH DAN KOTA'
                        break
                    elif results.group(2) in '07':
                        prodi = 'S1 TEKNIK ELEKTRO'
                        break
                    else:
                        print('Kode prodi anda salah, Silakan masukkan kembali')
                        break
                break
            elif results.group(1) in ['K','k','P','p','X','x']:
                fakultas = 'FKIP'
                while True:
                    if results.group(2) in '01':
                        prodi = 'S1 BIMBINGAN DAN KONSELING'
                        break
                    elif results.group(2) in '02':
                        prodi = 'S1 PENDIDIKAN TEKNIK INFORMATIKA DAN KOMPUTER'
                        break
                    elif results.group(2) in '03':
                        prodi = 'S1 PENDIDIKAN MATEMATIKA'
                        break
                    elif results.group(2) in '04':
                        prodi = 'S1 PENDIDIKAN LUAR BIASA'
                        break
                    elif results.group(2) in '05':
                        prodi = 'S1 PENDIDIKAN BAHASA DAN SASTRA INDONESIA'
                        break
                    elif results.group(2) in '06':
                        prodi = 'S1 PENDIDIKAN TEKNIK BANGUNAN'
                        break
                    elif results.group(2) in '07':
                        prodi = 'S1 PENDIDIKAN GURU SEKOLAH DASAR'
                        break
                    elif results.group(2) in '08':
                        prodi = 'S1  PENDIDIKAN EKONOMI'
                        break
                    elif results.group(2) in '09':
                        prodi = 'S1 PENDIDIKAN GEOGRAFI'
                        break
                    elif results.group(2) in '10':
                        prodi = 'S1 PENDIDIKAN BAHASA JAWA'
                        break
                    elif results.group(2) in '11':
                        prodi = 'S1 PENDIDIKAN BAHASA INGGRIS'
                        break
                    elif results.group(2) in '12':
                        prodi = 'S1 PENDIDIKAN SENI RUPA'
                        break
                    elif results.group(2) in '13':
                        prodi = 'S1 PENDIDIKAN FISIKA'
                        break
                    elif results.group(2) in '14':
                        prodi = 'S1 PENDIDIKAN KIMIA'
                        break
                    elif results.group(2) in '15':
                        prodi = 'S1 PENDIDIKAN BIOLOGI'
                        break
                    elif results.group(2) in '16':
                        prodi = 'S1 PENDIDIKAN SEJARAH'
                        break
                    elif results.group(2) in '17':
                        prodi = 'S1 PENDIDIKAN PANCASILA DAN KEWARGANEGARAAN'
                        break
                    elif results.group(2) in '18':
                        prodi = 'S1 PENDIDIKAN SOSIOLOGI ANTROPOLOGI'
                        break
                    elif results.group(2) in '19':
                        prodi = 'S1 PENDIDIKAN TEKNIK MESIN'
                        break
                    elif results.group(2) in '20':
                        prodi = 'S1 PENDIDIKAN GURU PENDIDIKAN ANAK USIA DINI'
                        break
                    elif results.group(2) in '21':
                        prodi = 'S1 PENDIDIKAN AKUNTANSI'
                        break
                    elif results.group(2) in '22':
                        prodi = 'S1 PENDIDIKAN ADMINISTRASI PERKANTORAN'
                        break
                    elif results.group(2) in '23':
                        prodi = 'S1 PENDIDIKAN ILMU PENGETAHUAN ALAM'
                        break
                    else:
                        print('Kode prodi anda salah, Silakan masukkan kembali')
                        break
                break
            elif results.group(1) in ['B','b']:
                fakultas = 'FIB'
                while True:
                    if results.group(2) in '01':
                        prodi = 'S1 SASTRA DAERAH'
                        break
                    elif results.group(2) in '02':
                        prodi = 'S1 SASTRA INDONESIA'
                        break
                    elif results.group(2) in '03':
                        prodi = 'S1 SASTRA INGGRIS'
                        break
                    elif results.group(2) in '04':
                        prodi = 'S1 ILMU SEJARAH'
                        break
                    elif results.group(2) in '05':
                        prodi = 'S1 SASTRA ARAB'
                        break
                    else:
                        print('Kode prodi anda salah, Silakan masukkan kembali')
                        break
                break
            elif results.group(1) in ['O','o']:
                fakultas = 'FKOR'
                while True:
                    if results.group(2) in '01':
                        prodi = 'S1 PENDIDIKAN JASMANI, KESEHATAN, DAN REKREASI'
                        break
                    elif results.group(2) in '02':
                        prodi = 'S1 PENDIDIKAN KEPELATIHAN OLAHRAGA'
                        break
                    else:
                        print('Kode prodi anda salah, Silakan masukkan kembali')
                        break
                break
            else:
                print('Silakan Masukkan Kembali NIM anda')
                break

        #mengelompokkan data (angkatan) berdasarkan kode dalam NIM
        angkatan = results.group(3)
        while True:
            if angkatan <= '21':
                angkatan = '20'+ str(results.group(3))
                break
            elif angkatan >= '21':
                angkatan = '19'+ str(results.group(3))
                break
            else:
                break
        
        #menginisiasi nomor urut
        no_urut = results.group(4)

        #mengembalikan variabel yang terdapat dalam fungsi
        return nim_mhs, nama_mhs, prodi, fakultas, no_urut, angkatan

    #Setelah membuat program regex diatas, selanjutnya adalah membuat data pada excel dengan judul kolom nim, nama, prodi, fakultas, no_urut, dan angkatan
    #mendefinisikan sebagai updatedata
    def updatedata():
        nim, nama, prodi, fakultas, no_urut, angkatan = datamahasiswauns()
        with open('identitasmahasiswa.csv','a') as file_object:
            file_object.write('\n' + nim + ',' + nama + ',' + prodi + ',' + fakultas + ',' + no_urut + ',' + angkatan)
    updatedata()

def EditDataMahasiswa():
    print('Data Mahasiswa UNS')
    MenampilkanDataMahasiswa()
    #input nim lama dan nim baru
    editnimlama = input('Silakan masukkan NIM yang akan anda edit : ').upper()
    editnimbaru = input('Silakan masukkan NIM baru anda : ').upper()
    
    #input nama lama dan nama baru
    editnamalama = input('Silakan masukkan nama yang akan anda edit : ').upper()
    editnamabaru = input('Silakan masukkan nama baru anda : ').upper()
    
    #membuat pola untuk NIM 
    nimlama_pattern = re.compile(r'(\w{1})(\d{2})(\d{2})(\d{3})')
    hasil = re.search(nimlama_pattern,editnimlama)
    #mengelompokkan data (fakultaslama dan program studi) berdasarkan kode dalam NIM
    while True:
        if hasil.group(1) in ['M','m']:
            fakultaslama = 'FMIPA'
            while True:
                if hasil.group(2) in '01':
                    prodilama = 'S1 MATEMATIKA'
                    break
                elif hasil.group(2) in '02':
                    prodilama = 'S1 FISIKA'
                    break
                elif hasil.group(2) in '03':
                    prodilama = 'S1 KIMIA'
                    break
                elif hasil.group(2) in '04':
                    prodilama = 'S1 BIOLOGI'
                    break
                elif hasil.group(2) in '05':
                    prodilama = 'S1 INFORMATIKA'
                    break
                elif hasil.group(2) in '06':
                    prodilama = 'S1 FARMASI'
                    break
                elif hasil.group(2) in '07':
                    prodilama = 'S1 STATISTIKA'
                    break
                elif hasil.group(2) in '08':
                    prodilama = 'S1 ILMU LINGKUNGAN'
                    break
                else:
                    print('Kode prodilama anda salah, Silakan masukkan kembali')
                    break
            break
        elif hasil.group(1) in ['F','f']:
            fakultaslama = 'FEB'
            while True:
                if hasil.group(2) in '01':
                    prodilama = 'S1 MANAJEMEN'
                    break
                elif hasil.group(2) in '02':
                    prodilama = 'S1 AKUNTANSI'
                    break
                elif hasil.group(2) in '03':
                    prodilama = 'S1 EKONOMI PEMBANGUNAN'
                    break
                else:
                    print('Kode prodilama anda salah, Silakan masukkan kembali')
                    break
            break
        elif hasil.group(1) in ['C','c']:
            fakultaslama = 'FSRD'
            while True:
                if hasil.group(2) in '01':
                    prodilama = 'S1 SENI RUPA MUNRI'
                    break
                elif hasil.group(2) in '02':
                    prodilama = 'S1 DESAIN KOMUNIKASI VISUAL'
                    break
                elif hasil.group(2) in '03':
                    prodilama = 'S1 DESAIN INTERIOR'
                    break
                elif hasil.group(2) in '04':
                    prodilama = 'S1 KRIYA SENI'
                    break
                else:
                    print('Kode prodilama anda salah, Silakan masukkan kembali')
                    break
            break
        elif hasil.group(1) in ['D','d']:
            fakultaslama = 'FISIP'
            while True:
                if hasil.group(2) in '01':
                    prodilama = 'S1 ILMU ADMINISTRASI NEGARA'
                    break
                elif hasil.group(2) in '02':
                    prodilama = 'S1 ILMU KOMUNIKASI'
                    break
                elif hasil.group(2) in '03':
                    prodilama = 'S1 SOSIOLOGI'
                    break
                elif hasil.group(2) in '04':
                    prodilama = 'S1 HUBUNGAN INTERNASIONAL'
                    break
                else:
                    print('Kode prodilama anda salah, Silakan masukkan kembali')
                    break
            break
        elif hasil.group(1) in ['E','e']:
            fakultaslama = 'FH'
            while True:
                if hasil.group(2) in '01':
                    prodilama = 'S1 ILMU HUKUM'
                    break
                else:
                    print('Kode prodilama anda salah, Silakan masukkan kembali')
                    break
            break
        elif hasil.group(1) in ['G','g','R','r']:
            fakultaslama = 'FK'
            while True:
                if hasil.group(2) in '01':
                    prodilama = 'S1 KEDOKTERAN'
                    break
                elif hasil.group(2) in '02':
                    prodilama = 'S1 PSIKOLOGI'
                    break
                else:
                    print('Kode prodilama anda salah, Silakan masukkan kembali')
                    break
            break
        elif hasil.group(1) in ['H','h']:
            fakultaslama = 'FP'
            while True:
                if hasil.group(2) in '01':
                    prodilama = 'S1  AGROTEKNOLOGI'
                    break
                elif hasil.group(2) in '02':
                    prodilama = 'S1 AGRIBISNIS'
                    break
                elif hasil.group(2) in '03':
                    prodilama = 'S1 PENYULUHAN DAN KOMUNIKASI PERTANIAN'
                    break
                elif hasil.group(2) in '04':
                    prodilama = 'S1 PETERNAKAN'
                    break
                elif hasil.group(2) in '05':
                    prodilama = 'S1 ILMU DAN TEKNOLOGI PANGAN'
                    break
                elif hasil.group(2) in '06':
                    prodilama = 'S1 ILMU TANAH'
                    break
                elif hasil.group(2) in '07':
                    prodilama = 'S1 PENGELOLAAN HUTAN'
                    break
                else:
                    print('Kode prodilama anda salah, Silakan masukkan kembali')
                    break
            break
        elif hasil.group(1) in ['I','i']:
            fakultaslama = 'FT'
            while True:
                if hasil.group(2) in '01':
                    prodilama = 'S1 TEKNIK SIPIL'
                    break
                elif hasil.group(2) in '02':
                    prodilama = 'S1 ARSITEKTUR'
                    break
                elif hasil.group(2) in '03':
                    prodilama = 'S1 TEKNIK INDUSTRI'
                    break
                elif hasil.group(2) in '04':
                    prodilama = 'S1 TEKNIK Mesin'
                    break
                elif hasil.group(2) in '05':
                    prodilama = 'S1 TEKNIK KIMIA'
                    break
                elif hasil.group(2) in '06':
                    prodilama = 'S1 PERENCANAAN WILAYAH DAN KOTA'
                    break
                elif hasil.group(2) in '07':
                    prodilama = 'S1 TEKNIK ELEKTRO'
                    break
                else:
                    print('Kode prodilama anda salah, Silakan masukkan kembali')
                    break
            break
        elif hasil.group(1) in ['K','k','P','p','X','x']:
            fakultaslama = 'FKIP'
            while True:
                if hasil.group(2) in '01':
                    prodilama = 'S1 BIMBINGAN DAN KONSELING'
                    break
                elif hasil.group(2) in '02':
                    prodilama = 'S1 PENDIDIKAN TEKNIK INFORMATIKA DAN KOMPUTER'
                    break
                elif hasil.group(2) in '03':
                    prodilama = 'S1 PENDIDIKAN MATEMATIKA'
                    break
                elif hasil.group(2) in '04':
                    prodilama = 'S1 PENDIDIKAN LUAR BIASA'
                    break
                elif hasil.group(2) in '05':
                    prodilama = 'S1 PENDIDIKAN BAHASA DAN SASTRA INDONESIA'
                    break
                elif hasil.group(2) in '06':
                    prodilama = 'S1 PENDIDIKAN TEKNIK BANGUNAN'
                    break
                elif hasil.group(2) in '07':
                    prodilama = 'S1 PENDIDIKAN GURU SEKOLAH DASAR'
                    break
                elif hasil.group(2) in '08':
                    prodilama = 'S1  PENDIDIKAN EKONOMI'
                    break
                elif hasil.group(2) in '09':
                    prodilama = 'S1 PENDIDIKAN GEOGRAFI'
                    break
                elif hasil.group(2) in '10':
                    prodilama = 'S1 PENDIDIKAN BAHASA JAWA'
                    break
                elif hasil.group(2) in '11':
                    prodilama = 'S1 PENDIDIKAN BAHASA INGGRIS'
                    break
                elif hasil.group(2) in '12':
                    prodilama = 'S1 PENDIDIKAN SENI RUPA'
                    break
                elif hasil.group(2) in '13':
                    prodilama = 'S1 PENDIDIKAN FISIKA'
                    break
                elif hasil.group(2) in '14':
                    prodilama = 'S1 PENDIDIKAN KIMIA'
                    break
                elif hasil.group(2) in '15':
                    prodilama = 'S1 PENDIDIKAN BIOLOGI'
                    break
                elif hasil.group(2) in '16':
                    prodilama = 'S1 PENDIDIKAN SEJARAH'
                    break
                elif hasil.group(2) in '17':
                    prodilama = 'S1 PENDIDIKAN PANCASILA DAN KEWARGANEGARAAN'
                    break
                elif hasil.group(2) in '18':
                    prodilama = 'S1 PENDIDIKAN SOSIOLOGI ANTROPOLOGI'
                    break
                elif hasil.group(2) in '19':
                    prodilama = 'S1 PENDIDIKAN TEKNIK MESIN'
                    break
                elif hasil.group(2) in '20':
                    prodilama = 'S1 PENDIDIKAN GURU PENDIDIKAN ANAK USIA DINI'
                    break
                elif hasil.group(2) in '21':
                    prodilama = 'S1 PENDIDIKAN AKUNTANSI'
                    break
                elif hasil.group(2) in '22':
                    prodilama = 'S1 PENDIDIKAN ADMINISTRASI PERKANTORAN'
                    break
                elif hasil.group(2) in '23':
                    prodilama = 'S1 PENDIDIKAN ILMU PENGETAHUAN ALAM'
                    break
                else:
                    print('Kode prodilama anda salah, Silakan masukkan kembali')
                    break
            break
        elif hasil.group(1) in ['B','b']:
            fakultaslama = 'FIB'
            while True:
                if hasil.group(2) in '01':
                    prodilama = 'S1 SASTRA DAERAH'
                    break
                elif hasil.group(2) in '02':
                    prodilama = 'S1 SASTRA INDONESIA'
                    break
                elif hasil.group(2) in '03':
                    prodilama = 'S1 SASTRA INGGRIS'
                    break
                elif hasil.group(2) in '04':
                    prodilama = 'S1 ILMU SEJARAH'
                    break
                elif hasil.group(2) in '05':
                    prodilama = 'S1 SASTRA ARAB'
                    break
                else:
                    print('Kode prodilama anda salah, Silakan masukkan kembali')
                    break
            break
        elif hasil.group(1) in ['O','o']:
            fakultaslama = 'FKOR'
            while True:
                if hasil.group(2) in '01':
                    prodilama = 'S1 PENDIDIKAN JASMANI, KESEHATAN, DAN REKREASI'
                    break
                elif hasil.group(2) in '02':
                    prodilama = 'S1 PENDIDIKAN KEPELATIHAN OLAHRAGA'
                    break
                else:
                    print('Kode prodilama anda salah, Silakan masukkan kembali')
                    break
            break
        else:
            print('Silakan Masukkan Kembali NIM anda')
            break

    #mengelompokkan data (angkatanlama) berdasarkan kode dalam NIM
    angkatanlama = hasil.group(3)
    while True:
        if angkatanlama <= '021':
            angkatanlama = '20'+ str(hasil.group(3))
            break
        elif angkatanlama >= '021':
            angkatanlama = '19'+ str(hasil.group(3))
            break
        else:
            break
    
    #menginisiasi nomor urut
    no_urutlama = hasil.group(4)
    
    #membuat pola untuk NIM 
    nimbaru_pattern = re.compile(r'(\w{1})(\d{2})(\d{2})(\d{3})')
    hasilbaru = re.search(nimbaru_pattern,editnimbaru)
    #mengelompokkan data (fakultas dan program studi) berdasarkan kode dalam NIM
    while True:
        if hasilbaru.group(1) in ['M','m']:
            fakultas = 'FMIPA'
            while True:
                if hasilbaru.group(2) in '01':
                    prodi = 'S1 MATEMATIKA'
                    break
                elif hasilbaru.group(2) in '02':
                    prodi = 'S1 FISIKA'
                    break
                elif hasilbaru.group(2) in '03':
                    prodi = 'S1 KIMIA'
                    break
                elif hasilbaru.group(2) in '04':
                    prodi = 'S1 BIOLOGI'
                    break
                elif hasilbaru.group(2) in '05':
                    prodi = 'S1 INFORMATIKA'
                    break
                elif hasilbaru.group(2) in '06':
                    prodi = 'S1 FARMASI'
                    break
                elif hasilbaru.group(2) in '07':
                    prodi = 'S1 STATISTIKA'
                    break
                elif hasilbaru.group(2) in '08':
                    prodi = 'S1 ILMU LINGKUNGAN'
                    break
                else:
                    print('Kode prodi anda salah, Silakan masukkan kembali')
                    break
            break
        elif hasilbaru.group(1) in ['F','f']:
            fakultas = 'FEB'
            while True:
                if hasilbaru.group(2) in '01':
                    prodi = 'S1 MANAJEMEN'
                    break
                elif hasilbaru.group(2) in '02':
                    prodi = 'S1 AKUNTANSI'
                    break
                elif hasilbaru.group(2) in '03':
                    prodi = 'S1 EKONOMI PEMBANGUNAN'
                    break
                else:
                    print('Kode prodi anda salah, Silakan masukkan kembali')
                    break
            break
        elif hasilbaru.group(1) in ['C','c']:
            fakultas = 'FSRD'
            while True:
                if hasilbaru.group(2) in '01':
                    prodi = 'S1 SENI RUPA MUNRI'
                    break
                elif hasilbaru.group(2) in '02':
                    prodi = 'S1 DESAIN KOMUNIKASI VISUAL'
                    break
                elif hasilbaru.group(2) in '03':
                    prodi = 'S1 DESAIN INTERIOR'
                    break
                elif hasilbaru.group(2) in '04':
                    prodi = 'S1 KRIYA SENI'
                    break
                else:
                    print('Kode prodi anda salah, Silakan masukkan kembali')
                    break
            break
        elif hasilbaru.group(1) in ['D','d']:
            fakultas = 'FISIP'
            while True:
                if hasilbaru.group(2) in '01':
                    prodi = 'S1 ILMU ADMINISTRASI NEGARA'
                    break
                elif hasilbaru.group(2) in '02':
                    prodi = 'S1 ILMU KOMUNIKASI'
                    break
                elif hasilbaru.group(2) in '03':
                    prodi = 'S1 SOSIOLOGI'
                    break
                elif hasilbaru.group(2) in '04':
                    prodi = 'S1 HUBUNGAN INTERNASIONAL'
                    break
                else:
                    print('Kode prodi anda salah, Silakan masukkan kembali')
                    break
            break
        elif hasilbaru.group(1) in ['E','e']:
            fakultas = 'FH'
            while True:
                if hasilbaru.group(2) in '01':
                    prodi = 'S1 ILMU HUKUM'
                    break
                else:
                    print('Kode prodi anda salah, Silakan masukkan kembali')
                    break
            break
        elif hasilbaru.group(1) in ['G','g','R','r']:
            fakultas = 'FK'
            while True:
                if hasilbaru.group(2) in '01':
                    prodi = 'S1 KEDOKTERAN'
                    break
                elif hasilbaru.group(2) in '02':
                    prodi = 'S1 PSIKOLOGI'
                    break
                else:
                    print('Kode prodi anda salah, Silakan masukkan kembali')
                    break
            break
        elif hasilbaru.group(1) in ['H','h']:
            fakultas = 'FP'
            while True:
                if hasilbaru.group(2) in '01':
                    prodi = 'S1  AGROTEKNOLOGI'
                    break
                elif hasilbaru.group(2) in '02':
                    prodi = 'S1 AGRIBISNIS'
                    break
                elif hasilbaru.group(2) in '03':
                    prodi = 'S1 PENYULUHAN DAN KOMUNIKASI PERTANIAN'
                    break
                elif hasilbaru.group(2) in '04':
                    prodi = 'S1 PETERNAKAN'
                    break
                elif hasilbaru.group(2) in '05':
                    prodi = 'S1 ILMU DAN TEKNOLOGI PANGAN'
                    break
                elif hasilbaru.group(2) in '06':
                    prodi = 'S1 ILMU TANAH'
                    break
                elif hasilbaru.group(2) in '07':
                    prodi = 'S1 PENGELOLAAN HUTAN'
                    break
                else:
                    print('Kode prodi anda salah, Silakan masukkan kembali')
                    break
            break
        elif hasilbaru.group(1) in ['I','i']:
            fakultas = 'FT'
            while True:
                if hasilbaru.group(2) in '01':
                    prodi = 'S1 TEKNIK SIPIL'
                    break
                elif hasilbaru.group(2) in '02':
                    prodi = 'S1 ARSITEKTUR'
                    break
                elif hasilbaru.group(2) in '03':
                    prodi = 'S1 TEKNIK INDUSTRI'
                    break
                elif hasilbaru.group(2) in '04':
                    prodi = 'S1 TEKNIK Mesin'
                    break
                elif hasilbaru.group(2) in '05':
                    prodi = 'S1 TEKNIK KIMIA'
                    break
                elif hasilbaru.group(2) in '06':
                    prodi = 'S1 PERENCANAAN WILAYAH DAN KOTA'
                    break
                elif hasilbaru.group(2) in '07':
                    prodi = 'S1 TEKNIK ELEKTRO'
                    break
                else:
                    print('Kode prodi anda salah, Silakan masukkan kembali')
                    break
            break
        elif hasilbaru.group(1) in ['K','k','P','p','X','x']:
            fakultas = 'FKIP'
            while True:
                if hasilbaru.group(2) in '01':
                    prodi = 'S1 BIMBINGAN DAN KONSELING'
                    break
                elif hasilbaru.group(2) in '02':
                    prodi = 'S1 PENDIDIKAN TEKNIK INFORMATIKA DAN KOMPUTER'
                    break
                elif hasilbaru.group(2) in '03':
                    prodi = 'S1 PENDIDIKAN MATEMATIKA'
                    break
                elif hasilbaru.group(2) in '04':
                    prodi = 'S1 PENDIDIKAN LUAR BIASA'
                    break
                elif hasilbaru.group(2) in '05':
                    prodi = 'S1 PENDIDIKAN BAHASA DAN SASTRA INDONESIA'
                    break
                elif hasilbaru.group(2) in '06':
                    prodi = 'S1 PENDIDIKAN TEKNIK BANGUNAN'
                    break
                elif hasilbaru.group(2) in '07':
                    prodi = 'S1 PENDIDIKAN GURU SEKOLAH DASAR'
                    break
                elif hasilbaru.group(2) in '08':
                    prodi = 'S1  PENDIDIKAN EKONOMI'
                    break
                elif hasilbaru.group(2) in '09':
                    prodi = 'S1 PENDIDIKAN GEOGRAFI'
                    break
                elif hasilbaru.group(2) in '10':
                    prodi = 'S1 PENDIDIKAN BAHASA JAWA'
                    break
                elif hasilbaru.group(2) in '11':
                    prodi = 'S1 PENDIDIKAN BAHASA INGGRIS'
                    break
                elif hasilbaru.group(2) in '12':
                    prodi = 'S1 PENDIDIKAN SENI RUPA'
                    break
                elif hasilbaru.group(2) in '13':
                    prodi = 'S1 PENDIDIKAN FISIKA'
                    break
                elif hasilbaru.group(2) in '14':
                    prodi = 'S1 PENDIDIKAN KIMIA'
                    break
                elif hasilbaru.group(2) in '15':
                    prodi = 'S1 PENDIDIKAN BIOLOGI'
                    break
                elif hasilbaru.group(2) in '16':
                    prodi = 'S1 PENDIDIKAN SEJARAH'
                    break
                elif hasilbaru.group(2) in '17':
                    prodi = 'S1 PENDIDIKAN PANCASILA DAN KEWARGANEGARAAN'
                    break
                elif hasilbaru.group(2) in '18':
                    prodi = 'S1 PENDIDIKAN SOSIOLOGI ANTROPOLOGI'
                    break
                elif hasilbaru.group(2) in '19':
                    prodi = 'S1 PENDIDIKAN TEKNIK MESIN'
                    break
                elif hasilbaru.group(2) in '20':
                    prodi = 'S1 PENDIDIKAN GURU PENDIDIKAN ANAK USIA DINI'
                    break
                elif hasilbaru.group(2) in '21':
                    prodi = 'S1 PENDIDIKAN AKUNTANSI'
                    break
                elif hasilbaru.group(2) in '22':
                    prodi = 'S1 PENDIDIKAN ADMINISTRASI PERKANTORAN'
                    break
                elif hasilbaru.group(2) in '23':
                    prodi = 'S1 PENDIDIKAN ILMU PENGETAHUAN ALAM'
                    break
                else:
                    print('Kode prodi anda salah, Silakan masukkan kembali')
                    break
            break
        elif hasilbaru.group(1) in ['B','b']:
            fakultas = 'FIB'
            while True:
                if hasilbaru.group(2) in '01':
                    prodi = 'S1 SASTRA DAERAH'
                    break
                elif hasilbaru.group(2) in '02':
                    prodi = 'S1 SASTRA INDONESIA'
                    break
                elif hasilbaru.group(2) in '03':
                    prodi = 'S1 SASTRA INGGRIS'
                    break
                elif hasilbaru.group(2) in '04':
                    prodi = 'S1 ILMU SEJARAH'
                    break
                elif hasilbaru.group(2) in '05':
                    prodi = 'S1 SASTRA ARAB'
                    break
                else:
                    print('Kode prodi anda salah, Silakan masukkan kembali')
                    break
            break
        elif hasilbaru.group(1) in ['O','o']:
            fakultas = 'FKOR'
            while True:
                if hasilbaru.group(2) in '01':
                    prodi = 'S1 PENDIDIKAN JASMANI, KESEHATAN, DAN REKREASI'
                    break
                elif hasilbaru.group(2) in '02':
                    prodi = 'S1 PENDIDIKAN KEPELATIHAN OLAHRAGA'
                    break
                else:
                    print('Kode prodi anda salah, Silakan masukkan kembali')
                    break
            break
        else:
            print('Silakan Masukkan Kembali NIM anda')
            break

    #mengelompokkan data (angkatan) berdasarkan kode dalam NIM
    angkatanbaru = hasilbaru.group(3)
    while True:
        if angkatanbaru <= '021':
            angkatanbaru = '20'+ str(hasilbaru.group(3))
            break
        elif angkatanbaru >= '021':
            angkatanbaru = '19'+ str(hasilbaru.group(3))
            break
        else:
            break
    
    #menginisiasi nomor urut
    no_urutbaru = hasilbaru.group(4)

    #membaca data dari csv
    data = pd.read_csv('identitasmahasiswa.csv')
    
    #proses mengubah data
    data['nim'] = data['nim'].replace({str(editnimlama):str(editnimbaru)})
    data['nama'] = data['nama'].replace({str(editnamalama):str(editnamabaru)})
    data['prodi'] = data['prodi'].replace({str(prodilama):str(prodi)})
    data['fakultas'] = data['fakultas'].replace({str(fakultaslama):str(fakultas)})
    data['no_urut'] = data['no_urut'].replace({str(no_urutlama):str(no_urutbaru)})
    data['angkatan'] = data['angkatan'].replace({str(angkatanlama):str(angkatanbaru)})

    #memperbarui data ke csv
    data.to_csv('identitasmahasiswa.csv', index = False)
    
def TambahDataMahasiswa():
    InputDataMahasiswa()

def MenampilkanDataInput():
    #menginputkan data NIM yang akan dicari
    datainput = input('Silakan masukkan NIM anda untuk menampilkan data: ').upper()
    data = pd.read_csv('identitasmahasiswa.csv')
    
    #mencari data berdasarkan NIM yang telah diinputkan
    datatampilan = data[data['nim'].str.contains(str(datainput))]
    print(datatampilan)

def MenampilkanDataMahasiswa():
    #membaca data pada file excel identitasmahasiswa.csv 
    data = pd.read_csv('identitasmahasiswa.csv')
    print(data)

def Selesai():
    print('Anda telah keluar dari program data mahasiswa')

choice = 1
while choice != 6:
    print('')
    print('----------------------------------------')
    print('>>>>>>>>>> SILAKAN PILIH MENU <<<<<<<<<<')
    print('----------------------------------------')
    print('[1] Input Data Mahasiswa')
    print('[2] Edit Data Mahasiswa')
    print('[3] Tambah Data Mahasiswa')
    print('[4] Menampilkan Data Input')
    print('[5] Menampilkan Data Mahasiswa')
    print('[6] Selesai')
    print('----------------------------------------')
    choice = int(input('Silakan masukkan menu (1/2/3/4/5/6) : '))
    print('----------------------------------------')
    if choice == 1 :
        InputDataMahasiswa()

    elif choice == 2 : 
        EditDataMahasiswa()

    elif choice == 3 :
        TambahDataMahasiswa()

    elif choice == 4 :
        MenampilkanDataInput()

    elif choice == 5 :
        MenampilkanDataMahasiswa()

    elif choice == 6 :
        Selesai()

    else :
        print('Pilihan anda salah, Silakan masukkan kembali')