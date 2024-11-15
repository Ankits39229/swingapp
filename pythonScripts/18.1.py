import winreg as reg

def check_admin_template(setting_name, category, policy, expected_value, manual_check=False):
    try:
        # Define the registry path for administrative template policies
        registry_path = f"SOFTWARE\\Policies\\Microsoft\\{category}\\{policy}"
        
        # Open the registry key
        reg_key = reg.OpenKey(reg.HKEY_LOCAL_MACHINE, registry_path, 0, reg.KEY_READ)
        
        # Get the value of the specified registry key
        value, reg_type = reg.QueryValueEx(reg_key, "Setting")
        
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

# Main function to check Administrative Templates (Computer) configurations
def audit_admin_templates():
    print("Starting Administrative Templates (Computer) Audit...\n")

    # Control Panel - Personalization
    check_admin_template(
        "Ensure 'Prevent enabling lock screen camera' is set to 'Enabled'",
        "Control Panel\\Personalization",
        "NoLockScreenCamera",
        1  # 1 represents 'Enabled'
    )
    check_admin_template(
        "Ensure 'Prevent enabling lock screen slide show' is set to 'Enabled'",
        "Control Panel\\Personalization",
        "NoLockScreenSlideShow",
        1
    )
    
    # Control Panel - Regional and Language Options
    check_admin_template(
        "Ensure 'Allow users to enable online speech recognition services' is set to 'Disabled'",
        "Control Panel\\Regional and Language Options",
        "AllowOnlineSpeechRecognition",
        0  # 0 represents 'Disabled'
    )
    check_admin_template(
        "Ensure 'Allow Online Tips' is set to 'Disabled'",
        "Control Panel\\Regional and Language Options",
        "AllowOnlineTips",
        0
    )

    # MS Security Guide
    check_admin_template(
        "Ensure 'Apply UAC restrictions to local accounts on network logons' is set to 'Enabled'",
        "MS Security Guide",
        "LocalAccountTokenFilterPolicy",
        1
    )
    check_admin_template(
        "Ensure 'Configure RPC packet level privacy setting for incoming connections' is set to 'Enabled'",
        "MS Security Guide",
        "RequirePrivacyForRPC",
        1
    )
    check_admin_template(
        "Ensure 'Configure SMB v1 client driver' is set to 'Enabled: Disable driver (recommended)'",
        "MS Security Guide",
        "SMBv1",
        1
    )
    check_admin_template(
        "Ensure 'Configure SMB v1 server' is set to 'Disabled'",
        "MS Security Guide",
        "SMBv1Server",
        0
    )
    check_admin_template(
        "Ensure 'Enable Certificate Padding' is set to 'Enabled'",
        "MS Security Guide",
        "CertPadding",
        1
    )
    check_admin_template(
        "Ensure 'Enable Structured Exception Handling Overwrite Protection (SEHOP)' is set to 'Enabled'",
        "MS Security Guide",
        "SEHOP",
        1
    )
    check_admin_template(
        "Ensure 'NetBT NodeType configuration' is set to 'Enabled: P-node (recommended)'",
        "MS Security Guide",
        "NetBTNodeType",
        1
    )
    check_admin_template(
        "Ensure 'WDigest Authentication' is set to 'Disabled'",
        "MS Security Guide",
        "WDigestAuth",
        0
    )

    print("\nAdministrative Templates (Computer) audit complete.")

# Run the audit
audit_admin_templates()
