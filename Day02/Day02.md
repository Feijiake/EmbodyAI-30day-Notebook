# Day 2 | 面向对象的Python

## 概述

感知代码的结构：机器人系统很复杂，不要写流水账代码。今日感知**面向对象（OOP）**之美。目标：能用 Class 封装一个机器人的感知模块和控制模块，让你的代码像艺术品一样整洁。

## 今日任务

- **上午**：学习Python类、继承、多态
- **下午**：写具有多重继承的机器人系统代码
- **晚上**：了解Conda与虚拟环境

## 学习笔记

### 上午任务

### 用大白话拆解核心概念

1.  **类与实例（Class & Instance）：** 想象你在工厂里设计一款“通用机器人”。类就是那张设计图纸，它规定了机器人有几个关节、电池容量是多少；而“实例”就是根据图纸组装出来的真实机器人小A、小B。
2.  **继承（Inheritance）：** 具身智能讲究效率。你先写了一个“基础移动底盘”的类，它有前进后退的功能。当你需要做一个“四足狗”时，你不需要从头写底盘代码，直接“继承”过来，然后再给它加上四条腿的功能。这就是“站在巨人的肩膀上”写代码。
3.  **多态（Polymorphism）：** 这是最酷的地方。假设你写了一个“执行指令”的命令。对于轮式机器人，它收到指令会“滚动”；对于机械臂，它收到指令会“抓取”。虽然指令名字都叫 `execute()`，但不同的机器人会根据自己的身体构造给出不同的反应。这让我们的 AI 大脑（VLA模型）可以用同一套逻辑控制不同的躯体。

### 下午任务

多重继承的原理其实就是让一个子类同时拥有多个父类的“基因”。在代码层面，Python 使用一种叫 **MRO（方法解析顺序）** 的机制来决定当多个父类有同名方法时，机器人该听谁的。你可以把它想象成一个“职场汇报关系”：当机器人收到指令时，它会先看自己能不能处理，如果不能，就按照你定义继承时的顺序，依次去问它的“各个领域的导师”。这种机制让我们的代码极具模块化——你可以单独优化视觉模块，而不用担心会破坏移动模块的逻辑。

### 具身智能系统代码示例

下面我为你准备了一个典型的多重继承案例。我们定义了一个“移动底盘类”和一个“视觉相机类”，然后通过多重继承创造出一个能够“边走边看”的巡检机器人。现代编程很多时候我们不需要自己写代码了，但是至少要能看懂代码在干什么

对代码的详细解释可以多问问AI

```python
class MobileBase:
    """移动底盘模块"""
    def __init__(self, speed=0.5):
        self.speed = speed
        print(f"[系统] 动力底盘已就绪，初始速度：{self.speed} m/s")

    def move(self, direction):
        print(f"[执行] 底盘正在向 {direction} 移动...")

class VisionSystem:
    """视觉感知模块"""
    def __init__(self, resolution="1080p"):
        self.resolution = resolution
        print(f"[系统] 摄像头已激活，分辨率：{self.resolution}")

    def sense_environment(self):
        print("[感知] 正在扫描周围环境，检测障碍物...")

class InspectionRobot(MobileBase, VisionSystem):
    """巡检机器人：继承了底盘和视觉两个系统的能力"""
    def __init__(self, name, speed, resolution):
        # 注意：在多重继承中，通常使用 super() 或类名手动初始化
        MobileBase.__init__(self, speed)
        VisionSystem.__init__(self, resolution)
        self.name = name
        print(f"--- {self.name} 机器人组装完毕！ ---")

    def perform_task(self):
        print(f"\n>>> {self.name} 开始执行任务：")
        self.sense_environment()  # 调用来自 VisionSystem 的方法
        self.move("前方仓库")      # 调用来自 MobileBase 的方法

# 实例化并运行
my_robot = InspectionRobot(name="阿波罗1号", speed=1.2, resolution="4K")
my_robot.perform_task()
```


### 晚上任务

在实际开发中因为不同的软件可能需要不同的python版本和包，而且有时他们是相互冲突的，因此还需要安装一个python版本管理的环境 conda。

**Conda安装教程：** https://blog.csdn.net/JineD/article/details/129507719

Conda 的指令非常直观，你可以把它们看作是管理不同"平行宇宙"的开关。掌握这四板斧，你就基本打通了 Conda 的任督二脉：

- **创建：** `conda create -n <环境名> python=<版本号>` —— 初始化一个专属的新房间
- **查看：** `conda env list` —— 列出所有已建好的房间
- **进入：** `conda activate <环境名>` —— 走进指定的房间开始工作
- **退出：** `conda deactivate` —— 离开房间，回到基础状态

当你准备开始干活时，需要从全局环境切换进你的特定房间，这时候就要用到激活指令。输入 `conda activate vision_lab`，你会发现终端命令行的最左边出现了一个括号 `(vision_lab)`，这代表你现在已经成功进入该环境，之后安装的任何插件或库都只会留在这个房间里，不会污染其他项目。

如果某天你发现有个环境彻底搞乱了，想把它删了重建，还可以使用 `conda remove -n <环境名> --all`，它会帮你把那个房间彻底清空。

**PyCharm 配置：**

Pycharm官方下载地址：https://www.jetbrains.com/pycharm/

在 PyCharm 中使用当前的 conda 环境：

![Pycharm添加Conda环境](./img/pycharm%20add%20conda%2001.png)

![Pycharm添加Conda环境](./img/pycharm%20add%20conda%2002.png)

![Pycharm添加Conda环境](./img/pycharm%20add%20conda%2003.png)

**小作业**

自己动手写一遍上午的代码，环境使用conda的Python 3.12 ，在pycharm中运行

## 思考与总结

## 心灵鸡汤

看不懂长篇代码没关系的，它就像一门外语，多看几遍就熟悉了。今天学累了就闭上眼睛休息一会儿，允许自己慢慢来。

## 相关资源
* **Python 官方教程（类部分）：** [Python Classes](https://docs.python.org/3/tutorial/classes.html) —— 最权威的基础说明。
* **GitHub 实战参考：** [LeRobot (Hugging Face)](https://github.com/huggingface/lerobot) —— 看看顶尖工程师是怎么定义机器人类的。