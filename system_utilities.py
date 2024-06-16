import subprocess
import re

# check the current active link selecting the first link in "UP mode" status
def get_active_link():
    """Get link (network interfaces) for running computer"""
    command = f"ip link show"
    output = subprocess.check_output(command, shell=True).decode()
    ###print (output)
    
    ip_pattern = r' UP mode ' ###r'inet\s+(\d+\.\d+\.\d+\.\d+)'
    # split output in lines and search pattern
    for str in output.split("\n"):
        ###print (str)
        match = re.search(ip_pattern, str)
        if match != None :
            ###print (match)
            ssub = str.split(":")
            ###print ("|"+ssub[1].strip()+"|")
            return ssub[1].strip()
"""    
    if match:
        ip_address = match.group(1)
        return ip_address
    else:
        return None
"""

# mainly interact with the Console and 
# perform Regular Expression search
#
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


def inquire_network():
    # present user the current eth0 address
    ###interface_name = "eth0"
    interface_name = get_active_link()
    ##print (f"You are currently conncted by means of the {interface_name} network card")
    str_ip_address = get_interface_ip(interface_name)
    if str_ip_address:
        print(f"IP address of current network interface {interface_name} is {str_ip_address}")
    else:
        print(f"No IP address found for {interface_name} may it be not the first network interface?")
    #
    ip_address = [int(x) for x in str_ip_address.split(".")]
    return ip_address

def get_ping_answ(host):
    """Get ping answer for host computer"""
    command = f"ping -c 5 {host}"
    print (command)
    result = subprocess.getstatusoutput(command)
    ### print (type(result),"\n",result)
    if result[0] == 0 :
        output = result[1] #.decode()
    elif result[0] == 1 :
        output = result[1] #.decode()
    else:
        output = "not found"
    return output

def parse_ping_answ(output) :
    pattern = r'100% packet loss'
    match = re.search(pattern, output)
    
    if match:
        return "Down"
    else:
        return "Up"

# 100% packet loss

def main():
    ### hostmin, hostmax = user_input()
    ### print (IPString(hostmin),"<->",IPString(hostmax))
    ###print (parse_ping_answ(get_ping_answ("192.168.0.240")))
    ###print (parse_ping_answ(get_ping_answ("192.168.0.241")))
    print(get_active_link())
    pass


# print('INIZIO')
if __name__ == '__main__':
    main()
# print('FINE')
