import numpy as np


class SecondOrderResonator:
    def __init__(self, sample_rate, center_freq, a2):
        """
        Инициализация резонатора второго порядка.

        :param sample_rate: частота дискретизации (Гц)
        :param center_freq: центральная частота (Гц)
        :param a2: параметр регулировки полосы пропускания (-1..+1)
        """
        self.sample_rate = sample_rate
        self.center_freq = center_freq
        self.a2 = a2

        # Расчет параметров фильтра согласно формуле (2.1)
        omega0 = 2 * np.pi * center_freq / sample_rate
        cos_omega0 = np.cos(omega0)

        # Коэффициенты передаточной функции
        self.b0 = 1 - self.a2
        self.a1 = -(self.a2 + 1) * cos_omega0

        # Инициализация состояний фильтра
        self.x1 = 0
        self.x2 = 0
        self.y1 = 0
        self.y2 = 0

    def filter(self, signal):
        """
        Применение фильтра к сигналу.

        :param signal: входной сигнал
        :return: отфильтрованный сигнал
        """
        output = np.zeros_like(signal)

        for i in range(len(signal)):
            x0 = signal[i]
            y0 = self.b0 * x0 - self.a1 * self.y1 - self.a2 * self.y2

            output[i] = y0

            # Обновление состояний
            self.x2 = self.x1
            self.x1 = x0
            self.y2 = self.y1
            self.y1 = y0

        return output