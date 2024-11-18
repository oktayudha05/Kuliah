package praktikum11;

class Pengarang {
  private String namaPengarang;
  public Pengarang(String namaPengarang) {
      this.namaPengarang = namaPengarang;
  }
  public String getInfoPengarang() {
      return "Pengarang: " + namaPengarang;
  }
}

class Buku {
  private String judul;
  private Pengarang pengarang;

  public Buku(String judul, Pengarang pengarang) {
      this.judul = judul;
      this.pengarang = pengarang;
  }
  public void infoBuku() {
      System.out.println("Judul Buku: " + judul + ", " + pengarang.getInfoPengarang());
  }
}

class Perpustakaan {
  private Buku[] daftarBuku;
  private int jumlahBuku;

  public Perpustakaan(int kapasitas) {
      daftarBuku = new Buku[kapasitas];
      jumlahBuku = 0;
  }
  public void tambahBuku(Buku buku) {
      if (jumlahBuku < daftarBuku.length) {
          daftarBuku[jumlahBuku] = buku;
          jumlahBuku++;
      } else {
          System.out.println("Perpustakaan penuh! Tidak bisa menambahkan buku.");
      }
  }
  public void infoPerpustakaan() {
      if (jumlahBuku == 0) {
          System.out.println("Perpustakaan kosong.");
      } else {
          System.out.println("Daftar Buku di Perpustakaan:");
          for (int i = 0; i < jumlahBuku; i++) {
              daftarBuku[i].infoBuku();
          }
      }
  }
  public void hapusPerpustakaan() {
      for (int i = 0; i < jumlahBuku; i++) {
          daftarBuku[i] = null;
      }
      jumlahBuku = 0;
      System.out.println("Perpustakaan telah dihapus beserta semua bukunya.");
  }
}

public class main {
  public static void main(String[] args) {
      Pengarang pengarang1 = new Pengarang("J.K. Rowling");
      Pengarang pengarang2 = new Pengarang("George Orwell");

      Buku buku1 = new Buku("Harry Potter", pengarang1);
      Buku buku2 = new Buku("1984", pengarang2);

      Perpustakaan perpustakaan = new Perpustakaan(5);

      perpustakaan.tambahBuku(buku1);
      perpustakaan.tambahBuku(buku2);

      perpustakaan.infoPerpustakaan();
      perpustakaan.hapusPerpustakaan();

      perpustakaan.infoPerpustakaan();
  }
}
