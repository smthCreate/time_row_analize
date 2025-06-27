import numpy as np
import os
from src.filter import SecondOrderResonator
from src.analysis import analyze_signal, detect_morse_timings
from src.visualization import plot_signal, plot_spectrum, save_morse_code
from src.morse import decode_morse_digit, MORSE_DIGITS
import matplotlib.pyplot as plt


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
    bandwidth_param = 0.57  # Параметр a2 для регулировки полосы

    # Создаем и применяем фильтр
    resonator = SecondOrderResonator(sample_rate, center_freq, bandwidth_param)
    filtered_signal = resonator.filter(signal)

    # Анализируем отфильтрованный сигнал
    filtered_spectrum = analyze_signal(filtered_signal)

    # Визуализируем результаты фильтрации
    plot_signal(filtered_signal, 'Отфильтрованный сигнал', 'results/filtered_signal.png')
    plot_spectrum(filtered_spectrum, 'Спектр отфильтрованного сигнала', 'results/filtered_spectrum.png')

    # Демодулируем и сохраняем код Морзе
    envelope = np.abs(filtered_signal)
    threshold = 0.5 * np.max(envelope)
    morse_signal = (envelope > threshold).astype(int)
    save_morse_code(morse_signal, 'results/morse_code.png')
    print(morse_signal)
    # Определяем длительности элементов
    dot_duration = detect_morse_timings(morse_signal, sample_rate)

    # Декодируем цифру
    morse_code = decode_morse_digit(morse_signal, sample_rate)
    digit = None
    for num, code in MORSE_DIGITS.items():
        if code == morse_code:
            digit = num
            break

    # Сохраняем итоговые результаты
    with open('results/results.txt', 'w', encoding='utf-8') as f:
        f.write(f"Итог работы:\n")
        f.write(f"1. Выбранное значение коэффициента a2: {bandwidth_param}\n")
        f.write(f"2. Длительность элементарного такта кода Морзе: {dot_duration:.4f} сек\n")
        f.write(f"3. Выбранное значение частоты настройки резонатора: {center_freq} Гц\n")



if __name__ == "__main__":
    main()