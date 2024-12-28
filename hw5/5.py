import time

def halting_simulator(program, max_steps=1000):
    """
    模擬停機檢測器：嘗試在有限步驟內判定是否停機
    program: 要檢測的程式（函數）
    max_steps: 最大允許執行的步驟數
    """
    start_time = time.time()

    for step in range(max_steps):
        try:
            if program(step):  # 運行程式，根據輸入步驟檢查停機狀態
                return f"程式在第 {step} 步停機"
        except Exception as e:
            return f"程式出錯，可能停機，錯誤信息: {e}"
    
        # 防止程式執行太久
        if time.time() - start_time > 5:  # 最多執行 5 秒
            return "超過時間限制，無法判定是否停機"

    return "程式可能進入無窮迴圈"

# 測試程式 1: 一定會停機
def test_program1(step):
    if step == 10:  # 當 step == 10 時停止
        return True
    return False

# 測試程式 2: 無窮迴圈
def test_program2(step):
    while True:  # 進入無窮迴圈
        pass

# 測試
print(halting_simulator(test_program1))  # 應該檢測到程式會停機
# print(halting_simulator(test_program2))  # 注意，這可能超時或卡住，建議不直接測試
