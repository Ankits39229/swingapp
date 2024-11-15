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
    
    # 18.9.13 Early Launch Antimalware
    check_policy(
        "Ensure 'Boot-Start Driver Initialization Policy' is set to 'Enabled: Good, unknown and bad but critical'",
        r"SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System",
        "BootStartDriverInitializationPolicy",
        1
    )
    
    # 18.9.14 Enhanced Storage Access
    check_policy(
        "Ensure 'Enhanced Storage Access' is set to 'Enabled'",
        r"SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System",
        "EnhancedStorageAccess",
        1
    )
    
    # 18.9.15 File Classification Infrastructure
    check_policy(
        "Ensure 'File Classification Infrastructure' is set to 'Enabled'",
        r"SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System",
        "FileClassificationInfrastructure",
        1
    )
    
    # 18.9.16 File Share Shadow Copy Provider
    check_policy(
        "Ensure 'File Share Shadow Copy Provider' is set to 'Enabled'",
        r"SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System",
        "FileShareShadowCopyProvider",
        1
    )
    
    # 18.9.17 Filesystem (formerly NTFS Filesystem)
    check_policy(
        "Ensure 'Filesystem (NTFS)' is set to 'Enabled'",
        r"SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System",
        "FilesystemNTFS",
        1
    )
    
    # 18.9.18 Folder Redirection
    check_policy(
        "Ensure 'Folder Redirection' is set to 'Enabled'",
        r"SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System",
        "FolderRedirection",
        1
    )
    
    # 18.9.19 Group Policy
    check_policy(
        "Ensure 'Configure registry policy processing: Do not apply during periodic background processing' is set to 'Enabled: FALSE'",
        r"SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\GroupPolicy",
        "RegistryPolicyProcessing",
        0
    )
    
    check_policy(
        "Ensure 'Configure registry policy processing: Process even if the Group Policy objects have not changed' is set to 'Enabled: TRUE'",
        r"SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\GroupPolicy",
        "RegistryPolicyProcessing",
        1
    )
    
    check_policy(
        "Ensure 'Configure security policy processing: Do not apply during periodic background processing' is set to 'Enabled: FALSE'",
        r"SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\GroupPolicy",
        "SecurityPolicyProcessing",
        0
    )
    
    check_policy(
        "Ensure 'Configure security policy processing: Process even if the Group Policy objects have not changed' is set to 'Enabled: TRUE'",
        r"SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\GroupPolicy",
        "SecurityPolicyProcessing",
        1
    )
    
    check_policy(
        "Ensure 'Continue experiences on this device' is set to 'Disabled'",
        r"SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\GroupPolicy",
        "ContinueExperiencesOnDevice",
        0
    )
    
    check_policy(
        "Ensure 'Turn off background refresh of Group Policy' is set to 'Disabled'",
        r"SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\GroupPolicy",
        "BackgroundRefresh",
        0
    )

    # 18.9.20 Internet Communication Management
    check_policy(
        "Ensure 'Turn off access to the Store' is set to 'Enabled'",
        r"SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\InternetCommunication",
        "AccessStore",
        1
    )
    
    check_policy(
        "Ensure 'Turn off downloading of print drivers over HTTP' is set to 'Enabled'",
        r"SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\InternetCommunication",
        "DownloadPrintDrivers",
        1
    )

    check_policy(
        "Ensure 'Turn off handwriting personalization data sharing' is set to 'Enabled'",
        r"SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\InternetCommunication",
        "HandwritingPersonalizationDataSharing",
        1
    )

    # 18.9.23 Kerberos
    check_policy(
        "Ensure 'Support device authentication using certificate' is set to 'Enabled: Automatic'",
        r"SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Kerberos",
        "DeviceAuthenticationWithCertificate",
        1
    )

    # 18.9.24 Kernel DMA Protection
    check_policy(
        "Ensure 'Enumeration policy for external devices incompatible with Kernel DMA Protection' is set to 'Enabled: Block All'",
        r"SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\KernelDMAProtection",
        "ExternalDevicePolicy",
        1
    )

    # 18.9.25 LAPS (Local Administrator Password Solution)
    check_policy(
        "Ensure 'Configure password backup directory' is set to 'Enabled: Active Directory' or 'Enabled: Azure Active Directory'",
        r"SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\LAPS",
        "PasswordBackupDirectory",
        1
    )

    check_policy(
        "Ensure 'Do not allow password expiration time longer than required by policy' is set to 'Enabled'",
        r"SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\LAPS",
        "PasswordExpirationPolicy",
        1
    )

    # 18.9.26 Local Security Authority
    check_policy(
        "Ensure 'Allow Custom SSPs and APs to be loaded into LSASS' is set to 'Disabled'",
        r"SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\LSASS",
        "AllowCustomSSPs",
        0
    )
    
    check_policy(
        "Ensure 'Configures LSASS to run as a protected process' is set to 'Enabled: Enabled with UEFI Lock'",
        r"SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\LSASS",
        "ProtectedProcess",
        1
    )

    # 18.9.28 Logon
    check_policy(
        "Ensure 'Block user from showing account details on sign-in' is set to 'Enabled'",
        r"SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Logon",
        "BlockAccountDetails",
        1
    )
    
    check_policy(
        "Ensure 'Do not display network selection UI' is set to 'Enabled'",
        r"SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Logon",
        "DisplayNetworkSelectionUI",
        0
    )

    print("\nAudit complete.")

# Run the audit
audit_policies()
