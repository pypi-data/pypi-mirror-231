import os

import numpy as np
import tifffile
import h5py

from cellbin.modules.stitching import Stitching
from cellbin.utils.file_manager import search_files, rc_key


def filename2index(file_name, style='motic', row_len=None):
    file_name = os.path.basename(file_name)
    if style.lower() in ['motic', 'cghd']:
        tags = os.path.splitext(file_name)[0].split('_')
        xy = list()
        for tag in tags:
            if (len(tag) == 4) and tag.isdigit(): xy.append(tag)
        x_str = xy[0]
        y_str = xy[1]
        return [int(y_str), int(x_str)]
    elif style.lower() == 'zeiss':
        line = os.path.splitext(file_name)[0].split('_')
        c = int(float(line[2]))
        r = int(float(line[1]))
        return [c, r]
    elif style.lower() == "leica dm6b":
        num = file_name.split("_")[1][1:]
        x = int(int(num) / row_len)
        y = int(int(num) % row_len)
        if x % 2 == 1:
            y = row_len - y - 1
        return [y, x]
    else:
        return None


def imagespath2dict(images_path, style='motic', row_len=None):
    image_support = ['.jpg', '.png', '.tif', '.tiff']
    fov_images = search_files(images_path, exts=image_support)
    src_fovs = dict()
    for it in fov_images:
        col, row = filename2index(it, style=style, row_len=row_len)
        src_fovs[rc_key(row, col)] = it

    return src_fovs


def test_stitching(image_src, rows, cols, chip_name, location=None, output_path=None):
    """
    Args:
        image_src: {'r_c': path, ...}
        rows:
        cols:
        location:
        output_path:
    """
    stitch = Stitching()
    stitch.set_size(rows, cols)
    if location is not None:
        stitch.set_global_location(loc)
    stitch.stitch(image_src, output)
    image = stitch.get_image()
    tifffile.imwrite(os.path.join(output, f'{chip_name}.tif'), image)

if __name__ == "__main__":
    ipr_path = r''
    src = r''
    output = r''

    with h5py.File(ipr_path) as conf:
        loc = conf['Research']['Stitch']['StitchFovLocation'][...]

    src_fovs = imagespath2dict(src)
    test_stitching(src_fovs, rows, cols, chip_name, loc, output)