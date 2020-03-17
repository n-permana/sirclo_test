class Cart:
    items = {}

    def tambahProduk(self,kode,qty):
        try :
            self.items[kode] = self.items[kode] + qty
        except:
            self.items[kode] = qty

    def hapusProduk(self,kode):
        try:
            del self.items[kode]
        except:
            pass

    def tampilkanCart(self):
        for kode in self.items:
            print(f"{kode} ({self.items[kode]})")

keranjang = Cart()
keranjang.tambahProduk("Pisang Hijau", 2)
keranjang.tambahProduk("Semangka Kuning", 3)
keranjang.tambahProduk("Apel Merah", 1)
keranjang.tambahProduk("Apel Merah", 4)
keranjang.tambahProduk("Apel Merah", 2)
keranjang.hapusProduk("Semangka Kuning")
keranjang.hapusProduk("Semangka Merah")
keranjang.tampilkanCart()