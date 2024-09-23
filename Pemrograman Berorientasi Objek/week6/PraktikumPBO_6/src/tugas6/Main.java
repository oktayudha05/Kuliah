package tugas6;

// Kelas abstrak Produk
abstract class Produk {
    protected String nama;
    protected double harga;

    public Produk(String nama, double harga) {
        this.nama = nama;
        this.harga = harga;
    }

    // Metode abstrak untuk menghitung diskon
    public abstract double hitungDiskon();

    // Metode untuk mendapatkan harga setelah diskon
    public double getHargaSetelahDiskon() {
        return harga - hitungDiskon();
    }

    @Override
    public String toString() {
        return "Nama: " + nama + ", Harga: " + harga;
    }
}

// Kelas turunan Buku
class Buku extends Produk {
    public Buku(String nama, double harga) {
        super(nama, harga);
    }

    @Override
    public double hitungDiskon() {
        return harga * 0.1; // Diskon 10% untuk Buku
    }
}

// Kelas turunan Elektronik
class Elektronik extends Produk {
    public Elektronik(String nama, double harga) {
        super(nama, harga);
    }

    @Override
    public double hitungDiskon() {
        return harga * 0.05; // Diskon 5% untuk Elektronik
    }
}

// Kelas turunan Pakaian
class Pakaian extends Produk {
    public Pakaian(String nama, double harga) {
        super(nama, harga);
    }

    @Override
    public double hitungDiskon() {
        return harga * 0.15; // Diskon 15% untuk Pakaian
    }
}

// Kelas KeranjangBelanja
class KeranjangBelanja {
    private Produk[] daftarProduk;
    private int jumlahProduk;

    public KeranjangBelanja(int kapasitas) {
        this.daftarProduk = new Produk[kapasitas];
        this.jumlahProduk = 0;
    }

    // Tambah produk ke dalam keranjang
    public void tambahProduk(Produk produk) {
        if (jumlahProduk < daftarProduk.length) {
            daftarProduk[jumlahProduk] = produk;
            jumlahProduk++;
        } else {
            System.out.println("Keranjang penuh!");
        }
    }

    // Hitung total harga setelah diskon
    public double hitungTotalHargaSetelahDiskon() {
        double total = 0;
        for (int i = 0; i < jumlahProduk; i++) {
            total += daftarProduk[i].getHargaSetelahDiskon();
        }
        return total;
    }

    // Menampilkan produk di dalam keranjang
    public void tampilkanProduk() {
        for (int i = 0; i < jumlahProduk; i++) {
            System.out.println(daftarProduk[i]);
        }
    }
}

// Main Class untuk menjalankan program
public class Main {
    public static void main(String[] args) {
        // Buat beberapa produk
        Buku buku = new Buku("Buku Pemrograman Java", 100000);
        Elektronik elektronik = new Elektronik("Smartphone", 3000000);
        Pakaian pakaian = new Pakaian("Kemeja", 150000);

        // Buat keranjang belanja dengan kapasitas 3 produk
        KeranjangBelanja keranjang = new KeranjangBelanja(3);

        // Tambah produk ke dalam keranjang
        keranjang.tambahProduk(buku);
        keranjang.tambahProduk(elektronik);
        keranjang.tambahProduk(pakaian);

        // Tampilkan produk yang ada di keranjang
        keranjang.tampilkanProduk();

        // Hitung dan tampilkan total harga setelah diskon
        double totalHarga = keranjang.hitungTotalHargaSetelahDiskon();
        System.out.println("Total harga setelah diskon: " + totalHarga);
    }
}
