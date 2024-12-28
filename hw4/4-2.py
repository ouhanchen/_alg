#蒙地卡羅方法

import numpy as np

def monte_carlo_integral(num_samples=100000):
    # 隨機生成 x, y, z，均勻分佈於 [0, 1]
    x = np.random.uniform(0, 1, num_samples)
    z = np.random.uniform(0, 1, num_samples)
    # 計算函數值
    f = 3 * x**2 + y**2 + 2 * z**2
    # 取平均值並乘以區域體積 (1^3 = 1)
    result = np.mean(f)
    return result

# 測試
monte_carlo_result = monte_carlo_integral(num_samples=100000)
print(f"蒙地卡羅積分結果: {monte_carlo_result}")