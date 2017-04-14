import tensorflow as tf
import numpy as np


# --------------------------------------------------------------------
# https://www.tensorflow.org/versions/r0.11/api_docs/python/
# --------------------------------------------------------------------

#-------------------------------------------------- 1. 텐서플로우 기본 Hello,World 출력 p40
#hello = tf.constant("hello, World!") #-- 생성
#sess =  tf.Session() #-- 텐서플로우 세션 생성
#print(sess.run(hello)) #-- 출력

#-------------------------------------------------- 2. 텐서플로우로 사칙연산 계산법 p46
#a = tf.placeholder("int32") # --
#b = tf.placeholder("int32") # --
#y = tf.multiply(a, b) #-- a와 b를 곱셈합니다. https://www.tensorflow.org/api_docs/python/tf/multiply
#sess =  tf.Session()
#print (sess.run(y, feed_dict={a:2, b:5})) #-- feed_dict :

#-------------------------------------------------- 3. 텐서보드 시각화를 통한 출력 p48
#a = tf.constant(10, name = "a")
#b = tf.constant(2, name = "b")
#y = tf.Variable(a*b, name = "y")
#model = tf.global_variables_initializer #initialize_all_variables() :: https://www.tensorflow.org/api_docs/python/tf/initialize_all_variables
#with tf.Session() as session:
#   merged = tf.summary.merge_all() # merge_all_summaries ::  https://www.tensorflow.org/api_docs/python/tf/contrib/deprecated/merge_all_summaries
#   writer = tf.train.SummaryWriter("/tmp/tensorflowlogs", session.graph)
#   session.run(model)
#print (session.run(y))

#-------------------------------------------------- 4.
