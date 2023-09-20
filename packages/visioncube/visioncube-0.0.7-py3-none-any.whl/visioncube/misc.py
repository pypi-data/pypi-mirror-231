#!/usr/bin/env python3


#
# class BrightnessCalibration(object):
#
#     def __init__(self):
#         pass
#
#     def _compute_lut(self, image: torch.Tensor, num_grids: int) -> torch.Tensor:
#         h, w = image.shape[:2]
#         x = image.float().reshape((1, 1, h, w))  # (1, 1, h, w)
#         gh, gw = h // num_grids, w // num_grids
#         x = F.avg_pool2d(
#             input=x,
#             kernel_size=(gh, gw),
#             stride=(gh, gw),
#             padding=(gh // 2, gw // 2),
#             count_include_pad=False
#         )
#         print(gh, gw)
#         print(x.shape)
#
#     def __call__(self, image: torch.Tensor) -> torch.Tensor:
#         pass
