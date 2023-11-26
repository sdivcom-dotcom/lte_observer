import json
import pandas as pd
import matplotlib.pyplot as plt

def load_data_from_json(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data

# Загружаем данные из файла JSON
filename = 'beeline_9_11_2023modem_name2.json'
data = load_data_from_json(filename)

# Создаем DataFrame из данных
df = pd.DataFrame(data)

# Преобразуем столбец 'data' в формат даты и времени
df['data'] = pd.to_datetime(df['data'])

# Выводим массивы значений для каждой переменной
print("Массив значений Rsrp:")
print(df['Rsrp'].values)

print("\nМассив значений Rsrq:")
print(df['Rsrq'].values)

print("\nМассив значений Rssnr:")
print(df['Rssnr'].values)

print("\nМассив значений SignalStrength:")
print(df['SignalStrength'].values)

# Строим графики
plt.figure(figsize=(15, 10))

# График для Rsrp
plt.subplot(221)
plt.plot(df['data'], df['Rsrp'], marker='o')
plt.title('График Rsrp')
plt.xlabel('Дата и время')
plt.ylabel('Rsrp')

# График для Rsrq
plt.subplot(222)
plt.plot(df['data'], df['Rsrq'], marker='o', color='orange')
plt.title('График Rsrq')
plt.xlabel('Дата и время')
plt.ylabel('Rsrq')

# График для Rssnr
plt.subplot(223)
plt.plot(df['data'], df['Rssnr'], marker='o', color='green')
plt.title('График Rssnr')
plt.xlabel('Дата и время')
plt.ylabel('Rssnr')

# График для SignalStrength
plt.subplot(224)
plt.plot(df['data'], df['SignalStrength'], marker='o', color='red')
plt.title('График SignalStrength')
plt.xlabel('Дата и время')
plt.ylabel('SignalStrength')

plt.tight_layout()
plt.show()