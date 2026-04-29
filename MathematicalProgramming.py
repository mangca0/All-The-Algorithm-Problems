from scipy.optimize import linprog
from scipy.optimize import minimize
from pulp import LpMaximize, LpProblem, LpVariable, LpMinimize


def func1():
    '''
    用linprog函数做线性规划
    :return:
    '''
    # 定义目标函数的系数
    c = [-2, -3, 5]

    # 定义不等式约束条件的系数矩阵
    A = [[-2, 5, -1],
         [1, 3, 1],]

    # 定义不等式约束条件的右侧向量
    b = [-10, 12]
    # b = [[-10], [12]]

    # 请自己完成 Aeq beq
    Aeq = [[1,1,1]]
    beq = [7]

    # 定义变量的边界 None表示无穷
    x1_bounds = (0, None)  # 对 x1 的边界
    x2_bounds = (0, None)  # 对 x2 的边界
    x3_bounds = (0, None)  # 对 x3 的边界

    # 使用 linprog 函数进行线性规划
    res = linprog(c, A_ub=A, b_ub=b, A_eq=Aeq, b_eq=beq,bounds=[x1_bounds, x2_bounds, x3_bounds], method='highs')

    # 打印结果
    print('最小值:', res.fun)
    print('最优解:', res.x)

def func2():
    '''
    用minimize函数做线性规划
    :return:
    '''
    # 定义目标函数的系数
    c = [-2, -3, 5]

    # 定义等式约束条件的函数
    def eq_constraint(x):
        return x[0] + x[1] + x[2] - 7

    # 定义不等式约束条件的函数
    def ineq_constraints(x):
        return [-2*x[0] + 5*x[1] - x[2] + 10,  # -2*x1 + 5*x2 - x3 >= -10 这个部分课上说错了，请注意
                x[0] + 3*x[1] + x[2] - 12]  # x1 + 3*x2 + x3 >= 12


    # 定义变量的边界
    bounds = [(0, None), (0, None), (0, None)]  # 对 x1 和 x2 的边界

    # 初始猜测值
    x0 = [0, 0, 0]

    # lambda = ff
    # def ff(x):a
    #     return c[0] * x[0] + c[1] * x[1] + c[2] * x[2]func

    # 使用 minimize 函数进行线性规划
    res = minimize(lambda x: c[0] * x[0] + c[1] * x[1] + c[2] * x[2], x0,
                   constraints=[{'type': 'eq', 'fun': eq_constraint},
                                {'type': 'ineq', 'fun': ineq_constraints}],
                   bounds=bounds,
                   method='SLSQP') #它提供了多种求解算法，如highs、SLSQP、COBYLA、L-BFGS-B等，你可以试试有什么效果

    # 打印结果
    print('最小值:', res.fun)
    print('最优解:', res.x)

def func6():
    '''
    整数规划
    :return:
    '''
    # 整数规划：创建一个LP问题，最大化问题
    problem = LpProblem("Integer Optimization Problem", LpMaximize)

    # 定义变量
    x = LpVariable("x", lowBound=0, cat='Integer')  # 整数变量
    y = LpVariable("y", lowBound=0, cat='Integer')  # 整数变量

    # 定义目标函数
    problem += 2 * x + 3 * y, "Objective Function" # problem = problem + 2x +3y

    # 添加约束条件
    problem += x + 2 * y <= 7
    problem += 3 * x - y <= 9

    # 解决问题
    problem.solve()

    # 打印结果
    print("最优解:")
    print("x =", x.value())
    print("y =", y.value())
    print("最优值:", problem.objective.value())

def funcc6():
    '''
    整数规划
    :return:
    '''
    # 整数规划：创建一个LP问题，最小化问题
    problem = LpProblem("Integer Optimization Problem", LpMinimize)

    # 定义变量
    x1 = LpVariable("x1", lowBound=0, cat='Integer')  # 整数变量
    x2 = LpVariable("x2", lowBound=0, cat='Integer')  # 整数变量
    x3 = LpVariable("x3", lowBound=0, cat='Integer')  # 整数变量
    x4 = LpVariable("x4", lowBound=0, cat='Integer')  # 整数变量
    x5 = LpVariable("x5", lowBound=0, cat='Integer')  # 整数变量
    x6 = LpVariable("x6", lowBound=0, cat='Integer')  # 整数变量

    # 定义目标函数
    problem += x1 + x2 + x3 + x4 + x5 + x6, "Objective Function"

    # 添加约束条件
    problem += x1 + x2 + x3 >= 1
    problem += x4 + x6 >= 1
    problem += x3 + x5 >= 1
    problem += x2 + x4 >= 1
    problem += x5 + x6 >= 1
    problem += x1 >= 1
    problem += x2 + x4 + x6 >= 1

    # 解决问题
    problem.solve()

    # 打印结果
    print("最优解:")
    print(f"x1 = {x1.varValue}")
    print(f"x2 = {x2.varValue}")
    print(f"x3 = {x3.varValue}")
    print(f"x4 = {x4.varValue}")
    print(f"x5 = {x5.varValue}")
    print(f"x6 = {x6.varValue}")
    print("最优值:", problem.objective.value())

def func7():
    '''
    非线性规划
    :return:
    '''
    # 定义目标函数
    def objective_function(x):
        return x[0] ** 2 + x[1] ** 2 + x[2] ** 2 + 8

    # 初始猜测值
    x0 = [0, 0, 0]

    # 定义约束条件
    constraints = ({'type': 'ineq', 'fun': lambda x: x[0] - 2 * x[1] + 2},
                   {'type': 'ineq', 'fun': lambda x: -x[0] - 2 * x[1] + 6},
                   {'type': 'ineq', 'fun': lambda x: -x[0] + 2 * x[1] + 2})

    # 求解非线性规划问题
    res = minimize(objective_function, x0, constraints=constraints)

    # 打印结果
    print('最小值:', res.fun)
    print('最优解:', res.x)

if __name__ == '__main__':
    funcc6()