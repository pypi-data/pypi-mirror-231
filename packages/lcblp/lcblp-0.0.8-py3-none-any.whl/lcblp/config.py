
class config:
    ### Preset ###
    resume = None
    workers = 0
    dataset_mean = [0.485, 0.456, 0.406]
    dataset_std = [0.229, 0.224, 0.225]
    dataset_max = 255.
    interpolation = 'Bicubic' #'Lanczos'
    mask_value = (0,) # should be index of class
    
    def __init__(self, args):
        ### Dataset ###
        self.path_data = args.path_data
        self.path_image = args.path_image
        self.path_label = args.path_label
        self.label_type = args.label_type     # navi, coco, pascal
        self.num_classes = args.num_classes
        self.valid_split = args.valid_split

        ### Model ###
        self.model_type = args.model_type     # FCN32s, DeepLabv3
        self.backbone = args.backbone         # {FCN32s, DeepLabv3}  = {'resnet50', 'resnet101'} # {ENet}  = None
        self.pretrained = args.pretrained     # {False, True, 'path_of_weight'}
        self.model_name = args.model_name     # 'model' = to model_YYMMDD # 'FCN32_resnet50'
        self.path_save = args.path_save       # 'weights/'

        ### Training ###
        self.path_train_output = args.path_train_output
        self.epochs = args.epochs
        self.batch_size = args.batch_size
        self.gpu = args.gpu

        self.input_size = args.input_size
        self.sampling_factor = args.sampling_factor
        
        self.resume = args.resume

        ### Scheduler ###
        self.init_lr = args.init_lr
        self.factor = args.factor             # Reduce factor
        self.patience = args.patience

        ### Transform ###
        self.path_aug = args.path_aug         # 'aug/sample.json'

        ### Test ###
        # self.test_save_dir = args.test_save_dir
        self.test_output_dir = args.test_output_dir
        self.test_data_dir = args.test_data_dir
        self.test_image_dir = args.test_image_dir
        self.test_label_dir = args.test_label_dir
        self.path_weight = args.path_weight
        self.weight_name = args.weight_name
        self.test_mode = args.test_mode
        self.merged_result = args.merged_result
        self.trained_crop = args.trained_crop