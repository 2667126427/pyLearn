
# coding: utf-8

# In[1]:


from __future__ import print_function, division
import tensorflow as tf


# In[2]:


hello = tf.constant("Hello world.")


# In[3]:


sess = tf.Session()
print(sess.run(hello))

