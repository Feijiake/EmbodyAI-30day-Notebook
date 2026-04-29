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