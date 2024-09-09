package praktikum4;

public class Mobil extends Kendaraan {
  private int jumlahPintu;

  public Mobil(String nama, int kecepatanMaks, String jenisMesin, int jumlahPintu) {
    super(nama, kecepatanMaks, jenisMesin);
    this.jumlahPintu = jumlahPintu;
  }

  public void tampilkanInfoMobil() {
    System.out.println("Kecepatan Maks: " + kecepatanMaks + " km/h");
    System.out.println("Jumlah Pintu: " + jumlahPintu);
  }
}
