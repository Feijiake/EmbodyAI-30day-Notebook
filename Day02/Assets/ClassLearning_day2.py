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