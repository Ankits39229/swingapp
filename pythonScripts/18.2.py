import winreg as reg

def check_mss_legacy(setting_name, registry_path, value_name, expected_value):
    try:
        # Open the registry key for MSS Legacy
        reg_key = reg.OpenKey(reg.HKEY_LOCAL_MACHINE, registry_path, 0, reg.KEY_READ)
        
        # Get the value
        value, reg_type = reg.QueryValueEx(reg_key, value_name)
        
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

def audit_mss_legacy():
    print("Starting MSS (Legacy) Audit...\n")
    
    # MSS (Legacy) Checks
    check_mss_legacy(
        "Ensure 'Enable Automatic Logon' is set to 'Disabled'",
        "SYSTEM\\CurrentControlSet\\Control\\Lsa",
        "AutoAdminLogon",
        0  # Disabled
    )
    check_mss_legacy(
        "Ensure 'IP source routing protection level' is set to 'Highest protection'",
        "SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters",
        "DisableIPSourceRouting",
        2  # Highest protection
    )
    check_mss_legacy(
        "Ensure 'Prevent the dial-up password from being saved' is set to 'Enabled'",
        "Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\Network",
        "DisableSavePassword",
        1  # Enabled
    )
    check_mss_legacy(
        "Ensure 'Enable ICMP redirects to override OSPF generated routes' is set to 'Disabled'",
        "SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters",
        "EnableICMPRedirect",
        0  # Disabled
    )
    check_mss_legacy(
        "Ensure 'Safe DLL search mode' is set to 'Enabled'",
        "SYSTEM\\CurrentControlSet\\Control\\Session Manager",
        "SafeDllSearchMode",
        1  # Enabled
    )
    print("\nMSS (Legacy) audit complete.")

def check_network(setting_name, registry_path, value_name, expected_value):
    try:
        # Open the registry key for Network settings
        reg_key = reg.OpenKey(reg.HKEY_LOCAL_MACHINE, registry_path, 0, reg.KEY_READ)
        
        # Get the value
        value, reg_type = reg.QueryValueEx(reg_key, value_name)
        
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

def audit_network():
    print("Starting Network Audit...\n")
    
    # Network Checks
    check_network(
        "Ensure 'Configure DNS over HTTPS (DoH) name resolution' is set to 'Enabled: Allow DoH'",
        "SYSTEM\\CurrentControlSet\\Services\\Dnscache\\Parameters",
        "EnableAutoDoh",
        1  # Enabled
    )
    check_network(
        "Ensure 'Configure NetBIOS settings' is set to 'Disable NetBIOS name resolution on public networks'",
        "SYSTEM\\CurrentControlSet\\Services\\NetBT\\Parameters\\Interfaces",
        "NetbiosOptions",
        2  # Disable on public networks
    )
    check_network(
        "Ensure 'Turn off multicast name resolution' is set to 'Enabled'",
        "SYSTEM\\CurrentControlSet\\Services\\Dnscache\\Parameters",
        "EnableMulticast",
        0  # Disabled
    )
    check_network(
        "Ensure 'Enable insecure guest logons' is set to 'Disabled'",
        "SYSTEM\\CurrentControlSet\\Services\\LanmanWorkstation\\Parameters",
        "AllowInsecureGuestAuth",
        0  # Disabled
    )
    check_network(
        "Ensure 'Require domain users to elevate when setting a network's location' is set to 'Enabled'",
        "Software\\Policies\\Microsoft\\Windows\\Network Connections",
        "NC_StdDomainUserSetLocation",
        1  # Enabled
    )
    print("\nNetwork audit complete.")

# Run the audits
audit_mss_legacy()
audit_network()
