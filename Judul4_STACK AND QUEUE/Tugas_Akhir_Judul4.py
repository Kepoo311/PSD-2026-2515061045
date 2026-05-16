class StackArray:
    def __init__(self, max_size=3):
        self.MAX = max_size
        self.st = [None] * self.MAX
        self.top_idx = -1

    def is_empty(self):
        return self.top_idx == -1

    def is_full(self):
        return self.top_idx == self.MAX - 1

    def push(self, x):
        if self.is_full():
            print("Parkiran penuh")
            return
        self.top_idx += 1
        self.st[self.top_idx] = x
        print(f"Kendaraan {x} berhasil parkir")

    def pop(self):
        if self.is_empty():
            print("Parkiran kosong")
            return
        print(f"Kendaraan {self.st[self.top_idx]} keluar")
        self.top_idx -= 1

    def peek(self):
        if self.is_empty():
            print("Parkiran kosong")
            return
        print(f"Kendaraan di blok terdepan: {self.st[self.top_idx]}")

    def display(self):
        if self.is_empty():
            print("Parkiran kosong")
            return
        print("Isi parkiran (atas ke bawah): ", end="")
        for i in range(self.top_idx, -1, -1):
            print(self.st[i], end=" ")
        print()


def main():
    stack = StackArray()
    pilih = 0
    while pilih != 5:
        print("\n=== Parkiran dengan stack ===")
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Tampilkan")
        print("5. Keluar")
        try:
            pilih = int(input("Pilih: "))
        except ValueError:
            print("Input tidak valid!")
            continue
        if pilih == 1:
            try:
                val = input("Mobil apa : ")
                stack.push(val)
            except ValueError:
                print("Input tidak valid!")
        elif pilih == 2:
            stack.pop()
        elif pilih == 3:
            stack.peek()
        elif pilih == 4:
            stack.display()
        elif pilih == 5:
            print("Program selesai.")
        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()
