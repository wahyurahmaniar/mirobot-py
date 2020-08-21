# Mirobot-Python例程



## 机械臂回归机械零点

```python
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
```



## 获取机械臂当前的状态

```python
'''
获取机械臂的状态
'''
from mirobot import Mirobot
import time
arm = Mirobot(portname='COM7', debug=False)

# 注:一定要配置为wait=False,非阻塞式等待
# 要不然会卡死
arm.home_simultaneous(wait=False)
time.sleep(15)

# 打印机械臂当前的状态
print("获取机械臂的状态 ?")
print(arm.get_status())
```

日志: 

返回的是一个数组，代表当前的机械臂的状态

```
['', 'Free memory: 2036', 'in homeing moving...ok', '<Idle,Angle(ABCDXYZ):0.000,0.000,0.000,0.000,0.000,0.000,0.000,Cartesian coordinate(XYZ RxRyRz):198.670,0.000,230.720,0.000,0.000,0.000,Pump PWM:0,Valve 
PWM:0,Motion_MODE:0>', 'ok'] 
```

## 