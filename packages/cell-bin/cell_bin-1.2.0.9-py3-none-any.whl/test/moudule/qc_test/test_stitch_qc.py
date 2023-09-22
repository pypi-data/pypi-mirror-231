import os
import numpy as np
from cellbin.modules.stitching import Stitching
from test.moudule.test_stitch import imagespath2dict

def test_stitch_qc(image_dict, fov_location):
    """
    用于显微镜拼接坐标评估
    Args:
        image_dict:
        fov_location:
    Return:

    """
    rows, cols = fov_location.shape[:2]

    stitch = Stitching()
    stitch.set_size(rows, cols)
    # stitch._init_parm(image_dict)
    # stitch._get_jitter(image_dict)
    stitch.stitch(image_dict)
    scope_x_dif, scope_y_dif = stitch._get_jitter_eval()
    cds_x_dif, cds_y_dif = stitch._get_stitch_eval()

    return [scope_x_dif, scope_y_dif], [cds_x_dif, cds_y_dif]

if __name__ == "__main__":
    image_path = r''

