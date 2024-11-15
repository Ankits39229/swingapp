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
    print("Starting Windows Security Policy Audit...\n")

    # MAPS Policies
    check_policy(
        "Ensure 'Configure local setting override for reporting to Microsoft MAPS' is set to 'Disabled'",
        r"SOFTWARE\Policies\Microsoft\Microsoft Defender\Reporting",
        "MAPSReporting",
        0
    )
    check_policy(
        "Ensure 'Join Microsoft MAPS' is set to 'Disabled'",
        r"SOFTWARE\Policies\Microsoft\Microsoft Defender\Reporting",
        "JoinMAPS",
        0
    )

    # Microsoft Defender Exploit Guard
    check_policy(
        "Ensure 'Configure Attack Surface Reduction rules' is set to 'Enabled'",
        r"SOFTWARE\Policies\Microsoft\Windows Defender\ExploitGuard",
        "EnableAttackSurfaceReductionRules",
        1
    )
    check_policy(
        "Ensure 'Configure Attack Surface Reduction rules: Set the state for each ASR rule' is configured",
        r"SOFTWARE\Policies\Microsoft\Windows Defender\ExploitGuard",
        "AttackSurfaceReductionRules_Enabled",
        1
    )
    check_policy(
        "Ensure 'Prevent users and apps from accessing dangerous websites' is set to 'Enabled: Block'",
        r"SOFTWARE\Policies\Microsoft\Windows Defender\NetworkProtection",
        "EnableNetworkProtection",
        1
    )

    # MpEngine Policies
    check_policy(
        "Ensure 'Enable file hash computation feature' is set to 'Enabled'",
        r"SOFTWARE\Policies\Microsoft\Windows Defender\MpEngine",
        "FileHashComputation",
        1
    )

    # Network Inspection System
    check_policy(
        "Ensure 'Scan all downloaded files and attachments' is set to 'Enabled'",
        r"SOFTWARE\Policies\Microsoft\Windows Defender\RealTimeProtection",
        "ScanDownloadedFiles",
        1
    )
    check_policy(
        "Ensure 'Turn off real-time protection' is set to 'Disabled'",
        r"SOFTWARE\Policies\Microsoft\Windows Defender\RealTimeProtection",
        "DisableRealtimeMonitoring",
        0
    )
    check_policy(
        "Ensure 'Turn on behavior monitoring' is set to 'Enabled'",
        r"SOFTWARE\Policies\Microsoft\Windows Defender\RealTimeProtection",
        "EnableBehaviorMonitoring",
        1
    )
    check_policy(
        "Ensure 'Turn on script scanning' is set to 'Enabled'",
        r"SOFTWARE\Policies\Microsoft\Windows Defender\RealTimeProtection",
        "EnableScriptScanning",
        1
    )

    # Remediation Policies
    check_policy(
        "Ensure 'Configure Watson events' is set to 'Disabled'",
        r"SOFTWARE\Policies\Microsoft\Windows Defender\Reporting",
        "ConfigureWatsonEvents",
        0
    )

    # Scan Policies
    check_policy(
        "Ensure 'Scan packed executables' is set to 'Enabled'",
        r"SOFTWARE\Policies\Microsoft\Windows Defender\Scan",
        "ScanPackedExecutables",
        1
    )
    check_policy(
        "Ensure 'Scan removable drives' is set to 'Enabled'",
        r"SOFTWARE\Policies\Microsoft\Windows Defender\Scan",
        "ScanRemovableDrives",
        1
    )
    check_policy(
        "Ensure 'Turn on e-mail scanning' is set to 'Enabled'",
        r"SOFTWARE\Policies\Microsoft\Windows Defender\Scan",
        "EnableEmailScanning",
        1
    )

    # Security Intelligence Updates
    check_policy(
        "Ensure 'Configure detection for potentially unwanted applications' is set to 'Enabled: Block'",
        r"SOFTWARE\Policies\Microsoft\Windows Defender\PUA",
        "EnablePuaDetection",
        1
    )
    check_policy(
        "Ensure 'Turn off Microsoft Defender AntiVirus' is set to 'Disabled'",
        r"SOFTWARE\Policies\Microsoft\Windows Defender",
        "DisableAntiVirus",
        0
    )

    # Microsoft Defender Application Guard
    check_policy(
        "Ensure 'Allow auditing events in Microsoft Defender Application Guard' is set to 'Enabled'",
        r"SOFTWARE\Policies\Microsoft\Windows Defender\ApplicationGuard",
        "AllowAuditingEvents",
        1
    )
    check_policy(
        "Ensure 'Allow camera and microphone access in Microsoft Defender Application Guard' is set to 'Disabled'",
        r"SOFTWARE\Policies\Microsoft\Windows Defender\ApplicationGuard",
        "AllowCameraMicrophoneAccess",
        0
    )
    check_policy(
        "Ensure 'Allow data persistence for Microsoft Defender Application Guard' is set to 'Disabled'",
        r"SOFTWARE\Policies\Microsoft\Windows Defender\ApplicationGuard",
        "AllowDataPersistence",
        0
    )
    check_policy(
        "Ensure 'Allow files to download and save to the host operating system from Microsoft Defender Application Guard' is set to 'Disabled'",
        r"SOFTWARE\Policies\Microsoft\Windows Defender\ApplicationGuard",
        "AllowDownloadAndSaveToHost",
        0
    )
    check_policy(
        "Ensure 'Configure Microsoft Defender Application Guard clipboard settings: Clipboard behavior setting' is set to 'Enabled: Enable clipboard operation from an isolated session to the host'",
        r"SOFTWARE\Policies\Microsoft\Windows Defender\ApplicationGuard",
        "EnableClipboardOperationFromIsolatedSession",
        1
    )
    check_policy(
        "Ensure 'Turn on Microsoft Defender Application Guard in Managed Mode' is set to 'Enabled: 1'",
        r"SOFTWARE\Policies\Microsoft\Windows Defender\ApplicationGuard",
        "EnableApplicationGuardManagedMode",
        1
    )

    print("\nAudit complete.")

# Run the audit
audit_policies()
