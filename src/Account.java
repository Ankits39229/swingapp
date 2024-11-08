import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class Account extends JPanel {
    private static final Color BACKGROUND_COLOR = new Color(32, 32, 32);
    private static final Color TEXT_COLOR = Color.WHITE;
    private static final Color ICON_BLUE = new Color(0, 120, 212);

    public Account() {
        setBackground(BACKGROUND_COLOR);
        setLayout(new BoxLayout(this, BoxLayout.Y_AXIS));
        setBorder(BorderFactory.createEmptyBorder(20, 20, 20, 20));

        JLabel header = new JLabel("Account Protection");
        header.setForeground(TEXT_COLOR);
        header.setFont(new Font("Segoe UI", Font.BOLD, 24));
        add(header);

        add(Box.createRigidArea(new Dimension(0, 20)));

        // Define account protection features
        String[] features = {
                "Windows Hello", "Dynamic Lock", "Security Key",
                "Password Settings", "App Passwords"
        };

        for (String feature : features) {
            JButton button = new JButton(feature);
            button.setAlignmentX(Component.LEFT_ALIGNMENT);
            button.setMaximumSize(new Dimension(300, 40));
            button.setBackground(new Color(45, 45, 45));
            button.setForeground(TEXT_COLOR);
            button.setFocusPainted(false);
            button.setBorderPainted(false);

            button.addActionListener(e -> showFeatureDialog(feature));
            button.addMouseListener(new java.awt.event.MouseAdapter() {
                public void mouseEntered(java.awt.event.MouseEvent e) {
                    button.setBackground(ICON_BLUE);
                }
                public void mouseExited(java.awt.event.MouseEvent e) {
                    button.setBackground(new Color(45, 45, 45));
                }
            });

            add(button);
            add(Box.createRigidArea(new Dimension(0, 10)));
        }
    }

    private void showFeatureDialog(String feature) {
        JDialog dialog = new JDialog((Frame) SwingUtilities.getWindowAncestor(this), feature, true);
        dialog.setSize(400, 300);
        dialog.setLocationRelativeTo(this);

        JPanel panel = new JPanel();
        panel.setBackground(BACKGROUND_COLOR);
        panel.setLayout(new BorderLayout(20, 20));
        panel.setBorder(BorderFactory.createEmptyBorder(20, 20, 20, 20));

        JLabel label = new JLabel("Configuring: " + feature);
        label.setForeground(TEXT_COLOR);
        label.setFont(new Font("Segoe UI", Font.BOLD, 16));

        JButton closeButton = new JButton("Close");
        closeButton.addActionListener(e -> dialog.dispose());

        panel.add(label, BorderLayout.CENTER);
        panel.add(closeButton, BorderLayout.SOUTH);

        dialog.add(panel);
        dialog.setVisible(true);
    }
}
