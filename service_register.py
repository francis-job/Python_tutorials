import socket
from time import sleep
from zeroconf import ServiceInfo, Zeroconf

def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]

#class registration():
#    
#    def __init__(self,dc_ip):
#        self.service_info=ServiceInfo("_jarvis._tcp.local.",
#                            "francis_job_testing_service._jarvis._tcp.local.",
#                            addresses = [socket.inet_aton(dc_ip)],
#                            port = 12345,
#                            properties = {'hai jarvis'},
#                            )
#        self.zero_conf.unregister_service(self.service_info)
#        sleep(0.05)
#        self.zero_conf.register_service(self.service_info)
#        printf("service started \n")
           
        

if __name__ == "__main__":

    while True:
        try:
            dc_ip = get_ip_address()
            break
        except KeyboardInterrupt:
            pass
    print("hey I got the Ip address {}".format(dc_ip))
    
    zero_conf = Zeroconf()
    
    service_info=ServiceInfo("_http._tcp.local.",
                           "francis_job_testing_service._http._tcp.local.",
                            addresses=[socket.inet_aton(dc_ip)],
                            port=1234
                           )
#    info = ServiceInfo(
#                     "_http._tcp.local.",
#                     "Francis's Test Web Site._http._tcp.local.",
#                      address=[socket.inet_aton(dc_ip)],
#                      port=80,
#                      properties = {"Hello_world"} )
    
    zero_conf.register_service(service_info)
    print("Registered successfully\n")    
    try:
        while True:
            sleep(0.1)
    except KeyboardInterrupt:
        pass
    finally:
        print("Unregistering...")
        zeroconf.unregister_service(info)
        zeroconf.close()
        
    



    
