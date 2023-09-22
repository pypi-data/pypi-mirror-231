import numpy as np
from glob import glob
import os
import cv2
import tifffile

from cellbin.modules.registration import Registration


def merge3ch(ch0, ch1):
    h0, w0 = ch1.shape
    hr, wr = (int(h0 / 3), int(w0 / 3))
    dim = (wr, hr)
    ch1r = cv2.resize(ch1, dim)
    ch0r = cv2.resize(ch0, dim)
    arr = np.zeros((hr, wr, 3), dtype=np.uint8)
    arr[:, :, 0] = ch0r
    arr[:, :, 2] = 100 * ch1r

    return arr


def json_to_regist(regist_path):
    import h5py
    ipr_path = glob(os.path.join(regist_path, "**.ipr"))[0]
    with h5py.File(ipr_path, "r") as f:
        # json_obj = json.load(f)
        scale_x = f["Register"].attrs["ScaleX"]
        scale_y = f["Register"].attrs["ScaleY"]
        rotation = f["Register"].attrs["Rotation"]
        # chip_template = f["ChipInfo"]["FOVTrackTemplate"]
        # offset_ori = f["AnalysisInfo"]["input_dct"]["offset"]
    chip_template = [[240, 300, 330, 390, 390, 330, 300, 240, 420], [240, 300, 330, 390, 390, 330, 300, 240, 420]]
    fov_stitched_path = glob(os.path.join(regist_path, '**fov_stitched.tif'))[0]
    fov_stitched = tifffile.imread(fov_stitched_path)

    # czi mouse brain -> stitch shape (2, x, x)
    if len(fov_stitched.shape) == 3:
        fov_stitched = fov_stitched[0, :, :]

    # try:
    #     gene_exp_path = glob(os.path.join(regist_path, "**raw.tif"))[0]
    # except IndexError:
    #     try:
    #         gene_exp_path = glob(os.path.join(regist_path, "3_vision", "**_gene_exp.tif"))[0]
    #     except IndexError:
    #         gene_exp_path = glob(os.path.join(regist_path, "3_vision", "**.gem.tif"))[0]

    gene_exp_path = glob(os.path.join(regist_path, "**gene.tif"))[0]
    gene_exp = cv2.imread(gene_exp_path, -1)

    track_template = np.loadtxt(glob(os.path.join(regist_path, '**template.txt'))[0])  # stitch template
    flip = True
    # im_shape = np.loadtxt(os.path.join(regist_path, "4_register", "im_shape.txt"))
    rg = Registration()
    rg.mass_registration_stitch(
        fov_stitched,
        gene_exp,
        chip_template,
        track_template,
        scale_x,
        scale_y,
        rotation,
        flip
    )
    print(rg.offset, rg.rot90, rg.score)
    rg.transform_to_regist()
    regist_img = rg.regist_img
    tifffile.imwrite(os.path.join(regist_path, "new_regist_1.tif"), regist_img)


if __name__ == '__main__':
    import time
    start = time.time()
    test_path = r"D:\Data\regist\FP200000340BR_D1"
    json_to_regist(test_path)
    end = time.time()
    print(f"time cost {end - start}")
