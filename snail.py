from datetime import datetime, timedelta
import pyautogui
import time
import sys

def function(timetostop):
    pyautogui.FAILSAFE = False
    numMin = None
    if ((len(sys.argv)<2) or sys.argv[1].isalpha() or int(sys.argv[1])<1):
        numMin = 3
    else:
        numMin = int(sys.argv[1])

    end_time = datetime.now() + timedelta(minutes=timetostop)

    while True:
        current_time = datetime.now()

        if current_time > end_time:
            break
        x=0
        while(x<numMin):
            time.sleep(15)
            x+=1
        for i in range(0,200):
            pyautogui.moveTo(0,i*4)
            if current_time > end_time:
                break   

        pyautogui.moveTo(1,1)
        for i in range(0,3):
            pyautogui.press("shift")
            

        print("Movement made at {}".format(datetime.now().time()))

    print("done")

def main():
    print("Enter time to run in minutes: ")
    timetostop = int(input())
    function(timetostop)

main()

