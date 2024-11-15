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
    print("Starting Network Security Policies Audit...\n")

    # Network security policies
    check_policy(
        "Network security: Allow Local System to use computer identity for NTLM - Enabled",
        r"SYSTEM\CurrentControlSet\Control\Lsa\MSV1_0",
        "UseMachineID",
        1
    )
    check_policy(
        "Network security: Allow LocalSystem NULL session fallback - Disabled",
        r"SYSTEM\CurrentControlSet\Control\Lsa\MSV1_0",
        "AllowNullSessionFallback",
        0
    )
    check_policy(
        "Network security: Allow PKU2U authentication requests - Disabled",
        r"SYSTEM\CurrentControlSet\Control\Lsa\pku2u",
        "AllowOnlineID",
        0
    )
    check_policy(
        "Network security: Configure encryption types allowed for Kerberos - AES128_HMAC_SHA1, AES256_HMAC_SHA1, Future encryption types",
        r"SYSTEM\CurrentControlSet\Control\Lsa\Kerberos\Parameters",
        "SupportedEncryptionTypes",
        0x7  # AES128_HMAC_SHA1 and AES256_HMAC_SHA1
    )
    check_policy(
        "Network security: Do not store LAN Manager hash value on next password change - Enabled",
        r"SYSTEM\CurrentControlSet\Control\Lsa",
        "NoLMHash",
        1
    )
    check_policy(
        "Network security: Force logoff when logon hours expire - Enabled",
        r"SYSTEM\CurrentControlSet\Control\Lsa",
        "ForceLogoffWhenHourExpire",
        1,
        manual_check=True
    )
    check_policy(
        "Network security: LAN Manager authentication level - Send NTLMv2 response only. Refuse LM & NTLM",
        r"SYSTEM\CurrentControlSet\Control\Lsa",
        "LmCompatibilityLevel",
        5
    )
    check_policy(
        "Network security: LDAP client signing requirements - Negotiate signing or higher",
        r"SYSTEM\CurrentControlSet\Services\LDAP",
        "LDAPClientIntegrity",
        1
    )
    check_policy(
        "Network security: Minimum session security for NTLM SSP clients - Require NTLMv2 session security, Require 128-bit encryption",
        r"SYSTEM\CurrentControlSet\Control\Lsa\MSV1_0",
        "NTLMMinClientSec",
        0x20080000
    )
    check_policy(
        "Network security: Minimum session security for NTLM SSP servers - Require NTLMv2 session security, Require 128-bit encryption",
        r"SYSTEM\CurrentControlSet\Control\Lsa\MSV1_0",
        "NTLMMinServerSec",
        0x20080000
    )

    print("\nAudit complete.")

# Run the audit
audit_policies()
