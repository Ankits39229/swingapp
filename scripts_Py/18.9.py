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

    # Delivery Optimization
    check_policy(
        "Ensure 'Download Mode' is NOT set to 'Enabled: Internet'",
        r"SOFTWARE\Policies\Microsoft\Windows\DeliveryOptimization",
        "DODownloadMode",
        0  # 0 = Disallowed, 1 = Allowed, 2 = Forced Internet
    )

    # Desktop App Installer
    check_policy(
        "Ensure 'Enable App Installer' is set to 'Disabled'",
        r"SOFTWARE\Policies\Microsoft\Windows\Appx",
        "EnableAppInstaller",
        0
    )
    check_policy(
        "Ensure 'Enable App Installer Experimental Features' is set to 'Disabled'",
        r"SOFTWARE\Policies\Microsoft\Windows\Appx",
        "EnableAppInstallerExperimentalFeatures",
        0
    )
    check_policy(
        "Ensure 'Enable App Installer Hash Override' is set to 'Disabled'",
        r"SOFTWARE\Policies\Microsoft\Windows\Appx",
        "EnableAppInstallerHashOverride",
        0
    )
    check_policy(
        "Ensure 'Enable App Installer ms-appinstaller protocol' is set to 'Disabled'",
        r"SOFTWARE\Policies\Microsoft\Windows\Appx",
        "EnableAppInstallerProtocol",
        0
    )

    # Event Log Service Settings
    check_policy(
        "Ensure 'Application: Control Event Log behavior when the log file reaches its maximum size' is set to 'Disabled'",
        r"SYSTEM\CurrentControlSet\Services\EventLog\Application",
        "Retention",
        0
    )
    check_policy(
        "Ensure 'Application: Specify the maximum log file size (KB)' is set to 'Enabled: 32,768 or greater'",
        r"SYSTEM\CurrentControlSet\Services\EventLog\Application",
        "MaxSize",
        32768
    )
    check_policy(
        "Ensure 'Security: Control Event Log behavior when the log file reaches its maximum size' is set to 'Disabled'",
        r"SYSTEM\CurrentControlSet\Services\EventLog\Security",
        "Retention",
        0
    )
    check_policy(
        "Ensure 'Security: Specify the maximum log file size (KB)' is set to 'Enabled: 196,608 or greater'",
        r"SYSTEM\CurrentControlSet\Services\EventLog\Security",
        "MaxSize",
        196608
    )
    check_policy(
        "Ensure 'Setup: Control Event Log behavior when the log file reaches its maximum size' is set to 'Disabled'",
        r"SYSTEM\CurrentControlSet\Services\EventLog\Setup",
        "Retention",
        0
    )
    check_policy(
        "Ensure 'Setup: Specify the maximum log file size (KB)' is set to 'Enabled: 32,768 or greater'",
        r"SYSTEM\CurrentControlSet\Services\EventLog\Setup",
        "MaxSize",
        32768
    )
    check_policy(
        "Ensure 'System: Control Event Log behavior when the log file reaches its maximum size' is set to 'Disabled'",
        r"SYSTEM\CurrentControlSet\Services\EventLog\System",
        "Retention",
        0
    )
    check_policy(
        "Ensure 'System: Specify the maximum log file size (KB)' is set to 'Enabled: 32,768 or greater'",
        r"SYSTEM\CurrentControlSet\Services\EventLog\System",
        "MaxSize",
        32768
    )

    # File Explorer Settings
    check_policy(
        "Ensure 'Turn off account-based insights, recent, favorite, and recommended files in File Explorer' is set to 'Enabled'",
        r"SOFTWARE\Policies\Microsoft\Windows\Explorer",
        "DisableRecentFiles",
        1
    )
    check_policy(
        "Ensure 'Turn off Data Execution Prevention for Explorer' is set to 'Disabled'",
        r"SOFTWARE\Policies\Microsoft\Windows\Explorer",
        "DisableDEP",
        0
    )
    check_policy(
        "Ensure 'Turn off heap termination on corruption' is set to 'Disabled'",
        r"SOFTWARE\Policies\Microsoft\Windows\Explorer",
        "DisableHeapCorruption",
        0
    )
    check_policy(
        "Ensure 'Turn off shell protocol protected mode' is set to 'Disabled'",
        r"SOFTWARE\Policies\Microsoft\Windows\Explorer",
        "DisableShellProtMode",
        0
    )

    # Location and Sensors
    check_policy(
        "Ensure 'Turn off location' is set to 'Enabled'",
        r"SOFTWARE\Policies\Microsoft\Windows\LocationAndSensors",
        "DisableLocation",
        1
    )

    # Messaging
    check_policy(
        "Ensure 'Allow Message Service Cloud Sync' is set to 'Disabled'",
        r"SOFTWARE\Policies\Microsoft\Windows\Messaging",
        "AllowCloudSync",
        0
    )

    # Microsoft Account
    check_policy(
        "Ensure 'Block all consumer Microsoft account user authentication' is set to 'Enabled'",
        r"SOFTWARE\Policies\Microsoft\Windows\System",
        "BlockConsumerMicrosoftAccount",
        1
    )

    print("\nAudit complete.")

# Run the audit
audit_policies()
