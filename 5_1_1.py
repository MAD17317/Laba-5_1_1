import time
from itertools import permutations
K = int(input("Введите количество членов комиссии (K): "))
def algoritm():
    members = list(range(1, K + 1))
    print("\nВсе возможные варианты:")
    for chair in members:
        for deputy in members:
            if deputy != chair:
                print(f"Председатель: {chair}, Заместитель: {deputy}")
    total = K * (K - 1)
    print(f"\nВсего вариантов: {total}")
start1 = time.time()
algoritm()
end1 = time.time()
print(f"Время выполнения: {end1-start1:.5f} секунд")
time1 = end1 - start1
def function():
    members = list(range(1, K + 1))
    all_pairs = permutations(members, 2)
    print("\nВсе возможные варианты:")
    for chair, deputy in all_pairs:
        print(f"Председатель: {chair}, Заместитель: {deputy}")
    total = K * (K - 1)
    print(f"\nВсего вариантов: {total}")
start2 = time.time()
function()
end2 = time.time()
print(f"Время выполнения: {end2-start2:.5f} секунд")
time2 = end2 - start2
if time1<time2: print('Алгоритмический способ быстрее')
else: print('Алгоритмический способ дольше')
