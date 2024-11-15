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
    
    # 18.6.14 Network Provider - Hardened UNC Paths
    check_policy(
        "Ensure 'Hardened UNC Paths' is set to 'Enabled, with \"Require Mutual Authentication\", \"Require Integrity\", and \"Require Privacy\" set for all NETLOGON and SYSVOL shares'",
        r"SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System",
        "EnableUNCCheck",
        1  # Assuming '1' means enabled
    )
    
    # 18.6.19.2.1 IPv6 Transition Technologies - Disable IPv6
    check_policy(
        "Ensure 'TCPIP6 Parameter 'DisabledComponents' is set to '0xff (255)'",
        r"SYSTEM\CurrentControlSet\Services\Tcpip6\Parameters",
        "DisabledComponents",
        255
    )

    # 18.6.20.1 Windows Connect Now - Configuration of wireless settings
    check_policy(
        "Ensure 'Configuration of wireless settings using Windows Connect Now' is set to 'Disabled'",
        r"SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Wireless",
        "EnableWindowsConnectNow",
        0
    )
    
    # 18.6.20.2 Windows Connect Now - Prohibit access of the Windows Connect Now wizards
    check_policy(
        "Ensure 'Prohibit access of the Windows Connect Now wizards' is set to 'Enabled'",
        r"SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Wireless",
        "ProhibitWindowsConnectNow",
        1
    )
    
    # 18.6.21.1 Windows Connection Manager - Minimize the number of simultaneous connections
    check_policy(
        "Ensure 'Minimize the number of simultaneous connections to the Internet or a Windows Domain' is set to 'Enabled: 3 = Prevent Wi-Fi when on Ethernet'",
        r"SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Network",
        "MinConnections",
        3
    )

    # 18.6.21.2 Windows Connection Manager - Prohibit connection to non-domain networks
    check_policy(
        "Ensure 'Prohibit connection to non-domain networks when connected to domain authenticated network' is set to 'Enabled'",
        r"SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Network",
        "ProhibitNonDomainConnection",
        1
    )
    
    # 18.6.23.2.1 WLAN Service - Allow Windows to automatically connect to suggested open hotspots
    check_policy(
        "Ensure 'Allow Windows to automatically connect to suggested open hotspots, to networks shared by contacts, and to hotspots offering paid services' is set to 'Disabled'",
        r"SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Network",
        "AutoConnectToOpenHotspots",
        0
    )

    # 18.7.1 Printers - Allow Print Spooler to accept client connections
    check_policy(
        "Ensure 'Allow Print Spooler to accept client connections' is set to 'Disabled'",
        r"SYSTEM\CurrentControlSet\Services\Spooler",
        "AllowClientConnections",
        0
    )

    # 18.7.2 Printers - Configure Redirection Guard
    check_policy(
        "Ensure 'Configure Redirection Guard' is set to 'Enabled: Redirection Guard Enabled'",
        r"SYSTEM\CurrentControlSet\Services\Spooler",
        "RedirectionGuard",
        1
    )

    # 18.7.8 Printers - Limits print driver installation to Administrators
    check_policy(
        "Ensure 'Limits print driver installation to Administrators' is set to 'Enabled'",
        r"SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Printers",
        "LimitDriverInstallationToAdmins",
        1
    )

    # 18.8.1.1 Notifications - Turn off notifications network usage
    check_policy(
        "Ensure 'Turn off notifications network usage' is set to 'Enabled'",
        r"SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer",
        "DisableNetworkUsageNotifications",
        1
    )
    
    # 18.8.2 Start Menu - Remove Personalized Website Recommendations from the Recommended section
    check_policy(
        "Ensure 'Remove Personalized Website Recommendations from the Recommended section in the Start Menu' is set to 'Enabled'",
        r"SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer",
        "RemovePersonalizedRecommendations",
        1
    )

    print("\nAudit complete.")

# Run the audit
audit_policies()
