import winreg as reg

def check_audit_policy(setting_name, category, subcategory, expected_value, manual_check=False):
    try:
        # Define the registry path for audit policies
        registry_path = f"SYSTEM\\CurrentControlSet\\Services\\Audit\\Policy\\{category}\\{subcategory}"
        
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

# Main function to check Advanced Audit Policy configurations
def audit_advanced_policies():
    print("Starting Advanced Audit Policy Configuration Audit...\n")

    # Account Logon
    check_audit_policy(
        "Ensure 'Audit Credential Validation' is set to 'Success and Failure'",
        "Account Logon",
        "Audit Credential Validation",
        "Success and Failure"
    )
    
    # Account Management
    check_audit_policy(
        "Ensure 'Audit Application Group Management' is set to 'Success and Failure'",
        "Account Management",
        "Audit Application Group Management",
        "Success and Failure"
    )
    check_audit_policy(
        "Ensure 'Audit Security Group Management' is set to include 'Success'",
        "Account Management",
        "Audit Security Group Management",
        "Success"
    )
    check_audit_policy(
        "Ensure 'Audit User Account Management' is set to 'Success and Failure'",
        "Account Management",
        "Audit User Account Management",
        "Success and Failure"
    )
    
    # Detailed Tracking
    check_audit_policy(
        "Ensure 'Audit PNP Activity' is set to include 'Success'",
        "Detailed Tracking",
        "Audit PNP Activity",
        "Success"
    )
    check_audit_policy(
        "Ensure 'Audit Process Creation' is set to include 'Success'",
        "Detailed Tracking",
        "Audit Process Creation",
        "Success"
    )
    
    # Logon/Logoff
    check_audit_policy(
        "Ensure 'Audit Account Lockout' is set to include 'Failure'",
        "Logon/Logoff",
        "Audit Account Lockout",
        "Failure"
    )
    check_audit_policy(
        "Ensure 'Audit Group Membership' is set to include 'Success'",
        "Logon/Logoff",
        "Audit Group Membership",
        "Success"
    )
    check_audit_policy(
        "Ensure 'Audit Logoff' is set to include 'Success'",
        "Logon/Logoff",
        "Audit Logoff",
        "Success"
    )
    check_audit_policy(
        "Ensure 'Audit Logon' is set to 'Success and Failure'",
        "Logon/Logoff",
        "Audit Logon",
        "Success and Failure"
    )
    check_audit_policy(
        "Ensure 'Audit Other Logon/Logoff Events' is set to 'Success and Failure'",
        "Logon/Logoff",
        "Audit Other Logon/Logoff Events",
        "Success and Failure"
    )
    check_audit_policy(
        "Ensure 'Audit Special Logon' is set to include 'Success'",
        "Logon/Logoff",
        "Audit Special Logon",
        "Success"
    )
    
    # Object Access
    check_audit_policy(
        "Ensure 'Audit Detailed File Share' is set to include 'Failure'",
        "Object Access",
        "Audit Detailed File Share",
        "Failure"
    )
    check_audit_policy(
        "Ensure 'Audit File Share' is set to 'Success and Failure'",
        "Object Access",
        "Audit File Share",
        "Success and Failure"
    )
    check_audit_policy(
        "Ensure 'Audit Other Object Access Events' is set to 'Success and Failure'",
        "Object Access",
        "Audit Other Object Access Events",
        "Success and Failure"
    )
    check_audit_policy(
        "Ensure 'Audit Removable Storage' is set to 'Success and Failure'",
        "Object Access",
        "Audit Removable Storage",
        "Success and Failure"
    )

    print("\nAdvanced Audit Policy Configuration audit complete.")

# Run the audit
audit_advanced_policies()
