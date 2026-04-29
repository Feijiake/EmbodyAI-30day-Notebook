# Day 01 | Linux与Git基础

## 概述

工程基建日：告别IDE！要在黑框框（终端）里优雅地敲代码。**掌握 Linux 常用命令是你进实验室的第一道坎**。目标：当导师给你一个干净的电脑时，你能迅速搭建起感知算法需要的环境。

## 今日任务

- **上午**：学习Ubuntu基本命令、Git核心逻辑
- **下午**：安装双系统，配置终端，建GitHub仓
- **晚上**：整理常用命令笔记

## 学习笔记

### 上午任务

我们在控制机器人（比如配置传感器或跑感知算法）时，通常没有鼠标可以点，只能靠输入纯文本指令。

**常用Linux命令：**

```bash
pwd                     # 确认自己当前所在的目录路径
mkdir robot_project     # 凭空建一个名为 robot_project 的文件夹
cd robot_project        # 走进去，进入这个文件夹
ls                      # 此时应该是空的
touch test.txt          # 创建一个空的txt
vim test.txt            # 在终端中查看和修改这个文件
cd ..                   # 返回上一级目录
python test.py          # 运行当前路径下的一个叫做test的py文件
```

**GitHub 协作：**

GitHub 是全球最大的程序员社交网络和代码托管平台，你可以把它理解为程序员界的"Instagram"或"代码版云盘"。如果说 Git 是你电脑里的"时光机"，那 GitHub 就是把你的时光机数据上传到云端的"大型公共图书馆"。在这个平台上，全世界的顶尖工程师都会把自己训练好的机器人模型、控制算法甚至是实验笔记公开出来。

在 Linux 中，把远程的代码"下载并建立连接"的过程叫做 `git clone`。这和你在网页上直接点"下载 ZIP"有本质区别：`git clone` 不仅把文件下载下来，还把这个仓库所有的历史版本记录全部带到了你的电脑里。

```bash
# 1. 建议先进入你的工作区目录，如果没有这个目录可以先建一个
mkdir -p ~/workspace
cd ~/workspace

# 2. 从 GitHub 克隆这个仓库到本地
git clone https://github.com/Feijiake/EmbodyAI-30day-Notebook.git

# 3. 进入刚刚下载好的文件夹
cd EmbodyAI-30day-Notebook

# 4. 查看一下里面的内容，确认下载成功
ls
```

### 下午任务

**双系统安装教程：** https://www.bilibili.com/video/BV1554y1n7zv/

**Linux系统配置：**

```bash
sudo apt update                           # 刷新软件库
sudo apt install git                      # 安装git
# 在这个过程中，系统会要求你输入电脑的管理员密码。
# 这里有个新手经常会懵的细节：在Linux终端里输入密码时，
# 屏幕上是没有任何星号或字符显示的，看起来就像死机了一样，
# 但实际上它已经接收到了，你只需要大胆地盲敲完密码然后按回车就行。
git --version                             # 验证安装
sudo apt install vim                      # 安装一个好用的文本编辑器
```

**关于 .bashrc：**

如果把 Linux 终端比作一个非常有仪式感的"智能管家"，那么 `.bashrc` 就是这个管家的"每日任务清单"。当你在 Linux 里打开一个终端窗口时，这个"管家"为了知道该怎么服务你，第一件事就是去读取用户根目录下的这个隐藏文件。它记录了你所有的个性化设置，比如：你想要终端显示的颜色是什么样，你常用的那些快捷指令（alias）是什么，以及最重要的——你安装的那些软件（比如 Conda 或 ROS）在系统硬盘里的具体位置（PATH）。

安装完软件后，即使不重启电脑也能直接在终端调用，这正是因为安装程序会自动在 `.bashrc` 的末尾写上一段代码。当你已经打开终端但修改了 `.bashrc` 时，输入 `source ~/.bashrc` 就可以让当前窗口立刻生效，而不用重启终端。

**Docker 安装：**

Docker 是 Linux 系统下的虚拟机，和 conda 一样也是为了配置干净的环境用的。比如我的电脑是 24.04，但是如果要使用的软件要求必须是 20.04，那在 Docker 中安装 20.04 的镜像就好了。

**Docker安装教程：** https://blog.csdn.net/yuchenhuaizhe/article/details/152008312

> Docker 的使用会在之后的项目中提及


### 晚上任务

**实践任务：**

自行查阅资料或问AI完成以下任务：

1. 在终端创建一个 workspace 路径
2. 在里面创建一个 `hello_world.py` 文件，内容是输出 `hello world`
3. 使用终端运行，并解决过程中出现的问题

## 思考与总结

## 心灵鸡汤

万事开头难，看着黑漆漆的终端觉得陌生很正常。今天只要把环境装好，你就已经超棒啦！记得喝杯甜甜的奶茶奖励自己哦。

## 相关资源

- 双系统安装教程：https://www.bilibili.com/video/BV1554y1n7zv/
- Conda安装教程：https://blog.csdn.net/JineD/article/details/129507719
- Docker安装教程：https://blog.csdn.net/yuchenhuaizhe/article/details/152008312
- PyCharm官方下载地址：https://www.jetbrains.com/pycharm/