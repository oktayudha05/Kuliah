package praktikum5;

// Kelas Induk Kendaraan
class Kendaraan { 
    String nama; 
    int kecepatan; 
 
    public void tampilkanInfo() { 
        System.out.println("Nama Kendaraan: " + nama); 
        System.out.println("Kecepatan: " + kecepatan + " km/jam"); 
    } 
} 
 
// Kelas Turunan KenadaraanDarat
class KendaraanDarat extends Kendaraan { 
    int jumlahRoda; 
 
    @Override 
    public void tampilkanInfo() { 
        super.tampilkanInfo(); 
        System.out.println("Jumlah Roda: " + jumlahRoda); 
    } 
}

// Kelas Turunan KenadaraanLaut
class KendaraanLaut extends Kendaraan { 
    int jumlahPropeler; 
 
    @Override 
    public void tampilkanInfo() { 
        super.tampilkanInfo(); 
        System.out.println("Jumlah Propeler: " + jumlahPropeler); 
    } 
}

// Kelas Turunan Mobil 
class Mobil extends KendaraanDarat { 
    int jumlahPintu; 
 
    @Override 
    public void tampilkanInfo() { 
        super.tampilkanInfo(); 
        System.out.println("Jumlah Pintu: " + jumlahPintu); 
    }  
}

// Kelas Turunan SepedaMotor
class SepedaMotor extends KendaraanDarat { 
    String jenisMesin; 
 
    @Override 
    public void tampilkanInfo() { 
        super.tampilkanInfo(); 
        System.out.println("Jenis Mesin: " + jenisMesin); 
    } 
} 

// Kelas Turunan Kapal
class Kapal extends KendaraanLaut { 
    int jumlahPenumpang; 
 
    @Override 
    public void tampilkanInfo() { 
        super.tampilkanInfo(); 
        System.out.println("Jumlah Penumpang: " + jumlahPenumpang); 
    } 
}

// Kelas Utama
public class Main { 
    public static void main(String[] args) { 
        Mobil mobil = new Mobil(); 
        mobil.nama = "Toyota";
        mobil.jumlahRoda = 4; 
        mobil.kecepatan = 180; 
        mobil.jumlahPintu = 4; 
        mobil.tampilkanInfo();
 
        SepedaMotor motor = new SepedaMotor(); 
        motor.nama = "Yamaha";
        motor.jumlahRoda = 2; 
        motor.kecepatan = 120; 
        motor.jenisMesin = "2-tak"; 
        motor.tampilkanInfo(); 

        Kapal kapal = new Kapal();
        kapal.nama = "Kapal Budiono Siregar";
        kapal.kecepatan = 50;
        kapal.jumlahPropeler = 2;
        kapal.jumlahPenumpang = 2;
        kapal.tampilkanInfo();
    } 
}

