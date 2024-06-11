
def IPStringToList(string):
    return [int(x) for x in string.split(".")]

def IPFromListToBigval(IPList):
    BigVal = 0
    for val in IPList :
        BigVal = (int(BigVal) << 8) | val
    return BigVal

def ConvertNetMask(Bits):
    NetMask = 1
    for i in range (1,Bits):
        NetMask = (NetMask << 1) + 1 
        #print ("NetMask cal = ", NetMask)
        #print ("{0:b}".format(NetMask))
    NetMask = NetMask << (32 - Bits)    
    return NetMask

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
    #
    #### NetMask = ((((((255 << 8) + 255) << 8) + 255) << 1) + 1) << 7
    print(IpotesiList)
    print("{0:b}".format(IPString))
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