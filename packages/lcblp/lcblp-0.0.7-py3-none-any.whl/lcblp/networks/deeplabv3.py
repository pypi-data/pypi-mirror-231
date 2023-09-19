import torch
import torch.nn as nn
import torch.nn.functional as F
from torchvision.models.segmentation import deeplabv3_resnet50, deeplabv3_resnet101

dict_last_nodes = {'resnet50' : 2048,
                   'resnet101': 2048}

dict_models = {'DeepLabv3'   : {'resnet50'   : deeplabv3_resnet50,
                                'resnet101'  : deeplabv3_resnet101}}

class DeepLabHead(nn.Sequential):
    def __init__(self, in_channels, num_classes):
        super(DeepLabHead, self).__init__(
            ASPP(in_channels, [12, 24, 36]),
            nn.Conv2d(256, 256, 3, padding=1, bias=False),
            nn.BatchNorm2d(256),
            nn.ReLU(),
            nn.Conv2d(256, num_classes, 1)
        )

class ASPPConv(nn.Sequential):
    def __init__(self, in_channels, out_channels, dilation):
        modules = [
            nn.Conv2d(in_channels, out_channels, 3, padding=dilation, dilation=dilation, bias=False),
            nn.BatchNorm2d(out_channels),
            nn.ReLU()
        ]
        super(ASPPConv, self).__init__(*modules)

class ASPPPooling(nn.Sequential):
    def __init__(self, in_channels, out_channels):
        super(ASPPPooling, self).__init__(
            nn.AdaptiveAvgPool2d(1),
            nn.Conv2d(in_channels, out_channels, 1, bias=False),
            nn.BatchNorm2d(out_channels),
            nn.ReLU())

    def forward(self, x):
        size = x.shape[-2:]
        for mod in self:
            x = mod(x)
        return F.interpolate(x, size=size, mode='bilinear', align_corners=False)

class ASPP(nn.Module):
    def __init__(self, in_channels, atrous_rates):
        super(ASPP, self).__init__()
        out_channels = 256
        modules = []
        modules.append(nn.Sequential(
            nn.Conv2d(in_channels, out_channels, 1, bias=False),
            nn.BatchNorm2d(out_channels),
            nn.ReLU()))

        rate1, rate2, rate3 = tuple(atrous_rates)
        modules.append(ASPPConv(in_channels, out_channels, rate1))
        modules.append(ASPPConv(in_channels, out_channels, rate2))
        modules.append(ASPPConv(in_channels, out_channels, rate3))
        modules.append(ASPPPooling(in_channels, out_channels))

        self.convs = nn.ModuleList(modules)

        self.project = nn.Sequential(
            nn.Conv2d(5 * out_channels, out_channels, 1, bias=False),
            nn.BatchNorm2d(out_channels),
            nn.ReLU(),
            nn.Dropout(0.5))

    def forward(self, x):
        res = []
        for conv in self.convs:
            res.append(conv(x))
        res = torch.cat(res, dim=1)
        return self.project(res)

class _DeepLabv3(nn.Module):
    def __init__(self, model):
        super().__init__()
        self.model = model
    
    def forward(self, x):
        return self.model(x)['out']

def DeepLabv3(backbone, num_classes, pretrained=False, input_size=None):
    if type(pretrained) is bool:
        model = dict_models['DeepLabv3'][backbone](pretrained=pretrained)
        model.classifier = DeepLabHead(dict_last_nodes[backbone], num_classes)
        model = _DeepLabv3(model)
        config, transforms = None, None
    else:
        model = dict_models['DeepLabv3'][backbone](pretrained=True)
        model.classifier = DeepLabHead(dict_last_nodes[backbone], num_classes)
        model = _DeepLabv3(model)
        checkpoint = torch.load(pretrained)
        
        try:
            model.load_state_dict(checkpoint['model_state_dict'])
        except:
            dict_weights_cvt = {}
            for key in checkpoint['model_state_dict']:
                #dict_weights_cvt[key.split('module.')[1]] = checkpoint['model_state_dict'][key]
                dict_weights_cvt['model.'+key] = checkpoint['model_state_dict'][key]
            
            model.load_state_dict(dict_weights_cvt)
        
        config, transforms = checkpoint['config'], checkpoint['transform']
    
    desc = f'DeepLabv3_{backbone}'
    
    return model, desc, config, transforms