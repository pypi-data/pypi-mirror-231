# 学习率动态调整
import torch
import torch.optim as optim

def get_optimizer(model, optimizer_type='adam', init_lr=0.001, momentum=None, weight_decay=None):
    """
    根据指定的优化器类型返回相应的优化器对象，并根据批次大小调整初始学习率。

    :param model: 要优化的神经网络模型
    :param optimizer_type: 优化器类型，可以是 'adam' 或 'sgd'，默认为 'adam'
    :param init_lr: 初始学习率，默认为 0.001
    :param momentum: SGD优化器的动量参数，默认为 None
    :param weight_decay: 权重衰减（L2正则化）参数，默认为 None
    :return: 优化器对象
    """
    if optimizer_type == 'adam':
        optimizer = optim.Adam(model.parameters(), lr=init_lr, betas=(momentum or 0.9, 0.999),
                               weight_decay=(weight_decay or 1e-4))
    elif optimizer_type == 'sgd':
        optimizer = optim.SGD(model.parameters(), lr=init_lr, momentum=(momentum or 0.9), nesterov=True,
                              weight_decay=(weight_decay or 1e-4))
    else:
        raise ValueError("Unsupported optimizer type:: {}".format(optimizer_type))

    return optimizer

class CustomScheduler:
    def __init__(self, optimizer, num_step, epochs, warmup=True, warmup_epochs=1, warmup_factor=1e-3):
        self.optimizer = optimizer
        self.num_step = num_step
        self.epochs = epochs
        if warmup is False:
            warmup_epochs = 0
        self.warmup = warmup
        self.warmup_epochs = warmup_epochs
        self.warmup_factor = warmup_factor

        self.scheduler = self.get_scheduler()

    def get_scheduler(self):
        assert self.num_step > 0 and self.epochs > 0

        def f(x):
            """
            根据step数返回一个学习率倍率因子，
            """
            if self.warmup is True and x <= (self.warmup_epochs * self.num_step):
                alpha = float(x) / (self.warmup_epochs * self.num_step)

                return self.warmup_factor * (1 - alpha) + alpha
            else:
                # warmup后lr倍率因子从1 -> 0
                # 参考deeplab_v2: Learning rate policy
                return (1 - (x - self.warmup_epochs * self.num_step) / ((self.epochs - self.warmup_epochs) * self.num_step)) ** 0.9

        return optim.lr_scheduler.LambdaLR(self.optimizer, lr_lambda=f)

    def step(self):
        self.scheduler.step()

    def get_lr(self):
        return [group['lr'] for group in self.optimizer.param_groups]
