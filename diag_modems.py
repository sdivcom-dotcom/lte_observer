import os
import subprocess
from read_modems import read_info_connect, find_count_devices
from decor import delete_trash

command_list_devices = "adb devices -l | grep usb"

def replase_string(input_string):
    input_string = input_string.decode('utf-8')
    input_string = input_string.replace("0123456789ABCDEF", "")
    input_string = input_string.replace("product:msm8916_32_512 model:UZ801 device:msm8916_32_512 transport_id", "")
    input_string = input_string.replace("device", "")
    output_string = input_string.replace(" ", "")
    return output_string


def find_num_devices(num):
    if num == "3":
        val = subprocess.check_output(command_list_devices, stderr=subprocess.STDOUT, shell=True)
        replase_string(val)
        lines = val.split('\n')
        lines = [line for line in lines if line]
        lines.sort()
        device1, device2, device3 = lines
        device1 = delete_trash(device1)
        device2 = delete_trash(device2)
        device3 = delete_trash(device3)
        device_mass = [device1,device2,device3]
    elif num == "2":
        val = subprocess.check_output(command_list_devices, stderr=subprocess.STDOUT, shell=True)
        replase_string(val)
        lines = val.split('\n')
        lines = [line for line in lines if line]
        lines.sort()
        device1, device2 = lines
        device1 = delete_trash(device1)
        device2 = delete_trash(device2)
        device_mass = [device1,device2]
    elif num == "1":
        val = subprocess.check_output(command_list_devices, stderr=subprocess.STDOUT, shell=True)
        replase_string(val)
        device1 = val
        device1 = delete_trash(device1)
        device_mass = device1
    else:
        val = subprocess.check_output(command_list_devices, stderr=subprocess.STDOUT, shell=True)
        replase_string(val)
        lines = val.split('\n')
        lines = [line for line in lines if line]
        lines.sort()
        device1 = lines
        device1 = delete_trash(device1)
        device_mass = device1
    return device_mass


def apn_reader(count,apn_mts, apn_beeline, apn_tele2, apn_mega):
    apn_mass = [apn_mts, apn_beeline, apn_tele2, apn_mega]
    if count == "3":
        if apn_mass == [1, 1, 1, 0]:
            print("Модем с Мегафон не доступен")
        elif apn_mass == [1, 1, 0, 1]:
            print("Модем с ТЕЛЕ2 не доступен")
        elif apn_mass == [1, 0, 1, 1]:
            print("Модем с Билайн не доступен")
        elif apn_mass == [0, 1, 1, 1]:
            print("Модем с МТС не доступен")
        else:
            pass
    elif count == "2":
        if apn_mass == [1, 1, 0, 0]:
            print("Модем с Мегафон не доступен")
            print("Модем с ТЕЛЕ2 не доступен")
        elif apn_mass == [1, 0, 0, 1]:
            print("Модем с ТЕЛЕ2 не доступен")
            print("Модем с Билайн не доступен")
        elif apn_mass == [0, 0, 1, 1]:
            print("Модем с Билайн не доступен")
            print("Модем с МТС не доступен")
        elif apn_mass == [0, 1, 1, 0]:
            print("Модем с МТС не доступен")
            print("Модем с Мегафон не доступен")
        elif apn_mass == [1, 0, 1, 0]:
            print("Модем с Билайн не доступен")
            print("Модем с Мегафон не доступен")
        elif apn_mass == [0, 1, 0, 1]:
            print("Модем с МТС не доступен")
            print("Модем с ТЕЛЕ2 не доступен")
        else:
            pass


def diag_devices():
    apn_mts = 0
    apn_beeline = 0
    apn_tele2 = 0
    apn_mega = 0
    count = find_count_devices()
    if count == "3":
        print("Прочитаем какие модемы работают")
        device_mass = find_num_devices(count)
        params = read_info_connect(device_mass[0])
        if params[2] == "internet.mts.ru":
            print("Модем с МТС доступен")
            apn_mts = 1
        elif params[2] == "internet.beeline.ru":
            print("Модем с Билайн доступен")
            apn_beeline = 1
        elif params[2] == "internet.tele2.ru":
            print("Модем с ТЕЛЕ2 доступен")
            apn_tele2 = 1
        elif params[2] == "internet":
            print("Модем с Мегафон доступен")
            apn_mega = 1
        else:
            pass
        params = read_info_connect(device_mass[1])
        if params[2] == "internet.mts.ru":
            print("Модем с МТС доступен")
            apn_mts = 1
        elif params[2] == "internet.beeline.ru":
            print("Модем с Билайн доступен")
            apn_beeline = 1
        elif params[2] == "internet.tele2.ru":
            print("Модем с ТЕЛЕ2 доступен")
            apn_tele2 = 1
        elif params[2] == "internet":
            print("Модем с Мегафон доступен")
            apn_mega = 1
        else:
            pass
        params = read_info_connect(device_mass[2])
        if params[2] == "internet.mts.ru":
            print("Модем с МТС доступен")
            apn_mts = 1
        elif params[2] == "internet.beeline.ru":
            print("Модем с Билайн доступен")
            apn_beeline = 1
        elif params[2] == "internet.tele2.ru":
            print("Модем с ТЕЛЕ2 доступен")
            apn_tele2 = 1
        elif params[2] == "internet":
            print("Модем с Мегафон доступен")
            apn_mega = 1
        else:
            pass
        apn_mass = []
        apn_reader(count,apn_mts, apn_beeline, apn_tele2, apn_mega)
        
    elif count == "2":
        print("Прочитаем какие модемы работают")
        device_mass = find_num_devices(count)
        params = read_info_connect(device_mass[0])
        if params[2] == "internet.mts.ru":
            print("Модем с МТС доступен")
            apn_mts = 1
        elif params[2] == "internet.beeline.ru":
            print("Модем с Билайн доступен")
            apn_beeline = 1
        elif params[2] == "internet.tele2.ru":
            print("Модем с ТЕЛЕ2 доступен")
            apn_tele2 = 1
        elif params[2] == "internet":
            print("Модем с Мегафон доступен")
            apn_mega = 1
        else:
            pass
        params = read_info_connect(device_mass[1])
        if params[2] == "internet.mts.ru":
            print("Модем с МТС доступен")
            apn_mts = 1
        elif params[2] == "internet.beeline.ru":
            print("Модем с Билайн доступен")
            apn_beeline = 1
        elif params[2] == "internet.tele2.ru":
            print("Модем с ТЕЛЕ2 доступен")
            apn_tele2 = 1
        elif params[2] == "internet":
            print("Модем с Мегафон доступен")
            apn_mega = 1
        else:
            pass
        apn_reader(count,apn_mts, apn_beeline, apn_tele2, apn_mega)
    elif count == "1":
        device_mass = find_num_devices(count)
        params = read_info_connect(device_mass)
        if params[2] == "internet.mts.ru":
            print("Модем МТС лишь доступен")
        elif params[2] == "internet.beeline.ru":
            print("Модем с Билайн лишь доступен")
        elif params[2] == "internet.tele2.ru":
            print("Модем с ТЕЛЕ2 лишь доступен")
        elif params[2] == "internet":
            print("Модем с Мегафон лишь доступен")
        else:
            pass
    
    else:
        print("Недоступен никакой из модемов, проверьте хаб!")