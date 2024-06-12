# manage to bit e net conversione

def IPString(IPList):
    ## print ("In IPString : current value of IPList", IPList)
    return (str(IPList[0])+"."+str(IPList[1])+"."+str(IPList[2])+"."+str(IPList[3]))

def IPStringToList(string):
    return [int(x) for x in string.split(".")]

def IPFromListToBigval(IPList):
    BigVal = 0
    for val in IPList :
        BigVal = (int(BigVal) << 8) | val
    return BigVal

def IPBigvalToList(Bigval):
    IPList = [0,0,0,0]
    IPList[3] = Bigval       & 0x000000FF
    IPList[2] = Bigval >> 8  & 0x000000FF # 0x0000FF00
    IPList[1] = Bigval >> 16 & 0x000000FF # 0x00FF0000
    IPList[0] = Bigval >> 24 & 0x000000FF # 0xFF000000
    # print (IPList)
    return IPList

def ConvertNetMask(Bits):
    NetMask = 1
    for i in range (1,Bits):
        NetMask = (NetMask << 1) + 1 
        #print ("NetMask cal = ", NetMask)
        #print ("{0:b}".format(NetMask))
    NetMask = NetMask << (32 - Bits)    
    return NetMask

def get_min_max_IP_Range(ip,bt):
    # Convert IP list to Long Integer
    bigval = IPFromListToBigval(ip)
    # Convert /xx bitmask to Long Integer
    NetMask = ConvertNetMask(bt)
    #
    ## print ("IPAsStr  ==>", bigval, "{0:b}".format(bigval))
    ## print ("NetMask  ==>",NetMask, "{0:b}".format(NetMask),"\n#")
    #
    Network = bigval & NetMask
    ###Hostmin = Network + 1
    Hostmin = Network
    ## print ("Network   =>", Network,"{0:b}".format(Network))
    ## print ("Hostmin   =>", Hostmin,"{0:b}".format(Hostmin) , IPBigvalToList(Hostmin))
    #
    Hosts = (1 << (32-bt)) - 1
    ## print ("Hosts  ====>", Hosts - 1,"{0:b}".format(Hosts - 1))
    #
    Broadcast = Network | Hosts
    ###Hostmax = Broadcast-1
    Hostmax = Broadcast
    ## print ("Hostmax   =>", Hostmax,  "{0:b}".format(Hostmax) , IPBigvalToList(Hostmax))
    ## print ("Broadcast =>", Broadcast,"{0:b}".format(Broadcast) )
    return Hostmin, Hostmax


def main():
    # era 192.168.0.240 uso solo 240
    Ipotesi = "192.168.0.130"
    IpotesiList = IPStringToList(Ipotesi)
    #####IpotesiList = [int(x) for x in Ipotesi.split(".")]  #[192, 168, 0, 240]
    #
    #IPString = 0 
    #for val in IpotesiList:
    #    IPString = (int(IPString) << (8)) | (val)
    #    #print("{0:b}".format(IPString))
    IPString = IPFromListToBigval(IpotesiList) 
    Test = IPBigvalToList(IPString)
    #
    #### NetMask = ((((((255 << 8) + 255) << 8) + 255) << 1) + 1) << 7
    print("Ipotesi",IpotesiList)
    print("{0:b}".format(IPString))
    print("Test   ",Test)
    #
    #print ("NetMask cal = ", NetMask)
    #print ("{0:b}".format(NetMask))
    #
    Bits = 28
    print("Netmask /",Bits)
    #
    #NetMask = 1
    #for i in range (1,Bits):
    #    NetMask = (NetMask << 1) + 1 
    #    #print ("NetMask cal = ", NetMask)
    #    #print ("{0:b}".format(NetMask))
    #NetMask = NetMask << (32 - Bits)
    #
    NetMask = ConvertNetMask(Bits)
    #
    print ("NetMask = ",NetMask)
    print ("{0:b}".format(NetMask))
    print ("IPString = ", IPString)
    print ("{0:b}".format(IPString))
    #
    Hostmin = IPString & NetMask
    Lower = Hostmin + 1
    print ("{0:b}".format(Lower))
    print(Hostmin,"<= Hostmin Lower =>", Lower)
    #
    Hosts = (1 << (32-Bits)) - 1
    print("Hosts = ", Hosts)
    Hostmax = Hostmin | Hosts
    Upper = Hostmax-1
    print ("{0:b}".format(Upper))
    print(Upper,"<= Upper Hostmax =>", Hostmax )


if __name__ == "__main__":
    main()