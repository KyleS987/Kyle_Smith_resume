import sys	#imports sys module for command-line argument handling
import nmap  #imports Nmap module; requires python-nmap library

#scanning function
def nmap_scan(target, start_port, end_port):
    nm = nmap.PortScanner()#initializes Nmap object
    port_range = '{}-{}'.format(start_port, end_port)
    try:
        nm.scan(hosts=target, arguments='-sS -p {}'.format(port_range))
        for host in nm.all_hosts():
            print('Host : %s (%s)' % (host, nm[host].hostname()))
            print('State : %s' % nm[host].state())
            for proto in nm[host].all_protocols():
                print('Protocol : %s' % proto)
                ports = nm[host][proto].keys()
                for port in ports:
                    print('Port : %s\tState : %s' % (port, nm[host][proto][port]['state']))
    except Exception as e:#handles exceptions during the scan
        print(f"An error occurred: {e}")#prints the error message

#main block to handle command-line arguements
if __name__ == "__main__":#checks if the script was run directly
    if len(sys.argv) != 4:#validates that exactly 3 arguements were passed
        print("Usage: python script.py <target_ip> <start_port> <end_port>")
        sys.exit(1)
    
    try:
        target = sys.argv[1]
        start_port = int(sys.argv[2])
        end_port = int(sys.argv[3])
        nmap_scan(target, start_port, end_port)
    except ValueError:#handles invalid input for port numbers
        print("Error: Start and end ports must be integers.")