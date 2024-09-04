package praktikum3;

public class Hewan {
  private String nama;
  private int umur;

  public Hewan(String nama, int umur) {
    this.nama = nama;
    this.umur = umur;
  }

  public String getNama() {
    return nama;
  }

  public void setNama(String nama) {
    this.nama = nama;
  }

  public int getUmur() {
    return umur;
  }

  public void setUmur(int umur) {
    this.umur = umur;
  }

  void suara() {
    System.out.println("Hewan bersuara");
  }

  void berlari() {
    System.out.println("Hewan sedang berlari");
  }

  void info() {
    System.out.println("Nama: " + nama);
    System.out.println("Umur: " + umur);
  }
}