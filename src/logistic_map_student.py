"""
Logistic映射与混沌系统研究
"""



import numpy as np
import matplotlib.pyplot as plt


def logistic_iteration(r, x0, num_iter):
    """
    此函数用于执行Logistic模型的迭代计算
    :param r: 参数r
    :param x0: 初始值
    :param num_iter: 迭代次数
    :return: 每次迭代后的x值数组
    """
    x = np.zeros(num_iter)
    x[0] = x0
    for i in range(1, num_iter):
        x[i] = r * x[i - 1] * (1 - x[i - 1])
    return x


# 任务1：Logistic模型的迭代
r_values = [2, 3.2, 3.45, 3.6]
x0 = 0.5
num_iter = 60

plt.figure(figsize=(12, 8))
for i, r in enumerate(r_values):
    x = logistic_iteration(r, x0, num_iter)
    plt.subplot(2, 2, i + 1)
    plt.plot(range(num_iter), x)
    plt.title(f'r = {r}')
    plt.xlabel('迭代次数')
    plt.ylabel('x')

    if r == 2:
        print(f"当 r = {r} 时，x 趋于 {x[-1]}，没有分岔。")
    elif r == 3.2:
        stable_values = np.unique(np.round(x[-20:], 5))
        print(f"当 r = {r} 时，x 趋于 {stable_values}，周期2分岔。")
    elif r == 3.45:
        stable_values = np.unique(np.round(x[-20:], 5))
        print(f"当 r = {r} 时，x 趋于 {stable_values}，周期4分岔。")
    elif r == 3.6:
        print(f"当 r = {r} 时，x 的取值没有明确趋向，混沌。")

plt.tight_layout()
plt.show()

# 任务2：费根鲍姆图的绘制
r_range = np.arange(2.6, 4, 0.001)
x0 = 0.5
num_iter = 250
transient = 100

x_values = []
for r in r_range:
    x = logistic_iteration(r, x0, num_iter)
    x_values.append(x[transient:])

plt.figure(figsize=(12, 8))
for i, r in enumerate(r_range):
    plt.scatter([r] * len(x_values[i]), x_values[i], s=0.1, color='k')

plt.title('费根鲍姆图')
plt.xlabel('r')
plt.ylabel('x')
plt.show()



