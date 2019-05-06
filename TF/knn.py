import torch
import numpy as np

device = torch.device('cpu')
# use gpu
if torch.cuda.is_available():
    device = torch.device('cuda')


def predict(image, label, train_images, train_labels, k=1):
    diss = torch.sum(torch.pow(train_images - image, 2), dim=1).cpu().numpy()
    arr = [(x, y) for x, y in zip(diss, train_labels)]
    arr.sort()
    # find first k members
    select = arr[:k]
    m = {}
    for _, lab in select:
        if lab in m.keys():
            m[lab] += 1
        else:
            m[lab] = 1
    pre = sorted(list(m.items()), key=lambda x: x[1], reverse=True)[0][0]
    if pre == label:
        return 1
    return 0


if __name__ == '__main__':
    print('loading data')
    train_images = np.load('data/train_images.npy', allow_pickle=True)
    train_labels = np.load('data/train_labels.npy', allow_pickle=True)
    test_images = np.load('data/test_images.npy', allow_pickle=True)
    test_labels = np.load('data/test_labels.npy', allow_pickle=True)
    print('load finished')
    # use GPU to accelerate knn
    train_images = torch.from_numpy(train_images).to(device=device)
    test_images = torch.from_numpy(test_images).to(device=device)
    sum_cnt = 10000
    k = 1
    corr = 0

    for i in range(sum_cnt):
        corr += predict(test_images[i], test_labels[i], train_images, train_labels, k)
        if (i + 1) % 1000 == 0:
            print(corr / (i + 1) * 100, '%')
    print('correct rate: %.2f%%' % (corr / sum_cnt * 100))
    '''
    k = 1, 96.91%
    k = 2, 96.91%
    3, 97.16
    5, 96.93
    8, 97.00
    16, 96.46
    32 95.93
    '''
