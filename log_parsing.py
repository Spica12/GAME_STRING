from datetime import datetime


# 2023-09-04 20:56:16.112894 - INFO - Generating map size_n: 5; size_m: 6

log_times = list()
logs = list()
with open('logs.txt', 'r') as file:
    for line in file:
        logs.append(line)
        time = datetime.strptime(line.split(' - ')[0], '%d.%m.%Y %H:%M:%S')
        log_times.append(time)


# start_date = input('Start date in format: (dd.mm.yyyy HH:MM:SS): ')

start_date = '04.09.2023 21:06:40'

start_date = datetime.strptime(start_date, '%d.%m.%Y %H:%M:%S')


# end_date = input('End date in format: (dd.mm.yyyy HH:MM:SS): ')

end_date = '04.09.2023 21:12:40'

end_date = datetime.strptime(end_date, '%d.%m.%Y %H:%M:%S')

for log, log_time in zip(logs, log_times):
    if start_date < log_time and log_time < end_date:
        print(log.strip())
