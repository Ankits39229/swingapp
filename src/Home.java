import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.awt.geom.*;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import javax.swing.border.*;
import java.util.concurrent.atomic.AtomicInteger;

public class Home extends JPanel {
    // Color scheme
    private static final Color BACKGROUND_COLOR = new Color(17, 23, 33);
    private static final Color CARD_BACKGROUND = new Color(27, 33, 43);
    private static final Color GRADIENT_START = new Color(32, 87, 209);
    private static final Color GRADIENT_END = new Color(66, 139, 247);
    private static final Color TEXT_COLOR = new Color(245, 245, 245);
    private static final Color SECONDARY_TEXT = new Color(179, 185, 198);
    private static final Color BORDER_COLOR = new Color(45, 55, 72);

    private JButton scanButton;
    private JProgressBar progressBar;
    private JTextArea outputArea;
    private JLabel statusLabel;
    private Timer pulseTimer;
    private float pulseAlpha = 0.0f;
    private boolean pulsing = false;

    public Home() {
        setBackground(BACKGROUND_COLOR);
        setLayout(new BorderLayout(30, 30));
        setBorder(BorderFactory.createEmptyBorder(40, 40, 40, 40));

        // Header Section with Gradient
        add(createHeaderPanel(), BorderLayout.NORTH);

        // Main Content
        add(createMainPanel(), BorderLayout.CENTER);

        // Initialize pulse animation
        setupPulseAnimation();
    }

    private JPanel createHeaderPanel() {
        JPanel headerPanel = new JGradientPanel(GRADIENT_START, GRADIENT_END);
        headerPanel.setLayout(new BoxLayout(headerPanel, BoxLayout.Y_AXIS));
        headerPanel.setBorder(new CompoundBorder(
                new RoundedBorder(10, BORDER_COLOR),
                new EmptyBorder(25, 25, 25, 25)
        ));

        JLabel iconLabel = createStyledLabel("🛡️", new Font("Segoe UI Emoji", Font.PLAIN, 48));
        JLabel headerLabel = createStyledLabel("Security Scanner", new Font("Segoe UI", Font.BOLD, 32));
        JLabel subHeaderLabel = createStyledLabel("Advanced System Protection & Threat Detection",
                SECONDARY_TEXT, new Font("Segoe UI", Font.PLAIN, 16));

        headerPanel.add(iconLabel);
        headerPanel.add(Box.createRigidArea(new Dimension(0, 15)));
        headerPanel.add(headerLabel);
        headerPanel.add(Box.createRigidArea(new Dimension(0, 10)));
        headerPanel.add(subHeaderLabel);

        return headerPanel;
    }

    private JPanel createMainPanel() {
        JPanel mainPanel = new RoundedPanel(20, CARD_BACKGROUND);
        mainPanel.setLayout(new BoxLayout(mainPanel, BoxLayout.Y_AXIS));
        mainPanel.setBorder(new EmptyBorder(30, 30, 30, 30));

        // Status Panel
        statusLabel = new JLabel("System Ready", new ImageIcon(), JLabel.LEFT);
        statusLabel.setForeground(SECONDARY_TEXT);
        statusLabel.setFont(new Font("Segoe UI", Font.BOLD, 14));
        statusLabel.setAlignmentX(Component.LEFT_ALIGNMENT);

        // Control Panel - Modified to use better layout
        JPanel controlPanel = new JPanel() {
            @Override
            public Dimension getMaximumSize() {
                Dimension max = super.getMaximumSize();
                Dimension pref = super.getPreferredSize();
                return new Dimension(max.width, pref.height);
            }
        };
        controlPanel.setLayout(new FlowLayout(FlowLayout.LEFT, 0, 0));
        controlPanel.setOpaque(false);
        controlPanel.setAlignmentX(Component.LEFT_ALIGNMENT);

        scanButton = createGradientButton("Scan Now");
        progressBar = createStyledProgressBar();

        // Add components to control panel with proper spacing
        controlPanel.add(Box.createHorizontalStrut(5)); // Add left padding
        controlPanel.add(scanButton);
        controlPanel.add(Box.createHorizontalStrut(10)); // Space between button and progress bar
        controlPanel.add(progressBar);

        // Output Panel
        JPanel outputPanel = new RoundedPanel(15, new Color(22, 28, 38));
        outputPanel.setLayout(new BorderLayout());
        outputPanel.setBorder(new EmptyBorder(20, 20, 20, 20));
        outputPanel.setAlignmentX(Component.LEFT_ALIGNMENT);

        outputArea = createStyledOutputArea();
        JScrollPane scrollPane = new JScrollPane(outputArea);
        scrollPane.setBorder(null);
        scrollPane.getViewport().setBackground(new Color(22, 28, 38));

        outputPanel.add(scrollPane);

        // Add all components with proper spacing
        mainPanel.add(statusLabel);
        mainPanel.add(Box.createRigidArea(new Dimension(0, 20)));
        mainPanel.add(controlPanel);
        mainPanel.add(Box.createRigidArea(new Dimension(0, 20)));
        mainPanel.add(outputPanel);

        return mainPanel;
    }

