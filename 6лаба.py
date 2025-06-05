import math
import timeit
from pandas import DataFrame
import matplotlib.pyplot as plt

# Рекурсивная функция F
def rec_F(n):
     if n == 0 or n == 1:
         return 3
     if n <= 23:
         return (n - 2) * rec_F(n - 1)
     prev = rec_F(n - 1)
     sign = 1 if n % 2 == 0 else -1
     return sign * (3 - prev / math.factorial(2 * n) - (n - 2))

# Итеративная функция F с кэшем факториала
def iter_F(n):
     if n == 0 or n == 1:
         return 3
     F_prev = 3
     fact = 2  # factorial(2)
     for k in range(2, n + 1):
         fact *= (2 * k - 1) * (2 * k)
         if k <= 23:
             F_curr = (k - 2) * F_prev
         else:
             sign = 1 if k % 2 == 0 else -1
             F_curr = sign * (3 - F_prev / fact - (k - 2))
         F_prev = F_curr
     return F_prev

if __name__ == '__main__':
    # сравнение для n от 0 до 30 включительно
    ns = list(range(0, 31))
    results = []
    for n in ns:
        t_rec = timeit.timeit(lambda: rec_F(n), number=10)
        t_it = timeit.timeit(lambda: iter_F(n), number=10)
        results.append((n, t_rec, t_it))

    # таблица
    df = DataFrame(results, columns=['n', 'Recursive Time (s)', 'Iterative Time (s)'])
    print(df.to_string(index=False))

    # график
    plt.figure(figsize=(8, 5))
    plt.plot(df['n'], df['Recursive Time (s)'], '--o', label='Recursive')
    plt.plot(df['n'], df['Iterative Time (s)'], '-o', label='Iterative')
    plt.xlabel('n')
    plt.ylabel('Time (s)')
    plt.title('Сравнение времени: рекурсия vs итерация для F(n)')
    plt.legend()
    plt.grid(True)
    plt.show()
