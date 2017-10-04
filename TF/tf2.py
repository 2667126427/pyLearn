
# coding: utf-8

# In[5]:


import tensorflow as tf


# In[6]:


a = tf.placeholder(tf.int16)
b = tf.placeholder(tf.int16)
add = tf.add(a, b)
mul = tf.multiply(a, b)


# In[8]:


with tf.Session() as sess:
    print("Addition with variables: %i" % sess.run(add, feed_dict={a: 2, b: 3}))
    print("Multiplication with variables: %i" % sess.run(mul, feed_dict={a: 2, b: 3}))


# In[32]:


matrix1 = tf.constant([[3., 3.]])
matrix2 = tf.constant([[2.], [2.]])
product = tf.multiply(matrix1, matrix2)
print(product)


# In[43]:


with tf.Session() as sess:
    result = sess.run(product)
    print(result)


# In[45]:


print(matrix1, matrix2)

