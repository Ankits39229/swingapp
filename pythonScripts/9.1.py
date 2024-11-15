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
def audit_firewall_policies():
    print("Starting Windows Defender Firewall Security Policy Audit...\n")

    # Domain Profile
    check_policy(
        "Ensure 'Windows Firewall: Domain: Firewall state' is set to 'On (recommended)'",
        r"SYSTEM\CurrentControlSet\Services\SharedAccess\Parameters\FirewallPolicy\DomainProfile",
        "EnableFirewall",
        1
    )
    check_policy(
        "Ensure 'Windows Firewall: Domain: Inbound connections' is set to 'Block (default)'",
        r"SYSTEM\CurrentControlSet\Services\SharedAccess\Parameters\FirewallPolicy\DomainProfile",
        "DefaultInboundAction",
        1
    )
    check_policy(
        "Ensure 'Windows Firewall: Domain: Settings: Display a notification' is set to 'No'",
        r"SYSTEM\CurrentControlSet\Services\SharedAccess\Parameters\FirewallPolicy\DomainProfile",
        "DisableNotifications",
        1
    )
    check_policy(
        "Ensure 'Windows Firewall: Domain: Logging: Name' is set to '%SystemRoot%\\System32\\logfiles\\firewall\\domainfw.log'",
        r"SYSTEM\CurrentControlSet\Services\SharedAccess\Parameters\FirewallPolicy\DomainProfile\Logging",
        "LogFilePath",
        r"%SystemRoot%\System32\logfiles\firewall\domainfw.log"
    )
    check_policy(
        "Ensure 'Windows Firewall: Domain: Logging: Size limit (KB)' is set to '16,384 KB or greater'",
        r"SYSTEM\CurrentControlSet\Services\SharedAccess\Parameters\FirewallPolicy\DomainProfile\Logging",
        "LogFileSize",
        16384
    )
    check_policy(
        "Ensure 'Windows Firewall: Domain: Logging: Log dropped packets' is set to 'Yes'",
        r"SYSTEM\CurrentControlSet\Services\SharedAccess\Parameters\FirewallPolicy\DomainProfile\Logging",
        "LogDroppedPackets",
        1
    )
    check_policy(
        "Ensure 'Windows Firewall: Domain: Logging: Log successful connections' is set to 'Yes'",
        r"SYSTEM\CurrentControlSet\Services\SharedAccess\Parameters\FirewallPolicy\DomainProfile\Logging",
        "LogSuccessfulConnections",
        1
    )
    
    # Private Profile
    check_policy(
        "Ensure 'Windows Firewall: Private: Firewall state' is set to 'On (recommended)'",
        r"SYSTEM\CurrentControlSet\Services\SharedAccess\Parameters\FirewallPolicy\StandardProfile",
        "EnableFirewall",
        1
    )
    check_policy(
        "Ensure 'Windows Firewall: Private: Inbound connections' is set to 'Block (default)'",
        r"SYSTEM\CurrentControlSet\Services\SharedAccess\Parameters\FirewallPolicy\StandardProfile",
        "DefaultInboundAction",
        1
    )
    check_policy(
        "Ensure 'Windows Firewall: Private: Settings: Display a notification' is set to 'No'",
        r"SYSTEM\CurrentControlSet\Services\SharedAccess\Parameters\FirewallPolicy\StandardProfile",
        "DisableNotifications",
        1
    )
    check_policy(
        "Ensure 'Windows Firewall: Private: Logging: Name' is set to '%SystemRoot%\\System32\\logfiles\\firewall\\privatefw.log'",
        r"SYSTEM\CurrentControlSet\Services\SharedAccess\Parameters\FirewallPolicy\StandardProfile\Logging",
        "LogFilePath",
        r"%SystemRoot%\System32\logfiles\firewall\privatefw.log"
    )
    check_policy(
        "Ensure 'Windows Firewall: Private: Logging: Size limit (KB)' is set to '16,384 KB or greater'",
        r"SYSTEM\CurrentControlSet\Services\SharedAccess\Parameters\FirewallPolicy\StandardProfile\Logging",
        "LogFileSize",
        16384
    )
    check_policy(
        "Ensure 'Windows Firewall: Private: Logging: Log dropped packets' is set to 'Yes'",
        r"SYSTEM\CurrentControlSet\Services\SharedAccess\Parameters\FirewallPolicy\StandardProfile\Logging",
        "LogDroppedPackets",
        1
    )
    check_policy(
        "Ensure 'Windows Firewall: Private: Logging: Log successful connections' is set to 'Yes'",
        r"SYSTEM\CurrentControlSet\Services\SharedAccess\Parameters\FirewallPolicy\StandardProfile\Logging",
        "LogSuccessfulConnections",
        1
    )
    

    print("\nAudit complete.")

# Run the audit
audit_firewall_policies()
