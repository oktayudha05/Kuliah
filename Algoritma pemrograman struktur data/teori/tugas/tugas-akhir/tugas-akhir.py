# Barang-barang masuk ke gudang
gudang = []

gudang.push("Barang A")
gudang.push("Barang B")
gudang.push("Barang C")

# Melihat barang teratas (tanpa mengeluarkannya)
print("Barang teratas di gudang:", gudang.peek())

# Mengeluarkan barang dari gudang (mengambil barang teratas)
barang_keluar = gudang.pop()
print("Barang yang dikeluarkan:", barang_keluar)

# Melihat barang teratas setelah pengeluaran
print("Barang teratas di gudang sekarang:", gudang.peek())

# Menambahkan barang baru ke gudang
gudang.push("Barang D")

# Melihat total barang di gudang
print("Total barang di gudang:", gudang.size())