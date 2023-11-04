import json
import pandas as pd
import matplotlib.pyplot as plt

def load_data_from_json(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data

def plot_data(data):
    df = pd.DataFrame(data)
    
    # Преобразовываем столбец 'data' в формат даты и времени
    df['data'] = pd.to_datetime(df['data'])
    
    # Строим графики
    fig, axes = plt.subplots(2, 2, figsize=(12, 8))
    
    # График для Rsrp
    axes[0, 0].plot(df['data'], df['Rsrp'])
    axes[0, 0].set_title('Rsrp vs. Data')
    
    # График для Rsrq
    axes[0, 1].plot(df['data'], df['Rsrq'])
    axes[0, 1].set_title('Rsrq vs. Data')
    
    # График для Rssnr
    axes[1, 0].plot(df['data'], df['Rssnr'])
    axes[1, 0].set_title('Rssnr vs. Data')
    
    # График для SignalStrength
    axes[1, 1].plot(df['data'], df['SignalStrength'])
    axes[1, 1].set_title('SignalStrength vs. Data')
    
    plt.tight_layout()
    plt.show()

# Загружаем данные из файла JSON
filename = 'data.json'
data = load_data_from_json(filename)

# Строим графики
plot_data(data)