import subprocess

# Function to check if a service is disabled
def check_service(service_name, display_name):
    try:
        # Query the service status using sc query
        result = subprocess.run(["sc", "query", service_name], capture_output=True, text=True)

        # Parse the result
        if "STATE" in result.stdout:
            if "STOPPED" in result.stdout and "DISABLED" in result.stdout:
                compliance = "PASS"
            else:
                compliance = "FAIL (Service is not disabled)"
        else:
            compliance = "PASS (Not Installed)"
    except Exception as e:
        compliance = f"FAIL (Error: {e})"

    # Output the result
    print(f"{display_name} - {compliance}")

# Main function to audit services
def audit_services():
    print("Starting System Services Audit...\n")

    # List of services to audit (includes previous list plus new entries from 5.24 to 5.44)
    services = [
        # Previous services from 5.1 to 5.23 (omitted for brevity in this code sample),
        ("RemoteRegistry", "Remote Registry"),
        ("RemoteAccess", "Routing and Remote Access"),
        ("LanmanServer", "Server"),
        ("simptcp", "Simple TCP/IP Services"),
        ("SNMP", "SNMP Service"),
        ("sacsvr", "Special Administration Console Helper"),
        ("SSDPSRV", "SSDP Discovery"),
        ("upnphost", "UPnP Device Host"),
        ("WMSvc", "Web Management Service"),
        ("WerSvc", "Windows Error Reporting Service"),
        ("Wecsvc", "Windows Event Collector"),
        ("WMPNetworkSvc", "Windows Media Player Network Sharing Service"),
        ("icssvc", "Windows Mobile Hotspot Service"),
        ("WpnService", "Windows Push Notifications System Service"),
        ("PushToInstall", "Windows PushToInstall Service"),
        ("WinRM", "Windows Remote Management (WS-Management)"),
        ("W3SVC", "World Wide Web Publishing Service"),
        ("XboxGipSvc", "Xbox Accessory Management Service"),
        ("XblAuthManager", "Xbox Live Auth Manager"),
        ("XblGameSave", "Xbox Live Game Save"),
        ("XboxNetApiSvc", "Xbox Live Networking Service")
    ]

    # Check each service
    for service_name, display_name in services:
        check_service(service_name, display_name)

    print("\nAudit complete.")

# Run the audit
audit_services()
