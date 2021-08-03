from zeroconf import ServiceBrowser, Zeroconf
import socket
from time import sleep

def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]

class Mylistener():

    def __init__(self):
        self.info_dict = {}
        self.found = False
        self.ipaddress = None
        self.port = None
        self.zeroconf = Zeroconf()
   
    def convert_ip_address(self, byte_address):
        self.ipaddress = str(byte_address[0]) + '.' + str(byte_address[1]) + '.' + \
                         str(byte_address[2]) + '.' + str(byte_address[3])
        return self.ipaddress

    def remove_service(self, zeroconf, type, name):
        self.found      = False
        self.ipaddress  = None
        self.port       = None
        print("Service {} removed".format(name))

    def add_service(self, zeroconf, type, name):
        self.found     = True
        info = self.zeroconf.get_service_info(type, name)
        self.ipaddress=socket.inet_ntoa(info.addresses[0])
        print("ipaddr is {}".format(self.ipaddress))
        self.port = info.port
        print("Service: {} is at {}:{}\n".format(name, self.ipaddress, self.port))

        
    

if __name__ == "__main__":

    while True:
        try:
            dc_ip = get_ip_address()
            break
        except KeyboardInterrupt:
            pass
    print("hey I got the Ip address {}".format(dc_ip))

    
    
    call = Mylistener()
    
    browser = ServiceBrowser(call.zeroconf,"_pst-mc._tcp.local.",listener=call)
    
    sleep(10)
  
    




