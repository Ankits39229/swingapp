import winreg as reg

# Function to check registry policy
def check_policy(setting_name, registry_path, key_name, expected_value, manual_check=False):
    try:
        # Open registry key
        reg_key = reg.OpenKey(reg.HKEY_LOCAL_MACHINE, registry_path, 0, reg.KEY_READ)
        # Get key value
        value, reg_type = reg.QueryValueEx(reg_key, key_name)
        
        # Manual check
        compliance = "MANUAL CHECK REQUIRED" if manual_check else "PASS" if value == expected_value else "FAIL"
        # Close registry key
        reg.CloseKey(reg_key)
        
    except FileNotFoundError:
        compliance = "FAIL (NOT CONFIGURED)"
    except Exception as e:
        compliance = f"FAIL (Error: {e})"
    
    # Output results
    print(f"{setting_name} - {compliance}")

# Main function to audit policies
def audit_policies():
    print("Starting Network Client, Server, and Access Policies Audit...\n")

    # Microsoft network client policies
    check_policy(
        "Microsoft network client: Digitally sign communications (always) - Enabled",
        r"SYSTEM\CurrentControlSet\Services\LanmanWorkstation\Parameters",
        "RequireSecuritySignature",
        1
    )
    check_policy(
        "Microsoft network client: Digitally sign communications (if server agrees) - Enabled",
        r"SYSTEM\CurrentControlSet\Services\LanmanWorkstation\Parameters",
        "EnableSecuritySignature",
        1
    )
    check_policy(
        "Microsoft network client: Send unencrypted password to third-party SMB servers - Disabled",
        r"SYSTEM\CurrentControlSet\Services\LanmanWorkstation\Parameters",
        "EnablePlainTextPassword",
        0
    )

    # Microsoft network server policies
    check_policy(
        "Microsoft network server: Amount of idle time required before suspending session - 15 or fewer minutes",
        r"SYSTEM\CurrentControlSet\Services\LanmanServer\Parameters",
        "AutoDisconnect",
        15
    )
    check_policy(
        "Microsoft network server: Digitally sign communications (always) - Enabled",
        r"SYSTEM\CurrentControlSet\Services\LanmanServer\Parameters",
        "RequireSecuritySignature",
        1
    )
    check_policy(
        "Microsoft network server: Digitally sign communications (if client agrees) - Enabled",
        r"SYSTEM\CurrentControlSet\Services\LanmanServer\Parameters",
        "EnableSecuritySignature",
        1
    )
    check_policy(
        "Microsoft network server: Disconnect clients when logon hours expire - Enabled",
        r"SYSTEM\CurrentControlSet\Services\LanmanServer\Parameters",
        "EnableForcedLogoff",
        1
    )
    check_policy(
        "Microsoft network server: Server SPN target name validation level - Accept if provided by client or higher",
        r"SYSTEM\CurrentControlSet\Services\LanmanServer\Parameters",
        "SmbServerNameHardeningLevel",
        1
    )

    # Network access policies
    check_policy(
        "Network access: Allow anonymous SID/Name translation - Disabled",
        r"SYSTEM\CurrentControlSet\Control\Lsa",
        "AllowAnonymousSIDNameLookup",
        0
    )
    check_policy(
        "Network access: Do not allow anonymous enumeration of SAM accounts - Enabled",
        r"SYSTEM\CurrentControlSet\Control\Lsa",
        "RestrictAnonymousSAM",
        1
    )

    print("\nAudit complete.")

# Run the audit
audit_policies()
