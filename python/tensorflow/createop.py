# !/usr/bin/env python
# @File Name: createop.py
# @Author: Joshua Liu
# @Email: liuchaozhenyu@gmail.com
# @Create Date: 2016-10-31 17:10:36
# @Last Modified: 2016-10-31 17:10:26
# @Description:
# 
import tensorflow as tf

# 创建一个常量op，产生一个 1x2 矩阵。这个 op 被作为一个节点加到默认图中
matrix1 = tf.constant([[3., 3.]])

# 创建另外一个常量 op，产生一个 2x1 矩阵
matrix2 = tf.constant([[2.], [2.]])

# 创建一个矩阵乘法 op，把 matrix1 和 matrix2 作为输入
product = tf.matmul(matrix1, matrix2)

sess = tf.Session()
result = sess.run(product)
print(result)
sess.close()
