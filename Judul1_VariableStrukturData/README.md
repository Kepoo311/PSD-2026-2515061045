
# Sistem manajemen stok barang

Sistem manajemen stok barang adalah sebuah program yang berfungsi untuk memudahkan para pemilik toko untuk mengelola stok barang. Program ini mengimplentasikan struktur data List 2 Dimensi yang berukuran 5x2, yang berisi data berupa nama dan stok barang.


## Penjelasan source code

![App Screenshot](https://gcdnb.pbrd.co/images/REId-J2PM6Sb.png)
![App Screenshot](https://gcdnb.pbrd.co/images/oWlOTWSDWVOb.png)
### Fungsi menu
Di baris 3 Terdapat sebuah fungsi bernama menu, didalam fungsi ini terdapat 7 baris kode, baris 4 terdapat perintah print untuk menampilkan garis pembatas, baris 5-9 berfungsi untuk menampilkan list fitur, dan barus 10 untuk menampilkan garis pembatas

### Fungsi utama
Fungsi menu berada di baris 13, yang di mana berisi kode utama yang akan di jalankan.

Baris 14 : Terdapat variable List_barang yang menampung list 2dimensi berukuran 5x2

Baris 15 : Terdapat variable running yang berupa boolean

Baris 16 : Terdapat perulangan while True yang berfungsi agar program terus berjalan sampai user keluar dari program.

baris 17 : Memanggil fungsi menu.

Baris 18-21 : Mengambil input pilihan user dan mengubahnya menjadi integer, jika gagal maka menampilkan error

Baris 23 : Kondisi jika user memilih fitur 1

Baris 24-25 : Menampilkan judul dari fitur

Baris 26 : Perulangan untuk menampilkan seluruh isi list barang

Baris 27 : Menampilkan nomor, nama barang, dan stok

Baris 28 : Menampilkan garis pembatas

Baris 29 : Kondisi jika user memilih fitur 2 yaitu tambah barang

Baris 30 : Menampilkan instruksi untuk memasukkan data barang

Baris 31 : Perulangan for untuk menginput 5 data barang

Baris 32-38 : Input nama dan stok barang dengan validasi yaitu stok harus angka

Baris 39 : Menampilkan garis pembatas

Baris 40 : Menampilkan data yang sudah diinput

Baris 41-42 : Menampilkan seluruh isi list barang

Baris 43 : Menampilkan garis pembatas

Baris 44 : Kondisi jika user memilih fitur 3 yaitu hapus barang

Baris 45 : Menampilkan instruksi untuk memilih data yang akan di hapus

Baris 46-47 : Menampilkan daftar barang

Baris 48 : Menampilkan garis pembatas

Baris 49-60 : Input nomor barang yang akan dihapus dengan validasi

Baris 53 : Menghapus data dari list menggunakan pop()

Baris 61 : Kondisi jika user memilih Fitur 4 yaitu edit barang

Baris 62 : Menampilkan instruksi untuk memilih data yang akan di edit

Baris 63-64 : Menampilkan daftar barang

Baris 65 : Menampilkan garis pembatas

Baris 66 : Variabel kontrol untuk proses edit

Baris 67-83 : Proses input nomor barang dan update data dengan validasi

Baris 75 : Mengganti data lama dengan data baru

Baris 86 : Kondisi jika user memilih fitur 5 yaitu keluar

Baris 87 : Mengubah running menjadi False agar loop berhenti

Baris 88 : Menampilkan pesan program selesai

Baris 93=94 : Memanggil fungsi main() untuk menjalankan program

## Output

1. Ini merupakan output saat memilih fitur yang pertama saat data belum di tambahkan

![App Screenshot](https://i.postimg.cc/fLXYD8y2/Screenshot-2026-04-30-000451.png)

2. Ini merupakan output saat memilih fitur yang kedua yaitu proses menambahkan data barang dan stok, serta melakukan test validasi

![App Screenshot](https://i.postimg.cc/JnJjMp0Y/Screenshot-2026-04-30-000515.png)

3. Ini merupakan output saat memilih fitur yang pertama saat data sudah di tambahkan

![App Screenshot](https://i.postimg.cc/mDM7Bmk6/Screenshot-2026-04-30-000534.png)

4. Ini merupakan output saat memilih fitur yang ketigas saat akan menghapus data

![App Screenshot](https://i.postimg.cc/V6MXmKvV/Screenshot-2026-04-30-000548.png)

5. Ini merupakan output saat memilih fitur yang keempat saat akan mengedit data

![App Screenshot](https://i.postimg.cc/k48WqTGz/Screenshot-2026-04-30-000602.png)

6. Ini merupakan output saat memilih fitur yang kelima saat akan mengakhiri program

![App Screenshot](https://i.postimg.cc/V6MXmK5y/Screenshot-2026-04-30-000625.png)


## Live demo

[Link Youtube](https://youtu.be/_FhQPg5UH1E)

