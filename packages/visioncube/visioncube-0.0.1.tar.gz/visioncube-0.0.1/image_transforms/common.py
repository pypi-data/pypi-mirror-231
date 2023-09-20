#!/usr/bin/env python3
import time
from ast import literal_eval

import cv2
import torch
import numpy as np
from torchvision.transforms import InterpolationMode
from imgaug import augmenters as iaa, BoundingBox, BoundingBoxesOnImage, SegmentationMapsOnImage, \
    Keypoint, KeypointsOnImage, HeatmapsOnImage

__all__ = [
    'DEFAULT_IMAGE_FIELD',
    'DEFAULT_BBOX_FIELD',
    'DEFAULT_MASK_FIELD',
    'DEFAULT_HEATMAP_FIELD',
    'DEFAULT_KEYPOINTS_FIELD',
    'INTERPOLATION',
    'eval_arg',
    'apply_augmenter',
    'AbstractTransform',
    'ImgaugAdapter',
    'SampleCuda',
    'SampleCPU',
]

DEFAULT_IMAGE_FIELD = 'image'
DEFAULT_BBOX_FIELD = 'bboxes'
DEFAULT_MASK_FIELD = 'mask'
DEFAULT_HEATMAP_FIELD = 'heatmap'
DEFAULT_KEYPOINTS_FIELD = 'keypoints'

INTERPOLATION = {
    'nearest': InterpolationMode.NEAREST,
    'cubic': InterpolationMode.BICUBIC,
    'linear': InterpolationMode.BILINEAR,
    'box': InterpolationMode.BOX,
    'hamming': InterpolationMode.HAMMING
}


def eval_arg(value, type_):
    if isinstance(value, str):
        if type_ is None:
            try:
                return literal_eval(value)
            except (ValueError, TypeError, SyntaxError, MemoryError, RecursionError):
                raise ValueError()
        else:
            if isinstance(value, type_):
                return value
            return type_(value)
    elif type_ is not None and not isinstance(value, type_):
        return type_(value)
    else:
        return value


def apply_augmenter(
        sample,
        augmenter: iaa.Augmenter):
    if augmenter is None:
        return sample.output()

    if not isinstance(augmenter, iaa.Augmenter):
        raise RuntimeError('Invalid augmenter.')

    if sample.image is None:
        return sample.output()

    aug_args = sample.get_args()
    aug_result = augmenter(**aug_args)

    if len(aug_args) == 1:
        aug_result = [aug_result]
    sample.set_args(aug_result)

    return sample


class AbstractTransform(object):

    def __call__(self, doc):
        raise NotImplementedError()


class ImgaugAdapter(AbstractTransform):

    def __init__(self, augmenter: iaa.Augmenter):
        self.augmenter = augmenter

    def __call__(self, doc):
        return apply_augmenter(doc, self.augmenter)


class AbstractSample(object):

    def __init__(self, doc):
        self.image = self._handle_image(doc)
        self.shape = self.get_image_shape()
        self.mask = self._handle_mask(doc)
        self.bboxes = self._handle_bboxes(doc)
        self.heatmap = self._handle_heatmap(doc)
        self.keypoints = self._handle_keypoints(doc)

    def _handle_image(self, doc):
        ...

    def _handle_mask(self, doc):
        ...

    def _handle_bboxes(self, doc):
        ...

    def _handle_heatmap(self, doc):
        ...

    def _handle_keypoints(self, doc):
        ...

    def get_image_shape(self):
        if self.image is not None:
            return self.image.shape


class SampleCuda(AbstractSample):

    def __init__(self, doc):
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        super().__init__(doc)

    def _handle_image(self, doc):

        image = doc.get(DEFAULT_IMAGE_FIELD)
        if image is None:
            return None

        if not torch.is_tensor(image):
            image = torch.from_numpy(image.copy()).to(self.device)
            image = image.permute((2, 0, 1)).float()

        return image

    def _handle_mask(self, doc):

        mask = doc.get(DEFAULT_MASK_FIELD)
        if mask is None:
            return None

        if isinstance(mask, bytes):
            mask = cv2.imdecode(np.frombuffer(mask, np.byte), cv2.IMREAD_GRAYSCALE)

        if not torch.is_tensor(mask):
            mask = torch.tensor(mask).unsqueeze(0).to(self.device)

        return mask

    def _handle_bboxes(self, doc):

        bboxes = doc.get(DEFAULT_BBOX_FIELD)
        if bboxes is None:
            return None

        if not torch.is_tensor(bboxes):
            bboxes = torch.tensor(bboxes).to(self.device)

        return bboxes

    def _handle_heatmap(self, doc):

        heatmap = doc.get(DEFAULT_HEATMAP_FIELD)
        if heatmap is None:
            return None

        if not torch.is_tensor(heatmap):
            heatmap = torch.from_numpy(heatmap.copy()).to(self.device)
            heatmap = heatmap.permute((2, 0, 1)).float()

        return heatmap

    def _handle_keypoints(self, doc):

        keypoints = doc.get(DEFAULT_KEYPOINTS_FIELD)
        if keypoints is None:
            return None

        if not torch.is_tensor(keypoints):
            keypoints = torch.tensor(keypoints).to(self.device)

        return keypoints

    def output(self):

        doc = {}
        if self.image is not None:
            doc[DEFAULT_IMAGE_FIELD] = self.image.permute((1, 2, 0)).cpu().numpy()

        if self.mask is not None:
            doc[DEFAULT_MASK_FIELD] = self.mask.squeeze(0).cpu().numpy()

        if self.bboxes is not None:
            doc[DEFAULT_BBOX_FIELD] = self.bboxes.cpu().numpy()

        if self.heatmap is not None:
            doc[DEFAULT_HEATMAP_FIELD] = self.heatmap.permute((1, 2, 0)).cpu().numpy()

        if self.keypoints is not None:
            doc[DEFAULT_KEYPOINTS_FIELD] = self.keypoints.cpu().numpy()

        return doc


