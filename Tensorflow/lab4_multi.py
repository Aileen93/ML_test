# Lab 4 Multi-variable linear regression
import tensorflow as tf
tf.set_random_seed(777)  # for reproducibility

x1_data = [3.500, 2.125, 2.125, 1.385, 0.751]
x2_data = [0.088, 0.088, 0.088, 0.082, 0.082]
x3_data = [0.30, 0.30, 0.30, 0, 0]

y_data = [10, 10, 10, 0, 0]

# placeholders for a tensor that will be always fed.
x1 = tf.placeholder(tf.float32)
x2 = tf.placeholder(tf.float32)
x3 = tf.placeholder(tf.float32)

Y = tf.placeholder(tf.float32)

w1 = tf.Variable(tf.random_normal([1]), name='weight1')
w2 = tf.Variable(tf.random_normal([1]), name='weight2')
w3 = tf.Variable(tf.random_normal([1]), name='weight3')
b = tf.Variable(tf.random_normal([1]), name='bias')

hypothesis = x1 * w1 + x2 * w2 + x3 * w3 + b
#hypothesis = x1 * w1 + x2 * w2 + b
print(hypothesis)

# cost/loss function
cost = tf.reduce_mean(tf.square(hypothesis - Y))

# Minimize. Need a very small learning rate for this data set
#optimizer = tf.train.GradientDescentOptimizer(learning_rate=1e-5)
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01)
train = optimizer.minimize(cost)

# Launch the graph in a session.
sess = tf.Session()
# Initializes global variables in the graph.
sess.run(tf.global_variables_initializer())

for step in range(4001):
    cost_val, hy_val, _ = sess.run([cost, hypothesis, train],
                                   feed_dict={x1: x1_data, x2: x2_data, x3: x3_data, Y: y_data})
    #                               feed_dict={x1: x1_data, x2: x2_data, Y: y_data})
    if __name__ == '__main__':
        if step % 20 == 0:
            print("\n\n",step, "Cost: ", cost_val, "\nPrediction:\n", hy_val)

    # <변수 2개>
    # [ 12.558218     6.64729643   6.64729643   3.43732738   0.71185541]
    # [ 12.56363487   6.64018536   6.64018536   3.44461799   0.71336913] 0.011
    # [ 12.56369781   6.6401062    6.6401062    3.44469929   0.71338511] 0.01
    # [ 12.56310368   6.64090538   6.64090538   3.44387126   0.71319938] 0.02
    # [ 12.56248093   6.64170647   6.64170647   3.4430604    0.71304536] 0.03
    # [ 12.16433239   6.70843172   6.70843172   3.76649332   1.25082648]
    #
    # <변수 3개> : 아이디, 국가번호, 이메일 주소의 비중
    #  [ 10.96676159   8.81822681   8.81822681   1.16229129   0.17162132]
    # [ 11.47009468   8.14769459   8.14769459   1.85668838   0.32475936]
    #
    # <변수 4개> : 아이디, 국가번호, 이메일 주소,


    #================================= 이제 이 값을 시그모이드 함수를 통해서 무한대로 보내버려보자
