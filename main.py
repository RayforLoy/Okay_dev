# -*- coding: UTF-8 -*-
import hashlib
import time

# 打开https://c.runoob.com/compile/6 把代码全部复制进去
# 把66666666替换成你的序列号，点击运行
# 设置界面左边选项栏最下面空白处连续点击会弹出来个框，输入生成的密码
# 开发者选项最下方空白处点击可打开隐藏选项

key = "66666666"+ str(time.strftime("%Y",time.localtime()) )+str(int(time.strftime("%m", time.localtime()) ))+str(int(time.strftime("%d", time.localtime()) ))+"010@okay.cn"
m = hashlib.md5()
m.update(key)
print(m.hexdigest()[-6:])