class SampleCPU(AbstractSample):

    def __init__(self, doc):
        super().__init__(doc)

    @staticmethod
    def _handle_image(doc):

        image = doc.get(DEFAULT_IMAGE_FIELD)
        if image is None:
            return None
        return image

    def _handle_mask(self, doc):

        mask = doc.get(DEFAULT_MASK_FIELD)
        if mask is None:
            return None

        if isinstance(mask, bytes):
            mask = cv2.imdecode(np.frombuffer(mask, np.byte), cv2.IMREAD_GRAYSCALE)
        assert isinstance(mask, np.ndarray)
        mask_rank = len(mask.shape)
        assert mask_rank == 2 or mask_rank == 3
        return SegmentationMapsOnImage(
            arr=mask,
            shape=self.shape
        )

    def _handle_bboxes(self, doc):

        bboxes = doc.get(DEFAULT_BBOX_FIELD)
        if bboxes is None:
            return None

        bbox_objs = []
        for bbox in bboxes:
            x1, y1, x2, y2, label = bbox
            bbox_obj = BoundingBox(x1, y1, x2, y2, label)
            bbox_objs.append(bbox_obj)
        return BoundingBoxesOnImage(
            bounding_boxes=bbox_objs,
            shape=self.shape
        )

    def _handle_heatmap(self, doc):

        heatmap = doc.get(DEFAULT_HEATMAP_FIELD)
        if heatmap is None:
            return None

        heatmap = (heatmap / 255).astype('float32')

        return HeatmapsOnImage(
            arr=heatmap,  # 输入应[0, 1], dtype: float32
            shape=self.shape
        )

    def _handle_keypoints(self, doc):

        keypoints = doc.get(DEFAULT_KEYPOINTS_FIELD)
        if keypoints is None:
            return None

        kps = []
        for kp in keypoints:
            kps.append(Keypoint(x=kp[0], y=kp[1]))

        return KeypointsOnImage(
            keypoints=kps,
            shape=self.shape
        )

    def get_args(self):

        aug_args = {}
        if self.image is not None:
            aug_args['image'] = self.image

        if self.bboxes is not None:
            aug_args['bounding_boxes'] = self.bboxes

        if self.mask is not None:
            aug_args['segmentation_maps'] = self.mask

        if self.heatmap is not None:
            aug_args['heatmaps'] = self.heatmap

        if self.keypoints is not None:
            aug_args['keypoints'] = self.keypoints

        return aug_args

    def set_args(self, aug_result):
        aug_result = iter(aug_result)

        if self.image is not None:
            self.image = next(aug_result)

        if self.bboxes is not None:
            self.bboxes = next(aug_result)

        if self.mask is not None:
            self.mask = next(aug_result)

        if self.heatmap is not None:
            self.heatmap = next(aug_result)

        if self.keypoints is not None:
            self.keypoints = next(aug_result)

    def _out_bboxes(self):

        bbox_objs = self.bboxes.remove_out_of_image_fraction(0.8).clip_out_of_image()
        bboxes = np.empty((len(bbox_objs), 5), dtype=np.float32)
        for i, bbox_obj in enumerate(bbox_objs):
            x1, y1, x2, y2, label = bbox_obj.x1, bbox_obj.y1, bbox_obj.x2, bbox_obj.y2, bbox_obj.label
            bboxes[i] = x1, y1, x2, y2, label

        return bboxes

    def _out_mask(self):
        return self.mask.arr.squeeze(-1)

    def out_heatmap(self):
        return self.heatmap.draw(size=self.heatmap.shape[:2])[0]

    def _out_keypoints(self):
        # keypoints_objs = self.keypoints.remove_out_of_image_fraction(0.8).clip_out_of_image()
        keypoints_objs = self.keypoints
        keypoints = np.empty((len(keypoints_objs), 2), dtype=np.float32)
        for i, kp in enumerate(keypoints_objs):
            keypoints[i] = kp.x, kp.y

        return keypoints

    def output(self):

        doc = dict()
        if self.image is not None:
            doc[DEFAULT_IMAGE_FIELD] = self.image

        if self.bboxes is not None:
            doc[DEFAULT_BBOX_FIELD] = self._out_bboxes()

        if self.mask is not None:
            doc[DEFAULT_MASK_FIELD] = self._out_mask()

        if self.heatmap is not None:
            doc[DEFAULT_HEATMAP_FIELD] = self.out_heatmap()

        if self.keypoints is not None:
            doc[DEFAULT_KEYPOINTS_FIELD] = self._out_keypoints()

        return doc
