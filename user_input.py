import subprocess
import re
import math
import IPUtils 

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

def ip_input_base():
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

def ip_input():
    string_IPvalue = input("Input full IP value as xxx.yyy.www.zzz ")
    return [int(x) for x in string_IPvalue.split(".")]

def decode(nm_val):
    if nm_val > 0 :
        print("decode nm_val", nm_val, float(nm_val), float(2))
        int_val = int(math.log(float(nm_val),float(2)))
    else :
        int_val = 0
    #if nm_val <= 0 :
    #    return 0
    print(int_val, 8 - int_val)
    return 8-int_val

def transform_bit(nm):
    # from digit to integer
    if nm[0] < 255 :
        int = decode(nm[0])
        return int
    elif nm[0] == 255 and nm[1] < 255:
        int = decode(nm[1])
        return 8 + int
    elif nm[0] == 255 and nm[1] == 255 and nm[2] < 255:
        int = decode(nm[2])
        return 16 + int
    elif nm[0] == 255 and nm[1] == 255 and nm[2] == 255 and nm[3] <= 255:
        int = decode(nm[3])
        print("In transform_bit in", nm[3]," out",int)
        return 24 + int
    else:
        return 0 #nm
    # return bitwise netmask

def nm_input(starting,ending,flag):
    # if flag is True entering a dotted netmask
    # if flag is False entering a bitwise netmask
    # get user value and process it
    if flag :
        netmask = ip_input()
        bit_netmask = transform_bit(netmask)
    else:
        bit_netmask = int_input("Enter an integer value from 0 to 32 : ") 
    print("ready to calculate final after",flag," we computed",bit_netmask)
    # calculate ending using starting and netmask
    calculate_final(starting,ending, int(bit_netmask))
    return starting, ending

def bit(ip,nip,num):
    # print ("bit " + str(num))
    powr = int(math.log((ip[3]),2))
    lor = int(ip[3] - (math.pow(2 , powr)))
    print ("IP, lor 2 powr ", ip[3], lor, 2, powr)
    if num == 0 :
        ip[3] = 0
        nip[3] = 255
    elif num == 1 :
        if ip[3] >= 128:
            ip[3] = 128
            nip[3] = 255
        else:
            ip[3] = 0
            nip[3] = 127
    elif num == 2 :
        if ip[3] >= 192:
            ip[3] = 192
            nip[3] = 255
        elif ip[3] >= 128 and ip[3] < 192:
            ip[3] = 128
            nip[3] = 191
        elif ip[3] >= 64 and ip[3] < 128:
            ip[3] = 64
            nip[3] = 127
        else:
            ip[3] = 0
            nip[3] = 63
    elif num == 3 :
        ret_num = 224    
    elif num == 4 :
        ret_num = 240    
    elif num == 4 :
        ret_num = 248
    elif num == 5 :
        ret_num = 252    
    elif num == 6 :
        ret_num = 254    
    elif num == 7 :
        ret_num = 255 
    return 

def calculate_final(ip,nip,nm):
    print (ip, nip, nm)
    # apply netmask on starting to calculate final
    if nm < 24 :
        print("Too big scan, reduced to /24")
    else:
        # bit(ip,nip,nm-24)
        # print("Calculate final ",ip[3], nip[3])
        print ("Calculate final ",ip, nip)
    return 

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
    valid = input("Are eth0 ", ip_address, " and your input", starting, " on the same LAN ? [N to restart] ")
    if valid == "N" : 
        starting = ip_input()
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
            ending = starting.copy()
            nm_input(starting,ending,True)
            correct = True
        elif choice == 3 :
            print("Selected Bitwise Netmask")
            ending = starting.copy()
            nm_input(starting,ending,False)
            correct = True
        else :
            choice = input("Unknown choice select again : ")
    #
    print("Current values are :\nstarting |"+ str(starting) + "| ending |" + str(ending) + "| netmask |" + str(choice) + "|")
    # choice = ['192.168.0.240']  # '192.168.0.240/32'
    return [starting,ending]
