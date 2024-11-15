import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import javax.swing.border.EmptyBorder;

public class Main extends JFrame {
    // Modern color scheme
    private static final Color BACKGROUND_COLOR = new Color(32, 33, 36);  // Darker background
    private static final Color MENU_BACKGROUND = new Color(28, 29, 32);   // Slightly darker menu
    private static final Color TEXT_COLOR = new Color(232, 234, 237);     // Soft white
    private static final Color ACCENT_COLOR = new Color(138, 180, 248);   // Modern blue
    private static final Color HOVER_COLOR = new Color(44, 45, 48);       // Subtle hover


    private final JPanel mainContentPanel;
    private final CardLayout cardLayout;

    public Main() {
        setTitle("Windows Security");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setSize(1200, 800);  // Larger default size
        setLayout(new BorderLayout(15, 15));  // Add spacing between major components
        getContentPane().setBackground(BACKGROUND_COLOR);

        // Add padding around the main container
        ((JPanel)getContentPane()).setBorder(new EmptyBorder(15, 15, 15, 15));

        // Initialize card layout for main content
        cardLayout = new CardLayout();
        mainContentPanel = new JPanel(cardLayout);
        mainContentPanel.setBackground(BACKGROUND_COLOR);

        // Create and add components with shadow effect
        JPanel sideMenuPanel = createSideMenu();
        add(createPanelWithShadow(sideMenuPanel), BorderLayout.WEST);
        add(createPanelWithShadow(mainContentPanel), BorderLayout.CENTER);

        // Add panels to card layout
        mainContentPanel.add(new Home(), "Home");
        mainContentPanel.add(new Clean(), "Clean");
        mainContentPanel.add(new Troubleshoot().getSplitPane(), "Troubleshoot");
        mainContentPanel.add(new Firewall(), "FIREWALL");
        mainContentPanel.add(new Audit(), "Audit");
        mainContentPanel.add(new Remediate(), "Remediate");
        mainContentPanel.add(new Account(), "Account");
        mainContentPanel.add(new Settings(), "Settings");

        // Modern system look and feel
        try {
            UIManager.setLookAndFeel(UIManager.getSystemLookAndFeelClassName());
            setupUIDefaults();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private void setupUIDefaults() {
        UIManager.put("Button.background", ACCENT_COLOR);
        UIManager.put("Button.foreground", TEXT_COLOR);
        UIManager.put("Button.font", new Font("Segue UI", Font.PLAIN, 13));
        UIManager.put("Button.focus", new Color(0, 0, 0, 0));
        UIManager.put("Button.select", ACCENT_COLOR.darker());
    }

    private JPanel createPanelWithShadow(JComponent content) {
        JPanel shadowPanel = new JPanel() {
            @Override
            protected void paintComponent(Graphics g) {
                super.paintComponent(g);
                Graphics2D g2d = (Graphics2D) g;
                g2d.setRenderingHint(RenderingHints.KEY_ANTIALIASING, RenderingHints.VALUE_ANTIALIAS_ON);

                // Create subtle shadow effect
                int shadow = 3;
                for (int i = 0; i < shadow; i++) {
                    g2d.setColor(new Color(0, 0, 0, 20 - i * 5));
                    g2d.drawRoundRect(i, i, getWidth() - i * 2 - 1, getHeight() - i * 2 - 1, 15, 15);
                }
            }
        };
        shadowPanel.setLayout(new BorderLayout());
        shadowPanel.setOpaque(false);
        shadowPanel.add(content);
        return shadowPanel;
    }

    private JPanel createSideMenu() {
        JPanel sideMenu = new JPanel();
        sideMenu.setPreferredSize(new Dimension(280, getHeight()));
        sideMenu.setBackground(MENU_BACKGROUND);
        sideMenu.setLayout(new BoxLayout(sideMenu, BoxLayout.Y_AXIS));
        sideMenu.setBorder(BorderFactory.createEmptyBorder(10, 0, 10, 0));


        String[][] menuItems = {
                {"Home", "Home"},
                {"Clean", "Clean"},
                {"Troubleshoot", "Troubleshoot"},
                {"Firewall", "FIREWALL"},
                {"Audit", "Audit"},
                {"Remediate", "Remediate"},
                {"Account", "Account"},
                {"Settings", "Settings"}
        };

        for (String[] item : menuItems) {
            JPanel menuItem = createMenuItem(item[0], item[1]);
            sideMenu.add(menuItem);
            sideMenu.add(Box.createRigidArea(new Dimension(0, 2)));
        }

        return sideMenu;
    }

    private JPanel createMenuItem(String text, String cardName) {
        JPanel item = new JPanel();
        item.setLayout(new BoxLayout(item, BoxLayout.X_AXIS));
        item.setBackground(MENU_BACKGROUND);
        item.setBorder(BorderFactory.createEmptyBorder(12, 25, 12, 25));
        item.setMaximumSize(new Dimension(Integer.MAX_VALUE, 50));

        // Icon (you can add specific icons for each menu item)
        JLabel iconLabel = new JLabel() {
            @Override
            protected void paintComponent(Graphics g) {
                super.paintComponent(g);
                Graphics2D g2d = (Graphics2D) g;
                g2d.setRenderingHint(RenderingHints.KEY_ANTIALIASING, RenderingHints.VALUE_ANTIALIAS_ON);
                g2d.setColor(TEXT_COLOR);

                // Simple geometric icon
                int size = 16;
                g2d.drawRect(2, 2, size - 4, size - 4);
            }
        };
        iconLabel.setPreferredSize(new Dimension(20, 20));

        // Menu text
        JLabel label = new JLabel(text);
        label.setForeground(TEXT_COLOR);
        label.setFont(new Font("Segue UI", Font.PLAIN, 14));

        item.add(iconLabel);
        item.add(Box.createRigidArea(new Dimension(15, 0)));
        item.add(label);
        item.add(Box.createHorizontalGlue());

        // Hover effect with animation
        item.addMouseListener(new MouseAdapter() {
            public void mouseClicked(MouseEvent e) {
                cardLayout.show(mainContentPanel, cardName);
            }

            public void mouseEntered(MouseEvent e) {
                item.setBackground(HOVER_COLOR);
                setCursor(new Cursor(Cursor.HAND_CURSOR));
            }

            public void mouseExited(MouseEvent e) {
                item.setBackground(MENU_BACKGROUND);
                setCursor(new Cursor(Cursor.DEFAULT_CURSOR));
            }
        });

        return item;
    }


    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            Main dashboard = new Main();
            dashboard.setVisible(true);
        });
    }
}