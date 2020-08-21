'''
设置机械臂关节的角度, 单位°
----------------------------------
- x:关节1
- y:关节2
- z:关节3
- a:关节4
- b:关节5
- c:关节6
- d:平动关节(滑轨)
'''
from mirobot import Mirobot
import time
arm = Mirobot(portname='COM7', debug=False)
arm.home_simultaneous()

# 设置单个关节的角度
print("测试设置单个关节的角度")
arm.go_to_axis(x=100.0, wait=True)
print("动作执行完毕")
# 状态查询
print(f"状态查询: {arm.get_status()}")
# 停顿2s
time.sleep(2)

# 设置多个关节的角度
print("设置多个关节的角度")
arm.go_to_axis(x=90, y=30, z=-20, a=10, b=20, c=45, wait=True)
print("动作执行完毕")
# 状态查询
print(f"状态查询: {arm.get_status()}")
# 停顿2s
time.sleep(2)
