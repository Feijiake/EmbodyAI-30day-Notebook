# 🦋 EmbodyAI-30day-Notebook 🦋

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/anomalyco/EmbodyAI-30day-Notebook/pulls)
[![Status](https://img.shields.io/badge/Status-In%20Progress-blue.svg)]()

> 这是对"具身智能30天速成计划"的笔记和内容补充仓库，记录30天学习历程。

---

## 📖 目录

- [第1周：工程筑基](#第1周工程筑基)
  - [Day01 | Linux与Git](./Day01/Day01.md)
  - [Day02 | Python面向对象](./Day02/Day02.md)
  - [Day03 | 线性代数与NumPy](./Day03/Day03.md)
  - [Day04 | 深度学习入门(1)](./Day04/Day04.md)
  - [Day05 | 深度学习入门(2)](./Day05/Day05.md)
  - [Day06 | 模型调试](./Day06/Day06.md)
  - [Day07 | Transformer](./Day07/Day07.md)
- [第2周：决策智能](#第2周决策智能)
  - [Day08 | 强化学习起步](./Day08/Day08.md)
  - [Day09 | Q-Learning](./Day09/Day09.md)
  - [Day10 | 策略梯度](./Day10/Day10.md)
  - [Day11 | 模仿学习](./Day11/Day11.md)
  - [Day12 | 动作分块](./Day12/Day12.md)
  - [Day13 | Diffusion Policy(1)](./Day13/Day13.md)
  - [Day14 | Diffusion Policy(2)](./Day14/Day14.md)
- [第3周：机器人躯体](#第3周机器人躯体)
  - [Day15 | 正运动学FK](./Day15/Day15.md)
  - [Day16 | 逆运动学IK](./Day16/Day16.md)
  - [Day17 | 仿真器搭建](./Day17/Day17.md)
  - [Day18 | 仿真环境交互](./Day18/Day18.md)
  - [Day19 | 仿真感知](./Day19/Day19.md)
  - [Day20 | 脑机结合](./Day20/Day20.md)
  - [Day21 | RL训练验证](./Day21/Day21.md)
- [第4周：前沿融合与项目实战](#第4周前沿融合与项目实战)
  - [Day22 | 3D视觉点云](./Day22/Day22.md)
  - [Day23 | 感知控制融合](./Day23/Day23.md)
  - [Day24 | VLM/VLA前沿](./Day24/Day24.md)
  - [Day25 | 开源VLA探索](./Day25/Day25.md)
  - [Day26 | 项目开发-数据](./Day26/Day26.md)
  - [Day27 | 项目开发-训练](./Day27/Day27.md)
  - [Day28 | 项目开发-测试](./Day28/Day28.md)
  - [Day29 | 项目开发-报告](./Day29/Day29.md)
  - [Day30 | 总结与下一步](./Day30/Day30.md)

---

## 📚 学习路线总览

***打卡手账本*** [https://github.com/Feijiake/EmbodyAI-DATA](https://github.com/Feijiake/EmbodyAI-DATA)

### 第1周：工程筑基

| Day | 主题 | 描述 | 笔记 |
|:---:|:---|:---|:---:|
| Day01 | Linux与Git | 终端命令、GitHub协作、环境搭建 | [笔记](./Day01/Day01.md) |
| Day02 | Python面向对象 | 类与继承、机器人系统设计 | [笔记](./Day02/Day02.md) |
| Day03 | 线性代数与NumPy | 矩阵运算、坐标变换、数据处理 | [笔记](./Day03/Day03.md) |
| Day04 | 深度学习入门(1) | MLP、反向传播、PyTorch基础 | [笔记](./Day04/Day04.md) |
| Day05 | 深度学习入门(2) | CNN、MNIST训练、Loss优化 | [笔记](./Day05/Day05.md) |
| Day06 | 模型调试 | 过拟合正则化、验证集、炼丹技巧 | [笔记](./Day06/Day06.md) |
| Day07 | Transformer | Attention机制、预训练模型 | [笔记](./Day07/Day07.md) |

### 第2周：决策智能

| Day | 主题 | 描述 | 笔记 |
|:---:|:---|:---|:---:|
| Day08 | 强化学习起步 | 马尔可夫决策、Gymnasium环境 | [笔记](./Day08/Day08.md) |
| Day09 | Q-Learning | DQN算法、CartPole平衡任务 | [笔记](./Day09/Day09.md) |
| Day10 | 策略梯度 | Actor-Critic、PPO算法 | [笔记](./Day10/Day10.md) |
| Day11 | 模仿学习 | 行为克隆(BC)、数据处理 | [笔记](./Day11/Day11.md) |
| Day12 | 动作分块 | Action Chunking、ALOHA项目 | [笔记](./Day12/Day12.md) |
| Day13 | Diffusion Policy(1) | 扩散模型原理、去噪过程 | [笔记](./Day13/Day13.md) |
| Day14 | Diffusion Policy(2) | 环境配置、官方代码阅读 | [笔记](./Day14/Day14.md) |

### 第3周：机器人躯体

| Day | 主题 | 描述 | 笔记 |
|:---:|:---|:---|:---:|
| Day15 | 正运动学FK | 杆件变换、齐次矩阵、空间坐标 | [笔记](./Day15/Day15.md) |
| Day16 | 逆运动学IK | 雅可比矩阵、四元数与欧拉角 | [笔记](./Day16/Day16.md) |
| Day17 | 仿真器搭建 | Isaac Gym / MuJoCo 安装配置 | [笔记](./Day17/Day17.md) |
| Day18 | 仿真环境交互 | URDF/MJCF模型、控制关节 | [笔记](./Day18/Day18.md) |
| Day19 | 仿真感知 | 本体感受数据读取、状态向量 | [笔记](./Day19/Day19.md) |
| Day20 | 脑机结合 | 奖励函数设计、触碰任务 | [笔记](./Day20/Day20.md) |
| Day21 | RL训练验证 | 并行训练、Success Rate评估 | [笔记](./Day21/Day21.md) |

### 第4周：前沿融合与项目实战

| Day | 主题 | 描述 | 笔记 |
|:---:|:---|:---|:---:|
| Day22 | 3D视觉点云 | RGB-D相机、Open3D可视化 | [笔记](./Day22/Day22.md) |
| Day23 | 感知控制融合 | 多模态网络架构、特征融合 | [笔记](./Day23/Day23.md) |
| Day24 | VLM/VLA前沿 | RT-1/RT-2、视觉-语言-动作 | [笔记](./Day24/Day24.md) |
| Day25 | 开源VLA探索 | Octo、OpenVLA、代码阅读 | [笔记](./Day25/Day25.md) |
| Day26 | 项目开发-数据 | 任务设计、数据整理、HDF5 | [笔记](./Day26/Day26.md) |
| Day27 | 项目开发-训练 | 网络训练、GPU调试、Loss监控 | [笔记](./Day27/Day27.md) |
| Day28 | 项目开发-测试 | 闭环测试、失败案例分析 | [笔记](./Day28/Day28.md) |
| Day29 | 项目开发-报告 | 调优改进、项目README | [笔记](./Day29/Day29.md) |
| Day30 | 总结与下一步 | 技术栈梳理、成果整理、自信出发 | [笔记](./Day30/Day30.md) |

---

## ✨ 功能特色

- 📁 **结构化目录** - 每天一个文件夹，Assets存放代码，img存放图片
- 📝 **Markdown笔记** - 使用Markdown格式记录学习内容
- 🔧 **模板复用** - TEMPLATE目录提供每日笔记模板
- 📖 **索引清晰** - README总览所有笔记链接，方便跳转

---

## 🚀 使用方法

1. **查看笔记** - 在上方的学习路线表格中点击对应天的"笔记"链接
2. **添加内容** - 在对应的 `DayXX/DayXX.md` 文件中添加你的学习笔记
3. **提交代码** - 将代码文件放入对应天的 `Assets/` 目录
4. **添加图片** - 将图片放入对应天的 `img/` 目录
5. **使用模板** - 参考 `TEMPLATE/DayXX.md` 创建新的每日笔记

---

## 🎓 30天后你将掌握

```
✅ Linux 终端操作与开发环境配置
✅ Python 面向对象编程与代码架构能力
✅ 深度学习核心原理（MLP/CNN/Transformer）
✅ 强化学习算法（DQN/PPO）与训练技巧
✅ 模仿学习与扩散策略（BC/Diffusion Policy）
✅ 机器人运动学（FK/IK）与空间变换
✅ 物理仿真器（Isaac Gym/MuJoCo）使用
✅ 具身智能端到端项目开发能力
✅ VLA前沿模型（RT、Octo）理解与应用
✅ 完整的科研项目成果（可展示的GitHub仓库）
```

---

## 💡 温馨提示

- 不需要按顺序完成，可以选择感兴趣的日子开始
- 遇到报错很正常，这是成长的一部分
- 善用 `Gemini` 等AI工具辅助学习
- 累了就休息，循序渐进比突击更有效
- **最重要的是：坚持就是胜利** ✨

---

## 📂 项目结构

```
EmbodyAI-30day-Notebook/
├── README.md           # 项目主文档
├── LICENSE             # MIT开源协议
├── .gitignore          # Git忽略配置
├── .private/           # 本地私有目录
│   └── memory.md       # 记忆文本（不上传git）
├── TEMPLATE/           # 每日笔记模板
│   ├── Assets/         # 代码目录
│   ├── img/            # 图片目录
│   └── DayXX.md        # 模板文件
├── Day01/ ~ Day30/     # 30天学习笔记
│   ├── Assets/         # 代码目录
│   ├── img/            # 图片目录
│   └── DayXX.md        # 学习笔记
```

---

<div align="center">

*30天，300小时，告别迷茫，拥抱具身智能的世界* 🦋

*具身智能笔记 | 30天成长手账* 🦋

</div>