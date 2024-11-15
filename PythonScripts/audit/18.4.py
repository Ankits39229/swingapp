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

    # 18.9.3 Audit Process Creation
    check_policy(
        "Ensure 'Include command line in process creation events' is set to 'Enabled'",
        r"SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Audit",
        "ProcessCreationIncludeCmdLine",
        1
    )

    # 18.9.4 Credentials Delegation
    check_policy(
        "Ensure 'Encryption Oracle Remediation' is set to 'Enabled: Force Updated Clients'",
        r"SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System",
        "EncryptionOracleRemediation",
        1
    )
    check_policy(
        "Ensure 'Remote host allows delegation of non-exportable credentials' is set to 'Enabled'",
        r"SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System",
        "AllowNonExportableDelegation",
        1
    )

    # 18.9.5 Device Guard
    check_policy(
        "Ensure 'Turn On Virtualization Based Security' is set to 'Enabled'",
        r"SOFTWARE\Policies\Microsoft\Windows\DeviceGuard",
        "EnableVirtualizationBasedSecurity",
        1
    )
    check_policy(
        "Ensure 'Turn On Virtualization Based Security: Select Platform Security Level' is set to 'Secure Boot or higher'",
        r"SOFTWARE\Policies\Microsoft\Windows\DeviceGuard",
        "PlatformSecurityLevel",
        2  # 2 corresponds to 'Secure Boot'
    )
    check_policy(
        "Ensure 'Turn On Virtualization Based Security: Virtualization Based Protection of Code Integrity' is set to 'Enabled with UEFI lock'",
        r"SOFTWARE\Policies\Microsoft\Windows\DeviceGuard",
        "CodeIntegrityPolicyEnforcement",
        1
    )
    check_policy(
        "Ensure 'Turn On Virtualization Based Security: Require UEFI Memory Attributes Table' is set to 'True'",
        r"SOFTWARE\Policies\Microsoft\Windows\DeviceGuard",
        "RequireUEFIMemoryAttributesTable",
        1
    )
    check_policy(
        "Ensure 'Turn On Virtualization Based Security: Credential Guard Configuration' is set to 'Enabled with UEFI lock'",
        r"SOFTWARE\Policies\Microsoft\Windows\DeviceGuard",
        "CredentialGuardConfiguration",
        1
    )
    check_policy(
        "Ensure 'Turn On Virtualization Based Security: Secure Launch Configuration' is set to 'Enabled'",
        r"SOFTWARE\Policies\Microsoft\Windows\DeviceGuard",
        "SecureLaunchConfiguration",
        1
    )
    check_policy(
        "Ensure 'Turn On Virtualization Based Security: Kernel-mode Hardware-enforced Stack Protection' is set to 'Enabled: Enabled in enforcement mode'",
        r"SOFTWARE\Policies\Microsoft\Windows\DeviceGuard",
        "KernelModeHardwareStackProtection",
        1
    )

    # 18.9.6 Device Health Attestation Service - Placeholder for future implementation if needed

    # 18.9.7 Device Installation
    check_policy(
        "Ensure 'Prevent installation of devices that match any of these device IDs' is set to 'Enabled'",
        r"SOFTWARE\Policies\Microsoft\Windows\DeviceInstall\Restrictions",
        "PreventDevIDInstallation",
        1
    )
    check_policy(
        "Ensure 'Prevent installation of devices that match any of these device IDs: PCI\\CC_0C0A' is set to 'Enabled'",
        r"SOFTWARE\Policies\Microsoft\Windows\DeviceInstall\Restrictions",
        "PreventPCI_0C0A_Installation",
        1
    )
    check_policy(
        "Ensure 'Prevent installation of devices using drivers that match these device setup classes' is set to 'Enabled'",
        r"SOFTWARE\Policies\Microsoft\Windows\DeviceInstall\Restrictions",
        "PreventDriverSetupInstallation",
        1
    )

    print("\nAudit complete.")

# Run the audit
audit_policies()
