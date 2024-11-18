package praktikum10;

interface OperasiHitung{
  int hitung(int a, int b);
}

class Pengurangan implements OperasiHitung {
  @Override
  public int hitung(int a, int b) {
  return a - b;
  }
}

class Penjumlahan implements OperasiHitung {
  @Override
  public int hitung(int a, int b) {
  return a + b;
  }
}

public class Main {
  public static void main(String[] args) {
    // Objek Penjumlahan
    OperasiHitung penjumlahan = new Penjumlahan();
    System.out.println("Penjumlahan: " +
    penjumlahan.hitung(10, 5)); // Output: 15
    // Objek Pengurangan
    OperasiHitung pengurangan = new Pengurangan();
    System.out.println("Pengurangan: " +
    pengurangan.hitung(10, 5)); // Output: 5
  }
}