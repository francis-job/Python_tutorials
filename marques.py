import threading
import os
import signal
import time
from dc_watchdog import DCWatchdog

i = 0
run = False
RED_LED="/sys/class/leds/beaglebone:green:usr-r"
GREEN_LED="/sys/class/leds/beaglebone:green:usr-g"
BLUE_LED="/sys/class/leds/beaglebone:green:usr-b"

def signal_handler(signalNumber,frame):
    global i
    i +=1
    if(i>2):
        i = 0
    return

def blinky(LED):
    global run
    thread1 = threading.currentThread()
    while (run == True):
        os.system('echo 0 >'+LED+'/brightness')
        time.sleep(1)
        os.system('echo 1 >'+LED+'/brightness')
        time.sleep(1)
    os.system('echo 0 >'+LED+'/brightness')
        
        

if __name__ == "__main__":
    
    
    LED = (RED_LED,GREEN_LED,BLUE_LED)
    color=("red", "green", "blue")
    watchdog = DCWatchdog()
    watchdog.ping(True)
    print('my process id is:', os.getpid())

    signal.signal(signal.SIGUSR1, signal_handler)
    os.system('echo 0 >'+LED[0]+'/brightness')
    os.system('echo 0 >'+LED[1]+'/brightness')
    os.system('echo 0 >'+LED[2]+'/brightness')
    
    while True:
        print("Blinking with color :",color[i]) 
        thread1 = threading.Thread(target=blinky,args=(LED[i],))
        run = True
        thread1.start()
        signal.pause()
        run = False
        thread1.join()
    
    


