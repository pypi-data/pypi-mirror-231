import os.path

import win32com.client as win32
from mailmerge import MailMerge

from xoffice.utils import make_dirs


def generate_docx_by_mailmerge(contents: dict, template: str, output: str):
    """
    以邮件合并的方式快速生产 docx 文档
    :param contents: 要替换到模板中的内容
    :param template: 文档模板
    :param output: 输出文件路径
    :return:
    """
    with MailMerge(template,
                   remove_empty_tables=False,
                   auto_update_fields_on_open="no") as document:
        document.merge(**contents)
        make_dirs(os.path.split(output)[0])
        document.write(output)


class Word:
    """
    Word 自动化常用操作
    """

    def __init__(self, path: str, display_alerts: bool = False, visible: bool = True):
        """
        初始化
        :param path: Word 文件地址
        :param display_alerts: 覆盖保存时是否出现警告提示
        :param visible: 程序窗口是否可见
        """
        try:
            # 调用 WPS 打开文件
            self.app = win32.DispatchEx('kwps.Application')
        except Exception:
            # 调用 Word 打开文件
            self.app = win32.DispatchEx('Word.Application')
        self.app.DisplayAlerts = display_alerts
        self.app.Visible = visible
        self.doc = self.app.Documents.Open(os.path.abspath(path))

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return self.close()

    def close(self):
        """
        关闭文档，退出应用程序
        :return:
        """
        self.doc.Close()
        self.app.Quit()

    def save(self, path: str):
        """
        另存为文件
        :param path:
        :return:
        """
        self.doc.SaveAs(os.path.abspath(path))

    @property
    def text(self) -> str:
        """
        获取文档中所有字符串，包括正文、页眉页脚、Shape 内文本
        :return:
        """
        texts = [self.doc.Content.Text]
        for section in self.doc.Sections:
            texts.append(section.Headers[0].Range.Text)
            texts.append(section.Footers[0].Range.Text)
            for shape in section.Headers[0].Shapes:
                if shape.TextFrame.HasText == -1:
                    texts.append(shape.TextFrame.TextRange.Text)
        for shape in self.doc.Shapes:
            if shape.TextFrame.HasText == -1:
                texts.append(shape.TextFrame.TextRange.Text)
        return "\r".join(texts)

    @staticmethod
    def _get_find_attrs(key: str, value: str):
        """
        辅助构造 Find.Execute 函数的参数
        :param key:
        :param value:
        :return:
        """
        return {
            "FindText": key,
            "MatchCase": True,
            "MatchWholeWord": False,
            "MatchWildcards": False,
            "MatchSoundsLike": False,
            "MatchAllWordForms": False,
            "Forward": True,
            "Wrap": 1,
            "Format": True,
            "ReplaceWith": value,
            "Replace": 2,
        }

    def _replace_content_text(self, key: str, value: str):
        """
        替换主题内容中的指定文本
        :param key:
        :param value:
        :return:
        """
        self.doc.Content.Find.Execute(**self._get_find_attrs(key, value))
        for shape in self.doc.Shapes:
            # 此处一定要判定 Shape 对象中是否包含文本，不然会报错
            if shape.TextFrame.HasText == -1:
                shape.TextFrame.TextRange.Find.Execute(**self._get_find_attrs(key, value))

    def _replace_header_and_footer_text(self, key: str, value: str):
        """
        替换页眉页脚中的指定文本
        :param key:
        :param value:
        :return:
        """
        for section in self.doc.Sections:
            section.Headers[0].Range.Find.Execute(**self._get_find_attrs(key, value))
            section.Footers[0].Range.Find.Execute(**self._get_find_attrs(key, value))
            for shape in section.Headers[0].Shapes:
                if shape.TextFrame.HasText == -1:
                    shape.TextFrame.TextRange.Find.Execute(**self._get_find_attrs(key, value))

    def replace_text(self, key: str, value: str):
        """
        替换文档中的指定文本
        :param key:
        :param value:
        :return:
        """
        self._replace_content_text(key, value)
        self._replace_header_and_footer_text(key, value)

    def replace_content_inline_shape(self, key: int, value: str):
        """
        替换文档主体内容中指定序号的内嵌图形，保持替换图片的宽度与原始图片相等
        :param key: 需要替换的内嵌图形在文档中的序号，从 0 开始
        :param value: 用于替换的图片路径
        :return:
        """
        pic_width = self.doc.InlineShapes[key].Width
        self.doc.InlineShapes[key].Select()
        new_pic = self.app.Selection.InlineShapes.AddPicture(os.path.abspath(value))
        pic_height = new_pic.Height / new_pic.Width * pic_width
        new_pic.Height = pic_height
        new_pic.Width = pic_width

    def select_content_text(self, text: str):
        """
        选中文档主体内容中的指定文本，搭配 paste 使用可以完成 office 软件间的部分互动
        :param text:
        :return:
        """
        return self.app.Selection.Find.Execute(FindText=text)

    def paste(self):
        """
        执行粘贴操作
        :return:
        """
        return self.app.Selection.PasteAndFormat(Type=19)

    def set_content_inline_shape_size(self, index: int = None, width: float = None, height: float = None):
        """
        保持图片长宽比的前提下设置指定序号的内嵌图像的宽度
        :param index: 序号从 0 开始
        :param width: 图片宽度，单位为 cm
        :param height: 图片高度，单位为 cm
        :return:
        """
        if index is None:
            index = self.doc.InlineShapes.Count - 1
        # 单位换算，磅到厘米
        if width is not None:
            width *= 28.35
        if height is not None:
            height *= 28.35
        shape = self.doc.InlineShapes[index]
        ratio = shape.Height / shape.Width
        if width is not None and height is None:
            height = ratio * width
        elif width is None and height is not None:
            width = height / ratio
        elif width is None and height is None:
            raise ValueError("width and height can not all be None")
        shape.Width = width
        shape.Height = height
