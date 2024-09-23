package praktikum6;

class Hewan {
  public void bersuara() {
  System.out.println("Hewan bersuara");
  }
  public void makan(String makanan) {
  System.out.println("Hewan makan " + makanan);
  }
  public void makan(String makanan, int jumlah) {
  System.out.println("Hewan makan " + jumlah + " porsi " + makanan);
  }
}

class Kucing extends Hewan {
  @Override
  public void bersuara() {
    System.out.println("Meong");
  }
}

class Anjing extends Hewan {
  @Override
  public void bersuara() {
    System.out.println("Guk guk");
  }
}

public class Main {
  public static void main(String[] args) {
  Hewan hewan = new Kucing();
  hewan.bersuara(); 
  Kucing kucing = new Kucing();
  kucing.makan("ikan"); 
  kucing.makan("ikan", 2); 
  Anjing anjing = new Anjing();
  anjing.bersuara(); 
  anjing.makan("daging", 3); 
  }
}