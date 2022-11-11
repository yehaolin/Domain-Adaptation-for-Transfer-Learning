import config
import model
import torch
import torch.utils.data as data
import torch.optim as optim
from torch.autograd import Variable
import torch.nn.init as init
import torch.nn as nn
from PIL import Image
from torchvision import transforms as T
import os
from pre_data import Ten

def cnn_compute(filename, weights):
    test_set = Ten(filename)
    test_loader = data.DataLoader(test_set, 1, shuffle=True)
    net = model.mobilenet()
    net.load_state_dict(torch.load(weights, map_location=lambda storage, loc: storage))

    yes = 0
    no = 0
    for step, (img, target) in enumerate(test_loader):
        img = torch.Tensor(img)
        img = Variable(img)

        output = net(img)
        value, indice = output.data.max(1, keepdim=True)
        if indice == target:
            yes += 1
        else:
            no += 1

    accurate = yes / step
    return accurate


if __name__ == '__main__':
    test_set = Ten(config.test_img_root)
    test_loader = data.DataLoader(test_set,1,shuffle=True)
    net = model.mobilenet()
    net.load_state_dict(torch.load(config.weight_root,map_location=lambda storage, loc: storage))

    yes = 0
    no = 0
    for step,(img,target) in enumerate(test_loader):
        img = torch.Tensor(img)
        img = Variable(img)

        output = net(img)
        value, indice = output.data.max(1, keepdim=True)
        if indice == target:
            yes += 1
        else:
            no += 1

    accurate = yes/step
    print(accurate)