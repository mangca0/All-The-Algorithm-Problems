import numpy as np
import random
import matplotlib.pyplot as plt
import pandas as pd

def get_vaccine_data(avg):
    """
    使用Excel中读取的实际疫苗生产时间数据
    """
    # 创建疫苗种类编号（0-9，对应10种疫苗）
    vaccine_types = np.arange(10)

    # 组合数据：第一行是疫苗编号，后面是生产时间数据
    data = np.vstack((vaccine_types, avg.T))
    return data

def produceData(n=10, m=4, low=None, high=None):
    """
    使用实际疫苗生产数据
    n: 疫苗种类数量（10种）
    m: 工位数量（4个工位）
    """
    # 1. 读取数据
    df = pd.read_excel("data.xlsx", sheet_name="Sheet2", header=None)

    # 2. 去掉第一行（标题行）
    df = df.iloc[1:]

    # 3. 将第三列的数据转换为数值类型并重塑为10x4矩阵
    avg = df[2].astype(float).values.reshape(10, 4)

    return get_vaccine_data(avg)

def makespan(data):
    """
    每个工件在每台机器上的完成时间
    :param data: m行n列，第1行工序编号，值加工时间
    """
    makespan = np.zeros_like(data)
    for i in range(makespan.shape[0]):
        for j in range(makespan.shape[1]):
            if i == 0:
                makespan[i, j] = data[i, j]
            if i == 1:
                makespan[i, j] = np.sum(data[1, :j + 1])
            if j == 0 and i != 0:
                makespan[i, j] = np.sum(data[1:i + 1, j])
    for i in range(2, makespan.shape[0]):
        for j in range(1, makespan.shape[1]):
            makespan[i, j] = data[i, j] + max(makespan[i, j - 1], makespan[i - 1, j])
    return makespan


def makespan_value(data):
    """
    最大生产流程时间
    :param data: m行n列，第1行工序编号，值加工时间
    """
    makespan_value = makespan(data)[-1, -1]
    return makespan_value


# 生成初始种群
def johnson(data):
    # 分组
    P = data[:, np.where(data[1] < data[2])[0]]
    Q = data[:, np.where(data[1] >= data[2])[0]]
    # 排序
    P = P[:, np.argsort(P[1])]
    Q = Q[:, np.argsort(-Q[2])]
    # 组合
    sequence = np.hstack([P[0], Q[0]])
    return sequence


def cds(data):
    # 分组，将m台机器的问题分解为为m-1组两机器的问题
    data_group = np.zeros([data.shape[0] - 2, 3, data.shape[1]])
    for i in range(data_group.shape[0]):
        data_group[i, 0] = data[0]
        for j in range(data.shape[1]):
            data_group[i, 1, j] = np.sum(data[1:i + 2, j])
            data_group[i, 2, j] = np.sum(data[-i - 1:, j])
    # 对每组分别运用johnson算法，找到每组的最优排列
    data_johnson = np.zeros([data_group.shape[0], data_group.shape[2]])
    for i in range(data_group.shape[0]):
        data_johnson[i] = johnson(data_group[i])
    sequences = np.array(data_johnson, dtype=int)
    return sequences


def ra(data):
    # 分组，将原问题转化为一个双机调度问题
    group_data = np.zeros([3, data.shape[1]], dtype=data.dtype)
    group_data[0] = data[0]
    for i in range(1, data.shape[0]):
        for j in range(data.shape[1]):
            group_data[1, j] += (data.shape[0] - i) * data[i, j]
            group_data[2, j] += i * data[i, j]
    # 运用johnson算法找到最优排列
    ra_data = johnson(group_data)
    return ra_data


def exchangeMutation(individual):
    mutated_individual = individual.copy()
    pos1, pos2 = random.sample(range(len(individual)), 2)  # 随机选取两个交换点
    mutated_individual[pos1], mutated_individual[pos2] = mutated_individual[pos2], mutated_individual[pos1]  # 交换基因
    return mutated_individual


def generatePopulation(popSize, data):
    pop = np.zeros([popSize, data.shape[1]], dtype=int)
    machineNum = data.shape[0] - 1  # 机器数
    pop[:machineNum - 1] = cds(data)  # 使用cds方法生成前m-1个
    pop[machineNum - 1] = ra(data)  # 使用ra方法生成第m个
    for i in range(popSize - machineNum):  # 剩下的个体从已经生成的个体中随机选择然后进行交换变异产生
        a = random.randint(0, machineNum - 1)
        pop[machineNum] = exchangeMutation(pop[a])
        machineNum += 1
    return pop


# 适应度函数
def fitness(popSize, data, pop):
    fitness = np.zeros([popSize, 1])
    makeSpan = np.zeros([popSize, 1])
    for i in range(popSize):
        makeSpan[i] = makespan_value(data[:, pop[i]])
    max_makeSpan = np.max(makeSpan)  # 计算每代种群中最大的最大完工时间
    for i in range(popSize):
        fitness[i] = max_makeSpan - makeSpan[i]
    return fitness


# 选择操作
def select(popSize, fitness):
    '''
    比例选择
    '''
    selectProbability = np.zeros([popSize, 1])
    totalFitness = np.sum(fitness)
    for i in range(popSize):
        selectProbability[i] = fitness[i] / totalFitness  # 最大完工时间越小的个体被选中的概率越大
    selectProbability_1d = selectProbability.flatten()  # 降维
    return selectProbability_1d


