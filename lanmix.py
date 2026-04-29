import numpy as np
import random
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import rcParams

# 设置中文字体，例如 SimHei（黑体）
rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体
rcParams['axes.unicode_minus'] = False   # 解决负号显示问题

# 适应度函数，目标是最小化最大生产流程时间
def fitness(schedule, processing_times):
    """
    适应度函数，计算调度方案的 makespan_value。
    :param schedule: 工件调度顺序（如 [0, 1, 2, ..., n-1]）
    :param processing_times: 工件加工时间矩阵
    """
    # 根据调度顺序重新排列加工时间矩阵
    schedule_idx = np.array(schedule) - 1  # 将1-10转换为0-9的索引
    rearranged = processing_times[schedule_idx]
    return makespan_value(rearranged)


# 初始化种群
def initialize_population(pop_size, num_jobs):
    """
    初始化种群，生成随机调度方案。
    :param pop_size: 种群规模
    :param num_jobs: 工件数量
    """
    return [np.array([x+1 for x in np.random.permutation(num_jobs)]) for _ in range(pop_size)]


# 选择父代
def selection(population, fitness_values, num_parents):
    """
    根据适应度值选择父代（贪心选择）。
    """
    parents = []
    sorted_indices = np.argsort(fitness_values)
    for i in range(num_parents):
        parents.append(population[sorted_indices[i]])
    return parents


# 交叉操作
def crossover(parents, offspring_size):
    """
    交叉操作，使用部分映射交叉（PMX）。
    """
    offspring = []
    for k in range(offspring_size[0]):
        parent1 = parents[k % len(parents)]
        parent2 = parents[(k + 1) % len(parents)]

        # 随机选择交叉点
        point1, point2 = sorted(random.sample(range(len(parent1)), 2))
        child = [-1] * len(parent1)

        # 保留 parent1 的部分基因
        child[point1:point2] = parent1[point1:point2]

        # 填充 child 的剩余位置
        for gene in parent2:
            if gene not in child:
                for i in range(len(child)):
                    if child[i] == -1:
                        child[i] = gene
                        break

        offspring.append(child)
    return offspring


# 变异操作
def mutation(offspring, mutation_rate=0.1):
    """
    变异操作，随机交换两个工件的位置。
    """
    for individual in offspring:
        if random.random() < mutation_rate:
            idx1, idx2 = random.sample(range(len(individual)), 2)
            individual[idx1], individual[idx2] = individual[idx2], individual[idx1]
    return offspring


# 遗传算法主函数
def genetic_algorithm(processing_times, pop_size, num_generations, mutation_rate):
    """
    遗传算法优化流水车间调度问题。
    :param processing_times: 工件加工时间矩阵
    :param pop_size: 种群规模
    :param num_generations: 迭代代数
    :param mutation_rate: 变异率
    """
    num_jobs = processing_times.shape[0]
    population = initialize_population(pop_size, num_jobs)
    best_outputs = []
    best_solution = None
    best_fitness = float('inf')  # 初始化最优适应度值

    for generation in range(num_generations):
        # 计算适应度值
        fitness_values = [fitness(individual, processing_times) for individual in population]
        current_best_idx = np.argmin(fitness_values)
        current_best_fitness = fitness_values[current_best_idx]

        # 更新全局最优解
        if current_best_fitness < best_fitness:
            best_fitness = current_best_fitness
            best_solution = population[current_best_idx]

        best_outputs.append(best_fitness)

        # 选择父代
        num_parents = pop_size // 2
        parents = selection(population, fitness_values, num_parents)

        # 生成子代
        offspring_size = (pop_size - len(parents), num_jobs)
        offspring_crossover = crossover(parents, offspring_size)
        offspring_mutation = mutation(offspring_crossover, mutation_rate)

        # 更新种群
        population = parents + offspring_mutation

        print(f"Generation {generation + 1}/{num_generations}, Best Fitness: {current_best_fitness}")

    # 绘制结果
    plt.plot(best_outputs)
    plt.xlabel('迭代次数')
    plt.ylabel('最大完工时间')
    plt.title('优化过程', fontsize=15)
    plt.show()

    return best_solution, best_fitness


# 数据相关函数
def produceData():
    """
    使用实际疫苗生产数据 (10种疫苗, 4个工位)。
    """
    # 此处假设数据在 data.xlsx 文件中，用户根据情况自行修改路径
    df = pd.read_excel("data.xlsx", sheet_name="Sheet2", header=None)
    df = df.iloc[1:]
    avg = df[2].astype(float).values.reshape(10, 4)
    return avg


def makespan(data):
    """
    计算每个工件在每台机器上的完成时间。
    """
    m, n = data.shape
    makespan = np.zeros((m, n))
    for i in range(m):
        for j in range(n):
            if i == 0 and j == 0:
                makespan[i, j] = data[i, j]
            elif i == 0:
                makespan[i, j] = makespan[i, j - 1] + data[i, j]
            elif j == 0:
                makespan[i, j] = makespan[i - 1, j] + data[i, j]
            else:
                makespan[i, j] = max(makespan[i - 1, j], makespan[i, j - 1]) + data[i, j]
    return makespan


def makespan_value(data):
    """
    计算最大生产流程时间。
    """
    return makespan(data)[-1, -1]


# 主程序
if __name__ == "__main__":
    # 读取加工时间数据
    processing_times = produceData()

    # 遗传算法参数
    pop_size = 50
    num_generations = 100
    mutation_rate = 0.1

    # 运行遗传算法
    best_schedule, best_makespan = genetic_algorithm(processing_times, pop_size, num_generations, mutation_rate)
    print(f"最优的工件加工次序为: {best_schedule}")
    print(f"最小的最大完工时间为: {best_makespan}")