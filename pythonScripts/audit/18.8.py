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

    # Removable Data Drives Policies (18.10.9.3)
    check_policy(
        "Ensure 'Allow access to BitLocker-protected removable data drives from earlier versions of Windows' is set to 'Disabled'",
        r"SOFTWARE\Policies\Microsoft\FVE",
        "DisableRemovableDriveBitLocker",
        1
    )
    check_policy(
        "Ensure 'Choose how BitLocker-protected removable drives can be recovered' is set to 'Enabled'",
        r"SOFTWARE\Policies\Microsoft\FVE",
        "RemovableDriveRecovery",
        1
    )
    check_policy(
        "Ensure 'Choose how BitLocker-protected removable drives can be recovered: Allow data recovery agent' is set to 'Enabled: True'",
        r"SOFTWARE\Policies\Microsoft\FVE",
        "AllowDataRecoveryAgent",
        1
    )
    check_policy(
        "Ensure 'Choose how BitLocker-protected removable drives can be recovered: Recovery Password' is set to 'Enabled: Do not allow 48-digit recovery password'",
        r"SOFTWARE\Policies\Microsoft\FVE",
        "DisableRecoveryPassword",
        1
    )
    check_policy(
        "Ensure 'Choose how BitLocker-protected removable drives can be recovered: Recovery Key' is set to 'Enabled: Do not allow 256-bit recovery key'",
        r"SOFTWARE\Policies\Microsoft\FVE",
        "DisableRecoveryKey",
        1
    )
    check_policy(
        "Ensure 'Choose how BitLocker-protected removable drives can be recovered: Omit recovery options from the BitLocker setup wizard' is set to 'Enabled: True'",
        r"SOFTWARE\Policies\Microsoft\FVE",
        "OmitRecoveryOptions",
        1
    )
    check_policy(
        "Ensure 'Choose how BitLocker-protected removable drives can be recovered: Save BitLocker recovery information to AD DS for removable data drives' is set to 'Enabled: False'",
        r"SOFTWARE\Policies\Microsoft\FVE",
        "SaveRecoveryInfoToADDS",
        0
    )
    check_policy(
        "Ensure 'Choose how BitLocker-protected removable drives can be recovered: Configure storage of BitLocker recovery information to AD DS:' is set to 'Enabled: Backup recovery passwords and key packages'",
        r"SOFTWARE\Policies\Microsoft\FVE",
        "BackupRecoveryInfoToADDS",
        1
    )
    check_policy(
        "Ensure 'Choose how BitLocker-protected removable drives can be recovered: Do not enable BitLocker until recovery information is stored to AD DS for removable data drives' is set to 'Enabled: False'",
        r"SOFTWARE\Policies\Microsoft\FVE",
        "DisableBitLockerUntilRecoveryInfoStored",
        0
    )
    check_policy(
        "Ensure 'Configure use of hardware-based encryption for removable data drives' is set to 'Disabled'",
        r"SOFTWARE\Policies\Microsoft\FVE",
        "DisableHardwareEncryption",
        1
    )
    check_policy(
        "Ensure 'Configure use of passwords for removable data drives' is set to 'Disabled'",
        r"SOFTWARE\Policies\Microsoft\FVE",
        "DisablePasswordForRemovableDrives",
        1
    )
    check_policy(
        "Ensure 'Configure use of smart cards on removable data drives' is set to 'Enabled'",
        r"SOFTWARE\Policies\Microsoft\FVE",
        "EnableSmartCardForRemovableDrives",
        1
    )
    check_policy(
        "Ensure 'Configure use of smart cards on removable data drives: Require use of smart cards on removable data drives' is set to 'Enabled: True'",
        r"SOFTWARE\Policies\Microsoft\FVE",
        "RequireSmartCardForRemovableDrives",
        1
    )
    check_policy(
        "Ensure 'Deny write access to removable drives not protected by BitLocker' is set to 'Enabled'",
        r"SOFTWARE\Policies\Microsoft\FVE",
        "DenyWriteAccessIfNotBitLockerProtected",
        1
    )
    check_policy(
        "Ensure 'Deny write access to removable drives not protected by BitLocker: Do not allow write access to devices configured in another organization' is set to 'Enabled: False'",
        r"SOFTWARE\Policies\Microsoft\FVE",
        "DenyWriteAccessToDevicesFromAnotherOrganization",
        0
    )

    # Camera Policies (18.10.10.1)
    check_policy(
        "Ensure 'Allow Use of Camera' is set to 'Disabled'",
        r"SOFTWARE\Policies\Microsoft\Windows\Camera",
        "AllowCamera",
        0
    )

    # Cloud Content Policies (18.10.12)
    check_policy(
        "Ensure 'Turn off cloud consumer account state content' is set to 'Enabled'",
        r"SOFTWARE\Policies\Microsoft\Windows\CloudContent",
        "DisableConsumerContent",
        1
    )
    check_policy(
        "Ensure 'Turn off cloud optimized content' is set to 'Enabled'",
        r"SOFTWARE\Policies\Microsoft\Windows\CloudContent",
        "DisableOptimizedContent",
        1
    )
    check_policy(
        "Ensure 'Turn off Microsoft consumer experiences' is set to 'Enabled'",
        r"SOFTWARE\Policies\Microsoft\Windows\CloudContent",
        "DisableConsumerExperiences",
        1
    )

    # Connect Policies (18.10.13.1)
    check_policy(
        "Ensure 'Require pin for pairing' is set to 'Enabled: First Time' OR 'Enabled: Always'",
        r"SOFTWARE\Policies\Microsoft\Windows\Bluetooth",
        "RequirePinForPairing",
        1
    )

    # Credential User Interface Policies (18.10.14)
    check_policy(
        "Ensure 'Do not display the password reveal button' is set to 'Enabled'",
        r"SOFTWARE\Policies\Microsoft\Windows\CredentialUI",
        "NoPasswordRevealButton",
        1
    )
    check_policy(
        "Ensure 'Enumerate administrator accounts on elevation' is set to 'Disabled'",
        r"SOFTWARE\Policies\Microsoft\Windows\CredentialUI",
        "EnumerateAdminAccountsOnElevation",
        0
    )
    check_policy(
        "Ensure 'Prevent the use of security questions for local accounts' is set to 'Enabled'",
        r"SOFTWARE\Policies\Microsoft\Windows\CredentialUI",
        "PreventSecurityQuestionsForLocalAccounts",
        1
    )

    # Data Collection and Preview Builds Policies (18.10.15)
    check_policy(
        "Ensure 'Allow Diagnostic Data' is set to 'Enabled: Diagnostic data off (not recommended)' or 'Enabled: Send required diagnostic data'",
        r"SOFTWARE\Policies\Microsoft\Windows\DataCollection",
        "AllowDiagnosticData",
        1
    )
    check_policy(
        "Ensure 'Configure Authenticated Proxy usage for the Connected User Experience and Telemetry service' is set to 'Enabled: Disable Authenticated Proxy usage'",
        r"SOFTWARE\Policies\Microsoft\Windows\DataCollection",
        "DisableAuthenticatedProxy",
        1
    )
    check_policy(
        "Ensure 'Disable OneSettings Downloads' is set to 'Enabled'",
        r"SOFTWARE\Policies\Microsoft\Windows\DataCollection",
        "DisableOneSettingsDownloads",
        1
    )
    check_policy(
        "Ensure 'Do not show feedback notifications' is set to 'Enabled'",
        r"SOFTWARE\Policies\Microsoft\Windows\DataCollection",
        "DoNotShowFeedbackNotifications",
        1
    )
    check_policy(
        "Ensure 'Enable OneSettings Auditing' is set to 'Enabled'",
        r"SOFTWARE\Policies\Microsoft\Windows\DataCollection",
        "EnableOneSettingsAuditing",
        1
    )
    check_policy(
        "Ensure 'Limit Diagnostic Log Collection' is set to 'Enabled'",
        r"SOFTWARE\Policies\Microsoft\Windows\DataCollection",
        "LimitDiagnosticLogCollection",
        1
    )
    check_policy(
        "Ensure 'Limit Dump Collection' is set to 'Enabled'",
        r"SOFTWARE\Policies\Microsoft\Windows\DataCollection",
        "LimitDumpCollection",
        1
    )

    # Preview Builds Policies (18.10.15.7)
    check_policy(
        "Ensure 'Control Preview Builds' is set to 'Enabled'",
        r"SOFTWARE\Policies\Microsoft\Windows\PreviewBuilds",
        "EnablePreviewBuilds",
        1
    )

if __name__ == "__main__":
    audit_policies()
