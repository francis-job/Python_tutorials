import zmq
import threading
import signal
from time import sleep
from dc_watchdog import DCWatchdog

run = False

class ZMQrecv():
    global run
    def __init__(self, context, client):
        self.context = context
        self.client = client
        self.client.connect("tcp://192.168.5.148:1234")
        self.client.subscribe("")
      
    def recv_msg(self):
        msg_thread = threading.currentThread()  
        while (run == True):
            #print("sending request %d" % i)
            #self.client.send_string(str(i))
            message = self.client.recv()
            print("Recieved message %s " %(message))
        self.client.close()
        self.context.term()
        print("thread joined")
           
            
def signal_handler(signalNumber,frame):
    global run
    print("SIGNAL RECIEVED")
   #run = False
    

if __name__ == "__main__":
    
    signal.signal(signal.SIGUSR1, signal_handler)
      
    while True:
        print("<<<STARTING NOW>>>")
        context = zmq.Context()
        client  = context.socket(zmq.SUB)
        run = True
        msg_queue = ZMQrecv(context,client)
        msg_thread = threading.Thread(target=msg_queue.recv_msg)
        msg_thread.start()
        signal.pause()
        run = False
        msg_thread.join()
        print("<<<ENDING NOW>>>")
        
        
    print("EXITED")        


