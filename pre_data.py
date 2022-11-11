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

class Ten(data.Dataset):##数据设置label
    def __init__(self,root):
        imgs = os.listdir(root)
        self.imgs = [os.path.join(root,img) for img in imgs]#加载全部图片路径
        self.transforms = T.Compose([
            T.ToTensor(), T.Normalize(mean=[0.5],std=[0.225])
            ])

    def __getitem__(self, index):
        img_path = self.imgs[index]
        img_path = img_path.replace('\\','/')
        Object = img_path.split('/')[-1].split('_')[-1].split('.')[0]
        if 'A' is Object:
            #label = [1,0,0,0,0,0,0,0,0,0]
            label = 0
        if 'B' is Object:
            #label = [0,1,0,0,0,0,0,0,0,0]
            label = 1
        if 'C' is Object:
            #label = [0,0,1,0,0,0,0,0,0,0]
            label = 2
        if 'D' is Object:
            #label = [0,0,0,1,0,0,0,0,0,0]
            label = 3
        if 'E' is Object:
            #label = [0,0,0,0,1,0,0,0,0,0]
            label = 4
        if 'F' is Object:
            #label = [0,0,0,0,0,1,0,0,0,0]
            label = 5
        if 'G' is Object:
            #label = [0,0,0,0,0,0,1,0,0,0]
            label = 6
        if 'H' is Object:
            #label = [0,0,0,0,0,0,0,1,0,0]
            label = 7
        if 'I' is Object:
            #label = [0,0,0,0,0,0,0,0,1,0]
            label = 8
        if 'J' is Object:
            #label = [0,0,0,0,0,0,0,0,0,1]
            label = 9

        data = Image.open(img_path)

        data = self.transforms(data)
        return data,label

    def __len__(self):
        return len(self.imgs)