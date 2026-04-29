import numpy as np  # 导入NumPy用于数值计算
import random  # 导入random库用于生成随机数
import matplotlib.pyplot as plt  # 导入Matplotlib用于绘图
import pandas as pd


def fitness(x):
    return (-10 * x[0]) - (np.exp((-x[1] / 10) - x[2]))  # 定义适应度函数，计算给定位置x的适应度值

def initialize_population(pop_size, D, p_low, p_up):
    population = np.random.uniform(low=p_low, high=p_up, size=(pop_size, D))  # 初始化种群，生成随机个体
    return population  # 返回生成的种群

# def selection(population, fitness_values, num_parents):
#     parents = np.zeros((num_parents, population.shape[1]))  # 初始化父代数组
#     for i in range(num_parents):
#         max_fitness_idx = np.argmax(fitness_values)  # 找到适应度值最高的个体索引
#         parents[i, :] = population[max_fitness_idx, :]  # 将适应度值最高的个体加入父代
#         fitness_values[max_fitness_idx] = -99999999999  # 设置适应度值为极小值，确保该个体不再被选择
#     return parents  # 返回选择的父代

def selection(population, fitness_values, num_parents):
    parents = np.zeros((num_parents, population.shape[1]))
    fitness_values_copy = fitness_values.copy()  # 创建适应度值的副本
    for i in range(num_parents):
        max_fitness_idx = np.argmax(fitness_values_copy)  # 使用副本找到最大适应度值的索引
        parents[i, :] = population[max_fitness_idx, :]
        fitness_values_copy[max_fitness_idx] = -99999999999  # 在副本上修改值
    return parents


def crossover(parents, offspring_size):
    offspring = np.zeros(offspring_size)  # 初始化子代数组
    crossover_point = np.uint8(offspring_size[1] / 2)  # 确定交叉点

    for k in range(offspring_size[0]):
        parent1_idx = k % parents.shape[0]  # 选择父代1的索引
        parent2_idx = (k + 1) % parents.shape[0]  # 选择父代2的索引
        offspring[k, 0:crossover_point] = parents[parent1_idx, 0:crossover_point]  # 交叉操作，生成子代
        offspring[k, crossover_point:] = parents[parent2_idx, crossover_point:]

    return offspring  # 返回生成的子代

def mutation(offspring, p_low, p_up, mutation_rate=0.1):
    for idx in range(offspring.shape[0]):
        for _ in range(offspring.shape[1]):
            if random.random() < mutation_rate:  # 如果随机数小于变异率
                offspring[idx, _] = np.random.uniform(p_low[_], p_up[_])  # 随机生成变异基因
    return offspring  # 返回变异后的子代


# def genetic_algorithm(fitness, p_low, p_up, pop_size, num_generations, mutation_rate):
#     D = len(p_low)  # 个体维度
#     population = initialize_population(pop_size, D, p_low, p_up)  # 初始化种群
#     best_outputs = []  # 存储每一代的最优适应度值
#
#     for generation in range(num_generations):
#         fitness_values = np.array([fitness(individual) for individual in population])  # 计算种群中每个个体的适应度值
#         best_outputs.append(np.min(fitness_values))  # 记录当前代的最优适应度值
#         parents = selection(population, fitness_values, num_parents=int(pop_size / 2))  # 选择优秀个体作为父代
#         offspring_crossover = crossover(parents, offspring_size=(pop_size - parents.shape[0], D))  # 交叉操作生成子代
#         offspring_mutation = mutation(offspring_crossover, p_low, p_up, mutation_rate)  # 变异操作生成新个体
#         population[0:parents.shape[0], :] = parents  # 更新种群，将父代保留
#         population[parents.shape[0]:, :] = offspring_mutation  # 更新种群，将新生成的子代加入种群
#
#         print(f"Generation {generation + 1}/{num_generations}, Best Fitness: {best_outputs[-1]}")  # 打印每代的最优适应度值
#
#     plt.plot(best_outputs)  # 绘制收敛过程图
#     plt.xlabel("Generation")
#     plt.ylabel("Objective")
#     plt.title("Genetic Algorithm")
#     plt.show()
#
#     best_idx = np.argmin(fitness_values)  # 找到最优个体的索引
#     return population[best_idx, :], fitness_values[best_idx]  # 返回最优个体的位置和适应度值

def genetic_algorithm(fitness, p_low, p_up, pop_size, num_generations, mutation_rate):
    D = len(p_low)
    population = initialize_population(pop_size, D, p_low, p_up)
    best_outputs = []
    best_solution = None
    best_fitness = float('inf')  # 初始化最优适应度值

    for generation in range(num_generations):
        fitness_values = np.array([fitness(individual) for individual in population])
        current_best_idx = np.argmin(fitness_values)
        current_best_fitness = fitness_values[current_best_idx]

        # 更新全局最优解
        if current_best_fitness < best_fitness:
            best_fitness = current_best_fitness
            best_solution = population[current_best_idx].copy()

        best_outputs.append(current_best_fitness)
        parents = selection(population, fitness_values.copy(), num_parents=int(pop_size / 2))
        offspring_crossover = crossover(parents, offspring_size=(pop_size - parents.shape[0], D))
        offspring_mutation = mutation(offspring_crossover, p_low, p_up, mutation_rate)
        population[0:parents.shape[0], :] = parents
        population[parents.shape[0]:, :] = offspring_mutation

        print(f"Generation {generation + 1}/{num_generations}, Best Fitness: {current_best_fitness}")

    plt.plot(best_outputs)
    plt.xlabel("Generation")
    plt.ylabel("Objective")
    plt.title("Genetic Algorithm")
    plt.show()

    return best_solution, best_fitness

low = [0, 1, 0]  # 定义搜索空间的下限
up = [1, 80, 120]  # 定义搜索空间的上限
pop_size = 50  # 定义种群规模
num_generations = 100  # 定义迭代次数
mutation_rate = 0.1  # 定义变异率

best_pos, best_fit = genetic_algorithm(fitness, low, up, pop_size, num_generations, mutation_rate)  # 运行遗传算法
print(f"Best Position: {best_pos}, Best Fitness: {best_fit}")  # 打印最优个体的位置和适应度值
