#黎曼積分法


def riemann_integral(num_points=100):
    dx = 1 / num_points
    dy = 1 / num_points
    dz = 1 / num_points
    result = 0

    for i in range(num_points):
        for j in range(num_points):
            for k in range(num_points):
                # 計算 x, y, z 的位置（使用左端點）
                x = i * dx
                y = j * dy
                z = k * dz
                # 函數值
                f = 3 * x**2 + y**2 + 2 * z**2
                # 加總體積
                result += f * dx * dy * dz
    
    return result

# 測試
riemann_result = riemann_integral(num_points=100)
print(f"黎曼積分結果: {riemann_result}")


