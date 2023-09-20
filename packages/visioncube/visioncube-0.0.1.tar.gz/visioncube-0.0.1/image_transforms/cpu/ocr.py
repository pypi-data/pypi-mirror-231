#!/usr/bin/python3
# -*- coding:utf-8 -*-

"""
author：yannan1
since：2023-06-06
"""
import easyocr

from ..common import DEFAULT_IMAGE_FIELD, AbstractTransform

__all__ = [
    # 'OCR',
]


class OCR(AbstractTransform):

    def __init__(self, lang: str = 'ch_sim') -> None:
        """OCR, 光学字符识别

        Args:
            lang: Language codes, 识别语言, {"ch_sim", "en", "ko", "ja"}, "ch_sim"
        """
        self.reader = easyocr.Reader([lang], gpu=False)

    def __call__(self, doc: dict) -> dict:
        image_field = doc.get('image_field', DEFAULT_IMAGE_FIELD)
        if image_field and image_field in doc:
            image = doc[image_field]
            doc['ocr'] = self.reader.readtext(image)

        return doc
