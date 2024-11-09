import javax.swing.*;
import javax.swing.border.EmptyBorder;
import java.awt.*;
import java.awt.event.ActionListener;
import java.awt.geom.*;
import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Clean extends JPanel {
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
    private static final int CARD_SPACING = 15;
    private static final int BUTTON_HEIGHT = 40;
    private static final int BUTTON_WIDTH = 200;
    private static final int PROGRESS_HEIGHT = 6;
    private static final int CARD_WIDTH = 280;
    private static final int CARD_HEIGHT = 200;

    public Clean() {
        setBackground(BACKGROUND_COLOR);
        setLayout(new BorderLayout());
        setBorder(new EmptyBorder(PADDING, PADDING, PADDING, PADDING));

        JPanel mainContent = new JPanel();
        mainContent.setLayout(new BoxLayout(mainContent, BoxLayout.Y_AXIS));
        mainContent.setBackground(BACKGROUND_COLOR);

        JPanel headerPanel = createHeaderPanel();
        mainContent.add(headerPanel);
        mainContent.add(Box.createRigidArea(new Dimension(0, CARD_SPACING * 2)));

        JPanel cardsContainer = new JPanel(new GridBagLayout());
        cardsContainer.setBackground(BACKGROUND_COLOR);

        JLabel quickScanStatus = createStatusLabel("Ready");
        JProgressBar quickScanProgress = createProgressBar();
        JPanel quickScanCard = createScanCard("Temporary Files",
                "Perform a temporary files cleaning to optimize basic performance",
                "appScripts/ae.py", quickScanProgress, quickScanStatus);

        JLabel fullScanStatus = createStatusLabel("Ready");
        JProgressBar fullScanProgress = createProgressBar();
        JPanel fullScanCard = createScanCard("Prefetch",
                "Perform prefetch files cleaning",
                "full_scan.py", fullScanProgress, fullScanStatus);

        JLabel customScanStatus = createStatusLabel("Ready");
        JProgressBar customScanProgress = createProgressBar();
        JPanel customScanCard = createScanCard("Full Clean",
                "Clean both Temporary & Prefetch files",
                "custom_scan.py", customScanProgress, customScanStatus);

        GridBagConstraints gbc = new GridBagConstraints();
        gbc.fill = GridBagConstraints.NONE;
        gbc.anchor = GridBagConstraints.CENTER;
        gbc.insets = new Insets(CARD_SPACING, CARD_SPACING, CARD_SPACING, CARD_SPACING);

        gbc.gridx = 0;
        gbc.gridy = 0;
        cardsContainer.add(quickScanCard, gbc);

        gbc.gridx = 1;
        cardsContainer.add(fullScanCard, gbc);

        gbc.gridx = 0;
        gbc.gridy = 1;
        gbc.gridwidth = 2;
        gbc.anchor = GridBagConstraints.PAGE_START;
        cardsContainer.add(customScanCard, gbc);

        JPanel centeringPanel = new JPanel(new GridBagLayout());
        centeringPanel.setBackground(BACKGROUND_COLOR);
        centeringPanel.add(cardsContainer);

        JScrollPane scrollPane = new JScrollPane(centeringPanel);
        scrollPane.setBackground(BACKGROUND_COLOR);
        scrollPane.setBorder(null);
        scrollPane.getVerticalScrollBar().setUnitIncrement(16);
        scrollPane.setHorizontalScrollBarPolicy(JScrollPane.HORIZONTAL_SCROLLBAR_AS_NEEDED);
        scrollPane.getVerticalScrollBar().setUnitIncrement(16);

        mainContent.add(scrollPane);
        add(mainContent, BorderLayout.CENTER);

        setPreferredSize(new Dimension(CARD_WIDTH * 2 + PADDING * 4,
                CARD_HEIGHT * 3 + PADDING * 6));
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

        JLabel header = new JLabel("System Cleanup");
        header.setForeground(TEXT_COLOR);
        header.setFont(HEADER_FONT);
        header.setAlignmentX(Component.CENTER_ALIGNMENT);

        JLabel subtitle = new JLabel("Optimize your system performance");
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

    private JPanel createScanCard(String title, String description, String script,
                                  JProgressBar progressBar, JLabel statusLabel) {
        JPanel card = new JPanel() {
            @Override
            protected void paintComponent(Graphics g) {
                Graphics2D g2 = (Graphics2D) g.create();
                g2.setRenderingHint(RenderingHints.KEY_ANTIALIASING, RenderingHints.VALUE_ANTIALIAS_ON);

                g2.setColor(CARD_BACKGROUND);
                g2.fill(new RoundRectangle2D.Float(0, 0, getWidth(), getHeight(), 20, 20));

                GradientPaint gradient = new GradientPaint(
                        0, 0, new Color(255, 255, 255, 10),
                        0, getHeight(), new Color(255, 255, 255, 0)
                );
                g2.setPaint(gradient);
                g2.fill(new RoundRectangle2D.Float(0, 0, getWidth(), getHeight(), 20, 20));

                g2.dispose();
            }
        };

        card.setLayout(new BoxLayout(card, BoxLayout.Y_AXIS));
        card.setBackground(CARD_BACKGROUND);
        card.setBorder(new EmptyBorder(PADDING, PADDING, PADDING, PADDING));
        card.setPreferredSize(new Dimension(CARD_WIDTH, CARD_HEIGHT));

        JLabel titleLabel = new JLabel(title);
        titleLabel.setForeground(TEXT_COLOR);
        titleLabel.setFont(CARD_TITLE_FONT);
        titleLabel.setAlignmentX(Component.CENTER_ALIGNMENT);

        JLabel descLabel = new JLabel("<html><div style='text-align: center; width: 200px;'>"
                + description + "</div></html>");
        descLabel.setForeground(SECONDARY_TEXT);
        descLabel.setFont(DESC_FONT);
        descLabel.setAlignmentX(Component.CENTER_ALIGNMENT);

        // Button wrapper panel for proper centering
        JPanel buttonWrapper = new JPanel();
        buttonWrapper.setLayout(new BoxLayout(buttonWrapper, BoxLayout.X_AXIS));
        buttonWrapper.setBackground(CARD_BACKGROUND);
        buttonWrapper.add(Box.createHorizontalGlue());
        buttonWrapper.add(createScanButton(e -> startScan(script, progressBar, statusLabel)));
        buttonWrapper.add(Box.createHorizontalGlue());
        buttonWrapper.setAlignmentX(Component.CENTER_ALIGNMENT);
        buttonWrapper.setMaximumSize(new Dimension(CARD_WIDTH - PADDING * 2, BUTTON_HEIGHT));

        JPanel progressPanel = new JPanel();
        progressPanel.setLayout(new BoxLayout(progressPanel, BoxLayout.Y_AXIS));
        progressPanel.setBackground(CARD_BACKGROUND);
        progressPanel.setAlignmentX(Component.CENTER_ALIGNMENT);
        progressPanel.setMaximumSize(new Dimension(BUTTON_WIDTH, 50));

        progressBar.setAlignmentX(Component.CENTER_ALIGNMENT);
        statusLabel.setAlignmentX(Component.CENTER_ALIGNMENT);

        progressPanel.add(progressBar);
        progressPanel.add(Box.createRigidArea(new Dimension(0, 8)));
        progressPanel.add(statusLabel);

        card.add(titleLabel);
        card.add(Box.createRigidArea(new Dimension(0, 10)));
        card.add(descLabel);
        card.add(Box.createRigidArea(new Dimension(0, 20)));
        card.add(buttonWrapper);
        card.add(Box.createRigidArea(new Dimension(0, 15)));
        card.add(progressPanel);

        return card;
    }

    private JProgressBar createProgressBar() {
        JProgressBar progressBar = new JProgressBar();
        progressBar.setBackground(PROGRESS_BACKGROUND);
        progressBar.setForeground(PROGRESS_COLOR);
        progressBar.setUI(new javax.swing.plaf.basic.BasicProgressBarUI() {
            protected Color getSelectionBackground() { return TEXT_COLOR; }
            protected Color getSelectionForeground() { return TEXT_COLOR; }
        });
        progressBar.setPreferredSize(new Dimension(BUTTON_WIDTH, PROGRESS_HEIGHT));
        progressBar.setMaximum(100);
        progressBar.setValue(0);
        progressBar.setStringPainted(false);
        return progressBar;
    }

    private JLabel createStatusLabel(String text) {
        JLabel label = new JLabel(text);
        label.setForeground(SECONDARY_TEXT);
        label.setFont(PROGRESS_FONT);
        label.setAlignmentX(Component.CENTER_ALIGNMENT);
        return label;
    }

    private JButton createScanButton(ActionListener listener) {
        JButton button = new JButton("Start Clean");
        button.setFont(BUTTON_FONT);
        button.setBackground(BUTTON_COLOR);
        button.setForeground(TEXT_COLOR);
        button.setFocusPainted(false);
        button.setPreferredSize(new Dimension(BUTTON_WIDTH, BUTTON_HEIGHT));
        button.addActionListener(listener);
        button.addMouseListener(new java.awt.event.MouseAdapter() {
            @Override
            public void mouseEntered(java.awt.event.MouseEvent evt) {
                button.setBackground(BUTTON_HOVER_COLOR);
            }
            @Override
            public void mouseExited(java.awt.event.MouseEvent evt) {
                button.setBackground(BUTTON_COLOR);
            }
        });
        return button;
    }

    private void startScan(String script, JProgressBar progressBar, JLabel statusLabel) {
        // Set initial UI state
        statusLabel.setText("Scanning...");
        progressBar.setValue(0);

        // Run the Python script in a separate thread to avoid blocking the UI
        new Thread(() -> {
            try {
                // Initialize the ProcessBuilder with the Python command and script path
                ProcessBuilder processBuilder = new ProcessBuilder("python", script);
                processBuilder.redirectErrorStream(true); // Merge stdout and stderr

                // Start the process
                Process process = processBuilder.start();

                // Read the output of the process
                try (BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()))) {
                    String line;
                    while ((line = reader.readLine()) != null) {
                        // Update the status label with each line of output from the script
                        String finalLine = line; // Variable for use in lambda
                        SwingUtilities.invokeLater(() -> statusLabel.setText(finalLine));
                    }
                }

                // Wait for the process to complete
                int exitCode = process.waitFor();
                if (exitCode == 0) {
                    SwingUtilities.invokeLater(() -> statusLabel.setText("Cleaning Complete"));
                    SwingUtilities.invokeLater(() -> progressBar.setValue(100));
                } else {
                    SwingUtilities.invokeLater(() -> statusLabel.setText("Error: Cleaning failed"));
                }
            } catch (Exception e) {
                SwingUtilities.invokeLater(() -> statusLabel.setText("Error: " + e.getMessage()));
            }
        }).start();
    }

}