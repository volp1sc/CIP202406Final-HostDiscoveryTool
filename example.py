import subprocess
import re

def get_interface_ip(interface):
    """Get IP address for a given network interface"""
    command = f"ip addr show {interface}"
    output = subprocess.check_output(command, shell=True).decode()

    ip_pattern = r'inet\s+(\d+\.\d+\.\d+\.\d+)'
    match = re.search(ip_pattern, output)
    
    if match:
        ip_address = match.group(1)
        return ip_address
    else:
        return None

interface_name = "eth0"
ip_address = get_interface_ip(interface_name)

if ip_address:
    print(f"IP address of {interface_name}: {ip_address}")
else:
    print(f"No IP address found for {interface_name}")
