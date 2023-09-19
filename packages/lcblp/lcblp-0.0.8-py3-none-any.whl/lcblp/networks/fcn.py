import torch
import torch.nn as nn
from torchvision.models.segmentation import fcn_resnet50, fcn_resnet101

dict_last_nodes = {'resnet50' : 2048,
                   'resnet101': 2048}

dict_models = {'FCN32s'   : {'resnet50'   : fcn_resnet50,
                             'resnet101'  : fcn_resnet101}}

class FCNHead(nn.Sequential):
    def __init__(self, in_channels, channels):
        inter_channels = in_channels // 4
        layers = [
            nn.Conv2d(in_channels, inter_channels, 3, padding=1, bias=False),
            nn.BatchNorm2d(inter_channels),
            nn.ReLU(),
            nn.Dropout(0.1),
            nn.Conv2d(inter_channels, channels, 1)
        ]

        super(FCNHead, self).__init__(*layers)

class _FCN32(nn.Module):
    def __init__(self, model):
        super().__init__()
        self.model = model
    
    def forward(self, x):
        return self.model(x)['out']
        

def FCN32s(backbone, num_classes, pretrained=False, input_size=None):
    if type(pretrained) is bool:
        model = dict_models['FCN32s'][backbone](pretrained=pretrained)
        model.classifier = FCNHead(dict_last_nodes[backbone], num_classes)
        model = _FCN32(model)
        config, transforms = None, None
    else:
        model = dict_models['FCN32s'][backbone](pretrained=False)
        model.classifier = FCNHead(dict_last_nodes[backbone], num_classes)
        model = _FCN32(model)
        checkpoint = torch.load(pretrained)
    
        ## for RKNN
        '''
        import time
        print('model : ', end='')
        st = time.time()
        model = dict_models['FCN32s'][backbone](pretrained=False)
        model.classifier = FCNHead(dict_last_nodes[backbone], num_classes)
        print(time.time()-st)
        model = _FCN32(model)
        print('checkpoint : ', end='')
        st = time.time()
        checkpoint = torch.load(pretrained)
        print(time.time()-st)
        '''
        
        try:
            model.load_state_dict(checkpoint['model_state_dict'])
            print('try')
        except:            
            dict_weights_cvt = {}
            for key in checkpoint['model_state_dict']:
                ## for original evaluate.py
                
                if 'aux' in key:
                    continue
                dict_weights_cvt[key.split('module.')[1]] = checkpoint['model_state_dict'][key]
                
                
                '''
                if 'aux' in key:
                    continue
                dict_weights_cvt['model.'+key] = checkpoint['model_state_dict'][key]
                '''
                
                ## for RKNN
                '''
                if 'aux' in key:
                    continue
                
                dict_weights_cvt[key] = checkpoint['model_state_dict'][key]
                '''
            model.load_state_dict(dict_weights_cvt)
        
            
        config, transforms = checkpoint['config'], checkpoint['transform']
    
    desc = f'FCN32s_{backbone}'
    
    return model, desc, config, transforms