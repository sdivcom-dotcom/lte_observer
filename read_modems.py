import os
import subprocess
from decor import delete_trash, delete_simbol
import time

command_adb = "adb -s "
command_list_devices = "adb devices -l | grep usb"


def find_count_devices():
    command_find_count = "lsusb | grep 'Qualcomm' | wc -l"
    retuse = subprocess.check_output(command_find_count, stderr=subprocess.STDOUT, shell=True)
    retuse = delete_simbol(retuse)
    return retuse


def find_devices():
    retuse = find_count_devices()
    if retuse == "4":
        val = subprocess.check_output(command_list_devices, stderr=subprocess.STDOUT, shell=True)
        val = val.decode('utf-8')
        val = val.replace("0123456789ABCDEF", "")
        val = val.replace("product:msm8916_32_512 model:UZ801 device:msm8916_32_512 transport_id", "")
        val = val.replace("device", "")
        val = val.replace(" ", "")
        lines = val.split('\n')
        lines = [line for line in lines if line]
        lines.sort()
        device1, device2, device3, device4 = lines
        device1 = delete_trash(device1)
        device2 = delete_trash(device2)
        device3 = delete_trash(device3)
        device4 = delete_trash(device4)
        device_mass = [device1,device2,device3,device4]
    else:
        device_mass = []
    return device_mass


def radio_switch(device, state):
    command_on = " shell radiooptions 1"
    command_off = " shell radiooptions 5"
    command_reboot = " shell radiooptions 0"
    reboot = "shell reboot"
    if state == "on":
        command = command_adb + device + command_on
        os.system(command)
    elif state == "off":
        command = command_adb + device + command_off
        os.system(command)
    elif state == "reboot":
        command = command_adb + device + command_reboot
        command2 = command_adb + device + reboot
        os.system(command)
        time.sleep(5)
        os.system(command2)
    else:
        pass


def find_connected_device(device):
    command_connect = " shell dumpsys connectivity | grep UNKNOWN/IDLE, | wc -l"
    command = command_adb + device + command_connect
    read_connect = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)
    read_connect = delete_simbol(read_connect)
    if read_connect == "10":
        response = 1
    else:
        response = 0
    return response


def read_info_connect(device):
    command_read_connect = " shell dumpsys connectivity | grep CONNECTED/CONNECTED,"
    command = command_adb + device + command_read_connect
    read_connect_device = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)
    read_connect_device = delete_simbol(read_connect_device)
    read_connect_device = read_connect_device.replace("state:CONNECTED/CONNECTED,", "")
    read_connect_device = read_connect_device.replace("NetworkInfo:type:mobile[LTE]", "")
    read_connect_device = read_connect_device.replace("roaming:false,", "")
    read_connect_device = read_connect_device.replace("isConnectedToProvisioningNetwork:false", "")
    read_connect_device = read_connect_device.replace("'", "")
    read_connect_device = read_connect_device.replace("reason", "")
    read_connect_device = read_connect_device.replace("failover", "")
    read_connect_device = read_connect_device.replace("extra", "")
    read_connect_device = read_connect_device.replace("isAvailable", "")
    read_connect_device = read_connect_device.replace(":", "")
    read_connect_device = read_connect_device.replace("\r", "")
    lines = read_connect_device.split(',')
    lines = [line for line in lines if line]
    lines.sort()
    param1, param2, param3, param4 = lines
    read_info_connect_params_mass = [param1, param2, param3, param4]
    return read_info_connect_params_mass


def read_info_lte(device):
    command_read_lte = " shell dumpsys activity broadcasts | grep LteRsrp"
    command = command_adb + device + command_read_lte
    read_lte_devce = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)
    read_lte_devce = delete_simbol(read_lte_devce)
    #print(read_lte_devce)
    read_lte_devce = read_lte_devce.replace("LteCqi=2147483647,CdmaDbm=-120,CdmaEcio=-160,GsmSignalStrength=99,isGsm=true,TdScdma=2147483647,EvdoDbm=-120,EvdoSnr=-1,EvdoEcio=-1,GsmBitErrorRate=0,", "")
    read_lte_devce = read_lte_devce.replace("CdmaDbm=-120", "")
    read_lte_devce = read_lte_devce.replace("CdmaEcio=-160", "")
    read_lte_devce = read_lte_devce.replace("EvdoDbm=-120", "")
    read_lte_devce = read_lte_devce.replace("EvdoEcio=0", "")
    read_lte_devce = read_lte_devce.replace("EvdoSnr=-1", "")
    read_lte_devce = read_lte_devce.replace("GsmBitErrorRate=0", "")
    read_lte_devce = read_lte_devce.replace("GsmSignalStrength=0", "")
    read_lte_devce = read_lte_devce.replace("LteCqi=0", "")
    read_lte_devce = read_lte_devce.replace("TdScdma=2147483647", "")
    read_lte_devce = read_lte_devce.replace("isGsm=true", "")
    read_lte_devce = read_lte_devce.replace("Bundle[{", "")
    read_lte_devce = read_lte_devce.replace("}]", "")
    read_lte_devce = read_lte_devce.replace("\r\n", "")
    read_lte_devce = read_lte_devce.replace("LteRsrp=", "")
    read_lte_devce = read_lte_devce.replace("LteRsrq=", "")
    read_lte_devce = read_lte_devce.replace("LteRssnr=", "")
    read_lte_devce = read_lte_devce.replace("LteSignalStrength=", "")
    read_lte_devce = read_lte_devce.replace("2147483647", "0")
    read_lte_devce = read_lte_devce.replace("\r", "")
    lines = read_lte_devce.split(',')
    lines = [line for line in lines if line]
    lines.sort()
    param1, param2, param3, param4 = lines 
    read_lte_devce_params_mass = [param1, param2, param3, param4]
    return read_lte_devce_params_mass


def main_read_modems():
    device_mass = find_devices()
    #print("find_devices", device_mass)
    val = find_connected_device(device_mass[0])
    val1 = read_info_connect(device_mass[0])
    val2 = read_info_lte(device_mass[0])
    #print("find_connected_device", val, val1, val2)
    val = find_connected_device(device_mass[1])
    val1 = read_info_connect(device_mass[1])
    val2 = read_info_lte(device_mass[1])
    #print("find_connected_device", val, val1, val2)
    val = find_connected_device(device_mass[2])
    val1 = read_info_connect(device_mass[2])
    val2 = read_info_lte(device_mass[2])
    #print("find_connected_device", val, val1, val2)
    val = find_connected_device(device_mass[3])
    val1 = read_info_connect(device_mass[3])
    val2 = read_info_lte(device_mass[3])
    #print("find_connected_device", val, val1, val2)



