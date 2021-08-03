import socket
from time import sleep
from zeroconf import ServiceInfo, Zeroconf

def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]


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
    
    zero_conf.register_service(service_info)
    print("Registered successfully\n")    
    try:
        while True:
            sleep(0.1)
    except KeyboardInterrupt:
        pass
    finally:
        print("Unregistering...")
        zeroconf.unregister_service(service_info)
        zeroconf.close()
        
    



    
