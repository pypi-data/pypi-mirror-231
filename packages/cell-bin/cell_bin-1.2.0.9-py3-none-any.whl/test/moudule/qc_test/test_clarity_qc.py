import os
import cv2
import pandas as pd
import numpy as np

from cellbin.modules.iqc.clarity_qc import ClarityQC
from cellbin.utils import clog
from cellbin.image import Image
from cellbin.dnn.tseg.yolo.detector import TissueSegmentationYolo


class TestClarity(object):
    def __init__(self):
        self.cqc = ClarityQC()
        self.tissue_cut = TissueSegmentationYolo()

    def load_tc_model(self, model_path):
        self.tissue_cut.f_init_model(
            model_path=model_path
        )

    def load_model(self, model_path):
        self.cqc.load_model(model_path)

    def run(self, img_path, save_dir, name='unknown'):
        ir = Image()
        ir.read(img_path)
        img = ir.image
        img = np.squeeze(img)  # 防止redundant axis
        tissue_mask = self.tissue_cut.f_predict(img)
        contours, hierarchy = cv2.findContours(
            tissue_mask,
            cv2.RETR_CCOMP,
            cv2.CHAIN_APPROX_SIMPLE
        )
        x, y = 0, 0  # default
        w, h = ir.width, ir.height  # default
        max_contour = 0
        for cnt in contours:
            cur_len = len(cnt)
            if cur_len > max_contour:
                max_contour = cur_len
                rect = cv2.boundingRect(cnt)
                x, y, w, h = rect
        img_cut = img[y: y+h, x: x+w]
        del img
        # ir.write_s(image=img, output_path=r"D:\Data\clarity_05_18\test\test.tif", )
        # 进行图像质量分析
        self.cqc.run(img)
        # 将分析结果展示在原图上
        self.cqc.post_process()
        # 可保存图片
        draw_img = self.cqc.draw_img
        # ir.write_s(draw_img, os.path.join(save_dir, f"{name}_clarity_qc.tif"),)
        del self.cqc.draw_img
        cv2.imwrite(os.path.join(save_dir, f"{name}_clarity_qc.tif"), draw_img)  # optional
        self.cqc.cluster()
        # self.cqc.fig.show()  # optional
        self.cqc.fig.savefig(os.path.join(save_dir, f"{name}_clarity_qc.png"), )

    def batch_test(self, img_dir, save_dir):
        results = []
        for i in os.listdir(img_dir):
            clog.info(f"----------{i}")
            sn = i.split(".")[0]
            img_path = os.path.join(img_dir, i)
            self.run(img_path, save_dir, sn)
            results.append([sn, self.cqc.score])
        df = pd.DataFrame(results, columns=['name', 'score'])
        df_save_path = os.path.join(save_dir, "clarity_result.csv")
        df.to_csv(df_save_path, index=False)


if __name__ == '__main__':
    img_dir = r"D:\Data\clarity\DAPI_9_XJ_Big"
    save_dir = r"D:\Data\clarity\DAPI_9_XJ_Big_result_2"
    # model_path = r"D:\Data\weights\clarity_eval_mobilev3small05064_DAPI_20230202_pytorch.onnx"
    model_path = r"D:\PycharmProjects\timm\output\train\20230608-185916-mobilenetv3_small_050-64\mobilenetv3_small_050.onnx"
    tc_model_path = r"D:\Data\weights\tissueseg_yolo_SH_20230131_th.onnx"
    test_clarity = TestClarity()
    test_clarity.load_model(model_path)
    # test_clarity.load_tc_model(tc_model_path)
    test_clarity.batch_test(img_dir, save_dir=save_dir)

    # img_path = r"D:\Data\Json\FNjson\PFA人_胎盘绒毛_SS200000319TL_E4_stitched.tif"
    # save_dir = r"D:\Data\Json\c_result"
    # test_clarity.run(img_path, save_dir, )
