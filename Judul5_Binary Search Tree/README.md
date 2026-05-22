
# Sistem parkir berbasis stack

Sebuah program sederhana yang berfungsi untuk mengatur sebuah parkiran.

## Penjelasan source code

![App Screenshot](https://i.imgur.com/aiGkY3F.png)
![App Screenshot](https://i.imgur.com/9T6cyOL.png)
![App Screenshot](https://i.imgur.com/ETpL6yA.png)
### Class Node
Di baris 1 Terdapat deklarasi sebuah kelas bernama Node untuk membuat struktur dasar penyimpan data.

Baris 2-6 : Terdapat fungsi inisialisasi __init__ yang menerima parameter username dan key, di dalamnya terdapat variabel self.username dan self.key untuk menampung data, serta self.left dan self.right yang diatur menjadi None sebagai penunjuk ke data anak (child node).

### Class BSTDasar
Di baris 9 Terdapat deklarasi sebuah kelas bernama BSTDasar sebagai inti dari struktur Binary Search Tree.

Baris 10-11 : Terdapat fungsi inisialisasi __init__ yang mengatur variabel self.root menjadi None sebagai penanda awal akar pohon (root) yang masih kosong.

Baris 13 : Terdapat fungsi insert_node yang menerima parameter root, username, dan key untuk menambahkan data baru ke dalam struktur tree.

Baris 14-15 : Kondisi jika root masih kosong, maka akan membuat dan mengembalikan objek Node baru yang berisi data.

Baris 16-17 : Kondisi jika key lebih kecil dari nilai root saat ini, maka akan melakukan rekursif untuk meletakkan node baru di sebelah kiri (root.left).

Baris 18-19 : Kondisi jika key lebih besar dari nilai root saat ini, maka akan melakukan rekursif untuk meletakkan node baru di sebelah kanan (root.right).

Baris 20 : Mengembalikan root yang telah diperbarui datanya.

Baris 22-23 : Terdapat fungsi insert yang bertugas memanggil fungsi insert_node mulai dari self.root agar mempermudah proses tambah data dari luar kelas.

Baris 25 : Terdapat fungsi search_node untuk mencari nilai skor di dalam tree.

Baris 26-27 : Kondisi jika root kosong, maka akan mengembalikan False yang menandakan data tidak ditemukan.

Baris 28-29 : Kondisi jika nilai key pada root saat ini sama dengan nilai yang dicari, maka mengembalikan True.

Baris 30-31 : Kondisi jika nilai yang dicari lebih kecil dari nilai root saat ini, maka akan mencari secara rekursif menelusuri anak sebelah kiri.

Baris 32 : Mengembalikan hasil pencarian secara rekursif ke anak sebelah kanan jika kondisi sebelumnya tidak terpenuhi.

Baris 34-35 : Terdapat fungsi search untuk mempermudah menjalankan fungsi search_node dengan titik awal self.root.

Baris 37-42 : Terdapat fungsi inorder untuk menelusuri dan menampilkan data secara berurutan dari kiri ke kanan (terkecil ke terbesar).

Baris 44-49 : Terdapat fungsi preorder untuk menelusuri dan menampilkan data dengan urutan dari root, kiri, lalu kanan.

Baris 51-56 : Terdapat fungsi postorder untuk menelusuri dan menampilkan data dengan urutan dari kiri, kanan, lalu diakhiri di root.

Baris 58 : Terdapat fungsi find_min untuk mencari node dengan nilai skor paling kecil.

Baris 59-60 : Kondisi jika root kosong maka akan mengembalikan nilai -1.

Baris 61-64 : Terdapat variabel current yang akan menelusuri perulangan while terus-menerus ke anak sebelah kiri hingga mentok, lalu mengembalikan nilai key dan username paling kecil tersebut.

Baris 66 : Terdapat fungsi find_max untuk mencari node dengan nilai skor paling besar.

Baris 67-68 : Kondisi jika root kosong maka akan mengembalikan nilai -1.

Baris 69-72 : Terdapat variabel current yang akan menelusuri perulangan while terus-menerus ke anak sebelah kanan hingga mentok, lalu mengembalikan nilai key dan username paling besar tersebut.

### Fungsi utama
Fungsi main berada di baris 76, yang di mana berisi kode utama yang akan di jalankan.

Baris 77 : Terdapat variabel bst yang menginisialisasi objek dari kelas BSTDasar.

Baris 78 : Terdapat variabel pilih yang menampung nilai angka 0.

Baris 79 : Terdapat perulangan while yang berfungsi agar program terus berjalan sampai user menginputkan angka 8 (keluar).

Baris 80-88 : Berfungsi untuk menampilkan list fitur menu Leaderboard.

Baris 89-93 : Mengambil input pilihan user dan mengubahnya menjadi integer, jika gagal karena bukan angka, maka menampilkan error dan mengulang program.

Baris 94 : Kondisi jika user memilih fitur 1 yaitu memasukkan username dan skor.

Baris 95-101 : Input username dan skor dengan validasi try-except (skor harus angka), menggunakan fungsi bst.insert untuk menyimpan data, serta menampilkan pesan bahwa data berhasil dimasukkan.

Baris 102 : Kondisi jika user memilih fitur 2 yaitu mencari skor.

Baris 103-110 : Input angka skor yang dicari dengan validasi try-except, kemudian menggunakan fungsi bst.search untuk mengecek lalu mencetak apakah skor tersebut ditemukan atau tidak.

Baris 111-114 : Kondisi jika user memilih fitur 3, menampilkan teks dan memanggil fungsi bst.inorder untuk mencetak susunan leaderboard.

Baris 115-118 : Kondisi jika user memilih fitur 4, menampilkan teks dan memanggil fungsi bst.preorder untuk mencetak susunan leaderboard.

Baris 119-122 : Kondisi jika user memilih fitur 5, menampilkan teks dan memanggil fungsi bst.postorder untuk mencetak susunan leaderboard.

Baris 123-125 : Kondisi jika user memilih fitur 6, memanggil bst.find_min dan mencetak data skor terkecil beserta usernamenya.

Baris 126-128 : Kondisi jika user memilih fitur 7, memanggil bst.find_max dan mencetak data skor terbesar beserta usernamenya.

Baris 129-130 : Kondisi jika user memilih fitur 8 yaitu keluar, maka akan menampilkan pesan program selesai.

Baris 131-132 : Kondisi else jika user memasukkan pilihan angka yang tidak ada di menu, maka menampilkan pesan pilihan tidak valid.

Baris 135-136 : Memanggil fungsi main() untuk memastikan dan menjalankan kode program utama jika file dieksekusi secara langsung.

## Output

1. Ini merupakan output saat memilih fitur yang pertama, user diminta untuk memasukkan username dan skor.

![App Screenshot](https://i.imgur.com/hWFYJjQ.png)

2. Ini merupakan output saat memilih fitur yang kedua, program akan menampilkan hasil pencarian dari pengguna apakah ditemukan atau tidak

![App Screenshot](https://i.imgur.com/uUgJHF1.png)

3. Ini merupakan output saat memilih fitur yang ketiga keempat dan kelima, dimana program akan menampilkan seluruh isi yang ada pada BST secara Inorder, Preorder, Postorder

![App Screenshot](https://i.imgur.com/rnH8m76.png)

4. Ini merupakan output saat memilih fitur yang keenam dan ketujuh, program akan menampilkan skor terkecil dan terbesar

![App Screenshot](https://i.imgur.com/7jMMcFR.png)






## Live demo

[Link Youtube](https://youtu.be/OutRrjfI9Jw)

