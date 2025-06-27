import numpy as np
from scipy.fft import fft, fftfreq


def analyze_signal(signal):
    """
    Анализ сигнала: вычисление амплитудного спектра.

    :param signal: входной сигнал
    :return: частоты и амплитуды спектра
    """
    n = len(signal)
    yf = fft(signal)
    xf = fftfreq(n, 1.0)[:n // 2]

    return xf, 2.0 / n * np.abs(yf[:n // 2])


def detect_morse_timings(binary_signal, sample_rate):
    """
    Определение длительности элементов кода Морзе.

    :param binary_signal: бинарный сигнал (1 - есть сигнал, 0 - нет)
    :param sample_rate: частота дискретизации
    :return: длительность точки в секундах
    """
    # Находим изменения состояния сигнала
    changes = np.diff(binary_signal, prepend=0)
    rise_times = np.where(changes == 1)[0]
    fall_times = np.where(changes == -1)[0]

    # Определяем длительности импульсов
    durations = []
    for i in range(len(rise_times)):
        if i < len(fall_times):
            durations.append(fall_times[i] - rise_times[i])

    if not durations:
        return 0.0

    # Длительность точки - минимальная длительность импульса
    dot_samples = min(durations)
    return dot_samples / sample_rate