
# Pencarian judul buku dengan metode Binary Searching

Sebuah program yang berfungsi untuk mencari judul buku dari sebuah struktur data array menggunakan metode Binary Searching


## Penjelasan source code

![App Screenshot](https://i.imgur.com/ppNyJZv.png)
![App Screenshot](https://i.imgur.com/UVX5jGR.png)
### Fungsi binary_search

Pada baris 1 - 17 terdapat sebuah fungsi yang berisi algoritma dari binary search

Baris 1 : Terdapat fungsi binary_search meminta 3 parameter yaitu : array, jumlah data (n), dan target yang dicari

Baris 2 : Terdapat variable l, yaitu sebuah variabel sementara yang berfungsi untuk menyimpan indeks batas kiri dari array yaitu indeks 0

Baris 3 : Terdapat variable r, berfungsi untuk menyimpan indeks batas kanan dari array

Baris 4 : Terdapat variable pos, berfungsi untuk menyimpan posisi indeks jika data ditemukan, di isi min -1 karena indeks -1 tidak terpakai

Baris 5 : Terdapat perulangan while yang berfungsi untuk mengecek selama batas kiri (l) lebih kecil sama dengan batas kanan (r)

Baris 6 : Terdapat variable m, berfungsi untuk mencari indeks nilai tengah atau median dari batasan array

Baris 7 : Menampilkan nilai median dan judul buku pada indeks median

Baris 8 : Terdapat fungsi perbandingan if, yang dimana jika nilai dari array pada indeks median sama dengan target yang dicari

Baris 9 : Mengubah nilai dari variable pos menjadi nilai dari indeks median (m)

Baris 10 : Menghentikan perulangan karena data sudah ditemukan menggunakan fungsi break

Baris 11 : Terdapat fungsi perbandingan elif, yang dimana jika nilai dari array pada indeks median lebih kecil secara alfabet dari target yang dicari

Baris 12 : Menampilkan tulisan Mencari di kanan

Baris 13 : Memperbarui batas kiri (l) dengan nilai m + 1 agar pencarian fokus pada sisi kanan array

Baris 14 : Terdapat else, kondisi jika nilai dari array pada indeks median lebih besar dari target yang dicari

Baris 15 : Menampilkan tulisan Mencari di kiri

Baris 16 : Memperbarui batas kanan (r) dengan nilai m - 1 agar pencarian fokus pada sisi kiri array

Baris 17 : Mengembalikan nilai pada variable pos

### Fungsi utama

Pada baris 20 - 47 terdapat fungsi main yang berfungsi untuk menjalankan program

Baris 20 : Terdapat fungsi main sebagai fungsi utama

Baris 21 : Terdapat try yang digunakan untuk menangkap error

Baris 22 : User diminta memasukkan jumlah buku dalam bentuk angka

Baris 23 : Jika user menginput selain angka maka akan terdetek error

Baris 24 : Menampilkan tulisan Input tidak valid!

Baris 25 : Menghentikan program jika terjadi error

Baris 26 : Variable untuk menyimpan array

Baris 27 : Menampilkan tulisan Masukkan judul buku yang terurut dari A-Z

Baris 28 : Terdapat perulangan sebanyak jumlah data yang dimasukkan user

Baris 29 : Terdapat perulangan while True yang berfungsi jika user salah input maka akan di suruh input ulang

Baris 30 : Terdapat try yang digunakan untuk menangkap error

Baris 31 : User diminta memasukkan judul buku

Baris 32 : Fungsi untuk memasukkan data judul buku ke array

Baris 33 : Jika input user sudah benar, akan menghentikan perulangan sambil lanjut ke input berikutnya

Baris 34 : Jika terjadi error saat penginputan judul buku maka akan terdetek error

Baris 35 : Menampilkan tulisan Input tidak valid!

Baris 36 : Menampilkan seluruh isi array atau list buku yang telah dimasukkan

Baris 37 : Terdapat perulangan while True yang berfungsi jika user salah input saat mencari target maka akan di suruh input ulang

Baris 38 : Terdapat try yang digunakan untuk menangkap error

Baris 39 : User diminta memasukkan judul buku yang ingin dicari sebagai target

Baris 40 : Jika input user sudah benar, akan menghentikan perulangan while

Baris 41 : Jika terjadi error saat penginputan target maka akan terdetek error

Baris 42 : Menampilkan tulisan Input tidak valid, silakan masukkan judul buku!

Baris 43 : Memanggil fungsi binary_search untuk mencari posisi data dan menyimpannya di variable pos

Baris 44 : Terdapat fungsi perbandingan if, yang dimana jika variable pos tidak sama dengan -1 (data ditemukan)

Baris 45 : Menampilkan tulisan Buku ditemukan pada rak beserta nilai indeks posisinya

Baris 46 : Terdapat else, kondisi jika buku tidak ditemukan (variable pos bernilai -1)

Baris 47 : Menampilkan tulisan Buku tidak tersedia


## Output

![App Screenshot](https://i.imgur.com/yelrdr4.png)

1. User di suruh masukin jumlah judul buku

2. User menginputkan judul buku yang urut dari A-Z

3. Output untuk array yang telah di-isi

4. User menginputkan judul buku yang ingin dicari

5. Menunjukka median awal dari array serta nilai dari media

6. Karena tidak cocok, sistem mencari di kanan

7. Menampilkan bahwa buku di temukan

## Live demo

[Link Youtube](https://youtu.be/foVbyxaZ3kk)

