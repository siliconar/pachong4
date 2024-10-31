import logging
import sys

from MyActions1 import MyActions1
from collections import namedtuple
from datetime import datetime, timedelta

#跑1天,带重启
def RunOneDay(SetSearchDate, SetSatID, SetBaseFolder, SetChromePath, SetAreaFilePath, SetBaseDelayTm, StartPage):

    #不带出错重新执行的跑1天,如果某页断连，这个函数是不管的，会在下面的代码重启，返回值表示哪个页面需要重启
    res = MyActions1(SetSearchDate, SetSatID, SetBaseFolder, SetChromePath,SetAreaFilePath, SetBaseDelayTm, StartPage)


    #判定是否完成
    while(res!=0):

        if res<-20000 and res>-30000:   # 如果有错，但是中国不存在，错误
            logging.error("中国不存在发生，重启")
            new_startpage = abs(res)-20000
            res = MyActions1(SetSearchDate, SetSatID, SetBaseFolder, SetChromePath, SetAreaFilePath, SetBaseDelayTm, new_startpage)
            continue
        elif res==-30000: #如果是因为没数据，那么单独标记出来
            logging.error("因单日无数据失败，不重启")
            break;

        elif res<0:  #如果有其他报错，直接退出
            break

        elif res>0:  #返回值>0，说明要重新执行第res页，因此重新执行
            new_startpage = res
            res = MyActions1(SetSearchDate, SetSatID, SetBaseFolder, SetChromePath, SetAreaFilePath, SetBaseDelayTm, new_startpage)
            continue


    #如果完成了
    if res == 0:
        print(SetSearchDate + "完成！！")
        return 0
    else:
        return res


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
# task1 = SearchTask('GF5A', '2024-09-24',  '2024-09-24')  #第一个搜索任务，注意，起始和结束日期都是包含的
# task2 = SearchTask('GF5B', '2024-09-16',  '2024-09-30')  #第一个搜索任务，注意，起始和结束日期都是包含的
# task3 = SearchTask('ZY1E', '2024-09-16',  '2024-09-30')  #第一个搜索任务，注意，起始和结束日期都是包含的
# task4 = SearchTask('ZY1F', '2024-09-21',  '2024-09-30')  #第一个搜索任务，注意，起始和结束日期都是包含的

# Tasks_List.append(task0)
# Tasks_List.append(task1)
# Tasks_List.append(task2)
# Tasks_List.append(task3)
# Tasks_List.append(task4)

# task6 = SearchTask('GF5A', '2024-02-15',  '2024-02-29')  #第一个搜索任务，注意，起始和结束日期都是包含的
# task7 = SearchTask('GF5B', '2024-02-15',  '2024-02-29')  #第一个搜索任务，注意，起始和结束日期都是包含的
# task8 = SearchTask('ZY1E', '2024-02-15',  '2024-02-29')  #第一个搜索任务，注意，起始和结束日期都是包含的
# task9 = SearchTask('ZY1F', '2024-02-15',  '2024-02-29')  #第一个搜索任务，注意，起始和结束日期都是包含的
# Tasks_List.append(task6)
# Tasks_List.append(task7)
# Tasks_List.append(task8)
# Tasks_List.append(task9)

#从这里开始，我们要把原来的重新扫一遍，为了全球数据。  我们要扫03-01到9月30所有数据
task11 = SearchTask('GF5A', '2024-03-01',  '2024-09-30')  #第一个搜索任务，注意，起始和结束日期都是包含的
task12 = SearchTask('GF5B', '2024-03-01',  '2024-09-30')  #第一个搜索任务，注意，起始和结束日期都是包含的
task13 = SearchTask('ZY1E', '2024-03-01',  '2024-09-30')  #第一个搜索任务，注意，起始和结束日期都是包含的
task14 = SearchTask('ZY1F', '2024-03-01',  '2024-09-30')  #第一个搜索任务，注意，起始和结束日期都是包含的
Tasks_List.append(task11)
Tasks_List.append(task12)
Tasks_List.append(task13)
Tasks_List.append(task14)




#----------- 系统基础设置
SetBaseDelayTm = 3  # 基础延时时间
# SetBaseFolder = "C:/Users/Administrator/Desktop/sun04/SaveImg/"
# SetChromePath = "C:/Users/Administrator/Desktop/sun04/pachong4/chromedriver_win64/chromedriver.exe"
# SetLogPath = "C:/Users/Administrator/Desktop/sun04/SaveImg/"
# SetAreaFilePath ="C:/Users/Administrator/Desktop/sun04/pachong4/custom.zip"

# SetBaseFolder = "C:/Users/bobby/Desktop/sun04/SaveImg/"
# SetChromePath = "C:/Users/bobby/Desktop/sun04/pachong4/chromedriver_win64/chromedriver.exe"
# SetLogPath = "C:/Users/bobby/Desktop/sun04/SaveImg/"
# SetAreaFilePath ="C:/Users/bobby/Desktop/sun04/pachong4/custom.zip"

SetBaseFolder = "C:/Users/SITP/Desktop/sun04/SaveImg/"
SetChromePath = "C:/Users/SITP/Desktop/sun04/pachong4/chromedriver_win64/chromedriver.exe"
SetLogPath = "C:/Users/SITP/Desktop/sun04/SaveImg/"
SetAreaFilePath ="C:/Users/SITP/Desktop/sun04/pachong4/custom.zip"

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

        res_1d = RunOneDay(i_date, SetSatID, SetBaseFolder, SetChromePath, SetAreaFilePath,SetBaseDelayTm, 1)
        if res_1d!=0:
            if res_1d == -30000:
                ErrorList.append(SetSatID + " " + i_date + ":单日无数据")  # 记录下来这个错误
                print("单日无数据: " + SetSatID + " " + i_date)
                logging.error("单日无数据:: " + SetSatID + " " + i_date)
            else:
                ErrorList.append(SetSatID + " " + i_date)  # 记录下来这个错误
                print("单日不成功: " + SetSatID + " " + i_date)
                logging.error("单日不成功: " + SetSatID + " " + i_date)

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








