import threading
import os
import signal
import socket
from zeroconf import ServiceInfo, ServiceBrowser, Zeroconf
from time import sleep as delay

class Mylistener(threading.Thread):

    def __init__(self, zeroconf, dc_ip, service_info):
        threading.Thread.__init__(self)
        self.ipaddress = None
        self.port = None
        self.zeroconf = zeroconf
        self.dc_ip = dc_ip
        self.service_info = service_info
        self.zeroconf.unregister_service(self.service_info)
        delay(0.5)
        self.zeroconf.register_service(self.service_info)
        print("Registered successfully\n")

        browser = ServiceBrowser(self.zeroconf,"_http._tcp.local.",self)

    def remove_service(self, zeroconf, type, name):
        self.ipaddress  = None
        self.port       = None
        print("Service {} removed".format(name))

    def update_service(self,zeroconf, type, name):
        pass

    def add_service(self, zeroconf, type, name):
        self.found     = True
        info = self.zeroconf.get_service_info(type, name)
        self.ipaddress=socket.inet_ntoa(info.addresses[0])
        print("ipaddr is {}".format(self.ipaddress))
        self.port = info.port
        print("Service: {} is at {}:{}\n".format(name, self.ipaddress, self.port))

def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]

def signal_handler(signalNumber,frame):
    pass

if __name__ == "__main__":

    signal.signal(signal.SIGUSR1, signal_handler)

    while True:
        try:
            dc_ip = get_ip_address()
            break
        except KeyboardInterrupt:
            pass
    print("hey I got My Ip address {}".format(dc_ip))
    service_info=ServiceInfo("_http._tcp.local.",
                             "francis_job_testing_service._http._tcp.local.",
                              addresses=[socket.inet_aton(dc_ip)],
                              port=1234
                               )
    
    try:
        while True:
            print("Starting Services\n")
            zeroconf = Zeroconf()
            service_handler = Mylistener(zeroconf,dc_ip,service_info)
            service_handler.start()
            signal.pause()   #main thread will pause here
            zeroconf.unregister_service(service_info)
            service_handler.join()
            zeroconf.close()
    except KeyboardInterrupt:
        pass
    finally:
        print("Unregistering...")
        zeroconf.unregister_service(service_info)
        zeroconf.close()
        service_handler.join()


    

