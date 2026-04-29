# Day 3 | 线性代数与NumPy

## 概述

理性的数学之美：机器人眼中的世界是数字和矩阵。理解**旋转矩阵**是感知空间的基础。NumPy是感知数据的载体，今天必须熟练掌握矩阵的切片和广播，让数据在你指尖跳舞。

## 今日任务

- **上午**：复习矩阵乘法、坐标系变换矩阵
- **下午**：熟练使用NumPy切片、广播运算
- **晚上**：注册并浏览HuggingFace仓

## 学习笔记

### 上午任务

首先是矩阵乘法。如果我们要计算 $C = A \times B$，你要记住的核心公式是 $C_{ij} = \sum (A_{ik} \times B_{kj})$。从工程角度看，这其实是在做“坐标基的变换”。矩阵 $A$ 的每一行都可以看作是一个观察视角，而矩阵 $B$ 的每一列则是被观察的数据。它们相乘的过程，本质上是将 $B$ 中的向量投影到 $A$ 所定义的空间坐标系中。在机器人控制里，矩阵乘法最关键的特性是**不可交换性**（$AB \neq BA$）。这意味着在三维空间中，如果你先绕 X 轴转 30 度再绕 Y 轴转 30 度，得到的结果和你先绕 Y 轴转再绕 X 轴转是完全不同的。在写代码控制机械臂时，一旦弄反了乘法顺序，机械臂就会像“抽筋”一样飞向完全错误的方向。



接下来说说最核心的**齐次变换矩阵（Homogeneous Transformation Matrix）**。我们通常用一个 $4 \times 4$ 的矩阵来表示机器人的姿态。它的结构非常精妙：左上角的 $3 \times 3$ 区域是**旋转矩阵（Rotation Matrix）**，负责描述机器人的朝向（Orientation）；右上角的 $3 \times 1$ 列向量是**平移向量（Translation Vector）**，负责描述机器人在空间中的具体位置（Position）。

$$T = \begin{bmatrix} R_{3\times3} & t_{3\times1} \\ 0_{1\times3} & 1 \end{bmatrix}$$



为什么要搞出最下面一行 $[0, 0, 0, 1]$ 呢？这是为了实现“仿射变换”的统一。如果没有这一行，旋转是乘法，平移是加法，计算起来非常麻烦。有了齐次坐标，我们只需要把三维坐标 $[x, y, z]$ 后面补一个 $1$ 变成 $[x, y, z, 1]^T$，然后直接用 $P' = T \times P$ 这一套矩阵乘法，就能一次性完成旋转和平移。这种“升维”的思想是现代图形学和机器人学的基石。

---

### 💡 学习方法与工程建议

* **手算一个 $2 \times 2$ 旋转矩阵**：尝试计算把点 $(1, 0)$ 绕原点逆时针旋转 90 度的矩阵运算，这能帮你建立最直观的数感。
* **理解“左乘”与“右乘”**：在机器人建模中，**左乘**（矩阵乘在左边）通常代表相对于**固定坐标系**（世界坐标系）的变换，而**右乘**（矩阵乘在右边）代表相对于**当前自身坐标系**的变换。搞混这个是新手最常犯的错误。
* **关注奇异值**：在后续学习强化学习控制时，你会遇到“奇异点”问题，这往往是因为旋转矩阵在某些角度下失去了自由度（比如万向节死锁），所以我们后来会引入**四元数（Quaternion）**来替代矩阵，但矩阵依然是底层运算的核心。

---

### 下午任务

切片的核心在于 `[start:stop:step]`。在具身智能中，这常用于从传感器流中提取特征。比如，我们拿到一个 $224 \times 224 \times 3$ 的 RGB 图像，但为了加速处理，我们只想看中间区域，或者每隔一个像素采样一次。

下面代码运行时如果有报错将报错全部发给AI

