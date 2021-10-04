# Data Nasabah
noatm = 12345678
pin = 1234
pemilikrekening = "Jamal Udin"
saldosekarang = 1000000

#Halaman Selamat Datang Dan Login Page
welcomemessage = "Selamat Datang Di ATM UYE, Silahkan masukan Nomor ATM Dan Pin Anda"
print(welcomemessage)

#Login Page
#Input Pin Dan No ATM
masukan_noatm = int(input("Silahkan Masukan No ATM: "))
masukanpin = int(input("Silahkan Masukan Pin: "))

#Welcome Message Menu
selamatdatang1 = "Selamat datang "  
selamatdatang2 = " Anda Berhasil Login"
menuatm = "1. Cek Saldo\n2. Ambil Uang\n3. Transfer Uang\n4. Keluar"

if (masukan_noatm == noatm and masukanpin == pin):
    print(selamatdatang1, pemilikrekening, selamatdatang2)
    print(menuatm)
else:
    print("Maaf Pin Atau No ATM Kamu salah, Kartu Kamu Keluar Otomatis")


#Menu ATM
def pilihanatm():
    if (masukan_noatm == noatm and masukanpin == pin):
        menu_atm = input("Silahkan Pilih Menu Yang Anda Inginkan ")

        #Cek Saldo
        if (menu_atm == "1"):
            print("Saldo Anda Saat Ini Rp.", saldosekarang)
            pilihanatm()

        # Ambil Uang
        elif (menu_atm == "2"):
            ambiluang = int(input("Silahkan masukan jumlah uang yang ingin diambil "))
            if saldosekarang > ambiluang:
                print("Anda Mengambil Uang Sebesar Rp.", ambiluang)
            elif saldosekarang < ambiluang:
                print("Maaf Saldo Anda Tidak Cukup")
            pilihanatm()

        # Kirim Uang
        elif (menu_atm == "3"):
            norek = int(input("Silahkan masukan nomor rekening tujuan "))
            kirimuang = int(input("Silahkan masukan jumlah uang yang ingin Dikirim "))
            if saldosekarang > kirimuang:
                print("Anda Sudah Mengirim Uang Sebesar Rp.", kirimuang, ", Ke Nomor Rekening", norek)
            elif saldosekarang < kirimuang:
                print("Maaf saldo anda tidak cukup")
            pilihanatm()

        # Keluar Dari menu
        elif (menu_atm == "4"):
            print("Anda sudah keluar dari menu ATM, Silahkan Ambil Kartu Anda, Terima Kasih")

        # Jika Angka Yang Diinput Tidak Tersedia
        else:
            print("Maaf perintah yang kamu masukan tidak tersedia")
            pilihanatm()
pilihanatm()
