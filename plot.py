import os
import json
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt


def load_data_from_json(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data


def what_day():
    now = datetime.now()
    time_mass = [now.day,now.month,now.year]
    time_mass = str(time_mass)
    time_mass = time_mass.replace("[", "")
    time_mass = time_mass.replace("]", "")
    time_mass = time_mass.replace(" ", "")
    time_mass = time_mass.replace(",", "_")
    return time_mass


def plot_data(data, prefix):
    df = pd.DataFrame(data)
    df['data'] = pd.to_datetime(df['data'])
    plt.figure(figsize=(12, 8))
    plt.plot(df['data'], df['Rsrp'])
    plt.title('Rsrp vs. Data')
    plt.xlabel('Date and Time')
    plt.ylabel('Rsrp')
    name = prefix + '_rsrp_plot.png'
    plt.savefig(name)
    plt.clf()
    plt.plot(df['data'], df['Rsrq'])
    plt.title('Rsrq vs. Data')
    plt.xlabel('Date and Time')
    plt.ylabel('Rsrq')
    plt.savefig('rsrq_plot.png')
    name = prefix + '_rsrq_plot.png'
    plt.savefig(name)
    plt.clf()
    plt.plot(df['data'], df['Rssnr'])
    plt.title('Rssnr vs. Data')
    plt.xlabel('Date and Time')
    plt.ylabel('Rssnr')
    name = prefix + '_rssnr_plot.png'
    plt.savefig(name)
    plt.clf()
    plt.plot(df['data'], df['SignalStrength'])
    plt.title('SignalStrength vs. Data')
    plt.xlabel('Date and Time')
    plt.ylabel('SignalStrength')
    name = prefix + '_signal_strength_plot.png'
    plt.savefig(name)
    plt.clf()


def opred_apn(filename):
    with open(filename, 'r') as file:
        file_content = file.read()
    if 'internet.mts.ru' in file_content:
        result = "mts"
    elif 'internet.beeline.ru' in file_content:
        result = "beeline"
    elif 'internet.tele2.ru' in file_content:
        result = "tele2"
    else:
        result = "megafon"
    return result


def corrector(filename):
    with open(filename, 'r') as file:
        file_content = file.read()
    if not file_content.endswith(']'):
        with open(filename, 'a') as file:
            file.write(']')
    else:
        pass


def move_file(filename, prefix):
    pref = prefix + "_" + filename
    command = "mv " + filename + " " + pref
    os.system(command)


def obrab(filename):
    prefix = opred_apn(filename)
    corrector(filename)
    data = load_data_from_json(filename)
    plot_data(data, prefix)
    move_file(filename, prefix)
    

def main():
    filename = what_day() + 'modem_name0.json'
    obrab(filename)
    filename = what_day() +  'modem_name1.json'
    obrab(filename)
    filename = what_day() +  'modem_name2.json'
    obrab(filename)
    filename = what_day() +  'modem_name3.json'
    obrab(filename)


main()
