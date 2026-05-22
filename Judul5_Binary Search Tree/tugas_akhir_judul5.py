class Node:
    def __init__(self, username, key):
        self.username = username
        self.key = key
        self.left = None
        self.right = None


class BSTDasar:
    def __init__(self):
        self.root = None

    def insert_node(self, root, username, key):
        if root is None:
            return Node(username, key)
        if key < root.key:
            root.left = self.insert_node(root.left, username, key)
        elif key > root.key:
            root.right = self.insert_node(root.right, username, key)
        return root

    def insert(self, username, key):
        self.root = self.insert_node(self.root, username, key)

    def search_node(self, root, key):
        if root is None:
            return False
        if root.key == key:
            return True
        if key < root.key:
            return self.search_node(root.left, key)
        return self.search_node(root.right, key)

    def search(self, key):
        return self.search_node(self.root, key)

    def inorder(self, root):
        if root is None:
            return
        self.inorder(root.left)
        print(f"{root.username}: {root.key}", end=" | ")
        self.inorder(root.right)

    def preorder(self, root):
        if root is None:
            return
        print(f"{root.username}: {root.key}", end=" | ")
        self.preorder(root.left)
        self.preorder(root.right)

    def postorder(self, root):
        if root is None:
            return
        self.postorder(root.left)
        self.postorder(root.right)
        print(f"{root.username}: {root.key}", end=" | ")

    def find_min(self, root):
        if root is None:
            return -1
        current = root
        while current.left is not None:
            current = current.left
        return current.key, current.username

    def find_max(self, root):
        if root is None:
            return -1
        current = root
        while current.right is not None:
            current = current.right
        return current.key, current.username



def main():
    bst = BSTDasar()
    pilih = 0
    while pilih != 8:
        print("\n=== Leaderboard ===")
        print("1. Masukkan Username dan skor")
        print("2. Cari Skor")
        print("3. Tampilkan leaderboard (Inorder)")
        print("4. Tampilkan leaderboard (Preorder)")
        print("5. Tampilkan leaderboard (Postorder)")
        print("6. Cari skor terkecil")
        print("7. Cari skor terbesar")
        print("8. Keluar")
        try:
            pilih = int(input("Pilih: "))
        except ValueError:
            print("Input tidak valid!")
            continue
        if pilih == 1:
            try:
                username = input("Masukkan Username: ")
                skor = int(input("Masukkan Skor: "))
                bst.insert(username, skor)
                print(f"Username {username} dan skor {skor} berhasil dimasukkan")
            except ValueError:
                print("Input tidak valid!")
        elif pilih == 2:
            try:
                skor = int(input("Cari Skor: "))
                if bst.search(skor):
                    print("Ditemukan")
                else:
                    print("Tidak ditemukan")
            except ValueError:
                print("Input tidak valid!")
        elif pilih == 3:
            print("Inorder: ", end="")
            bst.inorder(bst.root)
            print()
        elif pilih == 4:
            print("Preorder: ", end="")
            bst.preorder(bst.root)
            print()
        elif pilih == 5:
            print("Postorder: ", end="")
            bst.postorder(bst.root)
            print()
        elif pilih == 6:
            skor, username = bst.find_min(bst.root)
            print(f"Skor terkecil: {skor} (Username: {username})")
        elif pilih == 7:
            skor, username = bst.find_max(bst.root)
            print(f"Skor terbesar: {skor} (Username: {username})")
        elif pilih == 8:
            print("Program selesai.")
        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()
