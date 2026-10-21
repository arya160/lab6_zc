import random
import matplotlib.pyplot as plt


# Оцінка рішення
def fitness(individual):
    return sum(individual)


# Створення початкової популяції
def create_population(size, bits):
    population = []

    for _ in range(size):
        individual = [random.randint(0, 1) for _ in range(bits)]
        population.append(individual)

    return population


# Вибір кращого з двох випадкових рішень
def selection(population):
    first = random.choice(population)
    second = random.choice(population)

    if fitness(first) > fitness(second):
        return first
    else:
        return second


# Схрещування двох рішень
def crossover(parent1, parent2):
    point = random.randint(1, len(parent1) - 1)

    child = parent1[:point] + parent2[point:]

    return child


# Мутація
def mutation(individual, mutation_rate):
    for i in range(len(individual)):
        if random.random() < mutation_rate:
            individual[i] = 1 - individual[i]

    return individual


# Основний генетичний алгоритм
def genetic_algorithm():

    history = []

    population_size = 20
    bits = 10
    generations = 30
    mutation_rate = 0.1

    population = create_population(population_size, bits)

    for generation in range(generations):

        new_population = []

        for _ in range(population_size):

            parent1 = selection(population)
            parent2 = selection(population)

            child = crossover(parent1, parent2)

            child = mutation(child, mutation_rate)

            new_population.append(child)

        population = new_population

        best = max(population, key=fitness)

        # Записуємо найкращу оцінку кожного покоління
        history.append(fitness(best))

        print(
            "Покоління:", generation + 1,
            "Найкраще рішення:", best,
            "Оцінка:", fitness(best)
        )

        if fitness(best) == bits:
            print("Оптимальне рішення знайдено!")
            break

    best = max(population, key=fitness)

    print("\nНайкраще знайдене рішення:", best)
    print("Його оцінка:", fitness(best))

    # Побудова графіка
    plt.plot(range(1, len(history) + 1), history, marker="o")
    plt.xlabel("Покоління")
    plt.ylabel("Найкраща оцінка")
    plt.title("Робота генетичного алгоритму")
    plt.grid()
    plt.show()


genetic_algorithm()