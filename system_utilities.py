import subprocess
import re

# mainly interact with the Console and 
# perform Regular Expression search

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
    print (parse_ping_answ(get_ping_answ("192.168.0.240")))
    print (parse_ping_answ(get_ping_answ("192.168.0.241")))
    pass


# print('INIZIO')
if __name__ == '__main__':
    main()
# print('FINE')