    private JLabel createStyledLabel(String text, Font font) {
        JLabel label = new JLabel(text);
        label.setFont(font);
        label.setForeground(TEXT_COLOR);
        label.setAlignmentX(Component.CENTER_ALIGNMENT);
        return label;
    }

    private JLabel createStyledLabel(String text, Color color, Font font) {
        JLabel label = createStyledLabel(text, font);
        label.setForeground(color);
        return label;
    }

    private JButton createGradientButton(String text) {
        JButton button = new JButton(text) {
            @Override
            protected void paintComponent(Graphics g) {
                Graphics2D g2 = (Graphics2D) g.create();
                g2.setRenderingHint(RenderingHints.KEY_ANTIALIASING, RenderingHints.VALUE_ANTIALIAS_ON);

                int w = getWidth();
                int h = getHeight();

                // Draw gradient background
                GradientPaint gradient = new GradientPaint(
                        0, 0, GRADIENT_START,
                        w, 0, GRADIENT_END
                );
                g2.setPaint(gradient);
                g2.fill(new RoundRectangle2D.Float(0, 0, w, h, 15, 15));

                // Draw pulsing effect if active
                if (pulsing) {
                    g2.setComposite(AlphaComposite.getInstance(AlphaComposite.SRC_OVER, pulseAlpha));
                    g2.setColor(Color.WHITE);
                    g2.fill(new RoundRectangle2D.Float(0, 0, w, h, 15, 15));
                }

                // Draw text
                g2.setColor(TEXT_COLOR);
                g2.setFont(getFont());
                FontMetrics fm = g2.getFontMetrics();
                int textX = (w - fm.stringWidth(getText())) / 2;
                int textY = (h - fm.getHeight()) / 2 + fm.getAscent();
                g2.drawString(getText(), textX, textY);

                g2.dispose();
            }

            @Override
            public Dimension getPreferredSize() {
                // Ensure button has proper height
                Dimension d = super.getPreferredSize();
                return new Dimension(220, 45);
            }

            @Override
            public Dimension getMinimumSize() {
                return getPreferredSize();
            }

            @Override
            public Dimension getMaximumSize() {
                return getPreferredSize();
            }
        };

        button.setFont(new Font("Segoe UI", Font.BOLD, 15));
        button.setForeground(TEXT_COLOR);
        button.setBackground(null);
        button.setBorder(null);
        button.setFocusPainted(false);
        button.setContentAreaFilled(false);
        button.setCursor(new Cursor(Cursor.HAND_CURSOR));

        button.addActionListener(new ScanButtonListener());
        button.addMouseListener(new MouseAdapter() {
            public void mouseEntered(MouseEvent e) {
                startPulsing();
            }
            public void mouseExited(MouseEvent e) {
                stopPulsing();
            }
        });

        return button;
    }

