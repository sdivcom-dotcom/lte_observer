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


def process_data(filename):
    data = load_data_from_json(filename)
    df = pd.DataFrame(data)
    df[['Rsrp', 'Rsrq', 'Rssnr', 'SignalStrength']] = df[['Rsrp', 'Rsrq', 'Rssnr', 'SignalStrength']].astype(int)
    df['sum_of_first_values'] = 0
    
    i = 0
    r = min(300, len(df))  # Убедимся, что r не больше количества строк в DataFrame
    while i < r:
        # Выводим первые значения каждой переменной
        first_value_rsrp = df['Rsrp'].values[i]
        first_value_rsrq = df['Rsrq'].values[i]
        first_value_rssnr = df['Rssnr'].values[i]
        first_value_signal_strength = df['SignalStrength'].values[i]
        #sum_of_first_values = (first_value_rsrp + first_value_rsrq + first_value_rssnr + first_value_signal_strength) / 4
        sum_of_first_values = (first_value_rsrp + first_value_signal_strength) / 2
        df.loc[i, 'sum_of_first_values'] = sum_of_first_values
        i = i + 1
    
    return df



def results_plot(namefile_mas):
    # Список файлов
    #    = ['beeline_9_11_2023modem_name2.json', 'megafon_9_11_2023modem_name0.json',
    #             'mts_9_11_2023modem_name1.json', 'tele2_9_11_2023modem_name3.json']

    # Построение графиков и расчет среднего арифметического для каждого файла
    for filename in namefile_mas:
        df = process_data(filename)
        
        # Построение графика
        plt.plot(range(len(df['sum_of_first_values'])), df['sum_of_first_values'], label=f'{filename} - Mean: {df["sum_of_first_values"].mean():.2f}')

    plt.xlabel('Time')
    plt.ylabel('Signal Strength')
    plt.title('Operators Signal Strength for day')
    plt.legend()
    name = "result" + what_day()
    plt.savefig(name)



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
    print(pref)
    command = "mv " + filename + " " + pref
    os.system(command)


def obrab(filename):
    prefix = opred_apn(filename)
    corrector(filename)
    data = load_data_from_json(filename)
    plot_data(data, prefix)
    response = prefix + "_" + filename
    return response
    

def mv_file(filename_mass):
    i = 0
    r = 4
    while i < r:
        filename = filename_mass[i]
        prefix = opred_apn(filename)
        move_file(filename, prefix)
        i = i + 1


def main():
    filename1 = what_day() + 'modem_name0.json'
    obrab(filename1)
    filename2 = what_day() +  'modem_name1.json'
    obrab(filename2)
    filename3 = what_day() +  'modem_name2.json'
    obrab(filename3)
    filename4 = what_day() +  'modem_name3.json'
    obrab(filename4)
    filename_mass = [filename1,filename2,filename3,filename4]
    results_plot(filename_mass)
    mv_file(filename_mass)
    print(filename_mass)

main()