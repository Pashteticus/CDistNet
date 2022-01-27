dst_vocab = 'cdistnet/utils/dict_36.txt'  # 98 + 空格
dst_vocab_size = 40
rgb2gray =False
keep_aspect_ratio = False
width = 128 #100
height = 32 #32
max_width = 180
is_lower = True  # True：训练的时候转成小写
cnn_num = 2
leakyRelu = False
hidden_units = 512
ff_units = 1024      #ff的隐藏层数512 1024
scale_embedding = True
attention_dropout_rate = 0.0
residual_dropout_rate = 0.1
num_encoder_blocks = 3
num_decoder_blocks = 3
num_heads = 8
beam_size = 10
n_best = 1
num_fiducial = 20           #number of fiducial points of TPS-STN
use_squ = True              #if fasle: use diag for tgt mask(not ready)
train_method = 'origin'     #dist:  use distributed train method origin
optim = 'origin'


# method choice
tps_block = 'TPS'           # TPS None
feature_block = 'Resnet45'    # None (not use cnn) origin Resnet(FAN) TFnet Resnet45
patch_block = None          # None wh_2_4_8 wh w+h+wh+avg vit w+h w+h+wh w+h+wh_ks w+wh2+wh4+wh6_ks
custom_encoder = None      # None swin-trans pvt text2img-msa(not ready) trans_blstm blstm_trans
custom_decoder = 'dssnetv3'      #u-net test3-decoder None dssnetv3


# dssnetv3 step1 step2
step1 = [True,False,False]     # pos feat gt
step2 = [False,True,True]      # sem_vis pos_vis pos_sem
flip_pos_sem = False
flip_pos_vis = False
use_gt_pos = True
# transformer = 'transformer' # transformer patch4_trans
data_aug = True

train = dict(
    grads_clip=5,
    optimizer='adam_decay',  # not used
    learning_rate_warmup_steps=10000,
    label_smoothing=True,  # fixed in code
    shared_embedding=False,  # not used
    device='cuda',
    is_train_gt=False,
    image_dir='/home/zhengsheng/datasets/TextRecog/mnt/ramdisk/max/90kDICT32px',
    # gt_file='../dataset/MJ/MJ_test/',
    gt_file=['dataset/MJ/MJ_train/',
            'dataset/MJ/MJ_test/',
            'dataset/MJ/MJ_valid/',
            'dataset/ST'],
    # gt_file='/home/zhengsheng/datasets/TextRecog/mnt/ramdisk/max/90kDICT32px/annotation_train_two_Synth_shuf_clean.txt',
    # image_dir='/data6/zhengtianlun/temp/icdar2015_test/images',
    # gt_file='/data6/zhengtianlun/temp/icdar2015_test/gt.txt',
    # hdf5='datasets/train.hdf5',  # train_two.hdf5 train_keep_aspect_ratio.hdf5  train_two_keep_aspect_ratio.hdf5
    num_worker=16,
    model_dir ='model/test',
    # model_dir='models/new_baseline_vis_1_0_0_1_0_0_3_32*128_tps_resnet45_epoch_6',  # 模型保存的目录
    num_epochs=6,
    # gpu_device_ids=[1,2,3,4,5,6,7],
    batch_size=700,  # 4gpu 1800
    model=None,
    # model ='models/new_baseline_dynametic_fusion_step1_1_0_0_step2_0_1_1_3_32*128_tps_resnet45_epoch_6/model_epoch_5.pth',
    # model='/data6/zhengtianlun/NRTR/models/new_baseline_transformer_4_32*128_tps_resnet45_epoch_5/model_epoch_3.pth',  # 加载的模型地址, None不加载  e.g. '/home/zhengsheng/github/NRTR/models/model_epoch_14.pth',
    # current_epoch=6,  # 从第几个epoch开始训练,根据加载的模型设置  e.g. 15
    save_iter=10000,
    display_iter=100,
    tfboard_iter=100,
    eval_iter=5000,
)


val = dict(
    model='models/baseline_two_32*100_1d_2cnn-test/model_epoch_1.pth',  # 加载的模型, 训练的时候用不到
    device='cuda',
    is_val_gt=False,
    image_dir='datasets/NewVersion/val_data',
    gt_file= [
               'dataset/eval/IC13_857',
               'dataset/eval/SVT',
                'dataset/eval/IIIT5k_3000',
               'dataset/eval/IC15_1811',
                'dataset/eval/SVTP',
               'dataset/eval/CUTE80'],
    # gt_file=['datasets/NewVersion/val_data/val_data.txt'],
    # gt_file='../dataset/MJ/MJ_valid/',
    # hdf5='datasets/val.hdf5',
    batch_size=800,  # 4gpu 1800
    num_worker=16,
)


test = dict(
    test_one=False,
    device='cuda',
    rotate=False,  # 测试时旋转90度
    best_acc_test=False,  # 测试评估模型中最好的结果
    eval_all=False,  # 测试全部，包括两个epoch之间保存的模型。例如model_epoch_9_iter_4080.pth
    s_epoch=5,  # 从第s_epoch开始测试，当s_epoch = -1: 不测试
    e_epoch=5,  # 到第e_epoch结束测试
    avg_s=-1,  # 从第avg_s到avg_e进行模型平均，当avg_s = -1: 不平均
    avg_e=9,
    avg_all=False,  # 如果True，模型平均的时候包括两个epoch之间保存的模型。例如model_epoch_9_iter_4080.pth
    # test_list=[
    #     'ICDAR2003_860',
    #     'ICDAR2003_867',
    #     'ICDAR2013_857',
    #     'ICDAR2013_1015',
    #     'ICDAR2015_1811',
    #     'ICDAR2015_2077',
    #     'IIIT5K',
    #     'SVT',
    #     'SVT-P',
    #     'CUTE80'
    # ],
    is_test_gt=False,
    test_list=[
               # 'dataset/eval/IC13_857',
               # 'dataset/eval/SVT',
               #  'dataset/eval/IIIT5k_3000',
               'dataset/eval/IC15_1811',
               #  'dataset/eval/SVTP',
               # 'dataset/eval/CUTE80'
    ],
    # test_list=[
    #     'ICDAR2013_857',
    #     'SVT',
    #     'IIIT5K',
    #     'ICDAR2015_1811',
    #     'SVT-P',
    #     'CUTE80'
    # ],
    image_dir='datasets/NewVersion',
    batch_size=1,
    num_worker=8,
    # model_dir='models/new_baseline_layer_4_pos_gt_pos_en_3_32*128_tps_resnet45_epoch_6',
    model_dir = 'models/test',
    # model_dir='models/sche_optim_sota_exp_32_128_tps_resnet45_dssnet_decoder',  # 测试加载的模型目录
    script_path='utils/Evaluation_TextRecog/script.py',
    python_path='/data6/zhengtianlun/miniconda3/envs/py2/bin/python2.7'
)
