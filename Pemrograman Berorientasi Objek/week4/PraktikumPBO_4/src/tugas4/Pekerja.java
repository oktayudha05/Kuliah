package tugas4;

public class Pekerja extends Manusia {
  private int gaji;

  public Pekerja(String nama, int usia, String pekerjaan, int gaji) {
    super(nama, usia, pekerjaan);
    this.gaji = gaji;
  }

  public void setGaji(int gaji) {
    this.gaji = gaji;
  }
  public int getGaji() {
    return gaji;
  }

  public String toString() {
    return "Nama: " + getNama() + "\n" +
           "Usia: " + usia + "\n" +
           "Pekerjaan: " + pekerjaan + "\n" +
           "Gaji: " + gaji;
  }
  
}
