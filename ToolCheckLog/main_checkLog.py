
#这个程序用来根据Tasks_List和Log，分析是否有未完成的任务，并输出控制台

from collections import namedtuple, defaultdict
import datetime
import re

# Generate new SearchTask objects for incomplete date ranges
def generate_search_tasks(sat_id, incomplete_dates):
    sorted_dates = sorted(incomplete_dates)
    tasks = []
    start_date = sorted_dates[0]
    for i in range(1, len(sorted_dates)):
        current_date = datetime.datetime.strptime(sorted_dates[i], '%Y-%m-%d')
        prev_date = datetime.datetime.strptime(sorted_dates[i - 1], '%Y-%m-%d')
        if (current_date - prev_date).days > 1:
            end_date = sorted_dates[i - 1]
            tasks.append(SearchTask(sat_id, start_date, end_date))
            start_date = sorted_dates[i]
    tasks.append(SearchTask(sat_id, start_date, sorted_dates[-1]))
    return tasks









# Define the tasks
SearchTask = namedtuple('SearchTask', ['SatID','StartDate', 'EndDate'])
Tasks_List = []

task11 = SearchTask('GF5A', '2024-01-01',  '2024-02-29')  #第一个搜索任务，注意，起始和结束日期都是包含的
task12 = SearchTask('GF5B', '2024-01-01',  '2024-02-29')  #第一个搜索任务，注意，起始和结束日期都是包含的
task13 = SearchTask('ZY1E', '2024-01-01',  '2024-02-29')  #第一个搜索任务，注意，起始和结束日期都是包含的
task14 = SearchTask('ZY1F', '2024-01-01',  '2024-02-29')  #第一个搜索任务，注意，起始和结束日期都是包含的
Tasks_List.append(task11)
Tasks_List.append(task12)
Tasks_List.append(task13)
Tasks_List.append(task14)

# Generate expected tasks
expected_tasks = defaultdict(set)

for task in Tasks_List:
    sat_id = task.SatID
    start_date = datetime.datetime.strptime(task.StartDate, '%Y-%m-%d')
    end_date = datetime.datetime.strptime(task.EndDate, '%Y-%m-%d')
    delta = end_date - start_date
    for i in range(delta.days + 1):
        date = start_date + datetime.timedelta(days=i)
        date_str = date.strftime('%Y-%m-%d')
        expected_tasks[sat_id].add(date_str)

# Read the log and extract successful dates
completed_tasks = defaultdict(set)

# Replace 'your_log_file.log' with the path to your actual log file
log_file_path = 'C:/Users/bobby/Desktop/1.log'

with open(log_file_path, 'r', encoding='ansi') as f:
    for line in f:
        if '运行成功，完毕' in line:
            # Extract satellite ID and date using regex
            match = re.search(r'\[(.*?):(.*?)\]', line)
            if match:
                sat_id = match.group(1)
                date_str = match.group(2)
                completed_tasks[sat_id].add(date_str)

# Find incomplete tasks
incomplete_tasks = defaultdict(set)

for sat_id in expected_tasks:
    expected_dates = expected_tasks[sat_id]
    completed_dates = completed_tasks.get(sat_id, set())
    incomplete_dates = expected_dates - completed_dates
    if incomplete_dates:
        incomplete_tasks[sat_id] = incomplete_dates

# Output incomplete tasks
for sat_id in incomplete_tasks:
    print(f'Satellite {sat_id} has incomplete tasks on dates:')
    for date_str in sorted(incomplete_tasks[sat_id]):
        print(date_str)

# 最后输出代码样式
print("代码样式=============")
for sat_id, dates in incomplete_tasks.items():
    search_tasks = generate_search_tasks(sat_id, dates)
    for task in search_tasks:
        print(f'task = SearchTask(\'{task.SatID}\', \'{task.StartDate}\', \'{task.EndDate}\')')