    private JProgressBar createStyledProgressBar() {
        JProgressBar bar = new JProgressBar() {
            private int animationIndex = 0;
            private Timer animationTimer = new Timer(50, e -> {
                animationIndex = (animationIndex + 5) % (getWidth() + 100);
                repaint();
            });

            @Override
            protected void paintComponent(Graphics g) {
                Graphics2D g2 = (Graphics2D) g.create();
                g2.setRenderingHint(RenderingHints.KEY_ANTIALIASING, RenderingHints.VALUE_ANTIALIAS_ON);

                // Draw background
                g2.setColor(new Color(45, 55, 72));
                g2.fill(new RoundRectangle2D.Float(0, 0, getWidth(), getHeight(), 10, 10));

                // Draw progress
                if (isIndeterminate()) {
                    // Custom indeterminate animation
                    int pos = animationIndex;
                    GradientPaint gradient = new GradientPaint(
                            pos - 50, 0, GRADIENT_START,
                            pos + 50, 0, GRADIENT_END
                    );
                    g2.setPaint(gradient);
                    g2.fill(new RoundRectangle2D.Float(pos - 50, 0, 100, getHeight(), 10, 10));
                } else {
                    // Normal progress
                    int width = (int) (getWidth() * (getPercentComplete()));
                    GradientPaint gradient = new GradientPaint(
                            0, 0, GRADIENT_START,
                            width, 0, GRADIENT_END
                    );
                    g2.setPaint(gradient);
                    g2.fill(new RoundRectangle2D.Float(0, 0, width, getHeight(), 10, 10));
                }

                g2.dispose();
            }

            @Override
            public void setIndeterminate(boolean newValue) {
                boolean oldValue = isIndeterminate();
                super.setIndeterminate(newValue);
                if (newValue && !oldValue) {
                    animationTimer.start();
                } else if (!newValue && oldValue) {
                    animationTimer.stop();
                }
            }
        };

        bar.setPreferredSize(new Dimension(200, 8));
        bar.setMaximumSize(new Dimension(200, 8));
        bar.setMinimumSize(new Dimension(200, 8));
        bar.setBorder(null);
        bar.setVisible(false);
        return bar;
    }
    private JTextArea createStyledOutputArea() {
        JTextArea area = new JTextArea(15, 45) {
            @Override
            public void append(String str) {
                super.append(str);
                // Fancy animation for new text
                Timer timer = new Timer(50, new ActionListener() {
                    float alpha = 0.0f;
                    public void actionPerformed(ActionEvent e) {
                        alpha += 0.1f;
                        if (alpha >= 1.0f) {
                            ((Timer)e.getSource()).stop();
                        }
                        setForeground(new Color(245, 245, 245, (int)(alpha * 255)));
                        repaint();
                    }
                });
                timer.start();
            }
        };

        area.setEditable(false);
        area.setForeground(TEXT_COLOR);
        area.setBackground(new Color(22, 28, 38));
        area.setFont(new Font("JetBrains Mono", Font.PLAIN, 13));
        area.setLineWrap(true);
        area.setWrapStyleWord(true);
        area.setBorder(BorderFactory.createEmptyBorder(10, 10, 10, 10));
        return area;
    }

    private void setupPulseAnimation() {
        pulseTimer = new Timer(50, e -> {
            if (pulsing) {
                pulseAlpha = (float) (0.2f * Math.sin(System.currentTimeMillis() / 500.0) + 0.2f);
                scanButton.repaint();
            }
        });
        pulseTimer.start();
    }

    private void startPulsing() {
        pulsing = true;
    }

    private void stopPulsing() {
        pulsing = false;
        pulseAlpha = 0.0f;
        scanButton.repaint();
    }

    private class ScanButtonListener implements ActionListener {
        private final AtomicInteger scanProgress = new AtomicInteger(0);

