
from tsjPython.tsjCommonFunc import *
import time

class globalTimeClass:
    count=0
    beginTime =-1
    lastTime =-1
    def __init__(self,time=0):
        self.beginTime = time
        self.lastTime = time
    def updateTime(self,message):
        if self.beginTime==-1 and self.lastTime==-1:
            splitLine("start time check")
            current_milli_time = round(time.time() * 1000)
            self.beginTime =current_milli_time
            self.lastTime =current_milli_time
            self.count =0
        else:
            print(message)
            current_milli_time = round(time.time() * 1000)
            yellowPrint("passTime {} from Last:  {:6d}ms, {:6f}s".format(self.count,current_milli_time-self.lastTime,float(current_milli_time-self.lastTime)/1000))
            yellowPrint("passTime {} from start: {:6d}ms, {:6f}s".format(self.count,current_milli_time-self.lastTime,float(current_milli_time-self.lastTime)/1000))
            self.lastTime =current_milli_time
            self.count+=1


globalTime = globalTimeClass(-1)


def passTime(message="passTime:"):
    globalTime.updateTime(message)


if __name__ == '__main__':
    passTime()
    time.sleep(1.5)
    passTime()
    time.sleep(0.2)
    passTime()
