# Lab 2 Linear Regression
import tensorflow as tf
# tf.set_random_seed(777)  # for reproducibility

# Try to find values for W and b to compute y_data = W * x_data + b
# We know that W should be 1 and b should be 0
# But let's use TensorFlow to figure it out
W = tf.Variable(tf.random_normal([1]), name='weight')
b = tf.Variable(tf.random_normal([1]), name='bias')

# Now we can use X and Y in place of x_data and y_data
# # placeholders for a tensor that will be always fed using feed_dict
# See http://stackoverflow.com/questions/36693740/
X = tf.placeholder(tf.float32, shape=[None])
Y = tf.placeholder(tf.float32, shape=[None])

# Our hypothesis XW+b
hypothesis = X * W + b

# cost/loss function
cost = tf.reduce_mean(tf.square(hypothesis - Y))

# Minimize
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.001)
train = optimizer.minimize(cost)

# Launch the graph in a session.
sess = tf.Session()
# Initializes global variables in the graph.
sess.run(tf.global_variables_initializer())


# 3차원의 배열 만들기 (x,y,z)
# b = np.array([[3500,88],[2125,88],[2755,88],[2125,88],[2125,88],[1385,82],[751,82],[1385,82]])
# print(b)


# Fit the line
for step in range(2001):
    cost_val, W_val, b_val, _ = \
        sess.run([cost, W, b, train],
    #             feed_dict={X: [3.500, 2.125, 2.125, 1.385, 0.751], Y: [0.088, 0.088, 0.088, 0.082, 0.082]})
                    feed_dict = {X: [3.500, 2.125, 2.125, 1.385, 0.751], Y: [1, 1, 1, 0, 0]})
    if step % 20 == 0:
        print(step, ':', cost_val, W_val, b_val)

# Testing our model
print(sess.run(hypothesis, feed_dict={X: [2.125, 3.500, 2.125, 3.500]}))
print(sess.run(hypothesis, feed_dict={X: [0.6, 0.751, 1.385]}))
