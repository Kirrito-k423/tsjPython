
from tsjPython.tsjCommonFunc import *


if __name__ == '__main__':
    passTime(CP=[0,1,2])
    for i in range(10):
        time.sleep(1.5)
        passTime(UP=[0])
        time.sleep(0.2)
        passTime(CP=[0])
        time.sleep(0.4)
        passTime(CP=[0])
