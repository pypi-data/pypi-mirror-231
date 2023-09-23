import numpy as np
from PIL import Image
import torch
import random
from thop import clever_format, profile
from torchsummary import summary

import torchvision.transforms.functional as F
from pyzjr.utils import gpu
from pyzjr.FM import getPhotopath
from torch.utils.data import DataLoader

def cvtColor(image):
    """Convert to RGB format"""
    if len(np.shape(image)) == 3 and np.shape(image)[2] == 3:
        return image
    else:
        img = image.convert('RGB')
        return img

def normalize_image(image, open=False):
    """
    将图像归一化到 [0, 1] 的范围
    :param image: 输入的图像
    :param open: 是否需要打开图像文件（默认为 False）
    :return: 归一化后的图像
    """
    if open:
        if isinstance(image, str):
            img_opened = Image.open(image)
            image = np.asarray(img_opened)
        else:
            raise ValueError("[pyzjr]:When `open` is True, `image` should be a file path string.")

    normalized_image = image / 255.0
    return normalized_image

def img2tensor(im, normalize=None):
    """NumPy图像数组转换为PyTorch张量"""
    tensor = torch.from_numpy(np.moveaxis(im / (255.0 if im.dtype == np.uint8 else 1), -1, 0).astype(np.float32))
    if normalize is not None:
        return F.normalize(tensor, **normalize)
    return tensor

def label2tensor(mask, num_classes, sigmoid):
    """标签或掩码图像转换为 PyTorch 张量"""
    if num_classes > 1:
        if not sigmoid:
            # softmax
            long_mask = np.zeros((mask.shape[:2]), dtype=np.int64)
            if len(mask.shape) == 3:
                for c in range(mask.shape[2]):
                    long_mask[mask[..., c] > 0] = c
            else:
                long_mask[mask > 127] = 1
                long_mask[mask == 0] = 0
            mask = long_mask
        else:
            mask = np.moveaxis(mask / (255.0 if mask.dtype == np.uint8 else 1), -1, 0).astype(np.float32)
    else:
        mask = np.expand_dims(mask / (255.0 if mask.dtype == np.uint8 else 1), 0).astype(np.float32)
    return torch.from_numpy(mask)

def resizepad_image(image, size, frame=True):
    """
    将调整图像大小并进行灰度填充
    :param image: 输入图像, PIL Image 对象
    :param size: 目标尺寸，形如 (width, height)
    :param frame: 是否进行不失真的resize
    :return: 调整大小后的图像，PIL Image 对象
    """
    iw, ih = image.size
    w, h = size
    if frame:
        scale = min(w/iw, h/ih)
        nw = int(iw*scale)
        nh = int(ih*scale)

        image = image.resize((nw,nh), Image.BICUBIC)
        new_image = Image.new('RGB', size, (128,128,128))
        new_image.paste(image, ((w-nw)//2, (h-nh)//2))
        return new_image, nw, nh
    else:
        new_image = image.resize((w, h), Image.BICUBIC)
        return new_image

def seed_torch(seed=11):
    """
    :param seed:设置随机种子以确保实验的可重现性
    """
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False

def summarys(input_shape, model):
    """
    打印模型的摘要信息，并计算模型的总浮点运算量和总参数数量
    :param input_shape:
    :param model:要进行计算的模型
    """
    device = gpu()
    models = model.to(device)
    summary(models, (3, input_shape[0], input_shape[1]))

    dummy_input = torch.randn(1, 3, input_shape[0], input_shape[1]).to(device)
    flops, params = profile(models.to(device), (dummy_input, ), verbose=False)
    flops = flops * 2
    flops, params = clever_format([flops, params], "%.3f")
    print('Total GFLOPS: %s' % (flops))
    print('Total params: %s' % (params))

def approximate_image(image):
    """
    Convert a single channel image into a binary image.
    Args:
        image : numpy array of image in datatype int16
    Return :
        image : numpy array of image in datatype uint8 only with 255 and 0
    """
    image[image > 127.5] = 255
    image[image < 127.5] = 0
    image = image.astype("uint8")
    return image

def ceilfloor_image(image):
    """
    The pixel value of the input image is limited between the maximum value of 255 and the minimum value of 0
    Args:
        image : numpy array of image in datatype int16
    Return :
        image : numpy array of image in datatype uint8 with ceilling(maximum 255) and flooring(minimum 0)
    """
    image[image > 255] = 255
    image[image < 0] = 0
    image = image.astype("uint8")
    return image

def find_mean(image_path):
    """
    Calculate the mean of all images under a given path
    Args:
        image_path : pathway of all images
    Return :
        mean : mean value of all the images
    """
    all_images,_ = getPhotopath(image_path,debug=False)
    num_images = len(all_images)
    mean_sum = 0

    for image in all_images:
        img_asarray = normalize_image(image, open=True)
        individual_mean = np.mean(img_asarray)
        mean_sum += individual_mean

    # Divide the sum of all values by the number of images present
    mean = mean_sum / num_images

    return mean

def find_stdev(image_path):
    """
    Args:
        image_path : pathway of all images
    Return :
        stdev : standard deviation of all pixels
    """
    # Initiation
    all_images, _ = getPhotopath(image_path, debug=False)
    num_images = len(all_images)

    std_sum = 0

    for image in all_images:
        img_asarray = normalize_image(image, open=True)
        individual_stdev = np.std(img_asarray)
        std_sum += individual_stdev

    std = std_sum / num_images

    return std

