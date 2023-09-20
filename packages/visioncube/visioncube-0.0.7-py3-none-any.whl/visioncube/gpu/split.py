#!/usr/bin/python3
# -*- coding:utf-8 -*-

"""
author：yannan1
since：2023-06-09
"""
import math
from typing import Sequence, Tuple

import torch

from ..common import AbstractTransform, DEFAULT_IMAGE_FIELD, eval_arg


class SlidingWindow(object):

    def __init__(self, win_size: int, overlap_ratio: float = 0.05) -> None:
        self.win_size = win_size
        self.overlap = int(win_size * overlap_ratio)

    def __call__(self, size: int) -> Sequence[Tuple[int, int, int]]:
        if size <= self.win_size:
            return [(0, size, 0)]

        win_size = self.win_size
        overlap = self.overlap
        num_wins = math.floor((size - win_size) / (win_size - overlap) + 0.5) + 1
        total = win_size + (num_wins - 1) * (win_size - overlap)
        remains = size - total
        # print(win_size, num_wins, total, remains)
        if remains == 0:
            num_big_overlaps = total - size
            num_small_overlaps = num_wins - 1
        elif remains > 0:
            # print('window expand')
            win_size += math.ceil(remains / num_wins)
            total = win_size + (num_wins - 1) * (win_size - overlap)
            num_big_overlaps = total - size
            num_small_overlaps = num_wins - 1 - num_big_overlaps
        else:
            # print('window squeeze')
            win_size -= math.floor(-remains / num_wins)
            total = win_size + (num_wins - 1) * (win_size - overlap)
            num_big_overlaps = total - size
            num_small_overlaps = num_wins - 1 - num_big_overlaps

        overlaps = [self.overlap + 1] * num_big_overlaps + [self.overlap] * num_small_overlaps
        win_list = [(0, win_size, 0)]
        pos = win_size
        for i in range(num_wins - 1):
            pos -= overlaps[i]
            win_list.append((pos, pos + win_size, overlaps[i]))
            pos += win_size
        return win_list


class Split(AbstractTransform):

    def __init__(
            self,
            max_size: int = 1200,
            win_size: int = 512,
            overlap_ratio: float = 0.05
    ) -> None:
        """Split, 拆分图像

        Args:
            win_size: Window size, 窗口大小, [1, 5000], 512
            overlap_ratio: Overlap ratio, 覆盖率, [0, 1], 0.05
        """
        super().__init__()
        win_size = eval_arg(win_size, None)
        overlap_ratio = eval_arg(overlap_ratio, None)

        self.sliding_win = SlidingWindow(win_size, overlap_ratio)
        self.max_area = max_size + max_size

    def __call__(self, doc: dict) -> dict:

        image_field = doc.get('image_field', DEFAULT_IMAGE_FIELD)
        if image_field and image_field in doc:
            image = doc[image_field]
            h, w = image.shape[2:]

            if h * w <= self.max_area:
                return doc
            h_win_list = self.sliding_win(h)
            w_win_list = self.sliding_win(w)

            thumbnails = []
            for row in h_win_list:
                y1, y2, yo = row
                for col in w_win_list:
                    x1, x2, xo = col

                    thumbnails.append({
                        'coordinate': [x1, y1, x2, y2, xo, yo],
                        'image': image[:, :, y1:y2, x1:x2]
                    })

            doc['thumbnails'] = thumbnails

        return doc


class Merge(AbstractTransform):

    def __init__(self) -> None:
        """Merge, 合并图像

        """
        super().__init__()

    def __call__(self, doc: dict) -> dict:

        image_field = doc.get('image_field', DEFAULT_IMAGE_FIELD)
        if image_field and image_field in doc:
            thumbnails = doc['thumbnails']
            image = doc[image_field]
            n, _, h, w = image.size()

            merge = torch.zeros((n, 3, h, w), dtype=image.dtype, device=image.device)

            for thumbnail in thumbnails:
                x1, y1, x2, y2, xo, yo = thumbnail['coordinate']
                merge[:, :, y1 + yo:y2, x1 + xo:x2] = thumbnail['image'][:, :, yo:, xo:]

            doc['merge'] = merge

        return doc
