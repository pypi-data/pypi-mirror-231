import cv2
import numpy as np

def readimg(path, mode="BGR"):
    """仅供BGR和RGB方式读取"""
    img = cv2.imread(path, cv2.IMREAD_COLOR)
    if mode=="RGB":
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return img

def add_weighted(img1, alpha, img2, beta):
    return img1.astype(float) * alpha + img2.astype(float) * beta

def normalize_np(image, mean, denominator=1):
    """零均值化法(中心化),可支持其他的均值化方法,修改denominator"""
    img = image.astype(np.float32)
    img -= mean
    img *= denominator
    return img

def normalization1(image, mean, std):
    image = image / 255  # values will lie between 0 and 1.
    image = (image - mean) / std
    return image

def normalization2(image, max, min):
    image_new = (image - np.min(image))*(max - min)/(np.max(image)-np.min(image)) + min
    return image_new

def clip(img, dtype, maxval):
    """截断图像的像素值到指定范围，并进行数据类型转换"""
    return np.clip(img, 0, maxval).astype(dtype)
