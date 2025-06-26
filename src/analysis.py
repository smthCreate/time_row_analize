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