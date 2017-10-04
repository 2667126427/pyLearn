from __future__ import print_function
import tensorflow as tf
import os

tf.app.flags.DEFINE_string(
    'log_dir', os.path.dirname(__file__) + '/logs',
    'Directories where event log are written to.')
FLAGS = tf.app.flags.FLAGS
if not os.path.isabs(os.path.expanduser(FLAGS.log_dir)):
    raise ValueError("You must set the absolute dir for log")

welcome = tf.concat("Welcome to TensorFlow world", 0)
with tf.Session() as sess:
    writer = tf.summary.FileWriter(os.path.expanduser(FLAGS.log_dir), sess.graph)
    print("output: ", sess.run(welcome))

writer.close()
sess.close()
'''
# Run the session
with tf.Session() as sess:
    writer = tf.summary.FileWriter(os.path.expanduser(FLAGS.log_dir), sess.graph)
    print("output: ", sess.run(welcome))

# Closing the writer.
writer.close()
sess.close()
'''