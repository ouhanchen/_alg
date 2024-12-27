# 方法 d：用遞迴+查表
def power2n_d(n, memo={}):
    # 如果結果已經存在於查表中，直接返回
    if n in memo:
        return memo[n]
    
    # 基本情況
    if n == 0:
        memo[n] = 1
        return 1
    
    # 遞迴計算並存入查表
    memo[n] = 2 * power2n_d(n - 1, memo)
    return memo[n]

# 測試函數
print('power2n_d(40)=', power2n_d(40))