# 交叉操作
def lox(parents):
    '''
    线性次序交叉（LOX）
    '''
    parent1 = parents[0]
    parent2 = parents[1]
    # 随机生成两个交叉点
    size = len(parent1)
    crossoverPoints = sorted(np.random.choice(size, 2, replace=False))
    # 初始化子代
    child1 = np.full(size, -1, dtype=int)
    child2 = np.full(size, -1, dtype=int)
    # 复制交叉点之间的片段到子代
    child1[crossoverPoints[0]:crossoverPoints[1]] = parent2[crossoverPoints[0]:crossoverPoints[1]]
    child2[crossoverPoints[0]:crossoverPoints[1]] = parent1[crossoverPoints[0]:crossoverPoints[1]]
    # 填充剩余的位置
    pointer1 = crossoverPoints[1]
    pointer2 = crossoverPoints[1]
    for i in range(size):
        if parent1[i] not in child1:
            child1[pointer1] = parent1[i]
            pointer1 = (pointer1 + 1) % size
        if parent2[i] not in child2:
            child2[pointer2] = parent2[i]
            pointer2 = (pointer2 + 1) % size
    return child1, child2


def crossover(popSize, pop, fitness, Pc):
    pop_children = pop.copy()
    selectProbability = select(popSize, fitness)  # 种群中每个个体被选中的概率
    individualNum = 0
    while individualNum < popSize - 2:
        if random.random() < Pc:
            parents_indices = np.random.choice(popSize, size=2, replace=False,
                                               p=selectProbability)  # 依据概率随机选择两个进行交叉的父代个体
            parents = pop[parents_indices]
            children = lox(parents)
            pop_children[individualNum] = children[0]
            pop_children[individualNum + 1] = children[1]
            individualNum += 2
    return pop_children


# 变异操作
def shiftMutation(individual, Pm):
    '''
    移位变异操作
    '''
    mutated_individual = individual.copy()  # 复制输入个体以防止修改原始个体
    for i in range(len(mutated_individual)):  # 对于个体中的每个基因都有Pm的变异概率
        if random.random() < Pm:
            index = random.randint(0, len(mutated_individual) - 1)  # 随机选择一个基因的位置
            # 移位操作
            gene = mutated_individual[i]  # 被移位的基因
            mutated_individual = np.delete(mutated_individual, i)  # 从当前位置移除元素
            mutated_individual = np.insert(mutated_individual, index, gene)  # 插入元素到新位置
    return mutated_individual


def mutation(pop, popSize, Pm):
    # 对种群中的每一个个体运用移位变异操作
    for i in range(popSize):
        pop[i] = shiftMutation(pop[i], Pm)
    return pop


def elite_reserved(fitness, pop, data):
    '''
    精英保留策略
    '''
    elite_population = np.zeros([2, data.shape[1]], dtype=int)
    # 选取出种群中适应度最大的两个个体
    elite_indices = np.argsort(fitness[:, 0])[-2:]
    elite_individuals = [pop[i] for i in elite_indices]
    elite_population[0] = elite_individuals[0]
    elite_population[1] = elite_individuals[1]
    return elite_population


# 遗传算法运行参数
popSize = 100  # 种群规模
generation = 100  # 迭代次数 100
Pc = 1  # 交叉概率 1
Pm = 0.05  # 变异概率 0.05
np.random.seed(1)  # 设置随机种子
produceTime = produceData(10, 10, 1, 99)  # 每个工件在各台机器上的加工时间
population = generatePopulation(popSize, produceTime)  # 初始种群

# 遗传算法主程序
pop_trace = np.zeros([generation, 3])
individual_trace = np.zeros([generation, produceTime.shape[1]], dtype=int)
best_times = []
for g in range(generation):
    fitness_value = fitness(popSize, produceTime, population)  # 计算各个个体的适应度
    elite_population = elite_reserved(fitness_value, population, produceTime)  # 保留下每一代中的精英个体
    pop_trace[g] = [g, np.mean(fitness_value), np.max(fitness_value)]  # 记录下每一代种群的平均适应度和最大适应度
    individual_trace[g] = population[np.argmax(fitness_value)]  # 记录下每代群体中适应度最大的个体
    crossover_children = crossover(popSize, population, fitness_value, Pc)  # 对种群进行交叉操作
    population = mutation(crossover_children, popSize, Pm)  # 对种群进行变异操作
    # 将保留下来的精英个体直接保存到下一代种群中
    population[popSize - 2] = elite_population[0]
    population[popSize - 1] = elite_population[1]
    best_time = makespan_value(produceTime[:, individual_trace[g]])  # 计算每代群体中适应度最大的个体的最大完工时间
    best_times.append(best_time)
    print(f'第{g + 1}代的工件加工次序为：{individual_trace[g]}，最大完工时间为：{best_time}')
best_individual = individual_trace[np.argmin(best_times)]
print("最优的工件加工次序为：", best_individual, end='，')
print("最小的最大完工时间为：", makespan_value(produceTime[:, best_individual]))

# 画迭代图
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

plt.plot(range(1, generation + 1), best_times)
plt.xlabel('迭代次数')
plt.ylabel('最大完工时间')
plt.title('优化过程', fontsize=15)
plt.show()
