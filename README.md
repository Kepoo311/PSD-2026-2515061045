
# Pengurutan episode anime berdasarkan rating menggunakan algoritma Bubble Sort

Ini adalah sebuah program yang berfungsi untuk mengurutkan episode dari suatu anime berdasarkan rating, program ini akan mengurutkan episode secara descending (Besar ke Kecil)


## Penjelasan source code

![App Screenshot](https://i.imgur.com/3wTZsB9.png)
![App Screenshot](https://i.imgur.com/RJ29AAx.png)
### Fungsi tukar
Pada baris 1 - 4 terdapat sebuah fungsi yang digunakan untuk menukar nilai pada array.

Baris 1 : fungsi tukar meminta 3 parameter yaitu : Array, index 0, index 1

Baris 2 : terdapat variable temp, yaitu sebuah variabel sementara yang berfungsi untuk menyimpan nilai dari array index 0

Baris 3 : terdapat variable arr[i], berfungsi untuk menukar nilai dari index 0 menjadi nilai dari index 1

Baris 4 : terdapat variable arr[i], berfungsi untuk menukar nilai dari index 1 menjadi nilai dari index 0

### Fungsi bubble_sort
Pada baris 7 - 11 terdapat sebuah fungsi yang berisi algoritma dari bubble sort

Baris 7 : Terdapat fungsi bubble_sort meminta 2 parameter yaitu: array dan jumlah data pada array

Baris 8 : Terdapat perulangan pertama yang berfungsi untuk mengecek index dari array sebelumnya (Index 0), terdapat n - 1 karena index array mulai dari 0, sedangkan user  menginputkan mulai dari index 1

Baris 9 : Terdapat perulangan kedua yang berfungsi untuk mengecek index dari array setelahnya (index 1)

Baris 10 : terdapat fungsi perbandingan if,yang dimana jika nilai dari index setelahnya lebih kecil dari nilai dari index sebelumnya maka nilai akan di tukar

Baris 11 : Memanggil fungsi tukar untuk menukar posisi nilai.

### Fungsi utama
Pada baris 14 - 35 terdapat fungsi main yang berfungsi untuk menjalankan program

Baris 14 : Terdapat fungsi main sebagai fungsi utama

Baris 15 : Terdapat try yang digunakan untuk menangkap error

Baris 16 : User diminta memasukkan jumlah episode anime dalam bentuk angka

Baris 17 : Jika user menginput selain angka maka akan terdetek error

Baris 18 : Menampilkan tulisan input tidak valid

Baris 19 : Menghentikan program jika terjadi error

Baris 20 : variable untuk menyimpan array

Baris 21 : Terdapat perulangan sebanyak jumlah data yang dimasukkan user

Baris 22 : Terdapat perulangan while True yang berfungsi jika user salah input maka akan di suruh input ulang

Baris 23 : Terdapat try yang digunakan untuk menangkap error

Baris 24 : User diminta memasukkan nomor episode

Baris 25 : User diminta memasukkan rating

Baris 26 : Fungsi untuk memasukkan data episode dan rating ke array

Baris 27 : Jika input user sudah benar, akan lanjut ke input berikutnya

Baris 28 : Jika user menginput selain angka maka akan terdetek error

Baris 29 : Menampilkan tulisan Input tidak valid, silakan masukkan angka!

Baris 30 : Menampilkan array sebelum di urut dengan bubble sort

Baris 31 : Memanggil fungsi bubble_sort untuk mengurutkan data

Baris 32 : Menampilkan tulisan array setelah  di urutkan

Baris 33 - 34 : menggunakan looping untuk menampilkan suluruh isi array



## Output

![App Screenshot](https://i.imgur.com/VuIAif3.png)

1. User di suruh masukin jumlah episode

2. User menginputkan episode ke berapa lalu input ratingnya

3. Output untuk array sebelum di urutkan

4. Output setelah array di urutkan dengan bubble sort

## Live demo

[Link Youtube](https://youtu.be/NxW6CFhpP5Q)

