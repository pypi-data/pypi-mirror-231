#!/usr/bin/python3
# -*- coding:utf-8 -*-

"""
author：yannan1
since：2023-09-20
"""

from setuptools import setup

setup(
    name='visioncube',
    version='0.0.1',
    description='Image Processing Tools',
    author='yanaenen',
    install_requires=[
        'imgaug',
        'torch',
        'torchvision',
        'kornia',
        'numpy',
        'opencv-python',
        'easyocr',
        'easydict',
    ],
    package_dir={'visioncube': '.'},
    entry_points={
        'console_scripts': [
            'visioncube = image_transforms.pipeline:TransformPipeline'
        ]
    },
    platforms='any',
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
    include_package_data=True,
    zip_safe=False,
)
