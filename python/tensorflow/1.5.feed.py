# !/usr/bin/env python
# @File Name: 1.5.feed.py
# @Author: Joshua Liu
# @Email: liuchaozhenyu@gmail.com
# @Create Date: 2016-11-01 18:11:41
# @Last Modified: 2016-11-01 18:11:20
# @Description:
# 
import tensorflow as tf

input1 = tf.placeholder(tf.type.float32)
input2 = tf.placeholder(tf.type.float32)
output = tf.mul(input1, input2)

with tf.Session() as sess:
    print(sess.run([output], feed_dict={input1:[7.], input2:[2.]}))
