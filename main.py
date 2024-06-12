from user_input import user_input
from host_discovery import get_hosts_answers

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
