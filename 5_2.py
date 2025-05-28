from itertools import permutations
import random
a=[]
K = int(input("Введите количество членов комиссии (K): "))
def generate_optimal_pair():
    ratings = {i: random.randint(1, 10) for i in range(1, K + 1)}
    print("Рейтинги членов комиссии:", ratings)
    # Все возможные пары (председатель, заместитель)
    members = list(ratings.keys())
    all_pairs = permutations(members, 2)
    # Фильтрация пар по ограничению (разница рейтингов <= 3)
    filtered_pairs = [
        (chair, deputy)
        for chair, deputy in all_pairs
        if abs(ratings[chair] - ratings[deputy]) <= 3]
    print("\nДопустимые варианты после фильтрации:")
    for chair, deputy in filtered_pairs:
        a.append(f"Председатель: {chair} (рейтинг {ratings[chair]}), Заместитель: {deputy} (рейтинг {ratings[deputy]})")
    for i in a:
        print (i)
    # Нахождение оптимальной пары (максимальная сумма рейтингов)
    if filtered_pairs:
        optimal_pair = max(
            filtered_pairs,
            key=lambda pair: ratings[pair[0]] + ratings[pair[1]])
        chair, deputy = optimal_pair
        total_rating = ratings[chair] + ratings[deputy]
        print(f"\nОптимальная пара: Председатель {chair} (рейтинг {ratings[chair]}), Заместитель {deputy} (рейтинг {ratings[deputy]})")
        print(f"Сумма рейтингов: {total_rating}")
    else:
        print("\nНет допустимых пар по заданным ограничениям.")
generate_optimal_pair()