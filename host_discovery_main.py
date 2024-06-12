from user_input import user_input, decode, ip_input
from IPUtils import IPStringToList,IPFromListToBigval,ConvertNetMask,IPBigvalToList,IPString,get_min_max_IP_Range
from system_utilities import get_ping_answ, parse_ping_answ

def maintest():
    ip = [192,168,0,240]
    ip = ip_input()
    # IPStringToList to be used from string
    bt = int(input("Enter IP Range (Netmask) as an Integer ? "))
    Hostmin, Hostmax = get_min_max_IP_Range(ip,bt)
    print ("Hostmin   =>", Hostmin,"{0:b}".format(Hostmin) , IPBigvalToList(Hostmin))
    print ("Hostmax   =>", Hostmax,  "{0:b}".format(Hostmax) , IPBigvalToList(Hostmax))

def get_hosts_answers(hostmin,hostmax):
    num_hm = IPFromListToBigval((hostmin))
    num_hx = IPFromListToBigval((hostmax))
    for host in range(num_hm,num_hx+1) :
        answer = (get_ping_answ(IPString(IPBigvalToList(host))))
        print (parse_ping_answ(answer))


def main():
    hostmin, hostmax = user_input()
    ### print (hostmin, hostmax)
    # ready to ping for hosts status
    get_hosts_answers(hostmin,hostmax)

# print('INIZIO')
if __name__ == '__main__':
    main()
# print('FINE')