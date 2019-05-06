import numpy as np
from multiprocessing import Pool, Value, Manager, Lock

def predict(params):
    image, label, k = params
    # 计算距离
    diss = np.sum(np.square(train_images - image), axis=1)
    # 将距离和标签结合
    arr = [(x, y) for (x, y) in zip(diss, train_labels)]
    # 排序得到前k个
    arr.sort() # build-in array的排序规则
    select = arr[:k] # 只要前K个
    m = {}
    for _, lab in select:
        if lab in m.keys():
            m[lab] += 1
        else:
            m[lab] = 1
    # 选出最大的的标记
    # key是label, value是数目
    pre = sorted(list(m.items()), key=lambda x: x[1], reverse=True)[0][0]
    print(label, pre)
    if pre == label:
       return 1
    return 0


print(np.__version__)
print('loading data')
train_images = np.load('train_images.npy', allow_pickle=True)
train_labels = np.load('train_labels.npy', allow_pickle=True)
test_images = np.load('test_images.npy', allow_pickle=True)
test_labels = np.load('test_labels.npy', allow_pickle=True)
print('load finished')

if __name__ == "__main__":
    pool = Pool(3)
    k = 1
    # lock = manager.Lock()
    result = pool.map(predict, [(*x, k) for x in zip(test_images, test_labels)])
    pool.close()
    pool.terminate()
    pool.join()
    print('%.2f%%' % (sum(result) / 100))
