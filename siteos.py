# libs
import time
from SCP import *
from boot_sequence import *
import random
# variable config
selection = None
isShutdown = 0
isSelfdestruct = 0
bootsequence()
print("Booting into Linux Kernal version 5.8...")
time.sleep(2)
print("Welcome to SITE OS!\n")
while (True):
    selection = str(input("1 to DESTROY ALL DATA, 2 to browse SCP dictionary, 3 to report a technical problem, 4 to report an SCP breach, 5 to shutdown: \nSITE OS: "))
    if (selection == "1"):
        print("destroying in in 5")
        time.sleep(1)
        print("4")
        time.sleep(1)
        print("3")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("1")
        time.sleep(1)
        bootsequence()
        time.sleep(1)
        print("No boot device detected")
        quit()
    elif (selection == "2"):
            SCPselection = str(input("\n1 for SCP-682, \n2 for SCP-079, \n3 for SCP-173, \n4 for SCP-012, \n5 for SCP-294: \nSITE OS:"))
            if (SCPselection == "1"):
                SCP682()
            elif(SCPselection == "2"):
                SCP079()
            elif(SCPselection == "3"):
                SCP173()
            elif(SCPselection == "4"):
                SCP012()
    elif (selection == "3"):
        random = random.randrange(0,72)
        problem = str(input("What is the technical problem you would like to report?"))
        print("The problem you reported today: \n", problem)
        print("We will get to it in", random, "hours")
