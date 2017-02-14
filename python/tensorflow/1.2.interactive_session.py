# !/usr/bin/env python
# @File Name: 1.2.interactive_session.py
# @Author: Joshua Liu
# @Email: liuchaozhenyu@gmail.com
# @Create Date: 2016-11-01 16:11:15
# @Last Modified: 2016-11-01 17:11:07
# @Description: 交互式应用
#   进入一个交互式 Tensorflow 会话。
#   交互式会话方便使用诸如 IPython 之类的 Python 交互环境，可
#   以避免使用一个变量来持有会话。
import tensorflow as tf
sess = tf.InteractiveSession()

x = tf.Variable([1.0, 2.0])
a = tf.constant([3.0, 3.0])

# 使用初始化器 initializer op 的 run() 方法初始化 'x'
x.initializer.run()

# 增加一个减法 sub op，从 'x' 减去 'a'。运行减法 op，输出结果。
sub = tf.sub(x, a)
print(sub.eval())

