package tugas9;

abstract class Hewan {
  abstract void suara();

  void info() {
    System.out.println("Ini adalah hewan");
  }
}

class Kucing extends Hewan {
  @Override
  void suara() {
    System.out.println("meong");
  }
}

class Anjing extends Hewan {
  @Override
  void suara() {
    System.out.println("guk guk");
  }
}

public class Main {
  public static void main(String[] args) {
    Hewan kucing = new Kucing();
    Hewan anjing = new Anjing();

    kucing.suara();

    anjing.suara();
  }
}
