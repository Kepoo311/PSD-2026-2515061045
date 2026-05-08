def binary_search(arr, n, target):
    l = 0
    r = n - 1
    pos = -1
    while l <= r:
        m = l + (r - l) // 2
        print(f"Median: {m}, judul: {arr[m]}")
        if arr[m] == target:
            pos = m
            break
        elif arr[m] < target:
            print("Mencari di kanan")
            l = m + 1
        else:
            print("Mencari di kiri")
            r = m - 1
    return pos


def main():
    try:
        n = int(input("Masukkan jumlah buku: "))
    except ValueError:
        print("Input tidak valid!")
        return
    arr = []
    print("Masukkan judul buku (urut dari A-Z):")
    for i in range(n):
        while True:
            try:
                judul_buku = input()
                arr.append(judul_buku)
                break
            except ValueError:
                print("Input tidak valid!")
    print(f"List buku: {arr}")
    while True:
        try:
            target = input("Masukkan judul buku yang ingin dicari: ")
            break
        except ValueError:
            print("Input tidak valid, silakan masukkan judul buku!")
    pos = binary_search(arr, n, target)
    if pos != -1:
        print(f"Buku ditemukan pada rak ke-{pos}")
    else:
        print("Buku tidak tersedia")


if __name__ == "__main__":
    main()
