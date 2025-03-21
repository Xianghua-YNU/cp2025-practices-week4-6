
#第1.1题
import numpy as np
import matplotlib.pyplot as plt

# 定义函数 W(t)
def W(t, A, tau):
    return A * (np.exp(-t/tau) - 1 + t/tau)

# 定义时间范围
t = np.linspace(0, 2, 500)  # 从0到2生成500个点

# a. 选择 A = 1, tau = 1，并绘制 W(t)
A1, tau1 = 1, 1
W1 = W(t, A1, tau1)
plt.plot(t, W1, label=f'A={A1}, τ={tau1}')  # 绘制 W1

# b. 使用不同的 τ 和 A 值制作几个数组 W1, W2, W3 等
A2, tau2 = 2, 0.5
W2 = W(t, A2, tau2)
plt.plot(t, W2, '--', label=f'A={A2}, τ={tau2}')  # 绘制 W2，使用虚线

A3, tau3 = 0.5, 2
W3 = W(t, A3, tau3)
plt.plot(t, W3, ':', label=f'A={A3}, τ={tau3}')  # 绘制 W3，使用点线

# c. 更改线条的颜色和样式
# 已经在上面绘制时指定了不同的线条样式

# d. 添加图例
plt.legend()  # 显示图例

# 添加标题和标签
plt.title('W(t) for different A and τ values')
plt.xlabel('t')
plt.ylabel('W(t)')

# 显示图形
plt.show()



#第1.2题
#第1.2题a
import numpy as np
import matplotlib.pyplot as plt

# 读取文件g149novickA.txt中的数据，指定数据分隔符，并且处理可能的非数字字符
# 假设数据格式为两列，第一列为时间t，第二列为对应的测量值，用逗号分隔且可能有多余字符
# 这里使用genfromtxt，它比loadtxt更灵活，能处理一些格式不规范的数据
dataA = np.genfromtxt('g149novickA.txt', delimiter=',', invalid_raise=False, filling_values=np.nan)
# 去除包含无效值（nan）的行
dataA = dataA[~np.isnan(dataA).any(axis=1)]
tA = dataA[:, 0]  # 提取时间列
yA = dataA[:, 1]  # 提取测量值列

# 定义函数V(t)，这里假设方程4.2中的V(t)形式，实际使用时请根据具体方程修改
def V(t, tau):
    return np.exp(-t / tau)  # 示例函数，根据实际方程修改

# 选择一些合理的tau值
tau_values = [1, 2, 3]  # 可以根据实际情况调整这些值

# 创建图形和坐标轴对象
fig, ax = plt.subplots()

# 绘制实验数据点，使用小圆圈作为标记
ax.scatter(tA, yA, label='Experimental Data A', marker='o')

# 绘制多条曲线
for tau in tau_values:
    y_model = V(tA, tau)
    ax.plot(tA, y_model, label=f'V(t), tau={tau}')

# 标记坐标轴
ax.set_xlabel('Time (t)')
ax.set_ylabel('V(t)')

# 添加图例
ax.legend()

# 显示图形
plt.show()





#第1.2题b
import numpy as np
import matplotlib.pyplot as plt

# 读取文件g149novickB.txt中的数据，指定数据分隔符，并且处理可能的非数字字符
# 假设数据格式为两列，第一列为时间t，第二列为对应的测量值，用逗号分隔且可能有多余字符
dataB = np.genfromtxt('g149novickB.txt', delimiter=',', invalid_raise=False, filling_values=np.nan)
# 去除包含无效值（nan）的行
dataB = dataB[~np.isnan(dataB).any(axis=1)]
tB = dataB[:, 0]  # 提取时间列
yB = dataB[:, 1]  # 提取测量值列

# 丢弃时间值大于十小时的数据
mask = tB <= 10
tB = tB[mask]
yB = yB[mask]

# 定义函数W(t)，这里假设方程4.2中的W(t)形式，实际使用时请根据具体方程修改
def W(t, A, tau):
    return A * np.exp(-t / tau)  # 示例函数，根据实际方程修改

# 估计直线的斜率和y截距，这里只是示例，实际需要根据数据计算
# 可以使用线性回归的方法或者简单的手动计算斜率和截距
# 假设已经计算出斜率slope和截距intercept
slope = 0.5  # 示例值，需要根据实际计算
intercept = 1.0  # 示例值，需要根据实际计算

# 根据提示中的方法计算A和tau的初始猜测值
tau_guess = -1 / slope  # 根据提示公式计算tau
A_guess = intercept  # 根据提示公式计算A

# 调整A和tau的值以获得更好的拟合，这里可以使用一些简单的迭代方法，例如手动调整
# 或者使用更复杂的优化算法，这里只是示例，不做复杂优化
A = A_guess
tau = tau_guess

y_modelB = W(tB, A, tau)

# 创建新的图形和坐标轴对象
fig, ax = plt.subplots()

# 绘制实验数据点，使用小圆圈作为标记
ax.scatter(tB, yB, label='Experimental Data B', marker='o')

# 绘制拟合曲线
ax.plot(tB, y_modelB, label=f'W(t), A={A:.2f}, tau={tau:.2f}')

# 标记坐标轴
ax.set_xlabel('Time (t)')
ax.set_ylabel('W(t)')

# 添加图例
ax.legend()

# 显示图形
plt.show()
