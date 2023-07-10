import tkinter as tk

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(number))

def button_clear():
    entry.delete(0, tk.END)

def button_equal():
    result = eval(entry.get())
    entry.delete(0, tk.END)
    entry.insert(tk.END, result)

# Создаем объект окна
window = tk.Tk()
window.title("Калькулятор")

# Создаем поле ввода
entry = tk.Entry(window, width=30, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Создаем кнопки
buttons = [
    ('7', 1, 0),
    ('8', 1, 1),
    ('9', 1, 2),
    ('/', 1, 3),
    ('4', 2, 0),
    ('5', 2, 1),
    ('6', 2, 2),
    ('*', 2, 3),
    ('1', 3, 0),
    ('2', 3, 1),
    ('3', 3, 2),
    ('-', 3, 3),
    ('0', 4, 0),
    ('.', 4, 1),
    ('=', 4, 2),
    ('+', 4, 3)
]

for label, row, column in buttons:
    btn = tk.Button(window, text=label, padx=20, pady=10, command=lambda label=label: button_click(label))
    btn.grid(row=row, column=column)

# Кнопка очистки
btn_clear = tk.Button(window, text='C', padx=20, pady=10, command=button_clear)
btn_clear.grid(row=5, column=0, columnspan=2)

# Запускаем главный цикл окна
window.mainloop()
