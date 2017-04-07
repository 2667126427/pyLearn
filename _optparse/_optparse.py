import optparse
from socket import *
from threading import Thread


def connScan(tgtHost, tgtPort):
    try:
        connSkt = socket(AF_INET, SOCK_STREAM)
        connSkt.connect((tgtHost, tgtPort))
        print('[+]%d/tcp open'% tgtPort)
        connSkt.close()
    except:
        print('[-]%d/tcp closed'% tgtPort)


def portScan(tgtHost, tgtPorts):
    try:
        tgtIP = gethostbyname(tgtHost)
    except:
        print('[-] Cannot resolve "%s": Unknown host'%tgtHost)
        return
    try:
        tgtName = gethostbyaddr(tgtIP)
        print('\n[+] Scan Results for: ' + tgtName[0])
    except:
        print('\n[+] Scan Results for: ' + tgtIP)
    setdefaulttimeout(1)
    for tgtPort in tgtPorts:
        print('Scanning port ' + tgtPort)
        connScan(tgtHost, int(tgtPort))


def main():
    parser = optparse.OptionParser('usage %prog -H' + '<target host> -p <target port>')
    parser.add_option('-H', dests='tgtHost', type='string', help='specify target host')
    parser.add_option('-H', dests='tgtHost', type='int', help='specify target host')
    (options, args) = parser.parse_args()
    tgtHost = options.tgtHost
    tgtPorts = options.tgtPort
    if (tgtHost == None) | (tgtPorts == None):
        print(parser.usage)
        exit(0)
    portScan(tgtHost, tgtPorts)

if __name__ == '__main__':
    main()
    Thread