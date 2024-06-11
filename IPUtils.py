
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