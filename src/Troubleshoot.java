import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.Component;
import java.awt.Cursor;
import java.awt.Dimension;
import java.awt.Font;
import java.awt.GridLayout;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import javax.swing.BorderFactory;
import javax.swing.Box;
import javax.swing.BoxLayout;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JSplitPane;
import javax.swing.SwingUtilities;
import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Troubleshoot {
    private static final Color BACKGROUND_COLOR = new Color(18, 18, 18);
    private static final Color PANEL_BACKGROUND = new Color(30, 30, 30);
    private static final Color TEXT_COLOR = new Color(255, 255, 255);
    private static final Color SECONDARY_TEXT_COLOR = new Color(170, 170, 170);
    private static final Color BUTTON_COLOR = new Color(238, 10, 10);
    private final VirusThreatProtectionPanel virusPanel;
    private final FirewallNetworkPanel firewallPanel;
    private final AccountProtectionPanel accountPanel;
    private final AppBrowserControlPanel appBrowserPanel;
    private final DeviceSecurityPanel deviceSecurityPanel;
    private final DevicePerformanceHealthPanel devicePerformancePanel;
    private final FamilyOptionsPanel familyPanel;
    private final ProtectionHistoryPanel historyPanel;
    private final SettingsPanel settingsPanel;
    private final JSplitPane splitPane;
    private final JPanel[] sidePanels;

    public Troubleshoot(JPanel... sidePanels) {
        this.sidePanels = sidePanels;
        this.virusPanel = new VirusThreatProtectionPanel();
        this.firewallPanel = new FirewallNetworkPanel();
        this.accountPanel = new AccountProtectionPanel();
        this.appBrowserPanel = new AppBrowserControlPanel();
        this.deviceSecurityPanel = new DeviceSecurityPanel();
        this.devicePerformancePanel = new DevicePerformanceHealthPanel();
        this.familyPanel = new FamilyOptionsPanel();
        this.historyPanel = new ProtectionHistoryPanel();
        this.settingsPanel = new SettingsPanel();
        JPanel mainPanel = new JPanel(new BorderLayout());
        mainPanel.setBackground(BACKGROUND_COLOR);
        mainPanel.setBorder(BorderFactory.createEmptyBorder(20, 20, 20, 20));
        JPanel headerPanel = this.createHeaderPanel();
        mainPanel.add(headerPanel, "North");
        JPanel gridPanel = this.createMainGridPanel();
        mainPanel.add(gridPanel, "Center");
        this.splitPane = new JSplitPane(1, mainPanel, new JPanel());
        this.splitPane.setDividerLocation(800);
        this.splitPane.setOneTouchExpandable(true);
        this.splitPane.setBackground(BACKGROUND_COLOR);
        this.splitPane.setRightComponent(new JPanel());
    }

    private JPanel createHeaderPanel() {
        JPanel headerPanel = new JPanel();
        headerPanel.setLayout(new BoxLayout(headerPanel, 1));
        headerPanel.setBackground(BACKGROUND_COLOR);
        JLabel titleLabel = new JLabel("Security at a Glance");
        titleLabel.setForeground(TEXT_COLOR);
        titleLabel.setFont(new Font("Segoe UI", 1, 24));
        JLabel subtitleLabel = new JLabel("<html>See what's happening with the security and health of your device<br>and take any actions needed.</html>");
        subtitleLabel.setForeground(SECONDARY_TEXT_COLOR);
        subtitleLabel.setFont(new Font("Segoe UI", 0, 14));
        headerPanel.add(titleLabel);
        headerPanel.add(Box.createVerticalStrut(10));
        headerPanel.add(subtitleLabel);
        return headerPanel;
    }

    private JPanel createMainGridPanel() {
        JPanel mainPanel = new JPanel(new GridLayout(3, 3, 20, 20));
        mainPanel.setBackground(BACKGROUND_COLOR);
        String[][] items = new String[][]{{"Virus & Threat Protection", "Manage your antivirus settings and scan your device for threats."}, {"Account Protection", "Manage your user accounts and security settings."}, {"Firewall & Network Protection", "Configure your firewall settings and monitor network activity."}, {"App & Browser Control", "Manage your app permissions and browser security settings."}, {"Device Security", "View status and manage hardware security features."}, {"Device Performance & Health", "Monitor the performance and health of your device."}, {"Family Options", "Manage how your family uses their devices."}, {"Protection History", "View latest protection actions and recommendations."}, {"Settings", "Adjust your security settings and preferences."}};

        for(int i = 0; i < items.length; ++i) {
            String title = items[i][0];
            String description = items[i][1];
            mainPanel.add(this.createItemPanel(title, description, i));
        }

        return mainPanel;
    }

    private JPanel createItemPanel(String title, String description, int index) {
        JPanel panel = new JPanel();
        panel.setLayout(new BoxLayout(panel, 1));
        panel.setBackground(PANEL_BACKGROUND);
        panel.setBorder(BorderFactory.createEmptyBorder(10, 10, 10, 10));
        JLabel iconLabel = new JLabel("■");
        iconLabel.setForeground(BUTTON_COLOR);
        iconLabel.setFont(new Font("Segoe UI", 1, 30));
        JButton titleButton = new JButton(title);
        titleButton.setForeground(TEXT_COLOR);
        titleButton.setFont(new Font("Segoe UI", 1, 14));
        titleButton.setBackground(PANEL_BACKGROUND);
        titleButton.setBorderPainted(false);
        titleButton.setFocusPainted(false);
        titleButton.setHorizontalAlignment(2);
        titleButton.addActionListener((e) -> {
            this.openSideBar(index);
        });
        JLabel descLabel = new JLabel("<html>" + description + "</html>");
        descLabel.setForeground(SECONDARY_TEXT_COLOR);
        descLabel.setFont(new Font("Segoe UI", 0, 12));
        panel.add(iconLabel);
        panel.add(Box.createVerticalStrut(10));
        panel.add(titleButton);
        panel.add(Box.createVerticalStrut(5));
        panel.add(descLabel);
        return panel;
    }

    private void openSideBar(int index) {
        JPanel selectedPanel = null;
        switch (index) {
            case 0 -> selectedPanel = this.virusPanel;
            case 1 -> selectedPanel = this.accountPanel;
            case 2 -> selectedPanel = this.firewallPanel;
            case 3 -> selectedPanel = this.appBrowserPanel;
            case 4 -> selectedPanel = this.deviceSecurityPanel;
            case 5 -> selectedPanel = this.devicePerformancePanel;
            case 6 -> selectedPanel = this.familyPanel;
            case 7 -> selectedPanel = this.historyPanel;
            case 8 -> selectedPanel = this.settingsPanel;
        }

        if (selectedPanel != null) {
            this.splitPane.setRightComponent(selectedPanel);
        } else {
            JPanel placeholder = new JPanel(new BorderLayout());
            placeholder.setBackground(PANEL_BACKGROUND);
            JLabel noInfoLabel = new JLabel("No Information Available");
            noInfoLabel.setForeground(TEXT_COLOR);
            noInfoLabel.setHorizontalAlignment(0);
            placeholder.add(noInfoLabel, "Center");
            this.splitPane.setRightComponent(placeholder);
        }

        this.splitPane.setDividerLocation(this.splitPane.getWidth() - 300);
        this.splitPane.revalidate();
        this.splitPane.repaint();
    }

    public JSplitPane getSplitPane() {
        return this.splitPane;
    }

    private JPanel createPlaceholderPanel(String message) {
        JPanel placeholder = new JPanel(new BorderLayout());
        placeholder.setBackground(PANEL_BACKGROUND);
        JLabel noInfoLabel = new JLabel(message);
        noInfoLabel.setForeground(TEXT_COLOR);
        noInfoLabel.setHorizontalAlignment(0);
        placeholder.add(noInfoLabel, "Center");
        return placeholder;
    }

//    public static void main(String[] args) {
//        SwingUtilities.invokeLater(() -> {
//            JFrame frame = new JFrame("Security App");
//            frame.setDefaultCloseOperation(3);
//            frame.setSize(1200, 800);
//            Troubleshoot troubleshoot = new Troubleshoot(new JPanel[0]);
//            frame.setContentPane(troubleshoot.getSplitPane());
//            frame.setVisible(true);
//        });
//    }

    public class VirusThreatProtectionPanel extends BaseSidebarPanel {
        public VirusThreatProtectionPanel() {
            super("Virus & Threat Protection");
        }

        protected JPanel createContentPanel() {
            JPanel contentPanel = new JPanel(new BorderLayout(0, 20));
            contentPanel.setBackground(PANEL_BACKGROUND);
            contentPanel.add(this.createScanSection(), BorderLayout.NORTH);
            contentPanel.add(this.createInfoArea(), BorderLayout.CENTER);
            return contentPanel;
        }

        private JPanel createScanSection() {
            JPanel scanPanel = new JPanel(new BorderLayout(0, 10));
            scanPanel.setBackground(PANEL_BACKGROUND);
            JButton scanButton = new JButton("Quick Scan");
            scanButton.setPreferredSize(new Dimension(200, 40));
            scanButton.setBackground(BUTTON_COLOR);
            scanButton.setForeground(Color.WHITE);
            scanButton.setFocusPainted(false);
            scanButton.setBorderPainted(false);
            scanButton.setCursor(new Cursor(Cursor.HAND_CURSOR));

            JLabel statusLabel = new JLabel("Ready to scan");
            statusLabel.setForeground(SECONDARY_TEXT_COLOR);
            statusLabel.setHorizontalAlignment(SwingConstants.CENTER);

            scanButton.addActionListener(new ActionListener() {
                @Override
                public void actionPerformed(ActionEvent e) {
                    scanButton.setText("Scanning...");
                    statusLabel.setText("Scan in progress...");

                    SwingUtilities.invokeLater(() -> {
                        try {
                            ProcessBuilder processBuilder = new ProcessBuilder("python", "appScripts/ae.py");
                            Process process = processBuilder.start();
                            BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));

                            StringBuilder output = new StringBuilder();
                            String line;
                            while ((line = reader.readLine()) != null) {
                                output.append(line).append("\n");
                            }
                            reader.close();

                            scanButton.setText("Quick Scan");
                            if (output.toString().isEmpty()) {
                                statusLabel.setText("Scan Complete. No Threats Found.");
                            } else {
                                statusLabel.setText("<html>Scan Complete.<br>" + output.toString().replaceAll("\n", "<br>") + "</html>");
                            }
                        } catch (Exception ex) {
                            ex.printStackTrace();
                            statusLabel.setText("Error: Could not complete scan.");
                        }
                    });
                }
            });

            scanPanel.add(scanButton, BorderLayout.CENTER);
            scanPanel.add(statusLabel, BorderLayout.SOUTH);
            return scanPanel;
        }

        private JPanel createInfoArea() {
            JPanel infoPanel = new JPanel(new BorderLayout());
            infoPanel.setBackground(PANEL_BACKGROUND);
            JLabel infoLabel = new JLabel("<html>Last scan: 1 hour ago<br>No threats detected</html>");
            infoLabel.setForeground(SECONDARY_TEXT_COLOR);
            infoLabel.setHorizontalAlignment(SwingConstants.CENTER);
            infoPanel.add(infoLabel, BorderLayout.CENTER);
            return infoPanel;
        }
    }

    class FirewallNetworkPanel extends BaseSidebarPanel {
        public FirewallNetworkPanel() {
            super("Firewall");
        }

        protected JPanel createContentPanel() {
            JPanel contentPanel = new JPanel(new BorderLayout(0, 20));
            contentPanel.setBackground(PANEL_BACKGROUND);
            contentPanel.add(this.createScanSection(), "North");
            contentPanel.add(this.createInfoArea(), "Center");
            return contentPanel;
        }

        private JPanel createScanSection() {
            JPanel scanPanel = new JPanel(new BorderLayout(0, 10));
            scanPanel.setBackground(PANEL_BACKGROUND);
            JButton scanButton = new JButton("Check");
            scanButton.setPreferredSize(new Dimension(200, 40));
            scanButton.setBackground(BUTTON_COLOR);
            scanButton.setForeground(Color.WHITE);
            scanButton.setFocusPainted(false);
            scanButton.setBorderPainted(false);
            scanButton.setCursor(new Cursor(12));
            JLabel statusLabel = new JLabel("Ready to scan");
            statusLabel.setForeground(SECONDARY_TEXT_COLOR);
            statusLabel.setHorizontalAlignment(0);
            scanButton.addActionListener((e) -> {
                scanButton.setText("Scanning...");
                statusLabel.setText("Scan in progress...");
                SwingUtilities.invokeLater(() -> {
                    try {
                        Process process = Runtime.getRuntime().exec("cmd /c echo Performing Quick Scan...");
                        BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));

                        String line;
                        while((line = reader.readLine()) != null) {
                            System.out.println(line);
                        }

                        scanButton.setText("Check");
                        statusLabel.setText("Scan Complete.");
                    } catch (Exception var5) {
                        Exception ex = var5;
                        ex.printStackTrace();
                    }

                });
            });
            scanPanel.add(scanButton, "Center");
            scanPanel.add(statusLabel, "South");
            return scanPanel;
        }

        private JPanel createInfoArea() {
            JPanel infoPanel = new JPanel(new BorderLayout());
            infoPanel.setBackground(PANEL_BACKGROUND);
            JLabel infoLabel = new JLabel("<html>Last scan: 1 hour ago<br>No threats detected</html>");
            infoLabel.setForeground(SECONDARY_TEXT_COLOR);
            infoLabel.setHorizontalAlignment(0);
            infoPanel.add(infoLabel, "Center");
            return infoPanel;
        }
    }

    class AccountProtectionPanel extends BaseSidebarPanel {
        public AccountProtectionPanel() {
            super("Account Protection");
        }

        protected JPanel createContentPanel() {
            return Troubleshoot.this.createPlaceholderPanel("Manage your user accounts and security settings.");
        }
    }

    class AppBrowserControlPanel extends BaseSidebarPanel {
        public AppBrowserControlPanel() {
            super("App & Browser Control");
        }

        protected JPanel createContentPanel() {
            return Troubleshoot.this.createPlaceholderPanel("Manage your app permissions and browser security settings.");
        }
    }

    class DeviceSecurityPanel extends BaseSidebarPanel {
        public DeviceSecurityPanel() {
            super("Device Security");
        }

        protected JPanel createContentPanel() {
            return Troubleshoot.this.createPlaceholderPanel("View status and manage hardware security features.");
        }
    }

    class DevicePerformanceHealthPanel extends BaseSidebarPanel {
        public DevicePerformanceHealthPanel() {
            super("Device Performance & Health");
        }

        protected JPanel createContentPanel() {
            return Troubleshoot.this.createPlaceholderPanel("Monitor the performance and health of your device.");
        }
    }

    class FamilyOptionsPanel extends BaseSidebarPanel {
        public FamilyOptionsPanel() {
            super("Family Options");
        }

        protected JPanel createContentPanel() {
            return Troubleshoot.this.createPlaceholderPanel("Manage how your family uses their devices.");
        }
    }

    class ProtectionHistoryPanel extends BaseSidebarPanel {
        public ProtectionHistoryPanel() {
            super("Protection History");
        }

        protected JPanel createContentPanel() {
            return Troubleshoot.this.createPlaceholderPanel("View latest protection actions and recommendations.");
        }
    }

    class SettingsPanel extends BaseSidebarPanel {
        public SettingsPanel() {
            super("Settings");
        }

        protected JPanel createContentPanel() {
            return Troubleshoot.this.createPlaceholderPanel("Adjust your security settings and preferences.");
        }
    }

    abstract class BaseSidebarPanel extends JPanel {
        protected static final Color PANEL_BACKGROUND = new Color(30, 30, 30);
        protected static final Color TEXT_COLOR = new Color(255, 255, 255);
        protected static final Color SECONDARY_TEXT_COLOR = new Color(170, 170, 170);
        protected static final Color BUTTON_COLOR = new Color(238, 10, 10);

        public BaseSidebarPanel(String title) {
            this.setLayout(new BorderLayout(10, 10));
            this.setBackground(PANEL_BACKGROUND);
            this.setMinimumSize(new Dimension(300, 500));
            this.setBorder(BorderFactory.createEmptyBorder(20, 20, 20, 20));
            JPanel headerPanel = this.createHeader(title);
            this.add(headerPanel, "North");
            JPanel contentPanel = this.createContentPanel();
            this.add(contentPanel, "Center");
        }

        protected JPanel createHeader(String title) {
            JPanel headerPanel = new JPanel(new BorderLayout());
            headerPanel.setBackground(PANEL_BACKGROUND);
            JLabel headerLabel = new JLabel(title);
            headerLabel.setForeground(TEXT_COLOR);
            headerLabel.setFont(new Font("Segoe UI", 1, 18));
            headerLabel.setBorder(BorderFactory.createEmptyBorder(0, 0, 20, 0));
            headerPanel.add(headerLabel, "Center");
            return headerPanel;
        }

        protected abstract JPanel createContentPanel();
    }
}
