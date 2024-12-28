import heapq  # 使用優先佇列（優化效率）

def dijkstra(graph, start):
    """
    計算從起點 start 到其他所有節點的最短路徑
    graph: 表示圖的鄰接表 (dictionary)，形如 {節點: [(鄰居, 權重), ...]}
    start: 起點節點
    返回: 到每個節點的最短距離字典
    """
    # 儲存最短距離的字典，初始為無窮大
    distances = {node: float('inf') for node in graph}
    distances[start] = 0  # 起點到自身距離為 0

    # 優先佇列，儲存 (距離, 節點) 格式
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # 如果發現當前距離大於已知最短距離，則跳過
        if current_distance > distances[current_node]:
            continue

        # 檢查鄰居節點
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

            # 如果發現更短的路徑，更新距離並加入佇列
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# 測試用例
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 6)],
    'C': [('A', 4), ('B', 2), ('D', 3)],
    'D': [('B', 6), ('C', 3)],
}

start_node = 'A'
shortest_distances = dijkstra(graph, start_node)
print(f"從節點 {start_node} 到其他節點的最短距離: {shortest_distances}")
