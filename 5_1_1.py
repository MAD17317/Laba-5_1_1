import time
K = int(input("Введите количество членов комиссии (K): "))
def generate_combinations():
    members = list(range(1, K + 1))
    print("\nВсе возможные варианты:")
    for chair in members:
        for deputy in members:
            if deputy != chair:
                print(f"Председатель: {chair}, Заместитель: {deputy}")
    total = K * (K - 1)
    end = time.time()
    print(f"\nВсего вариантов: {total}")
    print(f"Время выполнения: {end - start:.5f} секунд")
start = time.time()
generate_combinations()
