import glob
import os.path
from typing import Sequence

import fitz
import img2pdf
from tqdm import tqdm

from xoffice.utils import compress_pic, make_dirs

# 标准纸张尺寸
A0 = (841, 1189)
A1 = (594, 841)
A2 = (420, 594)
A3 = (297, 420)
A4 = (210, 297)
A5 = (148, 210)
A6 = (105, 148)
A0_L = (1189, 841)
A1_L = (841, 594)
A2_L = (594, 420)
A3_L = (420, 297)
A4_L = (297, 210)
A5_L = (210, 148)
A6_L = (148, 105)


def img_to_pdf(
        dir_path: str,
        free: bool = False,
        size: Sequence = None,
        compress: bool = False,
        compress_target: int = 200,
        out_path: str = None
):
    """
    图片转 pdf 文件
    :param dir_path: 图片所在文件夹，文件夹中图片请按照顺序编号，例如 0001.jpg、0002.jpg
    :param free: 设为 True 后，页面尺寸随图片尺寸动态变化，两者始终保持一致
    :param size: 页面尺寸
    :param compress: 设为 True 后，对图片进行压缩，降低图片质量。开启此功能会大幅延长 pdf 文件生成时间
    :param compress_target: 图片压缩的目标体积，kB
    :param out_path: 输出的 pdf 文件地址，为空时默认在图片文件夹所在目录下创建同名 pdf 文件
    :return:
    """
    if size is None:
        size = A4

    layout_fun = img2pdf.default_layout_fun
    if not free:
        size = (img2pdf.mm_to_pt(size[0]), img2pdf.mm_to_pt(size[1]))
        layout_fun = img2pdf.get_layout_fun(size)

    split_dir = os.path.split(dir_path)
    if out_path is None:
        basename = split_dir[1] + ".pdf"
        out_path = os.path.join(split_dir[0], basename)

    imgs = []
    for name in tqdm(glob.glob(os.path.join(dir_path, "*.*"))):
        if not compress:
            imgs.append(name)
        else:
            imgs.append(compress_pic(name, target_size=compress_target))

    make_dirs(os.path.split(out_path)[0])
    with open(out_path, "wb") as f:
        f.write(img2pdf.convert(imgs, layout_fun=layout_fun))


def pdf_to_img(
        file_path: str,
        index: Sequence[int] = None,
        out_dir: str = None,
        zoom_x: float = 4,
        zoom_y: float = 4,
        rotation_angle: float = 0
):
    """
    pdf 文件转为 png 图片
    :param file_path: pdf 文件路径
    :param index: 可以指定将哪些页面转为图片，序号从 0 开始
    :param out_dir: 输出文件夹，默认在 pdf 文件所在文件夹创建同名文件夹保存图片
    :param zoom_x: x 轴缩放尺寸
    :param zoom_y: y 轴缩放尺寸
    :param rotation_angle: 页面旋转角度，顺时针为正
    :return:
    """
    if out_dir is None:
        tem = os.path.split(file_path)
        dir_name = os.path.splitext(tem[1])[0]
        out_dir = os.path.join(tem[0], dir_name)
    make_dirs(out_dir)

    with fitz.open(file_path) as pdf:
        num = pdf.page_count
        fill_num = len(str(num))
        img_format = "%0{}d.png".format(fill_num)

        for page_index in tqdm(range(num)):
            if index is not None:
                if page_index not in index:
                    continue
            page = pdf[page_index]
            # 设置缩放和旋转系数,zoom_x, zoom_y取相同值，表示等比例缩放
            trans = fitz.Matrix(zoom_x, zoom_y).prerotate(rotation_angle)
            pm = page.get_pixmap(matrix=trans, alpha=False)
            file_path = os.path.join(out_dir, img_format % (page_index + 1))
            pm.save(file_path)
