package oktario;

// produk
abstract class Produk {
    private String namaProduk;
    private double harga;

    abstract String tampilkanInfo();

    public void setNamaProduk(String namaProduk) {
        this.namaProduk = namaProduk;
    }
    public String getNamaProduk() {
        return this.namaProduk;
    }
    public void setHarga(double harga) {
        this.harga = harga;
    }
    public double getHarga() {
        return this.harga;
    }
}

// pegawai
abstract class Pegawai {
    private String namaPegawai;
    private String gaji;

    abstract String tampilkanInfo();

    public void setNamaPegawai(String namaPegawai) {
        this.namaPegawai = namaPegawai;
    }
    public String getNamaPegawai() {
        return this.namaPegawai;
    }
    public void setGaji(String gaji) {
        this.gaji = gaji;
    }
    public String getGaji() {
        return this.gaji;
    }
}

// turunan produk
class Elektronik extends Produk {
    private int garansi;

    public void setGaransi(int garansi) {
        this.garansi = garansi;
    }
    public int getGaransi() {
        return this.garansi;
    }

    @Override
    public String tampilkanInfo() {
        return "Nama Produk: " + getNamaProduk() + "\nHarga: " + getHarga() + "\nGaransi: " + garansi + " tahun";
    }
}

class Makanan extends Produk {
    private String tanggalKadaluarsa;

    public void setTanggalKadaluarsa(String tanggalKadaluarsa) {
        this.tanggalKadaluarsa = tanggalKadaluarsa;
    }
    public String getTanggalKadaluarsa() {
        return this.tanggalKadaluarsa;
    }

    @Override
    public String tampilkanInfo() {
        return "Nama Produk: " + getNamaProduk() + "\nHarga: " + getHarga() + "\nTanggal Kadaluarsa: " + tanggalKadaluarsa;
    }
}

// turunan pegawai
class PegawaiTetap extends Pegawai {
    private String tunjangan;

    public void setTunjangan(String tunjangan) {
        this.tunjangan = tunjangan;
    }
    public String getTunjangan() {
        return this.tunjangan;
    }

    @Override
    public String tampilkanInfo() {
        return "Nama Pegawai: " + getNamaPegawai() + "\nGaji: " + getGaji() + "\nTunjangan: " + tunjangan;
    }
}

class PegawaiKontrak extends Pegawai {
    private String lamaKontrak;

    public void setLamaKontrak(String lamaKontrak) {
        this.lamaKontrak = lamaKontrak;
    }
    public String getLamaKontrak() {
        return this.lamaKontrak;
    }

    @Override
    public String tampilkanInfo() {
        return "Nama Pegawai: " + getNamaPegawai() + "\nGaji: " + getGaji() + "\nLama Kontrak: " + lamaKontrak;
    }
}

public class Main {
    public static void main(String[] args) { 
        // 1. Output Produk Elektronik
        System.out.println("1. Output Produk");
        Produk elektronik = new Elektronik();
        elektronik.setNamaProduk("Laptop");
        elektronik.setHarga(5000000);
        ((Elektronik) elektronik).setGaransi(2);
        System.out.println(elektronik.tampilkanInfo());
        System.out.println();

        // 2. Output Pegawai Tetap
        System.out.println("2. Output Pegawai");
        Pegawai pegawaiTetap = new PegawaiTetap();
        pegawaiTetap.setNamaPegawai("Budi");
        pegawaiTetap.setGaji("5000000");
        ((PegawaiTetap) pegawaiTetap).setTunjangan("1000000");
        System.out.println(pegawaiTetap.tampilkanInfo());
        System.out.println();

        // 3. Output Polimorfisme Produk dan Pegawai
        System.out.println("3. Output Polimorfisme");
        Produk snack = new Makanan();
        snack.setNamaProduk("Snack");
        snack.setHarga(15000);
        ((Makanan) snack).setTanggalKadaluarsa("2023-12-30");
        System.out.println(snack.tampilkanInfo());

        Pegawai pegawaiKontrak = new PegawaiKontrak();
        pegawaiKontrak.setNamaPegawai("Andi");
        pegawaiKontrak.setGaji("3000000");
        ((PegawaiKontrak) pegawaiKontrak).setLamaKontrak("12 bulan");
        System.out.println(pegawaiKontrak.tampilkanInfo());
    }
}
