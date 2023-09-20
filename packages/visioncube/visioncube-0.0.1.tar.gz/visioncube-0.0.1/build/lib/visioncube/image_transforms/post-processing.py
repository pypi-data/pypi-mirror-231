#! /usr/bin/env python
# -*- coding UTF-8 -*-

"""
@Author : tangxx11
@Since  : 2023/5/23 上午11:27
"""
from typing import Tuple

import cv2 as cv
import numpy as np


class TraditionalProcess(object):

    def __init__(self, *args, **kwargs):
        pass

    def __call__(self, *args, **kwargs):
        pass


def convert_image_to_gray(image: np.ndarray) -> np.ndarray:
    if len(image.shape) == 3 and image.shape[-1] == 3:
        gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    else:
        gray = image
    return gray


class ThresholdingImage(object):

    def __init__(self, thr: float = 0):
        self.thr = thr
        self.method = cv.THRESH_BINARY + cv.THRESH_OTSU if thr == 0 else cv.THRESH_BINARY

    def __call__(self, image: np.ndarray, *args, **kwargs) -> np.ndarray:
        """
        Args:
            image: np.ndarray, could be BGR or grayscale
            *args:
            **kwargs:

        Returns:

        """
        gray = convert_image_to_gray(image)
        ret, threshold = cv.threshold(gray, self.thr, 255, self.method)
        return threshold


class TopHat(object):

    def __init__(self, kernel_shape: str = 'ellipse', kernel_size: Tuple = (3, 3)):
        """TopHat
        T_hat(f) = f - (f * b)
        适用于光照不均匀的图像前背景分割
        用于暗背景上的亮物体

        Args:
            kernel_shape: shape of the kernel, choose from ['rectangle', 'cross', 'ellipse']
        """
        if kernel_shape.lower() == 'ellipse':
            shape = cv.MORPH_ELLIPSE
        elif kernel_shape.lower() == 'rect':
            shape = cv.MORPH_RECT
        elif kernel_shape.lower() == 'cross':
            shape = cv.MORPH_CROSS
        else:
            raise ValueError('Wrong shape')

        self.kernel = cv.getStructuringElement(shape, kernel_size)

    def __call__(self, image: np.ndarray, *args, **kwargs) -> np.ndarray:
        """
        Args:
            image: binary mask, np.ndarray
            *args:
            **kwargs:

        Returns:

        """
        gray = convert_image_to_gray(image)
        tophat_img = cv.morphologyEx(gray, cv.MORPH_TOPHAT, self.kernel, *args, **kwargs)
        # tophat_img = gray - tophat_img

        return tophat_img


class BottomHat(TopHat):

    def __call__(self, image: np.ndarray, *args, **kwargs) -> np.ndarray:
        """
        B_hat(f) = (f * b) - f
        用于亮背景上的暗物体
        """

        gray = convert_image_to_gray(image)
        bottom_img = cv.morphologyEx(gray, cv.MORPH_BLACKHAT, self.kernel)
        # mask = bottom_img - gray
        return bottom_img


class MorphologyOpen(object):

    def __init__(self):
        """notes
        平滑轮廓，切断狭窄区域，消除小的孤岛和尖刺
        """


class MorphologyClose(object):

    def __init__(self):
        """notes
        平滑轮廓，融合狭窄间断和细长沟壑，消除小的孔洞
        """


class ConditionalDilate():

    def __init__(self):
        """
        在给定的前景范围内填充孔洞等
        X_k = (X_(k-1) + B) \cap A
        where A^c is the foreground of the image

        Args:
        """

    def __call__(self, bin_img: np.ndarray, *args, **kwargs) -> np.ndarray:
        """

        Args:
            bin_img: binary image
            *args:
            **kwargs:

        Returns:

        """
        cnts, _ = cv.findContours(bin_img, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

