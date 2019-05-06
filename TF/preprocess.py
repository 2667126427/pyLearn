import numpy as np

def load_image(filename, count):
    # 全部使用二进制读写即可
    # 前8个字节是magic number
    fp = open(filename, 'rb')
    fp.read(8) # 直接丢弃
    data = np.ndarray((count, 28 * 28))
    byte_arr = fp.read()
    for i in range(count):
        data[i] = np.array(list(byte_arr[i * 28 * 28:(i +  1) * 28 * 28]), dtype=np.int16)
    return data

def load_label(filename, count):
    fp = open(filename, 'rb')
    fp.read(8) # 直接丢弃
    data = np.ndarray(count, dtype=np.ndarray)
    byte_arr = fp.read()
    for i in range(count):
        data[i] = int(byte_arr[i])
    return data

def preprocess():
    # 文件写入numpy的特有文档加速读取速度
    train_images = load_image('train-images-idx3-ubyte', 60000)
    train_images.dump('train_images.npy')
    train_labels = load_label('train-labels-idx1-ubyte', 60000)
    train_labels.dump('train_labels.npy')
    test_images= load_image('t10k-images-idx3-ubyte', 10000)
    test_images.dump('test_images.npy')
    test_labels = load_label('t10k-labels-idx1-ubyte', 10000)
    test_labels.dump('test_labels.npy')

preprocess()

'''
t10k-images-idx3-ubyte
-rw-r--r-- 1 yaning yaning 9.8K  5月  6 08:39 t10k-labels-idx1-ubyte
-rw-r--r-- 1 yaning yaning  45M  5月  6 08:39 train-images-idx3-ubyte
-rw-r--r-- 1 yaning yaning  59K  5月  6 08:39 train-labels-idx1-ubyte

'''