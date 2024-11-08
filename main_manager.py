import logging
import sys

# from MyAction2 import MyActions2#
from MyActions1 import MyActions1
from collections import namedtuple
from datetime import datetime, timedelta


import concurrent.futures
import subprocess
import queue
import time


class ScriptManager:
    def __init__(self, max_workers=3, max_retries=3, check_output=None):
        self.max_workers = max_workers  # 并行任务数
        self.max_retries = max_retries  # 最大重试次数
        self.check_output = check_output  # 返回值检测函数
        self.tasks = []  # 用于存储任务信息
        self.results = {}

    def add_task(self, func, *args):
        """添加任务到任务列表中"""
        self.tasks.append((func, args))

    def _run_task(self, func, args, retry=0):
        """运行脚本并捕捉异常和返回值"""
        try:
            result = func(*args)

            log_prefix_str = "["+args[1]+":"+ args[0]+"]"
            # 检查返回值
            res_check = self.check_output(result,args[1],args[0])   # 这个返回值0 表示不重启，正值表示重启第N页，负值表示错误且不重启
            if self.check_output and  res_check!=0:
                if retry < self.max_retries:
                    logging.warning( log_prefix_str +  "返回值不符合预期，正在重试..." + ":页码:" + str(res_check))
                    print(log_prefix_str +f"返回值不符合预期，正在重试({retry + 1}/{self.max_retries})..."+ ":页码:" + str(res_check))
                    tmpargs_tulple = args[:-1] + (res_check,)
                    return self._run_task(func, tmpargs_tulple, retry + 1)   #注意，这里重启，页码和之前不一样
                else:
                    logging.error(log_prefix_str+"返回值不符合预期，超过最大重试次数:" +":页码:"+str(res_check))
                    raise ValueError("返回值不符合预期，超过最大重试次数")
            elif res_check==0:
                print(log_prefix_str + "运行成功，完毕")
                logging.info(log_prefix_str+"运行成功，完毕")

            return result
        except Exception as e:
            error_message = str(e)
            print("["+args[1]+":"+ args[0]+"]"+f"任务{func.__name__}异常错误: {error_message}")
            logging.warning("["+args[1]+":"+ args[0]+"]"+"异常错误:" + str(e))
            if retry < self.max_retries:
                print("["+args[1]+":"+ args[0]+"]" + f"修复异常，正在重试({retry + 1}/{self.max_retries})...")
                logging.warning("["+args[1]+":"+ args[0]+"]" + "修复异常,正在重试:")
                return self._run_task(func, args, retry + 1)
            else:
                print("["+args[1]+":"+ args[0]+"]" + f"任务{func.__name__}彻底失败，超过最大重试次数")
                logging.error("["+args[1]+":"+ args[0]+"]" + "任务彻底失败,超过最大重试次数")
                return None


    def start(self):
        """启动任务管理器并行执行任务列表中的任务"""
        with concurrent.futures.ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            for func, args in self.tasks:
                future = executor.submit(self._run_task, func, args)
                # self.results[func.__name__] = future
                self.results["["+args[1]+":"+ args[0]+"]"] = future
                time.sleep(20)  #每隔15秒才能启动下一个任务


    def get_results(self):
        """获取任务执行结果"""
        for func_name, future in self.results.items():
            try:
                result = future.result()
                if result !=0:   ##我们只打印失败的
                    print(f"{func_name} 执行结果: {result}")
                    logging.info( func_name + "执行结果:" + str(result))
            except Exception as e:
                print(f"{func_name} 执行失败: {e}")
                logging.info(func_name +"执行失败:" + str(e))

#----------------------------------------
#把日期间隔，生成一连串的日期
def convert_date_string(start_date_str,end_date_str):
    # 将字符串转换为日期对象
    start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
    end_date = datetime.strptime(end_date_str, '%Y-%m-%d')

    # 初始化一个空列表来存储所有日期字符串
    date_list = []

    # 生成两个日期之间的所有日期
    current_date = start_date
    while current_date <= end_date:
        # 将日期转换为字符串并添加到列表中
        date_list.append(current_date.strftime('%Y-%m-%d'))
        # 将日期加1天
        current_date += timedelta(days=1)
    return date_list






#----------- 系统基础设置
SetBaseDelayTm = 3  # 基础延时时间

# 南通
SetBaseFolder = "C:/Users/Administrator/Desktop/sun04/SaveImg/"
SetChromePath = "C:/Users/Administrator/Desktop/sun04/pachong4/chromedriver_win64/chromedriver.exe"
SetLogPath = "C:/Users/Administrator/Desktop/sun04/SaveImg/"
SetAreaFilePath ="C:/Users/Administrator/Desktop/sun04/pachong4/custom.zip"

