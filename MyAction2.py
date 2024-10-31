

import time
import math
import random

def MyActions2(SetSearchDate, SetSatID, SetBaseFolder, SetChromePath, SetAreaFilePath, SetBaseDelayTm, StartPage=1):
    print("任务启动")
    time.sleep(SetBaseDelayTm + 3)
    arggg = [SetSearchDate, SetSatID, SetBaseFolder, SetChromePath, SetAreaFilePath, SetBaseDelayTm, StartPage]
    print("参数：")
    print(arggg)

    rd = random.randint(0,3)
    print("rd:"+str(rd))
    if rd ==0:
        return 0
    elif rd==1:
        return 1
    elif rd==2:
        return 2
    else:
        return -20000-rd



    # return -30000
    # return 3
    # return 0
