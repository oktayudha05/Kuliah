package praktikum3;

public class Main {
  public static void main(String[] args) {
    Hewan kucing = new Hewan("Abu", 2);
    kucing.suara();
    kucing.info();

    Hewan anjing = new Hewan("Zidhan", 19);
    anjing.berlari();
    anjing.info();

    Mobil lando = new Mobil("Mclaren", "mcl33", 2018);
    lando.setWarna("Orange");
    lando.info();
    lando.startEngine();

    Mobil bottas = new Mobil("Mercedes", "W10", 2019);
    bottas.setWarna("Silver");
    bottas.info();
    bottas.startEngine();
  }
}
