import matplotlib.pyplot as plt
import numpy as np

def plot_signal(signal, title, filename):
    """
    Построение графика сигнала и сохранение в файл.
    """
    plt.figure(figsize=(12, 4))
    plt.plot(signal)
    plt.title(title)
    plt.xlabel('Отсчеты')
    plt.ylabel('Амплитуда')
    plt.grid(True)
    plt.savefig(filename)
    plt.close()

def plot_spectrum(spectrum, title, filename):
    """
    Построение амплитудного спектра сигнала.
    """
    xf, yf = spectrum
    plt.figure(figsize=(12, 4))
    plt.plot(xf, yf)
    plt.title(title)
    plt.xlabel('Частота (Гц)')
    plt.ylabel('Амплитуда')
    plt.grid(True)
    plt.savefig(filename)
    plt.close()

def save_morse_code(binary_signal, filename):
    """
    Визуализация бинарного сигнала с кодом Морзе.
    """
    plt.figure(figsize=(12, 2))
    plt.step(range(len(binary_signal)), binary_signal, where='post')
    plt.title('Демодулированный код Морзе')
    plt.xlabel('Отсчеты')
    plt.ylabel('Состояние (0/1)')
    plt.yticks([0, 1], ['0', '1'])
    plt.grid(True)
    plt.savefig(filename)
    plt.close()