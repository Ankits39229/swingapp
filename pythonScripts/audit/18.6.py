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

    # Clipboard Synchronization
    check_policy(
        "Ensure 'Allow Clipboard synchronization across devices' is set to 'Disabled'",
        r"SOFTWARE\Policies\Microsoft\Windows\System",
        "AllowClipboardSync",
        0
    )
    
    # User Activities Upload
    check_policy(
        "Ensure 'Allow upload of User Activities' is set to 'Disabled'",
        r"SOFTWARE\Policies\Microsoft\Windows\System",
        "AllowUploadUserActivities",
        0
    )

    # PIN Complexity (manual check)
    check_policy(
        "Ensure 'PIN Complexity' is configured properly",
        r"SOFTWARE\Policies\Microsoft\Windows\System",
        "PinComplexity",
        0,  # Example value, could vary based on specific policy configurations
        manual_check=True
    )
    
    # Power Management Settings
    check_policy(
        "Ensure 'Allow network connectivity during connected-standby (on battery)' is set to 'Disabled'",
        r"SOFTWARE\Policies\Microsoft\Windows\Power",
        "AllowNetworkConnectivityOnBattery",
        0
    )
    check_policy(
        "Ensure 'Allow network connectivity during connected-standby (plugged in)' is set to 'Disabled'",
        r"SOFTWARE\Policies\Microsoft\Windows\Power",
        "AllowNetworkConnectivityPluggedIn",
        0
    )
    check_policy(
        "Ensure 'Require a password when a computer wakes (on battery)' is set to 'Enabled'",
        r"SOFTWARE\Policies\Microsoft\Windows\Power",
        "RequirePasswordOnWakeupBattery",
        1
    )
    check_policy(
        "Ensure 'Require a password when a computer wakes (plugged in)' is set to 'Enabled'",
        r"SOFTWARE\Policies\Microsoft\Windows\Power",
        "RequirePasswordOnWakeupPluggedIn",
        1
    )

    # Remote Assistance
    check_policy(
        "Ensure 'Configure Offer Remote Assistance' is set to 'Disabled'",
        r"SOFTWARE\Policies\Microsoft\Windows\RemoteAssistance",
        "OfferRemoteAssistance",
        0
    )
    check_policy(
        "Ensure 'Configure Solicited Remote Assistance' is set to 'Disabled'",
        r"SOFTWARE\Policies\Microsoft\Windows\RemoteAssistance",
        "SolicitedRemoteAssistance",
        0
    )

    # Remote Procedure Call (RPC)
    check_policy(
        "Ensure 'Enable RPC Endpoint Mapper Client Authentication' is set to 'Enabled'",
        r"SOFTWARE\Policies\Microsoft\Windows\RPC",
        "EnableRPCClientAuthentication",
        1
    )
    check_policy(
        "Ensure 'Restrict Unauthenticated RPC clients' is set to 'Enabled: Authenticated'",
        r"SOFTWARE\Policies\Microsoft\Windows\RPC",
        "RestrictRPCClients",
        1
    )

    # Trusted Platform Module (TPM)
    check_policy(
        "Ensure 'Enable TPM' is set to 'Enabled'",
        r"SOFTWARE\Policies\Microsoft\Windows\TPM",
        "EnableTPM",
        1
    )

    # User Profile Advertisements
    check_policy(
        "Ensure 'Turn off the advertising ID' is set to 'Enabled'",
        r"SOFTWARE\Policies\Microsoft\Windows\Personalization",
        "TurnOffAdvertisingId",
        1
    )

    # Windows Time Service
    check_policy(
        "Ensure 'Enable Windows NTP Client' is set to 'Enabled'",
        r"SOFTWARE\Policies\Microsoft\Windows\TimeService",
        "EnableNTPClient",
        1
    )
    check_policy(
        "Ensure 'Enable Windows NTP Server' is set to 'Disabled'",
        r"SOFTWARE\Policies\Microsoft\Windows\TimeService",
        "EnableNTPServer",
        0
    )

    # Windows File Protection
    check_policy(
        "Ensure 'Windows File Protection' is enabled",
        r"SOFTWARE\Policies\Microsoft\Windows\System",
        "EnableFileProtection",
        1
    )
    
    # Audit complete
    print("\nAudit complete.")

# Run the audit
audit_policies()
