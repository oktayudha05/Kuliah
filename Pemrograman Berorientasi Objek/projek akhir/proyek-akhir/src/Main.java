import javax.swing.SwingUtilities;

public class Main {
    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            Tampilan pengingat = new Tampilan();
            pengingat.setVisible(true);
        });
    }
}