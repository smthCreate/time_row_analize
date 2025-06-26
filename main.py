import numpy as np
import os
from src.filter import SecondOrderResonator
from src.analysis import analyze_signal
from src.visualization import plot_signal, plot_spectrum, save_morse_code


def main():
    # Создаем папку для результатов, если ее нет
    os.makedirs('results', exist_ok=True)

    # Загружаем сигнал из файла
    signal = np.loadtxt('data/signal.txt')

    # Анализируем исходный сигнал
    original_spectrum = analyze_signal(signal)

    # Визуализируем исходные данные
    plot_signal(signal, 'Исходный сигнал с помехами', 'results/original_signal.png')
    plot_spectrum(original_spectrum, 'Спектр исходного сигнала', 'results/original_spectrum.png')

    # Параметры резонатора (подбираются экспериментально)
    sample_rate = 1000  # Частота дискретизации (Гц)
    center_freq = 50  # Центральная частота (Гц) - нужно уточнить по спектру
    bandwidth = 5  # Ширина полосы пропускания (Гц)

    # Создаем и применяем фильтр
    resonator = SecondOrderResonator(sample_rate, center_freq, bandwidth)
    filtered_signal = resonator.filter(signal)

    # Анализируем отфильтрованный сигнал
    filtered_spectrum = analyze_signal(filtered_signal)

    # Визуализируем результаты фильтрации
    plot_signal(filtered_signal, 'Отфильтрованный сигнал', 'results/filtered_signal.png')
    plot_spectrum(filtered_spectrum, 'Спектр отфильтрованного сигнала', 'results/filtered_spectrum.png')

    # Демодулируем и сохраняем код Морзе
    save_morse_code(filtered_signal, sample_rate, 'results/morse_code.png')


if __name__ == "__main__":
    main()