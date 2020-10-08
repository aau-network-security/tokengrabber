from os import system
from optparse import OptionParser
queries_liste = {}

def process(pkt):
    global quiet
    global databaseConn
    ip46 = IPv6 if IPv6 in pkt else IP
    if pkt.haslayer(DNSQR) and UDP in pkt and pkt[UDP].sport == 53 and ip46 in pkt:
        query = pkt[DNS].qd.qname.decode("utf-8") if pkt[DNS].qd != None else "?"

        if not pkt[ip46].dst in queries_liste:
            queries_liste[pkt[ip46].dst] = {}

        if not pkt[ip46].src in queries_liste[pkt[ip46].dst]:
            queries_liste[pkt[ip46].dst][pkt[ip46].src] = {}

        if not query in queries_liste[pkt[ip46].dst][pkt[ip46].src]:
            queries_liste[pkt[ip46].dst][pkt[ip46].src][query] = 1
        else:
            queries_liste[pkt[ip46].dst][pkt[ip46].src][query] += 1


        #system('cls')
        #print("{:15s} | {:15s} | {:15s} | {}".format("IP source", "DNS server", "Count DNS request", "Query"))
        for ip in queries_liste:
            #print("{:15s}".format(ip))  # IP source
            for query_server in queries_liste[ip]:
                #print(" " * 18 + "{:15s}".format(query_server))  # IP of DNS server
                for query in queries_liste[ip][query_server]:
                    #print(" " * 36 + "{:19s} {}".format(str(queries_liste[ip][query_server][query]), query))  # Count DNS request | DNS
                    if "canarytokens.com" in query:
                        print("Canarytoken detected!!")



if __name__ == "__main__":
    parser = OptionParser(usage="%prog: [options]")
    parser.add_option("-i", "--iface", dest="iface", default='', help="Interface. Ex: enp0s7")
    (options, args) = parser.parse_args()
    iface = options.iface


    try:
        from scapy.all import sniff
        from scapy.all import ARP
        from scapy.all import DNSQR
        from scapy.all import UDP
        from scapy.all import IP
        from scapy.all import IPv6
        from scapy.all import DNS


        #system('cls')
        #print("{:15s} | {:15s} | {:15s} | {}".format("IP source", "DNS server", "Count DNS request", "Query"))

        if iface != "":
            sniff(filter='udp port 53', store=0, prn=process, iface=iface)
        else:
            sniff(filter='udp port 53', store=0, prn=process)
    except ImportError:
        from sys import exit
        exit("Import Scapy!!")