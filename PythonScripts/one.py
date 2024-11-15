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

    # Password Policies
    check_policy(
        "Ensure 'Enforce password history' is set to '24 or more password(s)'",
        r"SYSTEM\CurrentControlSet\Services\Netlogon\Parameters",
        "EnforcePasswordHistory",
        24
    )
    check_policy(
        "Ensure 'Maximum password age' is set to '365 or fewer days, but not 0'",
        r"SYSTEM\CurrentControlSet\Services\Netlogon\Parameters",
        "MaximumPasswordAge",
        365
    )
    check_policy(
        "Ensure 'Minimum password age' is set to '1 or more day(s)'",
        r"SYSTEM\CurrentControlSet\Services\Netlogon\Parameters",
        "MinimumPasswordAge",
        1
    )
    check_policy(
        "Ensure 'Minimum password length' is set to '14 or more character(s)'",
        r"SYSTEM\CurrentControlSet\Services\Netlogon\Parameters",
        "MinimumPasswordLength",
        14
    )
    check_policy(
        "Ensure 'Password must meet complexity requirements' is set to 'Enabled'",
        r"SYSTEM\CurrentControlSet\Services\Netlogon\Parameters",
        "PasswordComplexity",
        1
    )
    check_policy(
        "Ensure 'Relax minimum password length limits' is set to 'Enabled'",
        r"SYSTEM\CurrentControlSet\Services\Netlogon\Parameters",
        "RelaxMinimumPasswordLengthLimits",
        1
    )
    check_policy(
        "Ensure 'Store passwords using reversible encryption' is set to 'Disabled'",
        r"SYSTEM\CurrentControlSet\Services\Netlogon\Parameters",
        "ClearTextPassword",
        0
    )
    
    # Account Lockout Policies
    check_policy(
        "Ensure 'Account lockout duration' is set to '15 or more minute(s)'",
        r"SYSTEM\CurrentControlSet\Services\Netlogon\Parameters",
        "LockoutDuration",
        15
    )
    check_policy(
        "Ensure 'Account lockout threshold' is set to '5 or fewer invalid logon attempt(s), but not 0'",
        r"SYSTEM\CurrentControlSet\Services\Netlogon\Parameters",
        "LockoutThreshold",
        5
    )
    check_policy(
        "Ensure 'Allow Administrator account lockout' is set to 'Enabled'",
        r"SYSTEM\CurrentControlSet\Services\Netlogon\Parameters",
        "AdminAccountLockout",
        1,
        manual_check=True  # Manual check required for administrator lockout setting
    )
    check_policy(
        "Ensure 'Reset account lockout counter after' is set to '15 or more minute(s)'",
        r"SYSTEM\CurrentControlSet\Services\Netlogon\Parameters",
        "ResetLockoutCount",
        15
    )

    print("\nAudit complete.")

# Run the audit
audit_policies()
