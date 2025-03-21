"""
Logistic映射与混沌系统研究
"""

import numpy as np
import matplotlib.pyplot as plt

def iterate_logistic(r, x0, n):
    """
    迭代Logistic映射
    
    参数:
        r: 增长率参数
        x0: 初始值
        n: 迭代次数
        
    返回:
        x: 迭代序列数组
    """
    pass
fjhfgkgk

def plot_time_series(r, x0, n):
    """
    绘制时间序列图
    
    参数:
        r: 增长率参数
        x0: 初始值
        n: 迭代次数
        
    返回:
        fig: matplotlib图像对象
    """
    pass

def plot_bifurcation(r_min, r_max, n_r, n_iterations, n_discard):
   r = np.linspace(r_min, r_max, n_r)
    x = np.zeros(n_iterations)
    x_plot = []
    r_plot = []
    
    for r_val in r:
        x[0] = 0.5
        for i in range(1, n_iterations):
            x[i] = r_val * x[i-1] * (1 - x[i-1])
        
        # 只保留稳定后的点
        x_plot.extend(x[n_discard:])
        r_plot.extend([r_val] * (n_iterations - n_discard))
    
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.plot(r_plot, x_plot, ',k', alpha=0.1, markersize=0.1)
    ax.set_xlabel('r')
    ax.set_ylabel('x')
    ax.set_title('Logistic映射分岔图')
    
    return fig

def main():
    """主函数"""
    # 时间序列分析
    r_values = [2.0, 3.2, 3.45, 3.6]
    x0 = 0.5
    n = 100
    
    for r in r_values:
        fig = plot_time_series(r, x0, n)
        fig.savefig(f"logistic_r{r}.png", dpi=300)
        plt.close(fig)
    
    # 分岔图分析
    fig = plot_bifurcation(2.5, 4.0, 1000, 1000, 100)
    fig.savefig("bifurcation.png", dpi=300)
    plt.close(fig)

if __name__ == "__main__":
    main()
