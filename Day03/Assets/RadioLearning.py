import numpy as np

# 模拟 1000 个激光雷达点 (x, y, z)
points = np.random.rand(1000, 3)

# 假设机器人的当前位置（质心）
robot_center = np.array([0.5, 0.2, 0.1]) # 形状是 (3,)

# 广播发生在这里！
# points 是 (1000, 3)，robot_center 是 (3,)
# NumPy 自动把 robot_center 想象成 (1000, 3) 的矩阵，每一行都是 [0.5, 0.2, 0.1]
relative_points = points - robot_center

# 高级技巧：强制升维触发广播
# 如果你想给 1000 个点分别乘以 1000 个不同的权重因子
weights = np.random.rand(1000) # 形状是 (1000,)
# weighted_points = points * weights # 报错！(1000,3) 和 (1000,) 不匹配
weighted_points = points * weights[:, np.newaxis] # 完美！(1000,3) * (1000,1) -> (1000,3)

print(f"点云处理完成，形状依然是: {relative_points.shape}")