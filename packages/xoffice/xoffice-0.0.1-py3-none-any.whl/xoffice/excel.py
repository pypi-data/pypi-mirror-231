import os.path
from typing import Union

import win32com.client as win32


class Excel:
    """
    Excel 常用自动化操作，主要是为了配合 Word 使用，因此只封装了获取数据的方法
    """

    def __init__(self, path: str, display_alerts: bool = False, visible: bool = True):
        """
        初始化
        :param path:
        :param display_alerts:
        :param visible:
        """
        try:
            self.app = win32.DispatchEx('ket.Application')
        except Exception:
            self.app = win32.DispatchEx('Excel.Application')
        self.app.DisplayAlerts = display_alerts
        self.app.Visible = visible
        self.doc = self.app.Workbooks.Open(os.path.abspath(path))
        self._sheets = {}

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

    def _get_sheet(self, name: Union[int, str]):
        """
        获取 sheet 对象
        :param name:
        :return:
        """
        if isinstance(name, int):
            name += 1
        sheet = self._sheets.get(name)
        if sheet is None:
            sheet = self.doc.Worksheets(name)
            self._sheets[name] = sheet
        return sheet

    def get_value(self, sht_name: Union[int, str], index: str):
        """
        获取指定单元格内数据
        :param sht_name:
        :param index:
        :return:
        """
        return self._get_sheet(sht_name).Range(index).Text

    def get_comment(self, sht_name: Union[int, str], index: str):
        """
        获取指定单元格的批注
        :param sht_name:
        :param index:
        :return:
        """
        return self._get_sheet(sht_name).Range(index).Comment.Text()

    def copy_chart(self, sht_name: Union[int, str], index: int):
        """
        复制指定图表
        :param sht_name:
        :param index: 图表序号
        :return:
        """
        return self._get_sheet(sht_name).ChartObjects(index + 1).Copy()

    def copy_shape(self, sht_name: Union[int, str], index: Union[str, int]):
        """
        复制指定图片，这里要注意，图表也会算在其中，使用序号时务必小心
        :param sht_name:
        :param index: 可以为图片的名称或其序号，此处的图片只能为浮动式图片
        :return:
        """
        if isinstance(index, int):
            index += 1
        return self._get_sheet(sht_name).Shapes(index).Copy()
