# from user_input import user_input
from user_input import user_input, bit, decode,ip_input
from IPUtils import IPStringToList,IPFromListToBigval,ConvertNetMask,IPBigvalToList

def main1():
    # get IP range
    answ = user_input()
    print(answ)

def main2():
    ip = [192,168,0,240]
    nip = ip.copy()
    bt = int(input("Range ? "))
    print(ip, nip, bt)
    bit(ip,nip,bt)
    print(ip, nip, bt)

def main():
    ip = [192,168,0,240]
    ip = ip_input()
    # IPStringToList to be used from string
    # nip = ip.copy()
    bt = int(input("Range ? "))
    bigval = IPFromListToBigval(ip)
    NetMask = ConvertNetMask(bt)
        #
    print ("IPAsStr  ==>", bigval, "{0:b}".format(bigval))
    print ("NetMask  ==>",NetMask, "{0:b}".format(NetMask),"\n#")
    #
    Network = bigval & NetMask
    Hostmin = Network + 1
    print ("Network   =>", Network,"{0:b}".format(Network))
    print ("Hostmin   =>", Hostmin,"{0:b}".format(Hostmin) , IPBigvalToList(Hostmin))
    #
    Hosts = (1 << (32-bt)) - 1
    print ("Hosts  ====>", Hosts - 1,"{0:b}".format(Hosts - 1))
    #
    Broadcast = Network | Hosts
    Hostmax = Broadcast-1
    print ("Hostmax   =>", Hostmax,  "{0:b}".format(Hostmax) , IPBigvalToList(Hostmax))
    print ("Broadcast =>", Broadcast,"{0:b}".format(Broadcast) )


# print('INIZIO')
if __name__ == '__main__':
    main()
# print('FINE')