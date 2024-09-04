package praktikum3;

public class Mobil {
  private String merk;
  private String model;
  private String warna;
  private int tahun;

  public Mobil(String merk, String model, int tahun) {
    this.merk = merk;
    this.model = model;
    this.tahun = tahun;
    this.warna = "Hitam";
  }

  public void setMerk(String merk) {
    this.merk = merk;
  }

  public String getMerk() {
    return merk;
  }

  public void setModel(String model) {
    this.model = model;
  }

  public String getModel() {
    return model;
  }

  public void setTahun(int tahun) {
    this.tahun = tahun;
  }

  public int getTahun() {
    return tahun;
  }

  public void setWarna(String warna) {
    this.warna = warna;
  }

  public String getWarna() {
    return warna;
  }

  public void startEngine() {
    System.out.println("Mesin mobil " + merk + " dinyalakan");
  }

  void info() {
    System.out.println("Merk: " + merk);
    System.out.println("Model: " + model);
    System.out.println("Warna: " + warna);
    System.out.println("Tahun: " + tahun);
  }
}
