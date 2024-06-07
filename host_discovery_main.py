# from user_input import user_input
from user_input import user_input, bit, decode

def main1():
    # get IP range
    answ = user_input()
    print(answ)

def main():
    ip = [192,168,0,240]
    nip = ip.copy()
    bt = int(input("Range ? "))
    print(ip, nip, bt)
    bit(ip,nip,bt)
    print(ip, nip, bt)

# print('INIZIO')
if __name__ == '__main__':
    main()
# print('FINE')