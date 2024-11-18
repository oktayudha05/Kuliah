package tugas10;

interface Pembayaran {
  double hitungPajak(double harga);
}

class Elektronik implements Pembayaran {
  @Override
  public double hitungPajak(double harga) {
      return harga * 0.10; // Pajak 10%
  }
}

class Makanan implements Pembayaran {
  @Override
  public double hitungPajak(double harga) {
      return harga * 0.05; // Pajak 5%
  }
}

public class Main {
  public static void main(String[] args) {
      Elektronik elektronik = new Elektronik();
      double hargaElektronik = 2000.0;
      double pajakElektronik = elektronik.hitungPajak(hargaElektronik);
      System.out.println("Pajak Elektronik (10% dari " + hargaElektronik + ") : " + pajakElektronik);

      Makanan makanan = new Makanan();
      double hargaMakanan = 500.0;
      double pajakMakanan = makanan.hitungPajak(hargaMakanan);
      System.out.println("Pajak Makanan (5% dari " + hargaMakanan + ") : " + pajakMakanan);
  }
}

