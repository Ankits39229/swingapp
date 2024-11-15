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

    # Policy Change
    check_audit_policy(
        "Ensure 'Audit Audit Policy Change' is set to include 'Success'",
        "Policy Change",
        "Audit Policy Change",
        "Success"
    )
    check_audit_policy(
        "Ensure 'Audit Authentication Policy Change' is set to include 'Success'",
        "Policy Change",
        "Authentication Policy Change",
        "Success"
    )
    check_audit_policy(
        "Ensure 'Audit Authorization Policy Change' is set to include 'Success'",
        "Policy Change",
        "Authorization Policy Change",
        "Success"
    )
    check_audit_policy(
        "Ensure 'Audit MPSSVC Rule-Level Policy Change' is set to 'Success and Failure'",
        "Policy Change",
        "MPSSVC Rule-Level Policy Change",
        "Success and Failure"
    )
    check_audit_policy(
        "Ensure 'Audit Other Policy Change Events' is set to include 'Failure'",
        "Policy Change",
        "Other Policy Change Events",
        "Failure"
    )
    
    # Privilege Use
    check_audit_policy(
        "Ensure 'Audit Sensitive Privilege Use' is set to 'Success and Failure'",
        "Privilege Use",
        "Sensitive Privilege Use",
        "Success and Failure"
    )
    
    # System
    check_audit_policy(
        "Ensure 'Audit IPsec Driver' is set to 'Success and Failure'",
        "System",
        "IPsec Driver",
        "Success and Failure"
    )
    check_audit_policy(
        "Ensure 'Audit Other System Events' is set to 'Success and Failure'",
        "System",
        "Other System Events",
        "Success and Failure"
    )
    check_audit_policy(
        "Ensure 'Audit Security State Change' is set to include 'Success'",
        "System",
        "Security State Change",
        "Success"
    )
    check_audit_policy(
        "Ensure 'Audit Security System Extension' is set to include 'Success'",
        "System",
        "Security System Extension",
        "Success"
    )
    check_audit_policy(
        "Ensure 'Audit System Integrity' is set to 'Success and Failure'",
        "System",
        "System Integrity",
        "Success and Failure"
    )

    print("\nAdvanced Audit Policy Configuration audit complete.")

# Run the audit
audit_advanced_policies()
