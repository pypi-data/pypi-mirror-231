#!/usr/bin/python3
# -*- coding:utf-8 -*-

"""
author：yannan1
since：2023-06-16
"""
import numpy as np
from imgaug import augmenters as iaa

from ..common import AbstractTransform, ImgaugAdapter, eval_arg

__all__ = [
    # 'Normalize',
    'Add',
    'Multiply',
    'Solarize',
    'AdditiveGaussianNoise',
    'AdditiveSaltPepperNoise',
    'RandomAdd',
    'RandomMultiply',
    'RandomSolarize',
]


class Normalize(AbstractTransform):

    def __init__(self) -> None:
        """Normalize, 标准化, 算术变换
        """
        self.mean = np.array([0.485, 0.456, 0.406], np.float32) * 255
        self.std = np.array([0.229, 0.224, 0.225], np.float32) * 255

    def __call__(self, sample):
        if sample.image is None:
            return sample

        sample.image = (sample.image - self.mean) / self.std

        return sample


class Add(ImgaugAdapter):

    def __init__(self, value: float = 0.0) -> None:
        """Add, 加变换, 算术变换

        Args:
            value: Value, 偏移, [-255.0, 255.0], 0.0
        """
        value = eval_arg(value, None)
        super().__init__(iaa.Add(value=value))


class Multiply(ImgaugAdapter):

    def __init__(self, mul: float = 1.0) -> None:
        """Multiply, 乘变换, 算术变换

        Args:
            mul: mul, 系数, [0.8, 1.2], 1.0
        """
        mul = eval_arg(mul, None)
        super().__init__(iaa.Multiply(mul=mul))


class Solarize(ImgaugAdapter):

    def __init__(self, threshold: float = 255.0) -> None:
        """Solarize, 反转变换, 算术变换

        Args:
            threshold: Threshold, 阈值, [0.0, 255.0], 255.0
        """
        threshold = eval_arg(threshold, None)
        super().__init__(iaa.Solarize(threshold=threshold))


class AdditiveGaussianNoise(ImgaugAdapter):

    def __init__(self, mean: float = 0.0, std: float = 3.0) -> None:
        """AdditiveGaussianNoise, 高斯噪声, 算术变换

        Args:
            mean: Mean, 均值, [0, 1], 0.0
            std: Standard deviation, 标准差, [0, 15], 3.0
        """
        mean = eval_arg(mean, None)
        std = eval_arg(std, None)
        super().__init__(iaa.AdditiveGaussianNoise(loc=mean, scale=std))


class AdditiveSaltPepperNoise(ImgaugAdapter):

    def __init__(self, p: float = 0.01) -> None:
        """AdditiveSaltPepperNoise, 椒盐噪声, 算术变换

        Args:
            p: Probability, 概率, (0.0, 0.03), 0.01
        """
        p = eval_arg(p, None)
        super().__init__(iaa.SaltAndPepper(p=p))


class RandomAdd(ImgaugAdapter):

    def __init__(self, value_min: float = -255.0, value_max: float = 255.0) -> None:
        """RandomAdd, 随机加变换, 算术变换

        Args:
            value_min: Value minimum, 偏移最小值, [-255.0, 255.0], -255.0
            value_max: Value maximum, 偏移最大值, [-255.0, 255.0], 255.0
        """
        value_min = eval_arg(value_min, None)
        value_max = eval_arg(value_max, None)
        super().__init__(iaa.Add(value=(value_min, value_max)))


class RandomMultiply(ImgaugAdapter):

    def __init__(self, mul_min: float = 0.8, mul_max: float = 1.2) -> None:
        """RandomMultiply, 随机乘变换, 算术变换

        Args:
            mul_min: Multiplier minimum, 乘数最小值, [0.8, 1.2], 0.8
            mul_max: Multiplier maximum, 乘数最大值, [0.8, 1.2], 1.2
        """
        mul_min = eval_arg(mul_min, None)
        mul_max = eval_arg(mul_max, None)
        super().__init__(iaa.Multiply(mul=(mul_min, mul_max)))


class RandomSolarize(ImgaugAdapter):

    def __init__(
            self,
            p: float = 1.0,
            threshold_min: float = 0.0,
            threshold_max: float = 255.0
    ) -> None:
        """RandomSolarize, 随机反转变换, 算术变换

        Args:
            p: Probability, 变换概率, [0, 1.0], 0.5
            threshold_min: Threshold minimum, 阈值最小值, [0.0, 255.0], 0.0
            threshold_max: Threshold maximum, 阈值最大值, [0.0, 255.0], 255.0
        """
        p = eval_arg(p, None)
        threshold_min = eval_arg(threshold_min, None)
        threshold_max = eval_arg(threshold_max, None)
        super().__init__(iaa.Solarize(p=p, threshold=(threshold_min, threshold_max)))
