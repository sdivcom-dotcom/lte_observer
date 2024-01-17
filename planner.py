import os
import subprocess
import time
from datetime import datetime

start_hour = 0
start_minute = 48

def what_day_str():
    now = datetime.now()
    time_mass = [now.day,now.month,now.year]
    time_mass = str(time_mass)
    time_mass = time_mass.replace("[", "")
    time_mass = time_mass.replace("]", "")
    time_mass = time_mass.replace(" ", "")
    time_mass = time_mass.replace(",", "_")
    return time_mass


def what_time_day():
    now = datetime.now()
    time_mass = [now.hour,now.minute]
    return time_mass


def what_time():
    now = datetime.now()
    time_mass = [now.day,now.month,now.year]
    return time_mass

def start_programm(name_file):
    command = "python3 " + name_file
    response = os.system(command)
    if response != 0:
        time.sleep(10)
        print("Повторный запуск")
        response = os.system(command)
        if response != 0:
            print("Повторный запуск не вышел")
        else:
            print("Повторный запуск вышел")
    else:
        pass
    return response


def prover_files():
    command = "ls | grep json | wc -l"
    val = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)
    val = val.decode('utf-8')
    val = val.replace(" ", "")
    val = val.replace("\n", "")
    if val == "4":
        response = 1
    else:
        response = 0
    return response


def new_dir(day_str):
    command_dir = "mkdir results_"
    command = command_dir + day_str
    os.system(command)


def cp_rm_results(day_str):
    command_cp = "cp *.json results_" + day_str + "&& cp *.png results_" + day_str
    os.system(command_cp)
    command_rm = "rm *.json && rm *.png"
    os.system(command_rm)
try:
    while True:
        time_mass = what_time_day()
        if time_mass[0] == start_hour and time_mass[1] == start_minute:
            print("Запуск программы для сборки результатов. Время старта=",time_mass)
            time.sleep(10)
            start_programm("cycle.py")
            val = prover_files()
            if val == 1:
                day_str = what_day_str()
                start_programm("plot.py")
                print("Запуск генерации графиков")
                new_dir(day_str)
                cp_rm_results(day_str)
            else:
                print("Не были созданы все файлы")
        else:
            time.sleep(60)
except KeyboardInterrupt:
    print("Выход из цикла по нажатию Ctrl+C")