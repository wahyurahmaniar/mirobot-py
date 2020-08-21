'''
机械臂回归机械零点
'''
from mirobot import Mirobot
import time
arm = Mirobot(portname='COM7', debug=False)

# 注:一定要配置为wait=False,非阻塞式等待
# 要不然会卡死
arm.home_simultaneous(wait=False)
# 等待15s
time.sleep(15)
# 完成Homing
print("homing done")