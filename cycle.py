import time
import json
from datetime import datetime
from diag_modems import diag_devices
from read_modems import find_devices, find_count_devices, read_info_connect, find_connected_device, read_info_lte, radio_switch


def what_day():
    now = datetime.now()
    time_mass = [now.day,now.month,now.year]
    time_mass = str(time_mass)
    time_mass = time_mass.replace("[", "")
    time_mass = time_mass.replace("]", "")
    time_mass = time_mass.replace(" ", "")
    time_mass = time_mass.replace(",", "_")
    return time_mass


def add_data_to_json(filename, Rsrp, Rsrq, Rssnr, SignalStrength, reason, failover, extra, isavailable, date=None):
    times = what_day()
    filename = times + filename + ".json"
    if date is None:
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        with open(filename, 'r') as file:
            existing_data = json.load(file)
    except FileNotFoundError:
        existing_data = []

    new_data = {
        "data": date,
        "Rsrp": Rsrp,
        "Rsrq": Rsrq,
        "Rssnr": Rssnr,
        "SignalStrength": SignalStrength,
        "reason": reason,
        "failover": failover,
        "extra": extra,
        "isAvailable": isavailable
    }

    existing_data.append(new_data)
    with open(filename, 'w') as file:
        json.dump(existing_data, file, indent=4)    


def sum_command(filename, device):
    find = find_connected_device(device)
    if find == 0:
        connect_dev = read_info_connect(device)
        reason = connect_dev[0]
        failover = connect_dev[1]
        extra = connect_dev[2]
        isAvailable = connect_dev[3]
        #print(connect_dev)
        dev_lte = read_info_lte(device)
        Rsrp = dev_lte[0]
        Rsrq = dev_lte[1]
        Rssnr = dev_lte[2]
        SignalStrength = dev_lte[3]
        #print(dev_lte)
        add_data_to_json(filename, Rsrp, Rsrq, Rssnr, SignalStrength, reason, failover, extra, isAvailable, date=None)
    else:
        pass


def reboot_modem(device):
    time.sleep(1)
    radio_switch(device,"off")
    time.sleep(10)
    radio_switch(device,"on")
    time.sleep(1)


def main(minute_cycle, sleep_time):
    print("Start Cycle")
    i = 0
    r = 3
    while i < r:
        dev_count = find_count_devices()
        if dev_count == "4":
            device_mass = find_devices()
            ii = 0
            rr = 4
            while ii < rr:
                ii = str(ii)
                filename = "modem_name" + ii
                ii = int(ii)
                sum_command(filename, device_mass[ii])
                ii = ii + 1
        else:
            print("Недостаточно модемов подключено к сети")
            print("Запускаю диагностику")
            diag_devices()
        time.sleep(sleep_time)
        ii = 0
        rr = 4
        while ii < rr:
            device_mass = find_devices()
            reboot_modem(device_mass[ii])
            ii = ii + 1
        time.sleep(sleep_time)
        i = i + 1
        print("Cycle =",i)

main(1, 120)