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
    print("Starting Accounts and Domain Member Policies Audit...\n")

    # Accounts Policies
    check_policy(
        "Ensure 'Accounts: Block Microsoft accounts' is set to 'Users can't add or log on with Microsoft accounts'",
        r"SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System",
        "NoConnectedUser",
        3
    )
    check_policy(
        "Ensure 'Accounts: Guest account status' is set to 'Disabled'",
        r"SAM\SAM\Domains\Account\Users\Names\Guest",
        "GuestAccountStatus",
        0
    )
    check_policy(
        "Ensure 'Accounts: Limit local account use of blank passwords to console logon only' is set to 'Enabled'",
        r"SYSTEM\CurrentControlSet\Control\Lsa",
        "LimitBlankPasswordUse",
        1
    )
    check_policy(
        "Configure 'Accounts: Rename administrator account'",
        r"SAM\SAM\Domains\Account\Users\Names\Administrator",
        "RenameAdministratorAccount",
        "NewAdminName"
    )
    check_policy(
        "Configure 'Accounts: Rename guest account'",
        r"SAM\SAM\Domains\Account\Users\Names\Guest",
        "RenameGuestAccount",
        "NewGuestName"
    )

    # Audit Policies
    check_policy(
        "Ensure 'Audit: Force audit policy subcategory settings to override audit policy category settings' is set to 'Enabled'",
        r"SYSTEM\CurrentControlSet\Control\Lsa",
        "SCENoApplyLegacyAuditPolicy",
        1
    )
    check_policy(
        "Ensure 'Audit: Shut down system immediately if unable to log security audits' is set to 'Disabled'",
        r"SYSTEM\CurrentControlSet\Control\Lsa",
        "CrashOnAuditFail",
        0
    )

    # Devices Policies
    check_policy(
        "Ensure 'Devices: Prevent users from installing printer drivers' is set to 'Enabled'",
        r"SYSTEM\CurrentControlSet\Control\Print\Providers\LanMan Print Services\Servers",
        "AddPrinterDrivers",
        1
    )

    # Domain Member Policies
    check_policy(
        "Ensure 'Domain member: Digitally encrypt or sign secure channel data (always)' is set to 'Enabled'",
        r"SYSTEM\CurrentControlSet\Services\Netlogon\Parameters",
        "SealSecureChannel",
        1
    )
    check_policy(
        "Ensure 'Domain member: Digitally encrypt secure channel data (when possible)' is set to 'Enabled'",
        r"SYSTEM\CurrentControlSet\Services\Netlogon\Parameters",
        "SignSecureChannel",
        1
    )

    print("\nAudit complete.")

# Run the audit
audit_policies()
