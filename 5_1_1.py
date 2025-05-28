import time
K = int(input("Введите количество членов комиссии (K): "))
def generate_chair_deputy_combinations():
    members = list(range(1, K + 1))
    print("\nВсе возможные варианты:")
    for chair in members:
        for deputy in members:
            if deputy != chair:
                print(f"Председатель: {chair}, Заместитель: {deputy}")
    total = K * (K - 1)
    print(f"\nВсего вариантов: {total}")
start = time.time()
generate_chair_deputy_combinations()
end = time.time()
print(f"Время выполнения: {end - start:.5f} секунд")