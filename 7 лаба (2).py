from itertools import permutations
from tkinter import *
from tkinter import scrolledtext, messagebox
import random
a,b=[],[]
def generate_optimal_pair(K):
    ratings = {i: random.randint(1, 10) for i in range(1, K + 1)}
    print("Рейтинги членов комиссии:", ratings)
    # Все возможные пары (председатель, заместитель)
    members = list(ratings.keys())
    all_pairs = permutations(members, 2)
    # Фильтрация пар по ограничению (разница рейтингов <= 3)
    filtered_pairs = [(chair, deputy) for chair, deputy in all_pairs if abs(ratings[chair] - ratings[deputy]) <= 3]
    print("\nДопустимые варианты после фильтрации:")
    for chair, deputy in filtered_pairs:
        a.append(f"Председатель: {chair} (рейтинг {ratings[chair]}), Заместитель: {deputy} (рейтинг {ratings[deputy]})")
    # Нахождение оптимальной пары (максимальная сумма рейтингов)
    return a
def optimal(K):
    ratings = {i: random.randint(1, 10) for i in range(1, K + 1)}
    # Все возможные пары (председатель, заместитель)
    members = list(ratings.keys())
    all_pairs = permutations(members, 2)
    # Фильтрация пар по ограничению (разница рейтингов <= 3)
    filtered_pairs = [(chair, deputy) for chair, deputy in all_pairs if abs(ratings[chair] - ratings[deputy]) <= 3]
    # Нахождение оптимальной пары (максимальная сумма рейтингов)
    if filtered_pairs:
        optimal_pair = max( filtered_pairs, key=lambda pair: ratings[pair[0]] + ratings[pair[1]])
        chair, deputy = optimal_pair
        b.append(f"Оптимальная пара: Председатель {chair} (рейтинг {ratings[chair]}), Заместитель {deputy} (рейтинг {ratings[deputy]})")
    return b
def on_run():
    try:
        K = int(entry_k.get())
    except ValueError:
        messagebox.showerror("Ошибка", "Ошибка")
        return
    gen = generate_optimal_pair(K)
    opt = optimal(K)
    output.config(state='normal')
    output.delete('1.0', END)
    output.insert(INSERT, f"Возможные варианты:\n{gen}\n\n")
    output.insert(INSERT, f"Самый оптимальный вариант:\n{opt}\n")
    output.config(state='disabled')
# Главное окно ввода и вывода
root = Tk()
root.geometry("600x500")
root.title("Лаб. №7")

# Фрейм для ввода
frame = Frame(root)
frame.pack(padx=10, pady=5)

# Ввод n
Label(frame, text="Количество  людей: ", font=('Arial', 14)).grid(row=0, column=0, sticky="w")
entry_k = Entry(frame)
entry_k.grid(row=0, column=1, padx=5)

# Кнопка запуска
btn = Button(frame, text="Выполнить", font=('Arial', 14), command=on_run)
btn.grid(row=1, column=0, columnspan=2, pady=8)

# Поле вывода с прокруткой
output = scrolledtext.ScrolledText(root, width=60, height=20)
output.pack(padx=10, pady=5)
output.config(state='disabled')
root.mainloop()