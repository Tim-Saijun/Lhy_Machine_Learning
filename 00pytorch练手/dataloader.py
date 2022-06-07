##dataset类似一堆扑克，告诉排在什么位置
##dataloader类似几张扑克，告诉如何取
from torch.utils.data import DataLoader
import torchvision.datasets

import dataset类

test_data = torchvision.datasets.CIFAR10("./00pytorch练手", train=False, transform=torchvision.transforms.ToTensor())

test_loader = DataLoader(dataset=test_data, batch_size=4, shuffle=True, num_workers=0, drop_last=False)
# 测试数据集中的第一张图片及target
img, target = test_data[0]
print(img.shape)
print(target)
