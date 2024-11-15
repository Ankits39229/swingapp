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

    # List of services to audit
    services = [
        ("BTAGService", "Bluetooth Audio Gateway Service"),
        ("bthserv", "Bluetooth Support Service"),
        ("Browser", "Computer Browser"),
        ("MapsBroker", "Downloaded Maps Manager"),
        ("lfsvc", "Geolocation Service"),
        ("IISADMIN", "IIS Admin Service"),
        ("irmon", "Infrared monitor service"),
        ("lltdsvc", "Link-Layer Topology Discovery Mapper"),
        ("LxssManager", "LxssManager"),
        ("FTPSVC", "Microsoft FTP Service"),
        ("MSiSCSI", "Microsoft iSCSI Initiator Service"),
        ("sshd", "OpenSSH SSH Server"),
        ("PNRPsvc", "Peer Name Resolution Protocol"),
        ("p2psvc", "Peer Networking Grouping"),
        ("p2pimsvc", "Peer Networking Identity Manager"),
        ("PNRPAutoReg", "PNRP Machine Name Publication Service"),
        ("Spooler", "Print Spooler"),
        ("wercplsupport", "Problem Reports and Solutions Control Panel Support"),
        ("RasAuto", "Remote Access Auto Connection Manager"),
        ("SessionEnv", "Remote Desktop Configuration"),
        ("TermService", "Remote Desktop Services"),
        ("UmRdpService", "Remote Desktop Services UserMode Port Redirector"),
        ("RpcLocator", "Remote Procedure Call (RPC) Locator")
    ]

    # Check each service
    for service_name, display_name in services:
        check_service(service_name, display_name)

    print("\nAudit complete.")

# Run the audit
audit_services()
