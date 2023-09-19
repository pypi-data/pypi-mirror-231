from .networks import fcn, deeplabv3, enet, segformer

dict_models = {'FCN32s'   : fcn.FCN32s,
               'DeepLabv3': deeplabv3.DeepLabv3,
               'ENet'     : enet.ENet,
               'SegFormer': segformer.SegFormer}

def get_model(model_type='FCN32s', backbone='resnet50', num_classes=21, pretrained=True, input_size=768):
    print(model_type)
    assert model_type in dict_models.keys()
    model, desc, config, transforms = dict_models[model_type](backbone=backbone, num_classes=num_classes, pretrained=pretrained, input_size=input_size)

    return model, desc, config, transforms