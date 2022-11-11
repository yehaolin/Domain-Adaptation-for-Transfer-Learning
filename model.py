import torch.nn as nn
import torch
import config

class mobilenet(nn.Module):
    def __init__(self):
        super(mobilenet,self).__init__()

        self.mobilenet = []

        def conv_bn(inp, oup, stride):
            return nn.Sequential(
                nn.Conv2d(inp, oup, 3, stride, 1, bias=False),
                nn.BatchNorm2d(oup),
                nn.ReLU(inplace=True)
            )

        def conv_dw(inp, oup, stride):
            return nn.Sequential(
                nn.Conv2d(inp, inp, 3, stride, 1, groups=inp, bias=False),
                nn.BatchNorm2d(inp),
                nn.ReLU(inplace=True),

                nn.Conv2d(inp, oup, 1, 1, 0, bias=False),
                nn.BatchNorm2d(oup),
                nn.ReLU(inplace=True),
            )

        self.model = nn.Sequential(
            conv_bn(1, 3, 1),
            conv_dw(3, 32, 1),
            conv_dw(32 ,64, 1),
            conv_dw(64, 128, 1),
            conv_dw(128, 256, 1),

            #nn.AvgPool2d(3),
        )

        self.fc1 = nn.Linear(25600, 2560)
        self.fc2 = nn.Linear(2560, 256)
        self.fc3 = nn.Linear(256, config.class_number)
    def forward(self, x):
        x = self.model(x)  #torch.Size([8, 256, 10, 10])
        #x = x.view(config.batch_size, 256)

        x = x.view(-1, 25600)
        x = self.fc1(x).view(config.batch_size,2560,1,1)
        x = self.fc2(x.view(config.batch_size,2560)).view(config.batch_size,256,1,1)
        x = self.fc3(x.view(config.batch_size,256))
        return x