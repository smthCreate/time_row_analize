import matplotlib.pyplot as plt
import numpy as np


def plot_signal(signal, title, filename):
    """
    Построение графика сигнала и сохранение в файл.

    :param signal: сигнал для визуализации
    :param title: заголовок графика
    :param filename: имя файла для сохранения
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

    :param spectrum: кортеж (частоты, амплитуды)
    :param title: заголовок графика
    :param filename: имя файла для сохранения
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


def save_morse_code(signal, sample_rate, filename):
    """
    Демодуляция и визуализация кода Морзе.

    :param signal: отфильтрованный сигнал
    :param sample_rate: частота дискретизации
    :param filename: имя файла для сохранения
    """
    # Простая демодуляция огибающей
    envelope = np.abs(signal)

    # Нормировка и пороговая обработка
    threshold = 0.5 * np.max(envelope)
    morse_code = (envelope > threshold).astype(int)

    # Визуализация
    plt.figure(figsize=(12, 4))
    plt.plot(morse_code)
    plt.title('Демодулированный код Морзе')
    plt.xlabel('Отсчеты')
    plt.ylabel('Состояние (0/1)')
    plt.yticks([0, 1], ['0', '1'])
    plt.grid(True)
    plt.savefig(filename)
    plt.close()