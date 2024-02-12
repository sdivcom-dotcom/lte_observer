
import time
from read_modems import find_devices, radio_switch


def reboot_modem(device):
    time.sleep(1)
    radio_switch(device,"off")
    time.sleep(10)
    radio_switch(device,"on")
    time.sleep(1)


def reboots_modems(device_mass):
    ii = 0
    rr = 4
    while ii < rr:
            reboot_modem(device_mass[ii])
            ii = ii + 1
    

def main(sleep_time):
    print("Start Cycle")
    #time.sleep(sleep_time)
    print("Перезагружаем модемы")
    device_mass = find_devices()
    reboots_modems(device_mass)
    time.sleep(sleep_time)


main(120)