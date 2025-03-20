import java.io.*;

public class Pengaturan {
    private static final int BATAS_DEFAULT_DUDUK_SANTAI = 15;
    
    private static final String[][] GERAKAN_PEREGANGAN = {
        {"Leher Bergoyang", "putar kepala ke kiri dan kanan 5 kali setiap arah"},
        {"Bahu Diputar", "putar bahu ke depan dan belakang 10 kali"},
        {"Lengan Direntangkan", "rentangkan lengan di atas kepala, tahan 10-15 detik"},
        {"Punggung Diputar", "putar badan ke kiri dan kanan pelan pelan"},
        {"Joget Ditempat", "angkat lututnya 30 detik"}
    };

    private int waktuDudukNyaman = BATAS_DEFAULT_DUDUK_SANTAI;
    private String pereganganFavorit = GERAKAN_PEREGANGAN[0][0];

    public void simpanPengaturan() {
        try (PrintWriter writer = new PrintWriter("setting.txt")) {
            writer.println(waktuDudukNyaman);
            writer.println(pereganganFavorit);
        } catch (IOException e) {
            System.out.println("gagal menyimpan pengaturan");
        }
    }

    public void muatPengaturan() {
        try (BufferedReader reader = new BufferedReader(new FileReader("setting.txt"))) {
            waktuDudukNyaman = Integer.parseInt(reader.readLine());
            pereganganFavorit = reader.readLine();
        } catch (IOException | NumberFormatException e) {
            waktuDudukNyaman = BATAS_DEFAULT_DUDUK_SANTAI;
            pereganganFavorit = GERAKAN_PEREGANGAN[0][0];
        }
    }

    public int getWaktuDudukNyaman() { return waktuDudukNyaman; }
    public void setWaktuDudukNyaman(int waktu) { this.waktuDudukNyaman = waktu; }
    
    public String getPereganganFavorit() { return pereganganFavorit; }
    public void setPereganganFavorit(String peregangan) { this.pereganganFavorit = peregangan; }

    public static String[][] getGerakanPeregangan() { return GERAKAN_PEREGANGAN; }
}