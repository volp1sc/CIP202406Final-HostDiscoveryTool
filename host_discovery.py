from user_input import user_input
from IPUtils import IPFromListToBigval,IPBigvalToList,IPString
from system_utilities import get_ping_answ, parse_ping_answ


def get_hosts_answers(hostmin,hostmax):
    num_hm = IPFromListToBigval((hostmin))
    num_hx = IPFromListToBigval((hostmax))
    up_devices = 0
    dw_devices = 0
    for host in range(num_hm,num_hx+1) :
        answer = (get_ping_answ(IPString(IPBigvalToList(host))))
        response_str = parse_ping_answ(answer)
        print (response_str)
        if response_str == "Up" :
            up_devices += 1
        elif response_str == "Down" :
            dw_devices += 1
    print (f"In proposed search range there were {up_devices} UP device(s)")
    print (f"and {dw_devices} DOWN device(s)")
    print (f"Search completed")


def main():
    #
    # request user information
    # return range of hosts to scan
    #
    hostmin, hostmax = user_input()
    #
    ###DEBUG#print (hostmin, hostmax)
    #
    # ready to ping for hosts status
    #
    get_hosts_answers(hostmin,hostmax)


if __name__ == '__main__':
    main()
