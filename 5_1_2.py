import time
from itertools import permutations
K = int(input("Введите количество членов комиссии (K): "))
def generate_chair_deputy_combinations():
    members = list(range(1, K + 1))
    all_pairs = permutations(members, 2)
    print("\nВсе возможные варианты:")
    for chair, deputy in all_pairs:
        print(f"Председатель: {chair}, Заместитель: {deputy}")
    total = K * (K - 1)
    print(f"\nВсего вариантов: {total}")
start = time.time()
generate_chair_deputy_combinations()
end = time.time()
print(f"Время выполнения: {end - start:.5f} секунд")