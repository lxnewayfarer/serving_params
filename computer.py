# -*- coding: utf-8 -*-


from math import factorial


class Computer():
    # Метод возвращает строку с результатами рассчета параметров для многоканальной СМО с очередью
    @staticmethod
    def compute(lambda_value, mu_value, n_value, m_value):
        result = ''

        if m_value:
            result += 'Многоканальная СМО с ограниченной очередью\n\n'
        else:
            result += 'Многоканальная СМО с неограниченной очередью\n\n'

        ro = lambda_value / mu_value
        result += '• Среднее число незанятых каналов ρ = ' + str(ro) + '\n'

        # calc p0
        if m_value:
            row = []
            for n in range(int(n_value) + 2):
                if n == 0:
                    row.append(1)
                elif n == n_value + 1:
                    row.append(ro ** (n) * (1 - (ro / (n-1)) ** m_value) /
                               (n-1) / factorial(n-1) / (1 - (ro / (n-1))))
                else:
                    row.append(ro ** n / factorial(n))
            p0 = sum(row) ** -1
        else:
            row = []
            for n in range(int(n_value) + 2):
                if n == 0:
                    row.append(1)
                elif n == n_value + 1:
                    row.append(ro ** (n) / factorial(n-1) / (n - 1 - ro))
                else:
                    row.append(ro ** n / factorial(n))
            p0 = sum(row) ** -1

        # check limit
        if ro / n_value < 1:
            result += '• ρ/n < 1: предельные вероятности существуют - очередь не растет до бесконечности/предела\n'
            result += '• Вероятность того, что очередь пуста р0 = ' + \
                str(p0) + '\n'
            if m_value:
                Potk = ro ** (n_value + m_value) * p0 / \
                    n_value**m_value / factorial(n_value)
                result += '• Вероятность отказа Pотк = ' + str(Potk) + '\n'
                result += '• Относительная пропускная способность Q = ' + \
                    str(1 - Potk) + '\n'
                result += '• Абсолютная пропускная способность А = ' + \
                    str(lambda_value * (1-Potk)) + '\n'
                Loch = ro ** (n_value + 1) * p0 * (1 - (m_value + 1 -
                                                        m_value * ro / n_value) * (ro / n_value) ** m_value)
                Loch = Loch / n_value / \
                    factorial(n_value) / (1 - ro / n_value) ** 2
                result += '• Среднее число заявок в очереди Lоч = ' + \
                    str(Loch) + '\n'
                k = ro * (1 - Potk)
                result += '• Среднее число заявок под обслуживанием k` = ' + \
                    str(k) + '\n'
                result += '• Среднее число заявок в системе Lсист = ' + \
                    str(Loch + k) + '\n'
                result += '• Среднее  время  пребывания  заявки  в  очереди Tоч = ' + \
                    str(Loch / ro) + '\n'
                result += '• Среднее  время  пребывания  заявки  в системе Tсист = ' + \
                    str((Loch + k) / ro) + '\n'
            else:
                Poch = ro ** (n_value + 1) * p0 / \
                    factorial(n_value) / (n_value - ro)
                result += '• Вероятность того, что заявка окажется в очереди Pоч = ' + \
                    str(Poch) + '\n'
                Loch = ro ** (n_value + 1) * p0 / (n_value *
                                                   factorial(n_value) * (1 - ro / n_value) ** 2)
                result += '• Среднее число заявок в очереди Lоч = ' + \
                    str(Loch) + '\n'
                result += '• Среднее число заявок в системе Lсист = ' + \
                    str(Loch + ro) + '\n'
                result += '• Коэффициент (доля) занятых каналов k3 = ' + \
                    str(ro / n_value) + '\n'
                result += '• Среднее  время  пребывания  заявки  в  очереди Tоч = ' + \
                    str(1 / lambda_value * Loch) + '\n'
                result += '• Среднее  время  пребывания  заявки  в системе Tсист = ' + \
                    str(1 / lambda_value * (Loch + ro)) + '\n'
            result += '• Относительная величина затрат при n = ' + str(n_value) + ': Cотн = ' +\
                str(1 / lambda_value * n_value + 3 *
                    (1 / lambda_value * Loch)) + '\n'
        else:
            result += '• ρ/n ≥ 1: очередь растет до бесконечности\n'
            for n in range(int(n_value), 100001):
                if n == 100000:
                    result += '• минимальное n чтобы очередь не росла до бесконечности превышает 10⁵'
                if ro / n < 1:
                    result += '• минимальное n чтобы очередь не росла до бесконечности = ' + \
                        str(n)
                    break

        return result
