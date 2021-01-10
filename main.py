# -*- coding: UTF-8 -*-
# Файл реализует графический интерфейс, отправляет введенные значения в Computer::computer
# И получает оттуда результат рассчета параметров в виде строки, которая выводится в интерфейс


from computer import Computer
from tkinter import *


# Многоканальная СМО с неограниченной очередью
def compute_first():
    try:
        m_value = m_field.get('1.0', END)[:-1]
        if m_value.isdigit():
            m_value = float(m_value)
        else:
            m_value = 0
        lambda_value = float(lambda_field.get('1.0', END))
        mu_value = float(mu_field.get('1.0', END))
        n_value = float(n_field.get('1.0', END))

        result = Computer.compute(lambda_value, mu_value, n_value, m_value)
    except Exception as exception:
        result = exception
    finally:
        result_field_1.delete('1.0', END)
        result_field_1.insert(1.0, result)


root = Tk()
root.title('Рассчет параметров систем массового обслуживания')

label = Label(text='Многоканальная СМО с очередью (если m - длина очереди не задана, \nто в таком случае очередь считается неограниченной)',
              font='Arial 14', padx=20)
label.grid(row=0, sticky='', column=0, columnspan=2)

lambda_label = Label(text='Интенсивность потока заявок λ = ')
lambda_field = Text(root, width=7, height=1, font='Arial 14', wrap=WORD)

lambda_label.grid(row=1, sticky='e', column=0)
lambda_field.grid(row=1, sticky='w', column=1)

mu_label = Label(text='Интенсивность потока обслуживания μ = ')
mu_field = Text(root, width=7, height=1, font='Arial 14', wrap=WORD)

mu_label.grid(row=2, sticky='e', column=0)
mu_field.grid(row=2, sticky='w', column=1)

n_label = Label(text='Количество каналов n = ')
n_field = Text(root, width=7, height=1, font='Arial 14', wrap=WORD)

n_label.grid(row=3, sticky='e', column=0)
n_field.grid(row=3, sticky='w', column=1)

m_label = Label(text='Длина очереди m = ')
m_field = Text(root, width=7, height=1, font='Arial 14', wrap=WORD)

m_label.grid(row=4, sticky='e', column=0)
m_field.grid(row=4, sticky='w', column=1)


compute_button_1 = Button(root, text='Рассчитать',
                          height=1, font='arial 14', command=compute_first)
compute_button_1.grid(row=5, column=0, columnspan=2)

result_field_1 = Text(root, height=20, width=75, font='Arial 14', wrap=WORD)
result_field_1.grid(row=6, column=0, columnspan=2, padx=20, pady=6)

root.mainloop()
