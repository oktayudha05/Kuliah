import java.io.*;
import java.time.*;
import java.time.format.DateTimeFormatter;

public class Catatan {
    private static final String FILE_LOG_AKTIVITAS = "log_aktivitas.txt";

    public void catatAktivitas(String aktivitas) {
        try (PrintWriter pencatat = new PrintWriter(new FileWriter(FILE_LOG_AKTIVITAS, true))) {
            LocalDateTime waktuSekarang = LocalDateTime.now();
            DateTimeFormatter formatWaktu = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss");
            
            pencatat.println(waktuSekarang.format(formatWaktu) + " - " + aktivitas);
        } catch (IOException e) {
            System.out.println("gagal mencacat aktivitas!");
        }
    }

    public String[] getLog() {
        try {
            return java.nio.file.Files.readAllLines(
                java.nio.file.Paths.get(FILE_LOG_AKTIVITAS)
            ).toArray(new String[0]);
        } catch (IOException e) {
            return new String[]{"Belum ada aktivitas yang tercatat"};
        }
    }
}