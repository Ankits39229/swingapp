import javax.swing.*;
import javax.swing.border.EmptyBorder;
import java.awt.*;
import java.awt.event.ActionListener;
import java.awt.geom.*;
import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Audit extends JPanel {
    // Define colors, fonts, and layout properties
    private static final Color BACKGROUND_COLOR = new Color(17, 24, 39);
    private static final Color CARD_BACKGROUND = new Color(31, 41, 55);
    private static final Color BUTTON_COLOR = new Color(220, 38, 38);      // Red
    private static final Color BUTTON_HOVER_COLOR = new Color(239, 68, 68); // Light red
    private static final Color TEXT_COLOR = new Color(243, 244, 246);
    private static final Color SECONDARY_TEXT = new Color(156, 163, 175);
    private static final Color PROGRESS_BACKGROUND = new Color(55, 65, 81);
    private static final Color PROGRESS_COLOR = new Color(239, 68, 68);    // Red
    private static final Color ACCENT_GLOW = new Color(220, 38, 38, 30);   // Red with transparency

    private static final Font HEADER_FONT = new Font("Segoe UI", Font.BOLD, 32);
    private static final Font BUTTON_FONT = new Font("Segoe UI", Font.BOLD, 14);
    private static final Font PROGRESS_FONT = new Font("Segoe UI", Font.BOLD, 12);
    private static final Font CARD_TITLE_FONT = new Font("Segoe UI", Font.BOLD, 18);
    private static final Font DESC_FONT = new Font("Segoe UI", Font.PLAIN, 13);

    private static final int PADDING = 20;
    private static final int BUTTON_HEIGHT = 40;
    private static final int BUTTON_WIDTH = 200;
    private static final int PROGRESS_HEIGHT = 6;

    private JTextArea outputArea;
    private JProgressBar progressBar;
    private JLabel statusLabel;

    public Audit() {
        setBackground(BACKGROUND_COLOR);
        setLayout(new BorderLayout());
        setBorder(new EmptyBorder(PADDING, PADDING, PADDING, PADDING));

        JPanel mainContent = new JPanel();
        mainContent.setLayout(new BoxLayout(mainContent, BoxLayout.Y_AXIS));
        mainContent.setBackground(BACKGROUND_COLOR);

        // Add header
        JPanel headerPanel = createHeaderPanel();
        mainContent.add(headerPanel);
        mainContent.add(Box.createRigidArea(new Dimension(0, PADDING * 2)));

        // Create main control panel
        JPanel controlPanel = createControlPanel();
        mainContent.add(controlPanel);
        mainContent.add(Box.createRigidArea(new Dimension(0, PADDING)));

        // Create output area
        JPanel outputPanel = createOutputPanel();
        mainContent.add(outputPanel);

        add(mainContent, BorderLayout.CENTER);
    }

    private JPanel createHeaderPanel() {
        JPanel headerPanel = new JPanel() {
            @Override
            protected void paintComponent(Graphics g) {
                super.paintComponent(g);
                Graphics2D g2 = (Graphics2D) g.create();
                g2.setRenderingHint(RenderingHints.KEY_ANTIALIASING, RenderingHints.VALUE_ANTIALIAS_ON);

                Point2D center = new Point2D.Float((float) getWidth() / 2, 0);
                float[] dist = {0.0f, 1.0f};
                Color[] colors = {ACCENT_GLOW, new Color(0, 0, 0, 0)};
                RadialGradientPaint glow = new RadialGradientPaint(center, getHeight(), dist, colors);

                g2.setPaint(glow);
                g2.fillOval(getWidth()/2 - 100, -100, 200, 200);
                g2.dispose();
            }
        };

        headerPanel.setLayout(new BoxLayout(headerPanel, BoxLayout.Y_AXIS));
        headerPanel.setBackground(BACKGROUND_COLOR);
        headerPanel.setPreferredSize(new Dimension(getWidth(), 100));

        JLabel header = new JLabel("Security Remediation");
        header.setForeground(TEXT_COLOR);
        header.setFont(HEADER_FONT);
        header.setAlignmentX(Component.CENTER_ALIGNMENT);

        JLabel subtitle = new JLabel("Remediate your system Configuration");
        subtitle.setForeground(SECONDARY_TEXT);
        subtitle.setFont(DESC_FONT);
        subtitle.setAlignmentX(Component.CENTER_ALIGNMENT);

        headerPanel.add(Box.createVerticalGlue());
        headerPanel.add(header);
        headerPanel.add(Box.createRigidArea(new Dimension(0, 8)));
        headerPanel.add(subtitle);
        headerPanel.add(Box.createVerticalGlue());

        return headerPanel;
    }

    private JPanel createControlPanel() {
        JPanel controlPanel = new JPanel();
        controlPanel.setLayout(new BoxLayout(controlPanel, BoxLayout.Y_AXIS));
        controlPanel.setBackground(CARD_BACKGROUND);
        controlPanel.setBorder(new EmptyBorder(PADDING, PADDING, PADDING, PADDING));

        // Create and configure progress bar
        progressBar = new JProgressBar();
        progressBar.setBackground(PROGRESS_BACKGROUND);
        progressBar.setForeground(PROGRESS_COLOR);
        progressBar.setPreferredSize(new Dimension(BUTTON_WIDTH, PROGRESS_HEIGHT));
        progressBar.setAlignmentX(Component.CENTER_ALIGNMENT);

        // Create status label
        statusLabel = new JLabel("Ready");
        statusLabel.setFont(PROGRESS_FONT);
        statusLabel.setForeground(SECONDARY_TEXT);
        statusLabel.setAlignmentX(Component.CENTER_ALIGNMENT);

        // Create scan button
        JButton scanButton = createScanButton(e -> startScan());
        scanButton.setAlignmentX(Component.CENTER_ALIGNMENT);

        // Add components to control panel
        controlPanel.add(scanButton);
        controlPanel.add(Box.createRigidArea(new Dimension(0, 15)));
        controlPanel.add(progressBar);
        controlPanel.add(Box.createRigidArea(new Dimension(0, 8)));
        controlPanel.add(statusLabel);

        return controlPanel;
    }

    private JPanel createOutputPanel() {
        JPanel outputPanel = new JPanel();
        outputPanel.setLayout(new BorderLayout());
        outputPanel.setBackground(CARD_BACKGROUND);
        outputPanel.setBorder(new EmptyBorder(PADDING, PADDING, PADDING, PADDING));

        outputArea = new JTextArea();
        outputArea.setBackground(BACKGROUND_COLOR);
        outputArea.setForeground(TEXT_COLOR);
        outputArea.setFont(new Font("Monospace", Font.PLAIN, 12));
        outputArea.setEditable(false);
        outputArea.setLineWrap(true);
        outputArea.setWrapStyleWord(true);

        JScrollPane scrollPane = new JScrollPane(outputArea);
        scrollPane.setPreferredSize(new Dimension(600, 300));
        scrollPane.setBorder(BorderFactory.createLineBorder(CARD_BACKGROUND));

        outputPanel.add(scrollPane, BorderLayout.CENTER);
        return outputPanel;
    }

    private JButton createScanButton(ActionListener action) {
        JButton button = new JButton("Remediate Audit");
        button.setFont(BUTTON_FONT);
        button.setBackground(BUTTON_COLOR);
        button.setForeground(Color.WHITE);
        button.setFocusPainted(false);
        button.setPreferredSize(new Dimension(BUTTON_WIDTH, BUTTON_HEIGHT));

        button.addMouseListener(new java.awt.event.MouseAdapter() {
            public void mouseEntered(java.awt.event.MouseEvent evt) {
                button.setBackground(BUTTON_HOVER_COLOR);
            }
            public void mouseExited(java.awt.event.MouseEvent evt) {
                button.setBackground(BUTTON_COLOR);
            }
        });

        button.addActionListener(action);
        return button;
    }

    private void startScan() {
        SwingWorker<Void, String> worker = new SwingWorker<>() {
            @Override
            protected Void doInBackground() throws Exception {
                statusLabel.setText("In Progress...");
                progressBar.setIndeterminate(true);
                outputArea.setText("");

                try {
                    ProcessBuilder pb = new ProcessBuilder("python", "PythonScripts/18.5.py");
                    Process process = pb.start();

                    BufferedReader reader = new BufferedReader(
                            new InputStreamReader(process.getInputStream()));
                    String line;
                    while ((line = reader.readLine()) != null) {
                        publish(line);
                    }

                    process.waitFor();
                } catch (Exception e) {
                    publish("Error: " + e.getMessage());
                    e.printStackTrace();
                }

                return null;
            }

            @Override
            protected void process(java.util.List<String> chunks) {
                for (String line : chunks) {
                    outputArea.append(line + "\n");
                }
            }

            @Override
            protected void done() {
                progressBar.setIndeterminate(false);
                progressBar.setValue(100);
                statusLabel.setText("Completed");
            }
        };

        worker.execute();
    }

//    public static void main(String[] args) {
//        SwingUtilities.invokeLater(() -> {
//            JFrame frame = new JFrame("Security Audit");
//            frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
//            frame.getContentPane().add(new Audit());
//            frame.setSize(800, 600);
//            frame.setLocationRelativeTo(null);
//            frame.setVisible(true);
//        });
//    }
}