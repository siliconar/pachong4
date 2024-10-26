import logging
import sys

from MyActions1 import MyActions1
from collections import namedtuple
from datetime import datetime, timedelta

#跑1天,带重启
def RunOneDay(SetSearchDate, SetSatID, SetBaseFolder, SetChromePath, SetBaseDelayTm, StartPage):

    #不带出错重新执行的跑1天,如果某页断连，这个函数是不管的，会在下面的代码重启，返回值表示哪个页面需要重启
    res = MyActions1(SetSearchDate, SetSatID, SetBaseFolder, SetChromePath, SetBaseDelayTm, StartPage)


    #判定是否完成
    while(res!=0):
        if res<0:  #如果有错，直接退出
            break

        elif res>0:  #返回值>0，说明要重新执行第res页，因此重新执行
            new_startpage = res
            res = MyActions1(SetSearchDate, SetSatID, SetBaseFolder, SetChromePath, SetBaseDelayTm, new_startpage)
            continue


    #如果完成了
    if res == 0:
        print(SetSearchDate + "完成！！")
        return 0
    else:
        return -1


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





#===================================================
# -----------用户设置的常量设置
SearchTask = namedtuple('SearchTask', ['SatID','StartDate', 'EndDate'])  #建立搜索任务结构体
Tasks_List = []  #建立任务列表

# 卫星选择 ZY1E ZY1dF GF5B GF5A
# task0 = SearchTask('ZY1F', '2024-09-01',  '2024-06-30')  #第一个搜索任务，注意，起始和结束日期都是包含的
# task1 = SearchTask('GF5A', '2024-09-01',  '2024-09-15')  #第一个搜索任务，注意，起始和结束日期都是包含的
# task2 = SearchTask('GF5B', '2024-09-01',  '2024-09-15')  #第一个搜索任务，注意，起始和结束日期都是包含的
# task3 = SearchTask('ZY1E', '2024-09-01',  '2024-09-15')  #第一个搜索任务，注意，起始和结束日期都是包含的
# task4 = SearchTask('ZY1F', '2024-09-02',  '2024-09-15')  #第一个搜索任务，注意，起始和结束日期都是包含的

# Tasks_List.append(task0)
# Tasks_List.append(task1)
# Tasks_List.append(task2)
# Tasks_List.append(task3)
# Tasks_List.append(task4)

task6 = SearchTask('GF5A', '2024-03-03',  '2024-03-14')  #第一个搜索任务，注意，起始和结束日期都是包含的
task7 = SearchTask('GF5B', '2024-03-01',  '2024-03-14')  #第一个搜索任务，注意，起始和结束日期都是包含的
task8 = SearchTask('ZY1E', '2024-03-01',  '2024-03-14')  #第一个搜索任务，注意，起始和结束日期都是包含的
task9 = SearchTask('ZY1F', '2024-03-01',  '2024-03-14')  #第一个搜索任务，注意，起始和结束日期都是包含的
Tasks_List.append(task6)
Tasks_List.append(task7)
Tasks_List.append(task8)
Tasks_List.append(task9)

#----------- 系统基础设置
SetBaseDelayTm = 3  # 基础延时时间
SetBaseFolder = "C:/Users/Administrator/Desktop/sun04/SaveImg/"
SetChromePath = "C:/Users/Administrator/Desktop/sun04/pachong3/chromedriver_win64/chromedriver.exe"
SetLogPath = "C:/Users/Administrator/Desktop/sun04/SaveImg/"

#---------- 自动设置日志
LogName = SetLogPath+"Log_"+datetime.now().strftime("%Y-%m-%d_%H-%M-%S")+".log"
logging.basicConfig(filename=LogName,level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


#------- 正式开始处理每一个task
ErrorList = []
for e_task in Tasks_List:
    date_list = convert_date_string(e_task.StartDate,e_task.EndDate)  #任务日期序列
    SetSatID = e_task.SatID
    #对每个日期进行循环
    for i_date in date_list:

        print("==================")
        print("开始下载: "+SetSatID+" "+i_date)
        logging.info("==================")
        logging.info("开始下载: "+SetSatID+" "+i_date)

        res_1d = RunOneDay(i_date, SetSatID, SetBaseFolder, SetChromePath, SetBaseDelayTm, 1)
        if res_1d!=0:
            ErrorList.append(SetSatID+" "+i_date)  #记录下来这个错误
            print("单日不成功: " + SetSatID+" "+i_date)
            logging.error("单日不成功: " + SetSatID+" "+i_date)
    #end for i_date in date_list:
#end for e_task in Tasks_List:

#---------程序结束，输出所有的错误
if len(ErrorList)==0:
    print("全部成功")
    logging.info("全部成功")
else:
    print("不成功列表:")
    logging.error("不成功列表:")
    for j_error in ErrorList:
        print(j_error)
        logging.error(j_error)