        @Override
        public void actionPerformed(ActionEvent e) {
            scanButton.setEnabled(false);
            progressBar.setVisible(true);
            progressBar.setIndeterminate(true);
            statusLabel.setText("⚡ Scanning System...");
            statusLabel.setForeground(GRADIENT_END);

            new Thread(() -> {
                try {
                    ProcessBuilder pb = new ProcessBuilder("python", "PythonScripts/2.1.py");
                    pb.redirectErrorStream(true);

                    Process process = pb.start();
                    BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));
                    String line;

                    outputArea.setText("");
                    while ((line = reader.readLine()) != null) {
                        String finalLine = line;
                        SwingUtilities.invokeLater(() -> {
                            outputArea.append("→ " + finalLine + "\n");
                            outputArea.setCaretPosition(outputArea.getDocument().getLength());
                        });
                    }

                    int exitCode = process.waitFor();
                    SwingUtilities.invokeLater(() -> {
                        if (exitCode == 0) {
                            outputArea.append("\n✅ Security scan completed successfully.\n");
                            statusLabel.setText("✅ Scan Complete");
                            statusLabel.setForeground(new Color(72, 187, 120));
                        } else {
                            outputArea.append("\n❌ Security scan encountered an error.\n");
                            statusLabel.setText("❌ Scan Failed");
                            statusLabel.setForeground(new Color(245, 101, 101));
                        }
                    });
                } catch (Exception ex) {
                    SwingUtilities.invokeLater(() -> {
                        outputArea.append("\n❌ Error: " + ex.getMessage() + "\n");
                        statusLabel.setText("❌ Error Occurred");
                        statusLabel.setForeground(new Color(245, 101, 101));
                    });
                } finally {
                    SwingUtilities.invokeLater(() -> {
                        scanButton.setEnabled(true);
                        progressBar.setIndeterminate(false);
                        progressBar.setVisible(false);
                    });
                }
            }).start();
        }
    }

    // Custom components
    private static class JGradientPanel extends JPanel {
        private final Color gradientStart;
        private final Color gradientEnd;

        public JGradientPanel(Color start, Color end) {
            this.gradientStart = start;
            this.gradientEnd = end;
            setOpaque(false);
        }

        @Override
        protected void paintComponent(Graphics g) {
            Graphics2D g2 = (Graphics2D) g.create();
            g2.setRenderingHint(RenderingHints.KEY_ANTIALIASING, RenderingHints.VALUE_ANTIALIAS_ON);

            GradientPaint gradient = new GradientPaint(
                    0, 0, gradientStart,
                    getWidth(), 0, gradientEnd
            );
            g2.setPaint(gradient);
            g2.fill(new RoundRectangle2D.Float(0, 0, getWidth(), getHeight(), 10, 10));
            g2.dispose();
        }
    }

    private static class RoundedPanel extends JPanel {
        private final int radius;
        private final Color backgroundColor;

        public RoundedPanel(int radius, Color bgColor) {
            this.radius = radius;
            this.backgroundColor = bgColor;
            setOpaque(false);
        }

        @Override
        protected void paintComponent(Graphics g) {
            Graphics2D g2 = (Graphics2D) g.create();
            g2.setRenderingHint(RenderingHints.KEY_ANTIALIASING, RenderingHints.VALUE_ANTIALIAS_ON);
            g2.setColor(backgroundColor);
            g2.fill(new RoundRectangle2D.Float(0, 0, getWidth(), getHeight(), radius, radius));
            g2.dispose();
        }
    }

    private static class RoundedBorder extends AbstractBorder {
        private final int radius;
        private final Color color;

        public RoundedBorder(int radius, Color color) {
            this.radius = radius;
            this.color = color;
        }

        @Override
        public void paintBorder(Component c, Graphics g, int x, int y, int width, int height) {
            Graphics2D g2 = (Graphics2D) g.create();
            g2.setRenderingHint(RenderingHints.KEY_ANTIALIASING, RenderingHints.VALUE_ANTIALIAS_ON);
            g2.setColor(color);
            g2.setStroke(new BasicStroke(2));
            g2.drawRoundRect(x, y, width - 1, height - 1, radius, radius);
            g2.dispose();
        }

        @Override
        public Insets getBorderInsets(Component c) {
            return new Insets(radius + 1, radius + 1, radius + 1, radius + 1);
        }

        @Override
        public Insets getBorderInsets(Component c, Insets insets) {
            insets.left = insets.right = insets.top = insets.bottom = radius + 1;
            return insets;
        }
    }
}
