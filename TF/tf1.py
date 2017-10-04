
# coding: utf-8

# In[1]:


import tensorflow as tf


# In[2]:


a = tf.constant(2)
b = tf.constant(3)


# In[3]:


with tf.Session() as sess:
    print("a = 2, b = 3.")
    print("Addition with constants: %i" % sess.run(a + b))
    print("Multiplication with constans: %i" % sess.run(a * b))

