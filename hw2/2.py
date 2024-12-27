def generate_permutations(n):  # 主函數
    result = []  # 用來儲存所有排列結果
    current = []  # 用來儲存當前排列
    used = [False] * n  # 用來標記某數字是否已經被使用過
    backtrack(n, current, used, result)  # 呼叫遞迴函數
    return result

def backtrack(n, current, used, result):  
    if len(current) == n:  # 如果排列的長度等於 n，表示完成一組排列
        result.append(current[:])  # 儲存排列（用切片避免修改）
        return

    for i in range(n):  # 從 0 到 n-1 嘗試每個數字
        if not used[i]:  # 如果這個數字還沒被使用過
            used[i] = True  # 標記這個數字為已使用
            current.append(i)  # 加入當前排列
            backtrack(n, current, used, result)  # 遞迴繼續生成排列
            current.pop()  # 回溯，移除最後一個數字
            used[i] = False  # 將該數字重新標記為未使用

# 測試排列程式
print(generate_permutations(2))  # 列出 2 個數的排列
print(generate_permutations(3))  # 列出 3 個數的排列
