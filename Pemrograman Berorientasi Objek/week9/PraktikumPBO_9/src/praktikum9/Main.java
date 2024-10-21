package praktikum9;

abstract class Kendaraan {
  abstract void berjalan();

  void info() {
    System.out.println("Ini adalah kendaraan");
  }
}

class Mobil extends Kendaraan {
  @Override
  void berjalan() {
    System.out.println("Mobil sedang berjalan dengan cepat");
  }
}

class Sepeda extends Kendaraan {
  @Override
  void berjalan() {
    System.out.println("Sepeda sedang berjalan dengan pelan");
  }
}

public class Main {
  public static void main(String[] args) {
    Kendaraan mobil = new Mobil();
    Kendaraan sepeda = new Sepeda();

    mobil.berjalan();
    mobil.info();

    sepeda.berjalan();
    sepeda.info();
  }
}
