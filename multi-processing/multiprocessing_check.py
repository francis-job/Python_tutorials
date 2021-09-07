import multiprocessing
import os
from time import sleep

def process_one():
    print("Hi I am Process Number 1")

def process_two():
    print("Hi I am Process Number 2")

if __name__ == "__main__":
    print("ID of the main process is {}".format(os.getpid()))

    p1 = multiprocessing.Process(target = process_one)
    p2 = multiprocessing.Process(target = process_two)

    p1.start()
    p2.start()

    print("Process ID for process_one is {}".format(p1.pid))
    print("Process ID for process_two is {}".format(p2.pid))
    
    print("process_one is alive : {}".format(p1.is_alive()))
    print("process_two is alive : {}".format(p2.is_alive()))
    
    sleep(10)

    p1.join()
    p2.join()
    
    print("Process has been finished")

    print("process_one is alive : {}".format(p1.is_alive()))
    print("process_two is alive : {}".format(p2.is_alive()))

