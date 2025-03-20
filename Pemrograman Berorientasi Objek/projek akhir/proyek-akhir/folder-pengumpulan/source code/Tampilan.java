import javax.swing.*;
import java.awt.*;
import java.util.ArrayList;
import java.util.Arrays;

public class Tampilan extends JFrame {
    private JLabel labelWaktu;
    private JButton tombolMulai, tombolLihatLog, tombolPengaturan;
    private JComboBox<String> pilihanLatihan;

    private Pengaturan pengaturan;
    private Catatan catatan;

    private Timer timerDetik, timerAktivitas;
    private int detikBerlalu = 0;

    public Tampilan() {
        setTitle("Pengingat Peregangan");
        setSize(500, 400);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(new FlowLayout());

        pengaturan = new Pengaturan();
        pengaturan.muatPengaturan();
        catatan = new Catatan();

        labelWaktu = new JLabel("Waktu Duduk: 00:00:00");
        labelWaktu.setFont(new Font("Arial", Font.BOLD, 20));

        tombolMulai = new JButton("Mulai Duduk");
        tombolLihatLog = new JButton("Riwayat Aktivitas");
        tombolPengaturan = new JButton("Pengaturan");

        pilihanLatihan = new JComboBox<>();
        for (String[] latihan : Pengaturan.getGerakanPeregangan()) {
            pilihanLatihan.addItem(latihan[0]);
        }

        add(labelWaktu);
        add(pilihanLatihan);
        add(tombolLihatLog);
        add(tombolPengaturan);
        add(tombolMulai);
        setupListeners();
        setupTimers();
    }

    private void setupListeners() {
        tombolMulai.addActionListener(e -> mulaiPemantauan());
        tombolLihatLog.addActionListener(e -> tampilkanLogAktivitas());
        tombolPengaturan.addActionListener(e -> tampilkanDialogPengaturan());
    }

    private void setupTimers() {
        timerDetik = new Timer(1000, e -> {
            detikBerlalu++;
            updateLabelWaktu();
        });

        timerAktivitas = new Timer(1000, e -> {
            int waktuBatas = pengaturan.getWaktuDudukNyaman();
            if (detikBerlalu >= waktuBatas) {
                String latihanDipilih = (String) pilihanLatihan.getSelectedItem();
                tampilkanPengingatPeregangan(latihanDipilih);
                catatan.catatAktivitas(latihanDipilih);
                detikBerlalu = 0;
            }
        });
    }

    private void updateLabelWaktu() {
        int jam = detikBerlalu / 3600;
        int menit = (detikBerlalu % 3600) / 60;
        int detik = detikBerlalu % 60;
        labelWaktu.setText(String.format("Waktu Duduk: %02d:%02d:%02d", jam, menit, detik));
    }

    private void mulaiPemantauan() {
        detikBerlalu = 0;
        timerDetik.start();
        timerAktivitas.start();
        catatan.catatAktivitas("Pemantauan duduk dimulai.");
        JOptionPane.showMessageDialog(this, "Pemantauan duduk dimulai!");
    }

    private void tampilkanPengingatPeregangan(String latihan) {
        String detailLatihan = "";
        for (String[] item : Pengaturan.getGerakanPeregangan()) {
            if (item[0].equals(latihan)) {
                detailLatihan = item[1];
                break;
            }
        }
        JOptionPane.showMessageDialog(this,
                "Waktunya bergerak!\n\n" + latihan + "\n" + detailLatihan,
                "Peringatan Peregangan",
                JOptionPane.INFORMATION_MESSAGE);
    }

    private void tampilkanLogAktivitas() {
        String[] logArray = catatan.getLog();
        ArrayList<String> logs = new ArrayList<>(Arrays.asList(logArray));
        JTextArea textArea = new JTextArea(20, 40);
        textArea.setEditable(false);
        for (String log : logs) {
            textArea.append(log + "\n");
        }
        JScrollPane scrollPane = new JScrollPane(textArea);
        JOptionPane.showMessageDialog(this, scrollPane, "Log Aktivitas", JOptionPane.PLAIN_MESSAGE);
    }

    private void tampilkanDialogPengaturan() {
        JPanel panel = new JPanel(new GridLayout(0, 2));
        JTextField fieldWaktuDuduk = new JTextField(String.valueOf(pengaturan.getWaktuDudukNyaman()));
        JComboBox<String> comboLatihan = new JComboBox<>();
        for (String[] latihan : Pengaturan.getGerakanPeregangan()) {
            comboLatihan.addItem(latihan[0]);
        }
        comboLatihan.setSelectedItem(pengaturan.getPereganganFavorit());

        panel.add(new JLabel("Waktu Duduk Maksimal (detik):"));
        panel.add(fieldWaktuDuduk);
        panel.add(new JLabel("Latihan Pilihan:"));
        panel.add(comboLatihan);

        int result = JOptionPane.showConfirmDialog(this, panel,
                "Pengaturan", JOptionPane.OK_CANCEL_OPTION);

        if (result == JOptionPane.OK_OPTION) {
            try {
                int waktuDuduk = Integer.parseInt(fieldWaktuDuduk.getText());
                String latihanDipilih = (String) comboLatihan.getSelectedItem();
                pengaturan.setWaktuDudukNyaman(waktuDuduk);
                pengaturan.setPereganganFavorit(latihanDipilih);
                pengaturan.simpanPengaturan();
                pilihanLatihan.setSelectedItem(latihanDipilih);
                JOptionPane.showMessageDialog(this, "Pengaturan disimpan!");
            } catch (NumberFormatException ex) {
                JOptionPane.showMessageDialog(this, "Masukkan angka yang valid untuk waktu duduk!");
            }
        }
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            Tampilan tampilan = new Tampilan();
            tampilan.setVisible(true);
        });
    }
}
