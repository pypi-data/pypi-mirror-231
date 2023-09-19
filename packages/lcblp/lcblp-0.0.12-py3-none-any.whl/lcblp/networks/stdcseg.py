import torch
import torch.nn as nn
from _models.model_stages import BiSeNet

# all batch length are same
dict_weight = {'STDCNet813'  : 'networks/_stdcseg/checkpoints/STDCNet813M_73.91.tar',
               'STDCNet1446' : 'networks/_stdcseg/checkpoints/STDCNet1446_76.47.tar'}

def STDCSeg(backbone, num_classes, pretrained=False, input_size=None):
    if type(pretrained) is bool:
        model = BiSeNet(backbone=backbone, n_classes=num_classes, pretrain_model=dict_weight[backbone] if pretrained else pretrained, use_boundary_8=True)
        config, transforms = None, None
    else:
        model = BiSeNet(backbone=backbone, n_classes=num_classes, pretrain_model=False, use_boundary_8=True)
        checkpoint = torch.load(pretrained)
        
        try:
            model.load_state_dict(checkpoint['model_state_dict'])
        except:
            dict_weights_cvt = {}
            for key in checkpoint['model_state_dict']:
                dict_weights_cvt[key.split('module.')[1]] = checkpoint['model_state_dict'][key]

            model.load_state_dict(dict_weights_cvt)
        
        config, transforms = checkpoint['config'], checkpoint['transform']
    
    desc = f'STDCSeg_{backbone}'
    
    return model, desc, config, transforms