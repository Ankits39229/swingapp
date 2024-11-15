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
    print("Starting Local Policies Audit...\n")

    # User Rights Assignment Policies
    check_policy(
        "Ensure 'Access Credential Manager as a trusted caller' is set to 'No One'",
        r"SYSTEM\CurrentControlSet\Services\Policy\AccessCredentialManager",
        "AccessCredentialManager",
        "No One"
    )
    check_policy(
        "Ensure 'Access this computer from the network' is set to 'Administrators, Remote Desktop Users'",
        r"SYSTEM\CurrentControlSet\Services\Policy\AccessFromNetwork",
        "AccessFromNetwork",
        "Administrators,Remote Desktop Users"
    )
    check_policy(
        "Ensure 'Act as part of the operating system' is set to 'No One'",
        r"SYSTEM\CurrentControlSet\Services\Policy\ActAsOS",
        "ActAsOS",
        "No One"
    )
    check_policy(
        "Ensure 'Adjust memory quotas for a process' is set to 'Administrators, LOCAL SERVICE, NETWORK SERVICE'",
        r"SYSTEM\CurrentControlSet\Services\Policy\AdjustMemoryQuotas",
        "AdjustMemoryQuotas",
        "Administrators,LOCAL SERVICE,NETWORK SERVICE"
    )
    check_policy(
        "Ensure 'Allow log on locally' is set to 'Administrators, Users'",
        r"SYSTEM\CurrentControlSet\Services\Policy\AllowLogOnLocally",
        "AllowLogOnLocally",
        "Administrators,Users"
    )
    check_policy(
        "Ensure 'Allow log on through Remote Desktop Services' is set to 'Administrators, Remote Desktop Users'",
        r"SYSTEM\CurrentControlSet\Services\Policy\AllowLogOnThroughRDS",
        "AllowLogOnThroughRDS",
        "Administrators,Remote Desktop Users"
    )
    check_policy(
        "Ensure 'Back up files and directories' is set to 'Administrators'",
        r"SYSTEM\CurrentControlSet\Services\Policy\BackupFiles",
        "BackupFiles",
        "Administrators"
    )
    check_policy(
        "Ensure 'Change the system time' is set to 'Administrators, LOCAL SERVICE'",
        r"SYSTEM\CurrentControlSet\Services\Policy\ChangeSystemTime",
        "ChangeSystemTime",
        "Administrators,LOCAL SERVICE"
    )
    check_policy(
        "Ensure 'Change the time zone' is set to 'Administrators, LOCAL SERVICE, Users'",
        r"SYSTEM\CurrentControlSet\Services\Policy\ChangeTimeZone",
        "ChangeTimeZone",
        "Administrators,LOCAL SERVICE,Users"
    )
    check_policy(
        "Ensure 'Create a pagefile' is set to 'Administrators'",
        r"SYSTEM\CurrentControlSet\Services\Policy\CreatePagefile",
        "CreatePagefile",
        "Administrators"
    )

    print("\nAudit complete.")

# Run the audit
audit_policies()
