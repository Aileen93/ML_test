
import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
print('TensorFlow version: {0}'.format(tf.__version__))
hello = tf.constant('Hello, TensorFlow!')
sess = tf.Session()
print(sess.run(hello))