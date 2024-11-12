import winreg as reg

# Define function to check a registry key's value against an expected value
def check_policy(setting_name, registry_path, key_name, expected_value, manual_check=False):
    try:
        # Open the registry key
        reg_key = reg.OpenKey(reg.HKEY_LOCAL_MACHINE, registry_path, 0, reg.KEY_READ)
        # Get the value of the specified registry key
        value, reg_type = reg.QueryValueEx(reg_key, key_name)
        
        # Check if manual verification is required
        if manual_check:
            compliance = "MANUAL CHECK REQUIRED"
        else:
            # Verify if the actual value matches the expected value
            compliance = "PASS" if value == expected_value else "FAIL"
        
        # Close the registry key
        reg.CloseKey(reg_key)
        
    except FileNotFoundError:
        compliance = "FAIL (NOT CONFIGURED)"
    except Exception as e:
        compliance = f"FAIL (Error: {e})"
    
    # Print detailed output for this setting
    print(f"{setting_name} - {compliance}")

# Main function to check policies
def audit_policies():
    print("Starting Windows 11 Security Policy Audit...\n")

    # Widgets
    check_policy(
        "Ensure 'Allow widgets' is set to 'Disabled'",
        r"SOFTWARE\Policies\Microsoft\Windows\CurrentVersion\Explorer",
        "AllowWidgets",
        0
    )
    
    # Windows Defender SmartScreen
    check_policy(
        "Ensure 'Configure Windows Defender SmartScreen' is set to 'Enabled: Warn and prevent bypass'",
        r"SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer",
        "SmartScreenEnabled",
        1
    )
    
    # Enhanced Phishing Protection
    check_policy(
        "Ensure 'Automatic Data Collection' is set to 'Enabled'",
        r"SOFTWARE\Microsoft\Windows Defender\SmartScreen",
        "PhishingProtection",
        1
    )
    check_policy(
        "Ensure 'Notify Malicious' is set to 'Enabled'",
        r"SOFTWARE\Microsoft\Windows Defender\SmartScreen",
        "NotifyMalicious",
        1
    )
    check_policy(
        "Ensure 'Notify Password Reuse' is set to 'Enabled'",
        r"SOFTWARE\Microsoft\Windows Defender\SmartScreen",
        "NotifyPasswordReuse",
        1
    )
    check_policy(
        "Ensure 'Notify Unsafe App' is set to 'Enabled'",
        r"SOFTWARE\Microsoft\Windows Defender\SmartScreen",
        "NotifyUnsafeApp",
        1
    )
    check_policy(
        "Ensure 'Service Enabled' is set to 'Enabled'",
        r"SOFTWARE\Microsoft\Windows Defender\SmartScreen",
        "ServiceEnabled",
        1
    )
    
    # Windows Game Recording and Broadcasting
    check_policy(
        "Ensure 'Enables or disables Windows Game Recording and Broadcasting' is set to 'Disabled'",
        r"SOFTWARE\Policies\Microsoft\Windows\GameDVR",
        "AllowGameDVR",
        0
    )

    # Windows Ink Workspace
    check_policy(
        "Ensure 'Allow suggested apps in Windows Ink Workspace' is set to 'Disabled'",
        r"SOFTWARE\Policies\Microsoft\Windows Ink Workspace",
        "AllowSuggestedApps",
        0
    )
    check_policy(
        "Ensure 'Allow Windows Ink Workspace' is set to 'Enabled: On, but disallow access above lock' OR 'Enabled: Disabled'",
        r"SOFTWARE\Policies\Microsoft\Windows Ink Workspace",
        "AllowWindowsInkWorkspace",
        0
    )
    
    # Windows Installer
    check_policy(
        "Ensure 'Allow user control over installs' is set to 'Disabled'",
        r"SOFTWARE\Policies\Microsoft\Windows\Installer",
        "AllowUserControlOverInstalls",
        0
    )
    check_policy(
        "Ensure 'Always install with elevated privileges' is set to 'Disabled'",
        r"SOFTWARE\Policies\Microsoft\Windows\Installer",
        "AlwaysInstallWithElevatedPrivileges",
        0
    )
    
    # Windows Logon Options
    check_policy(
        "Ensure 'Enable MPR notifications for the system' is set to 'Disabled'",
        r"SOFTWARE\Policies\Microsoft\Windows\System",
        "EnableMPRNotifications",
        0
    )
    check_policy(
        "Ensure 'Sign-in and lock last interactive user automatically after a restart' is set to 'Disabled'",
        r"SOFTWARE\Policies\Microsoft\Windows\System",
        "SignInAndLockLastUser",
        0
    )
    
    # PowerShell
    check_policy(
        "Ensure 'Turn on PowerShell Script Block Logging' is set to 'Enabled'",
        r"SOFTWARE\Policies\Microsoft\Windows\PowerShell",
        "ScriptBlockLogging",
        1
    )
    check_policy(
        "Ensure 'Turn on PowerShell Transcription' is set to 'Enabled'",
        r"SOFTWARE\Policies\Microsoft\Windows\PowerShell",
        "Transcription",
        1
    )
    
    # Windows Remote Management (WinRM)
    check_policy(
        "Ensure 'Allow Basic authentication' is set to 'Disabled'",
        r"SOFTWARE\Policies\Microsoft\Windows\WinRM\Service",
        "AllowBasicAuthentication",
        0
    )
    check_policy(
        "Ensure 'Allow unencrypted traffic' is set to 'Disabled'",
        r"SOFTWARE\Policies\Microsoft\Windows\WinRM\Service",
        "AllowUnencryptedTraffic",
        0
    )
    check_policy(
        "Ensure 'Disallow Digest authentication' is set to 'Enabled'",
        r"SOFTWARE\Policies\Microsoft\Windows\WinRM\Service",
        "DisallowDigestAuthentication",
        1
    )
    check_policy(
        "Ensure 'Allow remote server management through WinRM' is set to 'Disabled'",
        r"SOFTWARE\Policies\Microsoft\Windows\WinRM\Service",
        "AllowRemoteServerManagement",
        0
    )
    
    # Windows Sandbox
    check_policy(
        "Ensure 'Allow clipboard sharing with Windows Sandbox' is set to 'Disabled'",
        r"SOFTWARE\Policies\Microsoft\Windows\Sandbox",
        "AllowClipboardSharing",
        0
    )
    check_policy(
        "Ensure 'Allow networking in Windows Sandbox' is set to 'Disabled'",
        r"SOFTWARE\Policies\Microsoft\Windows\Sandbox",
        "AllowNetworking",
        0
    )

    # Windows Update
    check_policy(
        "Ensure 'No auto-restart with logged on users for scheduled automatic updates installations' is set to 'Disabled'",
        r"SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate",
        "NoAutoRestartWithLoggedOnUsers",
        0
    )
    check_policy(
        "Ensure 'Configure Automatic Updates' is set to 'Enabled'",
        r"SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate",
        "ConfigureAutomaticUpdates",
        1
    )
    check_policy(
        "Ensure 'Configure Automatic Updates: Scheduled install day' is set to '0 - Every day'",
        r"SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate",
        "ScheduledInstallDay",
        0
    )
    check_policy(
        "Ensure 'Enable features introduced via servicing that are off by default' is set to 'Disabled'",
        r"SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate",
        "EnableServicingFeatures",
        0
    )
    check_policy(
        "Ensure 'Remove access to “Pause updates” feature' is set to 'Enabled'",
        r"SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate",
        "RemovePauseUpdates",
        1
    )
    
    print("\nAudit complete.")

# Run the audit
audit_policies()
