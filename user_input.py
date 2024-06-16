import re
from IPUtils import get_min_max_IP_Range,IPBigvalToList,IPString
from system_utilities import inquire_network

def int_input(prompt):
    str_value = input(prompt)
    while not str_value.isnumeric():
        prompt("Not a numeric value")
        str_value = input(prompt)
    return int(str_value)

# return user input as IP range inside a list
# acceptable are two IP in dotted notation
# or an IP and a gateway mask

def decode(nm_val):
    # from integer to bits
    ### print ("@ decode start" , nm_val)
    int_val = 0
    if nm_val >= 0 :
        if nm_val in [0, 128, 192, 224, 240, 248, 252, 254, 255] :
            ### print("@ decode nm_val acceptable", nm_val, float(nm_val), float(2))
            # int_val = int(math.log(float(nm_val),float(2)))
            if nm_val == 0 :
                int_val = 0
            elif nm_val == 128 :
                int_val = 1
            elif nm_val == 192 :
                int_val = 2
            elif nm_val == 224 :
                int_val = 3
            elif nm_val == 240 :
                int_val = 4
            elif nm_val == 248 :
                int_val = 5
            elif nm_val == 252 :
                int_val = 6
            elif nm_val == 255 :
                int_val = 8
        else :
            print ("@ decode nm_val unacceptable value forced to 0")
            print ("use only one of the following 128, 192, 224, 240, 248, 252, 254, 255")
    else :
        int_val = 0
    #if nm_val <= 0 :
    #    return 0
    ### print(int_val, 8 - int_val)
    return int_val

def transform_bit(nm):
    # from xxx.yyy.www.zzz digit to biwise integer
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
        ###print("In transform_bit in", nm[3]," out",int)
        return 24 + int
    else:
        return 0 #nm
    # return bitwise netmask

"""
    ip_pattern = r'inet\s+(\d+\.\d+\.\d+\.\d+)'
    match = re.search(ip_pattern, output)
    
    if match:
        ip_address = match.group(1)
        return ip_address
    else:
        return None
"""

def not_valid_ip(stringIP):
    pattern = r'\d+\.\d+\.\d+\.\d+'
    match = re.search(pattern, stringIP)
    ###print (pattern)
    ###print (stringIP)
    match = re.search(pattern, stringIP)
    if match == None :
        return True
    #
    pattern = r'\d+\.\d+\.\d+\.\d+/\d+'
    ###print (pattern)
    ###print (stringIP)
    match = re.search(pattern, stringIP)
    ###print (match)
    if match == None:
        return False
    else:
        print ("wrong digits", match)
        print ("use only xxx.yyy.www.zzz no other characters")
        return True

def ip_input():
    string_IPvalue = input("Input full IP value as xxx.yyy.www.zzz ")
    while not_valid_ip(string_IPvalue) :
        string_IPvalue = input("Input full IP value as xxx.yyy.www.zzz ")
    return [int(x) for x in string_IPvalue.split(".")]

def nm_input(starting,ending,flag):
    # if flag is True entering a dotted netmask
    # if flag is False entering a bitwise netmask
    # get user value and process it
    if flag :
        print("Enter a string in the xxx.yyy.www.zzz format")
        netmask = ip_input()
        bit_netmask = transform_bit(netmask)
    else:
        bit_netmask = int_input("Enter an integer value from 24 to 32 : ") 
    ### print("ready to calculate final with",flag," and transformed netmask",bit_netmask)
    # calculate ending using starting and netmask
    hostmin, hostmax = calculate_final(starting,ending, int(bit_netmask))
    return hostmin, hostmax

def calculate_final(ip,nip,nm):
    ###print (IPString(ip), IPString(nip), int(nm))
    # apply netmask on starting to calculate final
    if nm < 24 :
        print("Too big scan, forced to /24")
        nm = 24
    else:
        # bit(ip,nip,nm-24)
        ##print("Calculate final ",ip[3], nip[3])
        ###print ("Calculate final ",IPString(ip), IPString(nip), int(nm))
        pass
    ip, nip = get_min_max_IP_Range(ip,nm)
    ###print((ip)," ^^^",(nip))
    ip = IPBigvalToList(ip)
    nip = IPBigvalToList(nip)
    print("\nThe calculated hosts are :\nfrom ("+IPString(ip)+") to ("+IPString(nip)+")\n")
    return ip, nip

def validate_proposed_IP(starting,ip_address):
    ###print ("@ validate", starting, ip_address)
    if (starting[0] == ip_address[0]) & (starting[1] == ip_address[1]) & (starting[2] == ip_address[2]) :
        ## print("Valid search ip on the same network")
        return starting
    else:
        print("\nYour Network IP address "+ IPString(ip_address)+ " and your input "+ IPString(starting)+ " are not on the same LAN")
        print("\nPlease enter a valid IP value on the same /24 subnet ?\n")
        repeat = ip_input()
        while not ((repeat[0] == ip_address[0]) & (repeat[1] == ip_address[1]) & (repeat[2] == ip_address[2]) ): 
            print("\nPlease enter a valid IP value on the same /24 subnet ?\n")
            repeat = ip_input()
        return repeat


def user_input():
    print ("Welcome to the Host Discovery Tool\n")
    ip_address = inquire_network()
    ##print (f"\nYour current IP address is {ip_address}")
    print("\nSelect a starting IP range to the Network Discovery\n")
    # print("Use dotted IP notation aaa.bbb.ccc.ddd")
    # use tailored input to discriminate good values; return a list of 4 value 0-255
    starting = ip_input()
    starting = validate_proposed_IP(starting,ip_address)
    #
    #
    print("\nSpecify the range in one of the following notation")
    print("1. Dotted  End-IP\n2. Dotted  Netmask\n3. Bitwise Netmask")
    #
    #
    correct = False
    while not correct :
        choice = int_input("Select a value among [1,2,3] -> ")
        if choice == 1 :
            print("\nSelected Dotted IP")
            ending = ip_input()
            hostmin = starting.copy()
            hostmax = ending.copy()
            correct = True
        elif choice == 2 :
            print("\nSelected Dotted Netmask")
            ending = starting.copy()
            hostmin, hostmax = nm_input(starting,ending,True)
            correct = True
        elif choice == 3 :
            print("\nSelected Bitwise Netmask")
            ending = starting.copy()
            hostmin, hostmax = nm_input(starting,ending,False)
            correct = True
        else :
            # choice = input("Unknown choice select again : ")
            print ("Unknown choice select again")
            correct = False
    #
    ### print("Current values are :\nstarting |"+ str(starting) + "| ending |" + str(ending) + "| netmask kind |" + str(choice) + "|")
    # choice = ['192.168.0.240']  # '192.168.0.240/32'
    ### print ("@ end user_input", hostmin, hostmax)
    return hostmin, hostmax


def main():
    hostmin, hostmax = user_input()
    print (IPString(hostmin),"<->",IPString(hostmax))


# print('INIZIO')
if __name__ == '__main__':
    main()
# print('FINE')
