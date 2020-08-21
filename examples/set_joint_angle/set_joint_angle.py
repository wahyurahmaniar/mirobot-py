'''
设置机械臂关节的角度, 单位°
'''
'''
机械臂回归机械零点
'''
from mirobot import Mirobot
import time
arm = Mirobot(portname='COM7', debug=False)

# 注:一定要配置为wait=False,非阻塞式等待
# 要不然会卡死
arm.home_simultaneous(wait=False)
time.sleep(15)

# 设置关节角度
arm.go_to_axis(x=90.0, wait=True)