import javax.swing.*;
import java.awt.*;

public class Settings extends JPanel {
    private static final Color BACKGROUND_COLOR = new Color(32, 32, 32);
    private static final Color TEXT_COLOR = Color.WHITE;

    public Settings() {
        setBackground(BACKGROUND_COLOR);
        setLayout(new BoxLayout(this, BoxLayout.Y_AXIS));
        setBorder(BorderFactory.createEmptyBorder(20, 20, 20, 20));

        JLabel header = new JLabel("Setting");
        header.setForeground(TEXT_COLOR);
        header.setFont(new Font("Segoe UI", Font.BOLD, 24));

        add(header);
        add(Box.createRigidArea(new Dimension(0, 20)));

        String[] features = {
                "Parentaldrth controls", "Screen time", "Content filtering",
                "Location sharing", "Activity reporting"
        };

        for (String feature : features) {
            JButton button = new JButton(feature);
            button.setAlignmentX(Component.LEFT_ALIGNMENT);
            button.setMaximumSize(new Dimension(300, 40));
            button.setBackground(new Color(45, 45, 45));
            button.setForeground(TEXT_COLOR);
            button.setFocusPainted(false);
            button.setBorderPainted(false);


            button.addMouseListener(new java.awt.event.MouseAdapter() {
                public void mouseEntered(java.awt.event.MouseEvent e) {
                    button.setBackground(new Color(0, 120, 212));
                }

                public void mouseExited(java.awt.event.MouseEvent e) {
                    button.setBackground(new Color(45, 45, 45));
                }
            });

            add(button);
            add(Box.createRigidArea(new Dimension(0, 10)));
        }
    }
}
