import java.time.LocalTime;

public class WaktuDuduk {
    private LocalTime waktuMulaiDuduk;
    
    public void mulaiPelacakan() {
        waktuMulaiDuduk = LocalTime.now();
    }
    
    public long dapatkanDurasiDuduk() {
        LocalTime waktuSekarang = LocalTime.now();
        return java.time.Duration.between(waktuMulaiDuduk, waktuSekarang).getSeconds();
    }
}