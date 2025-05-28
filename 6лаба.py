import math
import time
import matplotlib.pyplot as plt
from functools import lru_cache
# Рекурсивная реализация с мемоизацией
@lru_cache(maxsize=None)
def F_rec(n):
    if n == 1:
        return 1
    return (-1) ** n * (2 * F_rec(n - 1) - G_rec(n - 1))
@lru_cache(maxsize=None)
def G_rec(n):
    if n == 1:
        return 1
    return F_rec(n - 1) / math.factorial(2 * n) + 2 * G_rec(n - 1)
# Итерационная реализация
def F_iter(n):
    if n == 1:
        return 1, 1
    f_prev, g_prev = 1, 1
    for i in range(2, n + 1):
        f_current = (-1) ** i * (2 * f_prev - g_prev)
        g_current = f_prev / math.factorial(2 * i) + 2 * g_prev
        f_prev, g_prev = f_current, g_current
    return f_prev, g_prev
# Сравнение производительности
def compare_methods(max_n):
    results = []
    for n in range(1, max_n + 1):
        # Рекурсивный расчет
        start = time.perf_counter()
        try:
            f_rec = F_rec(n)
            g_rec = G_rec(n)
            rec_time = time.perf_counter() - start
        except RecursionError:
            print(f"Рекурсия прервана на n={n} из-за переполнения стека")
            f_rec, g_rec, rec_time = float('nan'), float('nan'), float('nan')
        # Итерационный расчет
        start = time.perf_counter()
        f_iter, g_iter = F_iter(n)
        iter_time = time.perf_counter() - start
        results.append((n, f_rec, g_rec, rec_time, iter_time))
    return results
# Параметры исследования
MAX_N = 30
# Получаем результаты
results = compare_methods(MAX_N)
# Выводим таблицу результатов
print("\nРезультаты вычислений:")
print("n\tF(n)\t\tG(n)\t\tРекурсия (с)\tИтерация (с)")
print("-" * 80)
for n, f, g, t_rec, t_iter in results:
        print(f"{n}\t{f:.6f}\t{g:.6f}\t{t_rec:.6f}\t\t{t_iter:.6f}")
# Построение графика
plt.figure(figsize=(12, 6))
n_values = [r[0] for r in results]
rec_times = [r[3] if not math.isnan(r[3]) else 0 for r in results]
iter_times = [r[4] for r in results]
plt.plot(n_values, rec_times, 'o-', label='Рекурсивный метод')
plt.plot(n_values, iter_times, 's-', label='Итерационный метод')
plt.xlabel('n')
plt.ylabel('Время выполнения (секунды)')
plt.title('Сравнение производительности методов')
plt.legend()
plt.grid(True)
plt.yscale('log')
plt.show()