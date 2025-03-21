import numpy as np
import matplotlib.pyplot as plt
import pandas as pd  # 用于读取Excel文件

class HIVModel:
    def __init__(self, A, alpha, B, beta):
        # 初始化模型参数
        self.A = A
        self.alpha = alpha
        self.B = B
        self.beta = beta

    def viral_load(self, time):
        # 计算病毒载量
        return self.A * np.exp(-self.alpha * time) + self.B * np.exp(-self.beta * time)

    def plot_model(self, time):
        # 绘制模型曲线
        viral_load = self.viral_load(time)
        plt.plot(time, viral_load, label='Model')


def load_hiv_data(filepath):
    try:
        # 从Excel文件中读取数据
        df = pd.read_excel(filepath)
        time_in_days = df.iloc[:, 0].values  # 假设第一列是时间
        viral_load = df.iloc[:, 1].values  # 假设第二列是病毒载量
        return time_in_days, viral_load
    except FileNotFoundError:
        print(f"文件 {filepath} 未找到，请检查路径。")
        return np.array([]), np.array([])


def main():
    # 生成时间序列
    time = np.linspace(0, 1, 11)

    # 探索模型，使用不同参数
    parameters = [
        (1, 1, 0, 2),
        (2, 0.5, 0, 1.5),
        (3, 0.2, 0, 1),
        (4, 0.1, 0, 0.5)
    ]

    for A, alpha, B, beta in parameters:
        model = HIVModel(A, alpha, B, beta)
        model.plot_model(time)

    plt.xlabel('Time')
    plt.ylabel('Viral Load')
    plt.title('HIV Viral Load Model Exploration')
    plt.legend()
    plt.show()

    # 加载实验数据
    filepath = r'D:\LenovoSoftstore\Install\ana\envs\hiv.xlsx'  # 假设文件名为hiv.xlsx
    time_in_days, viral_load = load_hiv_data(filepath)

    if len(time_in_days) > 0 and len(viral_load) > 0:
        # 可视化实验数据
        plt.figure()
        plt.scatter(time_in_days, viral_load, marker='o', label='Experimental Data')
        plt.xlabel('Days since treatment')
        plt.ylabel('Viral Load (arbitrary units)')
        plt.title('HIV Viral Load Experimental Data')
        plt.legend()
        plt.show()

        # 叠加模型和实验数据
        plt.figure()
        # 这里可以手动调整参数，先使用一组示例参数
        A, alpha, B, beta = 1000, 0.1, 100, 0.2
        model = HIVModel(A, alpha, B, beta)
        model.plot_model(time_in_days)
        plt.scatter(time_in_days, viral_load, marker='o', label='Experimental Data')
        plt.xlabel('Days since treatment')
        plt.ylabel('Viral Load (arbitrary units)')
        plt.title('HIV Viral Load Model vs Experimental Data')
        plt.legend()
        plt.show()

        # 分析初始值和长期行为
        # 初始值 V(0) = A + B
        # 长期行为：当 t 很大时，因为 β > α，exp(-βt) 比 exp(-αt) 更快趋近于 0，所以 V(t) 近似为 A * exp(-αt)
        # 可以根据实验数据的初始值确定 A + B 的值，根据长期数据确定 A 和 α 的值
        # 这里假设已经确定了 A 和 α 的值，只调整 B 和 β
        A = 1000
        alpha = 0.1
        B = 100
        beta = 0.2
        # 可以通过循环手动调整 B 和 β，直到满意为止
        for _ in range(10):
            model = HIVModel(A, alpha, B, beta)
            plt.figure()
            model.plot_model(time_in_days)
            plt.scatter(time_in_days, viral_load, marker='o', label='Experimental Data')
            plt.xlabel('Days since treatment')
            plt.ylabel('Viral Load (arbitrary units)')
            plt.title('HIV Viral Load Model vs Experimental Data')
            plt.legend()
            plt.show()
            # 这里可以根据图像手动调整 B 和 β 的值
            B += 10
            beta += 0.01

        # 计算 T 细胞感染率的倒数 1/α
        inverse_alpha = 1 / alpha
        hiv_latency = 10 * 365  # 十年换算成天数
        print(f"T细胞感染率的倒数 1/α 为 {inverse_alpha} 天，HIV潜伏期约为 {hiv_latency} 天。")


if __name__ == "__main__":
    main()
