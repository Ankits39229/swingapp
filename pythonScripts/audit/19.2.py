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

    # News and Interests
    check_policy(
        "Ensure 'Enable news and interests on the taskbar' is set to 'Disabled'",
        r"SOFTWARE\Policies\Microsoft\Windows\WindowsFeeder\State",
        "NewsAndInterests",
        0
    )

    # OneDrive
    check_policy(
        "Ensure 'Prevent the usage of OneDrive for file storage' is set to 'Enabled'",
        r"SOFTWARE\Policies\Microsoft\Windows\OneDrive",
        "DisableFileSyncNGSC",
        1
    )

    # Push To Install
    check_policy(
        "Ensure 'Turn off Push To Install service' is set to 'Enabled'",
        r"SOFTWARE\Policies\Microsoft\Windows\PushToInstall",
        "DisablePushToInstall",
        1
    )

    # Remote Desktop Services (RemoteFX USB Device Redirection)
    check_policy(
        "Ensure 'Disable Cloud Clipboard integration for server-to-client data transfer' is set to 'Enabled'",
        r"SOFTWARE\Policies\Microsoft\Windows\CloudClipboard",
        "DisableCloudClipboard",
        1
    )
    check_policy(
        "Ensure 'Do not allow passwords to be saved' is set to 'Enabled'",
        r"SOFTWARE\Policies\Microsoft\Windows\RemoteDesktop",
        "DisableSavePassword",
        1
    )
    check_policy(
        "Ensure 'Allow users to connect remotely by using Remote Desktop Services' is set to 'Disabled'",
        r"SOFTWARE\Policies\Microsoft\Windows\RemoteDesktop",
        "fDenyTSConnections",
        1
    )

    # Remote Desktop Session Host
    check_policy(
        "Ensure 'Allow UI Automation redirection' is set to 'Disabled'",
        r"SOFTWARE\Policies\Microsoft\Windows\TerminalServer",
        "AllowUIAutomationRedirection",
        0
    )
    check_policy(
        "Ensure 'Do not allow COM port redirection' is set to 'Enabled'",
        r"SOFTWARE\Policies\Microsoft\Windows\TerminalServer",
        "DisableComPortRedirection",
        1
    )
    check_policy(
        "Ensure 'Do not allow drive redirection' is set to 'Enabled'",
        r"SOFTWARE\Policies\Microsoft\Windows\TerminalServer",
        "DisableDriveRedirection",
        1
    )

    # Security Settings
    check_policy(
        "Ensure 'Always prompt for password upon connection' is set to 'Enabled'",
        r"SOFTWARE\Policies\Microsoft\Windows\TerminalServer",
        "PromptForPassword",
        1
    )
    check_policy(
        "Ensure 'Require secure RPC communication' is set to 'Enabled'",
        r"SOFTWARE\Policies\Microsoft\Windows\TerminalServer",
        "RequireSecureRPC",
        1
    )
    check_policy(
        "Ensure 'Require use of specific security layer for remote (RDP) connections' is set to 'Enabled: SSL'",
        r"SOFTWARE\Policies\Microsoft\Windows\TerminalServer",
        "SecurityLayer",
        1
    )
    check_policy(
        "Ensure 'Require user authentication for remote connections by using Network Level Authentication' is set to 'Enabled'",
        r"SOFTWARE\Policies\Microsoft\Windows\TerminalServer",
        "UserAuthenticationRequired",
        1
    )
    check_policy(
        "Ensure 'Set client connection encryption level' is set to 'Enabled: High Level'",
        r"SOFTWARE\Policies\Microsoft\Windows\TerminalServer",
        "EncryptionLevel",
        3  # High Encryption Level
    )

    # Session Time Limits
    check_policy(
        "Ensure 'Set time limit for active but idle Remote Desktop Services sessions' is set to 'Enabled: 15 minutes or less, but not Never (0)'",
        r"SOFTWARE\Policies\Microsoft\Windows\TerminalServer",
        "IdleSessionLimit",
        15
    )
    check_policy(
        "Ensure 'Set time limit for disconnected sessions' is set to 'Enabled: 1 minute'",
        r"SOFTWARE\Policies\Microsoft\Windows\TerminalServer",
        "DisconnectedSessionLimit",
        1
    )

    # Temporary folders
    check_policy(
        "Ensure 'Do not delete temp folders upon exit' is set to 'Disabled'",
        r"SOFTWARE\Policies\Microsoft\Windows\Explorer",
        "NoDeleteTempFilesOnExit",
        0
    )

    # RSS Feeds
    check_policy(
        "Ensure 'Prevent downloading of enclosures' is set to 'Enabled'",
        r"SOFTWARE\Policies\Microsoft\Windows\RSS",
        "DisableEnclosures",
        1
    )

    # Search
    check_policy(
        "Ensure 'Allow Cloud Search' is set to 'Enabled: Disable Cloud Search'",
        r"SOFTWARE\Policies\Microsoft\Windows\Search",
        "AllowCloudSearch",
        0  # Disabling Cloud Search
    )
    check_policy(
        "Ensure 'Allow Cortana' is set to 'Disabled'",
        r"SOFTWARE\Policies\Microsoft\Windows\Search",
        "AllowCortana",
        0
    )
    check_policy(
        "Ensure 'Allow Cortana above lock screen' is set to 'Disabled'",
        r"SOFTWARE\Policies\Microsoft\Windows\Search",
        "AllowCortanaAboveLockScreen",
        0
    )
    check_policy(
        "Ensure 'Allow indexing of encrypted files' is set to 'Disabled'",
        r"SOFTWARE\Policies\Microsoft\Windows\Search",
        "DisableIndexingEncryptedFiles",
        1
    )
    check_policy(
        "Ensure 'Allow search and Cortana to use location' is set to 'Disabled'",
        r"SOFTWARE\Policies\Microsoft\Windows\Search",
        "AllowLocationForSearch",
        0
    )
    check_policy(
        "Ensure 'Allow search highlights' is set to 'Disabled'",
        r"SOFTWARE\Policies\Microsoft\Windows\Search",
        "DisableSearchHighlights",
        1
    )

    # Microsoft Store
    check_policy(
        "Ensure 'Disable all apps from Microsoft Store' is set to 'Disabled'",
        r"SOFTWARE\Policies\Microsoft\Windows\Store",
        "DisableStoreApps",
        0
    )
    check_policy(
        "Ensure 'Only display the private store within the Microsoft Store' is set to 'Enabled'",
        r"SOFTWARE\Policies\Microsoft\Windows\Store",
        "PrivateStoreOnly",
        1
    )
    check_policy(
        "Ensure 'Turn off Automatic Download and Install of updates' is set to 'Disabled'",
        r"SOFTWARE\Policies\Microsoft\Windows\Store",
        "DisableAutoInstallUpdates",
        0
    )
    check_policy(
        "Ensure 'Turn off the offer to update to the latest version of Windows' is set to 'Enabled'",
        r"SOFTWARE\Policies\Microsoft\Windows\Store",
        "DisableUpgradeOffer",
        1
    )
    check_policy(
        "Ensure 'Turn off the Store application' is set to 'Enabled'",
        r"SOFTWARE\Policies\Microsoft\Windows\Store",
        "DisableStore",
        1
    )

    print("\nAudit complete.")

# Run the audit
audit_policies()
