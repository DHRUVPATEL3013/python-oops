
from multiprocessing import Process
import time

def task1():
    print("Task 1 started")
    time.sleep(3)
    print("Task 1 finished")

def task2():
    print("Task 2 started")
    time.sleep(2)
    print("Task 2 finished")

if __name__=="__main__":
  p1 = Process(target=task1)
  p2 = Process(target=task2)

  p1.start()
  p2.start()

  p1.join()
  p2.join()

  print("Main process finished")
