
# Sistem parkir berbasis stack

Sebuah program sederhana yang berfungsi untuk mengatur sebuah parkiran.

## Penjelasan source code

![App Screenshot](https://i.postimg.cc/NGnFnz5n/Screenshot-2026-05-16-195100.png)
![App Screenshot](https://i.postimg.cc/fWPyPrVn/Screenshot-2026-05-16-195108.png)
### Class StackArray dan Fungsi __init__
Pada baris 1 - 5 terdapat definisi class dan fungsi awal untuk menyiapkan stack array.

Baris 1 : Terdapat pembuatan class dengan nama StackArray

Baris 2 : Terdapat fungsi __init__ yang meminta parameter max_size dengan nilai default 3 untuk membatasi kapasitas maksimal stack (parkiran)

Baris 3 : Terdapat variable self.MAX, yaitu variabel yang berfungsi untuk menyimpan nilai maksimal dari stack

Baris 4 : Terdapat variable self.st, berfungsi untuk membuat list array kosong (berisi None) sebesar batas maksimal yang sudah ditentukan

Baris 5 : Terdapat variable self.top_idx, berfungsi untuk menyimpan indeks dari data paling atas (nilai awalnya -1 yang menandakan stack/parkiran masih kosong)

### Fungsi is_empty
Pada baris 7 - 8 terdapat sebuah fungsi yang digunakan untuk mengecek apakah stack kosong.

Baris 7 : Terdapat fungsi is_empty

Baris 8 : Mengembalikan nilai True jika indeks teratas (top_idx) bernilai -1 (kosong), dan False jika tidak

### Fungsi is_full
Pada baris 10 - 11 terdapat sebuah fungsi yang digunakan untuk mengecek apakah stack sudah penuh.

Baris 10 : Terdapat fungsi is_full

Baris 11 : Mengembalikan nilai True jika indeks teratas sama dengan nilai self.MAX dikurang 1 (karena indeks array selalu dimulai dari 0)

### Fungsi push
Pada baris 13 - 19 terdapat sebuah fungsi yang berfungsi untuk memasukkan data ke dalam stack.

Baris 13 : Terdapat fungsi push yang meminta 1 parameter yaitu: x (data kendaraan yang mau dimasukkan)

Baris 14 : Terdapat fungsi perbandingan if, yang memanggil fungsi is_full() untuk mengecek apakah parkiran sudah penuh

Baris 15 : Menampilkan tulisan "Parkiran penuh" jika kondisi if bernilai benar

Baris 16 : Menghentikan proses dan keluar dari fungsi menggunakan return

Baris 17 : Menambahkan nilai indeks teratas (self.top_idx) dengan 1

Baris 18 : Memasukkan nilai x ke dalam array (self.st) pada posisi indeks teratas yang baru

Baris 19 : Menampilkan tulisan kendaraan berhasil parkir beserta namanya

### Fungsi pop
Pada baris 21 - 26 terdapat sebuah fungsi yang berfungsi untuk mengeluarkan data paling atas dari stack.

Baris 21 : Terdapat fungsi pop

Baris 22 : Terdapat fungsi perbandingan if, untuk mengecek apakah parkiran masih kosong dengan memanggil fungsi is_empty()

Baris 23 : Menampilkan tulisan "Parkiran kosong" jika kondisi if bernilai benar

Baris 24 : Menghentikan proses dan keluar dari fungsi

Baris 25 : Menampilkan tulisan kendaraan keluar beserta nama kendaraan yang posisinya ada di indeks teratas

Baris 26 : Mengurangi nilai indeks teratas (self.top_idx) dengan 1 agar posisi teratas pindah ke elemen di bawahnya

### Fungsi peek
Pada baris 28 - 32 terdapat sebuah fungsi yang berfungsi untuk melihat data paling atas tanpa mengeluarkannya.

Baris 28 : Terdapat fungsi peek

Baris 29 : Terdapat fungsi perbandingan if, untuk mengecek apakah parkiran masih kosong

Baris 30 : Menampilkan tulisan "Parkiran kosong" jika kondisi if bernilai benar

Baris 31 : Menghentikan proses dan keluar dari fungsi

Baris 32 : Menampilkan tulisan kendaraan di blok terdepan beserta nama kendaraannya

### Fungsi display
Pada baris 34 - 41 terdapat sebuah fungsi yang berfungsi untuk menampilkan seluruh isi stack dari atas ke bawah.

Baris 34 : Terdapat fungsi display

Baris 35 : Terdapat fungsi perbandingan if, untuk mengecek apakah parkiran kosong

Baris 36 : Menampilkan tulisan "Parkiran kosong" jika kondisi if bernilai benar

Baris 37 : Menghentikan proses dan keluar dari fungsi

Baris 38 : Menampilkan tulisan "Isi parkiran (atas ke bawah): " tanpa membuat baris baru (menggunakan end="")

Baris 39 : Terdapat perulangan for yang berjalan mundur, mulai dari nilai indeks teratas sampai indeks ke 0

Baris 40 : Menampilkan isi array pada indeks ke-i ke layar, dipisahkan dengan spasi

Baris 41 : Menampilkan baris kosong (enter) agar tampilan selanjutnya lebih rapi

### Fungsi utama
Pada baris 44 - 74 terdapat fungsi main yang berfungsi untuk menjalankan program.

Baris 44 : Terdapat fungsi main sebagai fungsi utama

Baris 45 : Membuat variabel stack yang diisi dengan cetakan StackArray()

Baris 46 : Membuat variabel pilih dengan nilai awal 0

Baris 47 : Terdapat perulangan while yang berfungsi untuk terus menjalankan menu selama variabel pilih tidak sama dengan angka 5

Baris 48 - 53 : Menampilkan pilihan menu parkiran ke layar

Baris 54 : Terdapat try yang digunakan untuk menangkap error

Baris 55 : User diminta memasukkan angka pilihan menu

Baris 56 : Jika user menginput selain angka maka akan terdetek error (ValueError)

Baris 57 : Menampilkan tulisan "Input tidak valid!"

Baris 58 : Melanjutkan perulangan ke tahap awal lagi menggunakan continue (melewati kode di bawahnya)

Baris 59 : Terdapat fungsi perbandingan if, jika user memilih angka 1

Baris 60 : Terdapat try yang digunakan untuk menangkap error

Baris 61 : User diminta memasukkan nama mobil dan disimpan ke variabel val

Baris 62 : Memanggil fungsi push pada stack untuk memasukkan nama mobil tersebut

Baris 63 : Jika terjadi error saat penginputan maka akan terdetek error

Baris 64 : Menampilkan tulisan "Input tidak valid!"

Baris 65 - 66 : Terdapat elif, jika user memilih angka 2 maka akan memanggil fungsi pop untuk mengeluarkan mobil

Baris 67 - 68 : Terdapat elif, jika user memilih angka 3 maka akan memanggil fungsi peek untuk melihat mobil paling depan

Baris 69 - 70 : Terdapat elif, jika user memilih angka 4 maka akan memanggil fungsi display untuk melihat isi parkiran

Baris 71 - 72 : Terdapat elif, jika user memilih angka 5 maka akan menampilkan tulisan "Program selesai."

Baris 73 - 74 : Terdapat else, kondisi jika user menginputkan angka selain 1 sampai 5 maka akan menampilkan tulisan "Pilihan tidak valid!"

## Output

1. Ini merupakan output saat memilih fitur yang pertama, user diminta untuk memasukkan jenis kendaraan

![App Screenshot](https://i.postimg.cc/h4YvY5XF/Screenshot-2026-05-16-195135.png)

2. Ini merupakan output saat memilih fitur yang kedua, dimana program akan mengeluarkan kendaraan dari stack

![App Screenshot](https://i.postimg.cc/8kYcY0jq/Screenshot-2026-05-16-195149.png)

3. Ini merupakan output saat memilih fitur yang ketiga, program akan menampilkan kendaraan yang berada paling atas

![App Screenshot](https://i.postimg.cc/RCYhYDNk/Screenshot-2026-05-16-195203.png)

4. Ini merupakan output saat memilih fitur yang ke empat, program akan menampilkan seluruh isi stack

![App Screenshot](https://i.postimg.cc/J7F0F2sW/Screenshot-2026-05-16-195212.png)

5. Ini merupakan output saat memilih fitur yang ke lima, program akan selesai

![App Screenshot](https://i.postimg.cc/zXRvYFg2/Screenshot-2026-05-16-195224.png)



## Live demo

[Link Youtube](https://youtu.be/8aezwZao6Xc)

