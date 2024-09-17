package tugas4;

public class Tugas4 {
  public static void main(String[] args) {
    Pekerja pekerja = new Pekerja("Zidhan", 19, "Tukang Tipu", 1000000);
    
    System.out.println("====sebelum di ganti====");

    System.out.println(pekerja.toString());
    pekerja.setNama("Zidhan Arzaq K.");
    
    System.out.println("====setelah di ganti====");
    System.out.println(pekerja.toString());
  }
}
