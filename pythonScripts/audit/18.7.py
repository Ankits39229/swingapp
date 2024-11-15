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

    # AutoPlay Policies
    check_policy(
        "Ensure 'Disallow Autoplay for non-volume devices' is set to 'Enabled'",
        r"SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer",
        "NoAutoPlayForNonVolume",
        1
    )
    check_policy(
        "Ensure 'Set the default behavior for AutoRun' is set to 'Enabled: Do not execute any autorun commands'",
        r"SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer",
        "NoDriveTypeAutoRun",
        255
    )
    check_policy(
        "Ensure 'Turn off Autoplay' is set to 'Enabled: All drives'",
        r"SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer",
        "NoAutoPlay",
        3
    )
    
    # Biometrics Policies
    check_policy(
        "Ensure 'Configure enhanced anti-spoofing' is set to 'Enabled'",
        r"SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Biometrics",
        "EnhancedAntiSpoofing",
        1
    )

    # BitLocker Drive Encryption Policies for Fixed Data Drives
    check_policy(
        "Ensure 'Allow access to BitLocker-protected fixed data drives from earlier versions of Windows' is set to 'Disabled'",
        r"SOFTWARE\Policies\Microsoft\FVE",
        "DisableBitlockerHardDriveAccess",
        1
    )
    check_policy(
        "Ensure 'Choose how BitLocker-protected fixed drives can be recovered' is set to 'Enabled'",
        r"SOFTWARE\Policies\Microsoft\FVE",
        "RecoveryPassword",
        1
    )
    check_policy(
        "Ensure 'Choose how BitLocker-protected fixed drives can be recovered: Allow data recovery agent' is set to 'Enabled: True'",
        r"SOFTWARE\Policies\Microsoft\FVE",
        "AllowDataRecoveryAgent",
        1
    )
    check_policy(
        "Ensure 'Choose how BitLocker-protected fixed drives can be recovered: Recovery Password' is set to 'Enabled: Allow 48-digit recovery password' or higher",
        r"SOFTWARE\Policies\Microsoft\FVE",
        "RecoveryPasswordLength",
        48
    )
    check_policy(
        "Ensure 'Choose how BitLocker-protected fixed drives can be recovered: Recovery Key' is set to 'Enabled: Allow 256-bit recovery key' or higher",
        r"SOFTWARE\Policies\Microsoft\FVE",
        "RecoveryKeyLength",
        256
    )
    check_policy(
        "Ensure 'Choose how BitLocker-protected fixed drives can be recovered: Omit recovery options from the BitLocker setup wizard' is set to 'Enabled: True'",
        r"SOFTWARE\Policies\Microsoft\FVE",
        "OmitRecoveryOptions",
        1
    )
    check_policy(
        "Ensure 'Choose how BitLocker-protected fixed drives can be recovered: Save BitLocker recovery information to AD DS for fixed data drives' is set to 'Enabled: False'",
        r"SOFTWARE\Policies\Microsoft\FVE",
        "SaveRecoveryInformationToAD",
        0
    )

    # BitLocker Drive Encryption Policies for Operating System Drives
    check_policy(
        "Ensure 'Allow enhanced PINs for startup' is set to 'Enabled'",
        r"SOFTWARE\Policies\Microsoft\FVE",
        "AllowEnhancedPins",
        1
    )
    check_policy(
        "Ensure 'Allow Secure Boot for integrity validation' is set to 'Enabled'",
        r"SOFTWARE\Policies\Microsoft\FVE",
        "AllowSecureBoot",
        1
    )
    check_policy(
        "Ensure 'Choose how BitLocker-protected operating system drives can be recovered' is set to 'Enabled'",
        r"SOFTWARE\Policies\Microsoft\FVE",
        "RecoveryPasswordForOSDrive",
        1
    )
    check_policy(
        "Ensure 'Choose how BitLocker-protected operating system drives can be recovered: Allow data recovery agent' is set to 'Enabled: False'",
        r"SOFTWARE\Policies\Microsoft\FVE",
        "AllowDataRecoveryAgentForOSDrive",
        0
    )
    check_policy(
        "Ensure 'Choose how BitLocker-protected operating system drives can be recovered: Recovery Password' is set to 'Enabled: Require 48-digit recovery password'",
        r"SOFTWARE\Policies\Microsoft\FVE",
        "OSDriveRecoveryPasswordLength",
        48
    )
    check_policy(
        "Ensure 'Require additional authentication at startup' is set to 'Enabled'",
        r"SOFTWARE\Policies\Microsoft\FVE",
        "RequireAdditionalAuthentication",
        1
    )
    check_policy(
        "Ensure 'Require additional authentication at startup: Allow BitLocker without a compatible TPM' is set to 'Enabled: False'",
        r"SOFTWARE\Policies\Microsoft\FVE",
        "AllowBitlockerWithoutTPM",
        0
    )

    print("\nAudit complete.")

# Run the audit
audit_policies()
