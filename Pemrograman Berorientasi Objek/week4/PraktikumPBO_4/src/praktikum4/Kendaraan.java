package praktikum4;

public class Kendaraan {
  private String nama;
  protected int kecepatanMaks;
  public String jenisMesin;

  public Kendaraan(String nama, int kecepatanMaks, String jenisMesin) {
    this.nama = nama;
    this.kecepatanMaks = kecepatanMaks;
    this.jenisMesin = jenisMesin;
  }

  public void tampilkanInfoKendaraan() {
    System.out.println("Nama: " + nama);
    System.out.println("Kecepatan Maks: " + kecepatanMaks);
    System.out.println("Jenis Mesin: " + jenisMesin);
  }
}

