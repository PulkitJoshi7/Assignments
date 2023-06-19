import multiprocessing
  
def print_num1():
    print("Num: 4")

def print_num2():
    print("Num: 3")

def print_num3():
    print("Num: 2")

def print_num4():
    print("Num: 1")
  

  
if __name__ == "__main__":

    p1 = multiprocessing.Process(target=print_num1)
    p2 = multiprocessing.Process(target=print_num2)
    p3 = multiprocessing.Process(target=print_num3)
    p4 = multiprocessing.Process(target=print_num4)
  

    p1.start()
    p2.start()
    p3.start()
    p4.start()

    p1.join()
    p2.join()
    p3.join()
    p4.join()
  

    print("Done!")