```python
import numpy as np
import matplotlib.pyplot as plt

# 1. 创建一个有特征的“图像”方便观察变化（不仅仅是随机噪声）
# 我们创建一个简单的渐变图
image = np.zeros((224, 224, 3))
for i in range(224):
    image[i, :, 0] = i / 224.0  # 红色通道：纵向渐变
    image[:, i, 1] = i / 224.0  # 绿色通道：横向渐变

# 2. 执行你的 NumPy 变换逻辑
center_crop = image[80:160, 80:160, :]  # 稍微调整范围，让裁剪效果更明显
downsampled = image[::10, ::10, :]     # 每隔10个像素采样，观察像素化效果
flipped_image = image[:, ::-1, :]      # 水平翻转

# 3. 使用 Matplotlib 进行可视化
fig, axes = plt.subplots(1, 4, figsize=(20, 5))

axes[0].imshow(image)
axes[0].set_title("Original (Observation)")

axes[1].imshow(center_crop)
axes[1].set_title("Center Crop (Focus)")

axes[2].imshow(downsampled, interpolation='nearest') # 禁用平滑，看清像素
axes[2].set_title("Downsampled (Efficiency)")

axes[3].imshow(flipped_image)
axes[3].set_title("Flipped (Data Augmentation)")

for ax in axes:
    ax.axis('off')

plt.tight_layout()
plt.show()
```

广播是 NumPy 最迷人也最容易出错的地方。它的规则很简单：如果两个数组的末尾维度（trailing dimension）相同，或者其中一个维度是 1，它们就可以进行运算。在具身智能中，这常用于“去中心化”：比如你有一万个雷达点云坐标，你想让它们集体减去机器人的质心坐标。

```python
# 模拟 1000 个激光雷达点 (x, y, z)
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
```
---

### 💡 学习方法与工程建议

* **形状对齐练习：**：当你遇到 ValueError: operands could not be broadcast together 时，拿出一张纸，把两个数组的 shape 从右往左写下来。只要对应的位置要么相等，要么有一个是 1，就能通。
* **省略号的妙用:”**：如果你在处理强化学习里的 Batch 数据，形状可能是 $(Batch, Time, Height, Width, Channels)$。如果你只想取所有 Batch 和 Time 里的第一个通道，可以写 data[..., 0]，这比写一堆冒号优雅得多。

---


### 晚上任务

如果你把具身智能比作做菜，NumPy 是你的刀工，矩阵是你的菜谱，那么 **Hugging Face (HF)** 就是全球最大的顶级食材超市。

在具身智能领域，HF 不再仅仅是聊聊天模型的地方，它现在是 **VLA（视觉-语言-动作）模型**和**标准化机器人数据集**的核心集散地。学会逛 HF，意味着你可以直接站在 Google、DeepMind 或顶级实验室的肩膀上进行开发，而不是从零开始训练一个只会挥手的机械臂。

如果你要在 HF 上关注一个仓，那绝对是 **`huggingface/lerobot`**。

* **仓库地址**：[https://github.com/huggingface/lerobot](https://github.com/huggingface/lerobot)
* **HF 模型/数据主页**：[https://huggingface.co/lerobot](https://huggingface.co/lerobot)

* **从 Dataset 看起**：不要先看模型，先去 HF 的 Datasets 频道搜 `lerobot/pusht`。这是一个经典的“推方块”任务。你会看到数据里不仅有图片，还有 `state`（状态）和 `action`（动作）。理解这些数据的对应关系，你就理解了具身智能的本质。
* **在线演示（Spaces）**：HF 最棒的地方在于 Space。你可以直接在浏览器里运行一些机器人的推理 Demo，感受一下 VLA 模型是如何把“给我拿个苹果”变成具体的关节转动角度的。

---


## 心灵鸡汤

数学确实很枯燥，觉得头晕是再正常不过的反应啦。一点点推导，算不明白就先放着，明天换个心情再看也是一样的。

## 相关资源