# 家里
# SetBaseFolder = "C:/Users/bobby/Desktop/sun04/SaveImg/"
# SetChromePath = "C:/Users/bobby/Desktop/sun04/pachong4/chromedriver_win64/chromedriver.exe"
# SetLogPath = "C:/Users/bobby/Desktop/sun04/SaveImg/"
# SetAreaFilePath ="C:/Users/bobby/Desktop/sun04/pachong4/custom.zip"

# 办公室
# SetBaseFolder = "C:/Users/SITP/Desktop/sun04/SaveImg/"
# SetChromePath = "C:/Users/SITP/Desktop/sun04/pachong4/chromedriver_win64/chromedriver.exe"
# SetLogPath = "C:/Users/SITP/Desktop/sun04/SaveImg/"
# SetAreaFilePath ="C:/Users/SITP/Desktop/sun04/pachong4/custom.zip"


SearchTask = namedtuple('SearchTask', ['SatID','StartDate', 'EndDate'])  #建立搜索任务结构体
Tasks_List = []  #建立任务列表

# task1 = SearchTask('GF5A', '2024-08-02',  '2024-08-02')  #第一个搜索任务，注意，起始和结束日期都是包含的
# Tasks_List.append(task1)

#从这里开始，我们要把原来的重新扫一遍，为了全球数据。  我们要扫03-01到9月30所有数据

# task11 = SearchTask('GF5A', '2024-03-14',  '2024-09-30')  #第一个搜索任务，注意，起始和结束日期都是包含的
# task12 = SearchTask('GF5B', '2024-03-01',  '2024-09-30')  #第一个搜索任务，注意，起始和结束日期都是包含的
# task13 = SearchTask('ZY1E', '2024-03-01',  '2024-09-30')  #第一个搜索任务，注意，起始和结束日期都是包含的
task14 = SearchTask('ZY1F', '2024-03-12',  '2024-09-30')  #第一个搜索任务，注意，起始和结束日期都是包含的
# Tasks_List.append(task11)
# Tasks_List.append(task12)
# Tasks_List.append(task13)
Tasks_List.append(task14)


#### 使用示例
if __name__ == "__main__":
    def check_output(output,newSatID, newDate):
        """返回值检查函数，例如检查是否包含某个字符串"""
        if output == -30000:
            print("["+newSatID+":"+ newDate+"]"+"[check_output]单日无数据")
            logging.warning("["+newSatID+":"+ newDate+"]"+"[check_output]单日无数据")
            return 0  #单日无数据不重启
        elif output<-20000 and output>-30000:   # 如果有错，但是中国不存在，错误
            print("["+newSatID+":"+ newDate+"]"+"[check_output]中国不存在发生，需要重启")
            logging.warning("["+newSatID+":"+ newDate+"]"+"[check_output]中国不存在发生，需要重启")
            new_startpage1 = abs(output)-20000
            return new_startpage1
        elif output>0:  #返回值>0，说明要重新执行第res页，因此重新执行
            print("["+newSatID+":"+ newDate+"]"+"[check_output]不明重启")
            logging.warning("["+newSatID+":"+ newDate+"]"+"[check_output]不明重启")
            new_startpage1 = output
            return new_startpage1
        elif output<0:  #如果有其他报错，直接退出
            return -1
        elif output ==0: # 如果是正常的，赶紧滚
            return 0

        return 0


    # ---------- 自动设置日志
    LogName = SetLogPath + "Log_" + datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".log"
    logging.basicConfig(filename=LogName, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')




    manager = ScriptManager(max_workers=8, max_retries=20, check_output=check_output)

    # 添加任务

    for e_task in Tasks_List:
        date_list = convert_date_string(e_task.StartDate, e_task.EndDate)  # 任务日期序列
        SetSatID = e_task.SatID   # 当前任务卫星编号
        #拆解成每个日期一个任务，然后压入
        for i_date in date_list:
            SetSearchDate = i_date
            new_startpage = 1

            # 压入任务队列
            manager.add_task(MyActions1, SetSearchDate, SetSatID, SetBaseFolder, SetChromePath, SetAreaFilePath,
                             SetBaseDelayTm, new_startpage)

            # manager.add_task(MyActions2, [SetSearchDate, SetSatID, SetBaseFolder, SetChromePath, SetAreaFilePath, SetBaseDelayTm, new_startpage])
            # arggg = [SetSearchDate, SetSatID, SetBaseFolder, SetChromePath, SetAreaFilePath, SetBaseDelayTm, new_startpage]
            # print(arggg)
    # 启动任务管理器
    manager.start()

    # 获取执行结果
    manager.get_results()