import time
import tensorflow as tf
import numpy as np
from train import train
import data_loader
while 1:
    print("start training and predict")

    tf.reset_default_graph()
    import argparse


    load_data = data_loader.load_data
    np.random.seed(555)
    parser = argparse.ArgumentParser()
    # 默认使用movie数据集
    parser.add_argument('--dataset', type=str, default='xingce', help='which dataset to use')
    parser.add_argument('--n_epochs', type=int, default=10, help='the number of epochs')
    parser.add_argument('--dim', type=int, default=8, help='dimension of user and entity embeddings')
    parser.add_argument('--L', type=int, default=1, help='number of low layers')
    parser.add_argument('--H', type=int, default=1, help='number of high layers')
    parser.add_argument('--batch_size', type=int, default=4096, help='batch size')
    parser.add_argument('--l2_weight', type=float, default=1e-6, help='weight of l2 regularization')
    parser.add_argument('--lr_rs', type=float, default=0.02, help='learning rate of RS task')
    parser.add_argument('--lr_kge', type=float, default=0.01, help='learning rate of KGE task')
    parser.add_argument('--kge_interval', type=int, default=3, help='training interval of KGE task')
    show_loss = False
    show_topk = False

    args = parser.parse_args()
    data = load_data(args)  # 加载数据集
    train(args, data, show_loss, show_topk)  # 进行训练及评估
    tf.reset_default_graph()
    args.dataset="shenlun"
    print(args.dataset)
    data = load_data(args)
    train(args, data, show_loss, show_topk)
    time.sleep(3600)
