# Sistem manajemen stok barang

def menu():
    print("================================================")
    print("1. Tampilkan semua list barang")
    print("2. Tambahkan barang baru")
    print("3. Hapus barang")
    print("4. Edit barang")
    print("5. Keluar")
    print("================================================")


def main():
    List_barang = [[0 for _ in range(2)] for _ in range(5)]
    running = True
    while running:
        menu()
        try:
            choice = int(input("Pilihan: "))
        except ValueError:
            print("Masukkan angka yang valid!")
            continue
        if choice == 1:
            print("================================================")
            print("Daftar barang:")
            for i in range(len(List_barang)):
                print(f"{i+1}. {List_barang[i][0]}: {List_barang[i][1]}")
            print("================================================")
        elif choice == 2:
            print("Silahkan masukkan nama barang dan stoknya:")
            for i in range(len(List_barang)):
                while True:
                    try:
                        List_barang[i][0] = input(f"Nama barang ke-{i+1} = ")
                        List_barang[i][1] = int(input(f"Stok barang ke-{i+1} = "))
                        break
                    except ValueError:
                        print("Input tidak valid, silakan masukkan angka untuk stok barang!")
            print("================================================")
            print("Data yang telah di input:")
            for row in List_barang:
                print(row)
            print("================================================")
        elif choice == 3:
            print("Silahkan pilih data yang akan di hapus:")
            for i in range(len(List_barang)):
                print(f"{i+1}. {List_barang[i][0]}: {List_barang[i][1]}")
            print("================================================")
            while True:
                try:
                    dele = int(input("Masukkan nomor barang : "))
                    if 1 <= dele <= len(List_barang):
                        List_barang.pop(dele - 1)
                        print("Barang  berhasil di hapus")
                        print("================================================")
                        break
                    else:
                        print("Nomor barang tidak valid!")
                except ValueError:
                    print("Input tidak valid, silakan masukkan angka!")
        elif choice == 4:
            print("Silahkan pilih data yang akan di edit:")
            for i in range(len(List_barang)):
                print(f"{i+1}. {List_barang[i][0]}: {List_barang[i][1]}")
            print("================================================")
            mengisi = True
            while mengisi:
                try:
                    edt = int(input("Masukkan nomor barang : "))
                    if 1 <= edt <= len(List_barang):
                        while True:
                            try:
                                nambar = input("Masukkan nama barang baru :")
                                stobar = input("Masukkan stok barang baru :")
                                List_barang[edt  - 1] = [nambar, int(stobar)]
                                print("Barang  berhasil di edit")
                                mengisi = False
                                print("================================================")
                                break
                            except ValueError:
                                print("Input tidak valid!")
                    else:
                        print("Nomor barang tidak valid!")
                except ValueError:
                    print("Input tidak valid, silakan masukkan angka!")
        elif choice == 5:
            running = False
            print("Program selesai.")
        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()
