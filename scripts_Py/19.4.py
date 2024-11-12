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

    # Windows Update Management Policies
    check_policy(
        "Ensure 'Manage preview builds' is set to 'Disabled'",
        r"SOFTWARE\Microsoft\WindowsUpdate\UX\Settings",
        "AllowPreviewBuilds",
        0
    )
    check_policy(
        "Ensure 'Select when Preview Builds and Feature Updates are received' is set to 'Enabled: 180 or more days'",
        r"SOFTWARE\Microsoft\WindowsUpdate\UX\Settings",
        "PreviewBuilds",
        180
    )
    check_policy(
        "Ensure 'Select when Quality Updates are received' is set to 'Enabled: 0 days'",
        r"SOFTWARE\Microsoft\WindowsUpdate\UX\Settings",
        "QualityUpdates",
        0
    )
    check_policy(
        "Ensure 'Enable optional updates' is set to 'Disabled'",
        r"SOFTWARE\Microsoft\WindowsUpdate\UX\Settings",
        "EnableOptionalUpdates",
        0
    )

    # Administrative Template User Settings
    check_policy(
        "Ensure 'Turn off toast notifications on the lock screen' is set to 'Enabled'",
        r"SOFTWARE\Policies\Microsoft\Windows\System",
        "LockScreenNotifications",
        1
    )
    
    # Internet Communication Management
    check_policy(
        "Ensure 'Turn off Help Experience Improvement Program' is set to 'Enabled'",
        r"SOFTWARE\Policies\Microsoft\Windows\Windows Search",
        "DisableWindowsConsumerFeatures",
        1
    )
    
    # Windows Components Policies
    check_policy(
        "Ensure 'Do not preserve zone information in file attachments' is set to 'Disabled'",
        r"SOFTWARE\Policies\Microsoft\Windows\Attachment Manager",
        "DoNotPreserveZoneInformation",
        0
    )
    check_policy(
        "Ensure 'Notify antivirus programs when opening attachments' is set to 'Enabled'",
        r"SOFTWARE\Policies\Microsoft\Windows\Attachment Manager",
        "AntivirusNotification",
        1
    )
    check_policy(
        "Ensure 'Configure Windows spotlight on lock screen' is set to 'Disabled'",
        r"SOFTWARE\Policies\Microsoft\Windows\Personalization",
        "NoLockScreen",
        1
    )
    check_policy(
        "Ensure 'Do not suggest third-party content in Windows spotlight' is set to 'Enabled'",
        r"SOFTWARE\Policies\Microsoft\Windows\Personalization",
        "NoThirdPartyContent",
        1
    )
    check_policy(
        "Ensure 'Do not use diagnostic data for tailored experiences' is set to 'Enabled'",
        r"SOFTWARE\Policies\Microsoft\Windows\DataCollection",
        "AllowTelemetry",
        0
    )
    check_policy(
        "Ensure 'Turn off all Windows spotlight features' is set to 'Enabled'",
        r"SOFTWARE\Policies\Microsoft\Windows\Personalization",
        "NoSpotlight",
        1
    )
    check_policy(
        "Ensure 'Turn off Spotlight collection on Desktop' is set to 'Enabled'",
        r"SOFTWARE\Policies\Microsoft\Windows\Personalization",
        "NoDesktopSpotlight",
        1
    )

    # Windows Defender SmartScreen Policies
    check_policy(
        "Ensure 'Turn off Windows Copilot' is set to 'Enabled'",
        r"SOFTWARE\Policies\Microsoft\Windows\Windows Copilot",
        "DisableCopilot",
        1
    )

    # Windows Installer Settings
    check_policy(
        "Ensure 'Always install with elevated privileges' is set to 'Disabled'",
        r"SOFTWARE\Policies\Microsoft\Windows\Installer",
        "AlwaysInstallElevated",
        0
    )

    # Network Sharing Policies
    check_policy(
        "Ensure 'Prevent users from sharing files within their profile' is set to 'Enabled'",
        r"SOFTWARE\Policies\Microsoft\Windows\NetworkSharing",
        "PreventSharingFiles",
        1
    )

    print("\nAudit complete.")

# Run the audit
audit_policies()
