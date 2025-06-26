import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Загрузка данных
data = np.loadtxt('data/signal.txt')

# Создание временной оси (предположим частоту дискретизации 1 кГц)
fs = 1000  # частота дискретизации
t = np.arange(len(data)) / fs

# Построение графика сигнала
plt.figure(figsize=(12, 6))
plt.plot(t, data)
plt.title('Сигнал с помехами')
plt.xlabel('Время (с)')
plt.ylabel('Амплитуда')
plt.grid()
plt.show()

# Вычисление спектра
n = len(data)
freq = np.fft.fftfreq(n, 1/fs)
fft_vals = np.fft.fft(data)

# Построение амплитудного спектра
plt.figure(figsize=(12, 6))
plt.plot(freq[:n//2], np.abs(fft_vals[:n//2]))
plt.title('Амплитудный спектр сигнала')
plt.xlabel('Частота (Гц)')
plt.ylabel('Амплитуда')
plt.grid()
plt.show()