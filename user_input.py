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

def int_input(prompt):
    str_value = input(prompt)
    while not str_value.isnumeric():
        prompt("Not a numeric value")
        str_value = input(prompt)
    return int(str_value)

# return user input as IP range inside a list
# acceptable are two IP in dotted notation
# or an IP and a gateway mask

def ip_input():
    for i in range (4):
        valid = False
        while not valid:
            int_value = int_input("Input integer value in the 0-255 range for "+str(i+1)+"^ subnet : ")
            if int_value >= 0 and int_value <= 255:
                    valid = True
            else:
                print("Numeric value not in 0-255 range, repeat please")
        if i == 0:
            aaa = int_value
        elif i == 1:
            bbb = int_value
        elif i == 2:
            ccc = int_value
        else:
            ddd = int_value 
    return [aaa, bbb, ccc, ddd]

def nm_input(starting,flag):
    # if flag is True entering a dotted netmask
    # if flag is False entering a bitwise netmask
    # get user value and process it
    if flag :
        netmask = ip_input()
    else:
        bit_netmask = int_input("Enter an integer value from 0 to 32 : ") 
        netmask = transform_bit(bit_netmask)
    # calculate ending using starting and netmask
    ending = calculate_final(starting,netmask)
    return ending

def transform_bit(bit):
    # from digit to integer
    return [255,255,255,255] #nm

def calculate_final(ip,nm):
    # apply netmask on starting to calculate final
    return ip # end

def user_input():
    # present user the current eth0 address
    interface_name = "eth0"
    ip_address = get_interface_ip(interface_name)
    if ip_address:
        print(f"Current IP address of {interface_name}: {ip_address}")
    else:
        print(f"No IP address found for {interface_name} may it be a wireless link ?")
    #
    print("Select a starting IP range to the Network Discovery")
    # print("Use dotted IP notation aaa.bbb.ccc.ddd")
    # use tailored input to discriminate good values; return a list of 4 value 0-255
    starting = ip_input()
    print(starting)
    #
    print("Specify the end of the range in one of the following notation")
    print("1. Dotted IP\n2. Dotted Netmask\n3. Bitwise Netmask")
    #
    # possible custom integer input like int_input("prompt",range)
    #
    correct = False
    while not correct :
        choice = int_input("Select a value among [1,2,3] -> ")
        if choice == 1 :
            print("Selected Dotted IP")
            ending = ip_input()
            correct = True
        elif choice == 2 :
            print("Selected Dotted Netmask")
            ending = nm_input(starting,True)
            correct = True
        elif choice == 3 :
            print("Selected Bitwise Netmask")
            ending = nm_input(starting,False)
            correct = True
        else :
            choice = input("Unknown choice select again : ")
    #
    print("Current values are :\nstarting |"+ str(starting) + "| ending |" + str(ending) + "| netmask |" + str(choice) + "|")
    # choice = ['192.168.0.240']  # '192.168.0.240/32'
    return [starting,ending]
