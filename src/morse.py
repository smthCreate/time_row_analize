import numpy as np
# Коды Морзе для цифр (точка = 1, тире = 111, пауза между элементами = 0)
MORSE_DIGITS = {
    0: '111111000',  # -----
    1: '101110000',  # .----
    2: '101011000',  # ..---
    3: '101010100',  # ...--
    4: '101010010',  # ....-
    5: '101010001',  # .....
    6: '101010111',  # -....
    7: '101011111',  # --...
    8: '101111111',  # ---..
    9: '111010101'  # ----.
}


def decode_morse_digit(signal, sample_rate, threshold=0.5):
    """
    Декодирование цифры из сигнала с кодом Морзе.

    :param signal: бинарный сигнал (1 - есть сигнал, 0 - нет)
    :param sample_rate: частота дискретизации
    :param threshold: порог для определения длительности точки
    :return: строка с кодом Морзе (точек и тире)
    """
    # Находим изменения состояния сигнала
    changes = np.diff(signal, prepend=0)
    rise_times = np.where(changes == 1)[0]
    fall_times = np.where(changes == -1)[0]

    # Определяем длительности импульсов и пауз
    durations = []
    for i in range(len(rise_times)):
        if i < len(fall_times):
            durations.append(fall_times[i] - rise_times[i])

    if not durations:
        return ""

    # Определяем длительность точки (минимальная длительность импульса)
    dot_duration = min(durations)

    # Строим код Морзе
    morse_code = []
    for duration in durations:
        if duration < 2 * dot_duration:
            morse_code.append('1')  # Точка
        else:
            morse_code.append('111')  # Тире

    return ''.join(morse_code)