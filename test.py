import json
from collections import Counter

def load_data_from_json(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data

# Загружаем данные из файла JSON
filename = 'beeline_9_11_2023modem_name2.json'
data = load_data_from_json(filename)

# Создаем список значений Rsrp
rsrp_values = [entry['SignalStrength'] for entry in data]

# Используем Counter для подсчета уникальных значений
rsrp_counter = Counter(rsrp_values)

# Общее количество значений
total_values = len(rsrp_values)

# Выводим результаты
print("Частота значений Rsrp:")
for value, count in rsrp_counter.items():
    print(f"{value}: {count} раза ({(count/total_values)*100:.2f}%)")

# Находим значение, которое встречается чаще всего
most_common_value, most_common_count = rsrp_counter.most_common(1)[0]
print(f"\nЗначение Rsrp, которое встречается чаще всего: {most_common_value} ({most_common_count} раз, {(most_common_count/total_values)*100:.2f}%)")
