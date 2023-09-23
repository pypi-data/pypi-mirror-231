import os
import xml.etree.ElementTree as ET
from io import BytesIO

import cv2
import markdown
import numpy as np
import toronado
from lxml import etree


def get_module_dir():
    """
    获取当前模块的主目录
    :return:
    """
    file_path = os.path.abspath(__file__)
    return os.path.dirname(file_path)


def make_dirs(*dirs):
    """
    创建任意个文件目录
    :param dirs: 待创建的文件夹路径
    :return:
    """
    for item in dirs:
        if item == "":
            continue
        os.makedirs(item, exist_ok=True)


def md_to_html(text: str, css: str = None) -> str:
    """
    md 格式文本转 html 字符串
    :param text: 待转换 md 格式字符串
    :param css: css 文件
    :return:
    """
    if css is None:
        css = os.path.join(get_module_dir(), "templates/md.css")
    # 读取 css 格式
    with open(css, "r", encoding="utf-8") as f:
        css = f.read()
    style = etree.Element("style")
    style.text = css

    # md 转 html
    text = markdown.markdown(text, extensions=["tables", "fenced_code"])
    e = etree.HTML(text)
    elements = e.xpath("/html/body/*")
    div = etree.Element("div")
    for item in elements:
        div.append(item)
    div.append(style)

    return toronado.from_string(ET.tostring(div, encoding="utf-8").decode("utf-8")).decode("utf-8")


def compress_pic(pic_path: str, target_size: int = 200, quality: int = 90, step: int = 5,
                 pic_type: str = '.jpg') -> bytes:
    """
    压缩图片
    :param pic_path: 图片路径
    :param target_size: 目标体积，kB
    :param quality: 起始压缩质量
    :param step: 压缩质量减小的步长
    :param pic_type: 图片格式
    :return:
    """
    with open(pic_path, 'rb') as f:
        pic_byte = f.read()

    img_np = np.frombuffer(pic_byte, np.uint8)
    img_cv = cv2.imdecode(img_np, cv2.IMREAD_ANYCOLOR)

    current_size = len(pic_byte) / 1024
    while current_size > target_size:
        pic_byte = cv2.imencode(pic_type, img_cv, [int(cv2.IMWRITE_JPEG_QUALITY), quality])[1]
        if quality - step < 0:
            break
        quality -= step
        current_size = len(pic_byte) / 1024
    return BytesIO(pic_byte).getvalue()
