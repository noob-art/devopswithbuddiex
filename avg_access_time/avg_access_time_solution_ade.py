from datetime import datetime, timedelta
from os import path, system
from sys import argv as argument

system('clear')
time_fmt = '%H:%M:%S %m-%d-%Y'

def calculate_interval(start,end):
    start_time = datetime.strptime(start, time_fmt)
    end_time = datetime.strptime(end, time_fmt)
    time_diff = end_time - start_time
    return time_diff

def average_interval(interval_list:list):
    average_interval = sum(interval_list,timedelta())/len(interval_list)
    average_interval_fmt = str(average_interval).split('.')[0]
    return str(average_interval_fmt)

def find_time_range(check_file):
    intervals=[]
    with open (check_file,'r') as file:
        for line in file: 
            parts = line.strip().split()
            clock_time, date, user_id, file_hash, file_status = parts
            time = f"{clock_time} {date}"


            print(f'{time=}\n{user_id=}\n{file_hash=}\n{file_status=}\n')

    #         time_diff = calculate_interval(start,end)
    #         print(time_diff)
    #         intervals.append(time_diff)
    # return average_interval(intervals)

def main():
    # if len(argument) != 2:
    #     error_message="\nDon't forget to pass in the log file ONLY"
    #     raise ValueError(f"{error_message}")

    # check_file = argument[1]
    check_file = 'log'

    # if not path.exists(check_file):
    #     raise FileNotFoundError(f"{check_file} does not exist")

    print(f'The average timespan is: {find_time_range(check_file)}')

if __name__ == "__main__":
    main()