import tensorflow as tf

print("test")

def showTensor():
    sess = tf.InteractiveSession()

    x = tf.Variable([1.0, 2.0])
    a = tf.constant([3.0, 3.0])

    # x에 대해서 연산을 수행해서 결과를 먼저 만든다.
    x.initializer.run()     # Initialize 'x' using the run() method of its initializer op.

    sub = tf.sub(x, a)      # Add an op to subtract 'a' from 'x'.  Run it and print the result
    print(sub.eval())       # [-2. -1.]

    print('-------------------------------------')

    # 결과를 내장하고 있다면 eval() 사용 가능. initializer 없이 x에 대해서 호출하면 비정상 종료
    print(a.eval())         # [ 3.  3.]
    print(x.eval())         # [ 1.  2.]

    # -1에서 1 사이의 정규분포 난수 3개 생성. b는 1행 3열의 텐서 객체
    b = tf.random_uniform([3], -1.0, 1.0)
    print(type(b))          # <class 'tensorflow.python.framework.ops.Tensor'>
    print(b.eval())         # [-0.16271138 -0.33350062  0.51194   ]

    # tensor라면 initializer 사용
    w = tf.Variable(tf.random_uniform([5, 3], 0, 32, dtype=tf.int32))
    w.initializer.run()
    print(w.eval())         # [[15  1 21] [14 16 27] [13 30 28] [23 21 26] [15 19 16]]

    print('-------------------------------------')

    x = [[1., 1.], [10., 2.]]
    print(tf.reduce_mean(x).eval())         # 3.5, 전체 평균
    print(tf.reduce_mean(x, 0).eval())      # [ 5.5  1.5], 0은 column
    print(tf.reduce_mean(x, 1).eval())      # [ 1.  6.], 1은 row

    sess.close()