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


transforms = T.Compose([
            T.ToTensor(), T.Normalize(mean=[0.5],std=[0.225])
            ])

net = model.mobilenet()
net.load_state_dict(torch.load(config.weight_root,map_location=lambda storage, loc: storage))

input = Image.open(config.test_img_root)
input = transforms(input)
input = torch.Tensor(input).unsqueeze(0)
input = Variable(input)

output = net(input)

value,indice = output.data.max(1,keepdim=True)
print(indice)
print(value)