package oktario;

// produk
abstract class Produk {
    private String namaProduk;
    private double harga;

    public Produk(String namaProduk, double harga) {
        this.namaProduk = namaProduk;
        this.harga = harga;
    }

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

    public Pegawai(String namaPegawai, String gaji) {
        this.namaPegawai = namaPegawai;
        this.gaji = gaji;
    }

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

    public Elektronik(String namaProduk, double harga, int garansi) {
        super(namaProduk, harga);
        this.garansi = garansi;
    }

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

    public Makanan(String namaProduk, double harga, String tanggalKadaluarsa) {
        super(namaProduk, harga);
        this.tanggalKadaluarsa = tanggalKadaluarsa;
    }

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

    public PegawaiTetap(String namaPegawai, String gaji, String tunjangan) {
        super(namaPegawai, gaji);
        this.tunjangan = tunjangan;
    }

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

    public PegawaiKontrak(String namaPegawai, String gaji, String lamaKontrak) {
        super(namaPegawai, gaji);
        this.lamaKontrak = lamaKontrak;
    }

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
        Produk elektronik = new Elektronik("Laptop", 5000000, 5);
        System.out.println(elektronik.tampilkanInfo());
        System.out.println();

        // 2. Output Pegawai Tetap
        System.out.println("2. Output Pegawai");
        Pegawai pegawaiTetap = new PegawaiTetap("Istoro", "5000000", "1000000");
        System.out.println(pegawaiTetap.tampilkanInfo());
        System.out.println();

        // 3. Output Polimorfisme Produk dan Pegawai
        System.out.println("3. Output Polimorfisme");
        Produk snack = new Makanan("Nabati", 2000, "2023-10-01");
        System.out.println(snack.tampilkanInfo());
        System.out.println();

        Pegawai pegawaiKontrak = new PegawaiKontrak("Ifad", "3000000", "1 bulan");
        System.out.println(pegawaiKontrak.tampilkanInfo());
    }
}
