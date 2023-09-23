import re

from tqdm import tqdm

from xoffice.excel import Excel
from xoffice.word import Word


def excel2word(word: str, excel: str, output: str):
    """
    根据 word 模板自动查找 excel 文件中的指定数据生成 word 报告
    :param word: word 模板文件地址
    :param excel: excel 数据文件
    :param output: 输出的 word 文档地址
    :return:
    """
    word = Word(word, visible=False)
    excel = Excel(excel, visible=False)
    targets = re.findall(r'({{ (.+?)/(.+?) }})', word.text)
    for target in tqdm(targets):
        text, sht, ind = target
        if sht.isdigit():
            sht = int(sht)
        try:
            if re.match(r'^[a-z]+[0-9]+$', ind, re.I) is not None:
                word.replace_text(text, excel.get_value(sht, ind))
            elif re.match(r'^c:(.+)$', ind) is not None:
                chart = re.match(r'^c:(.+)$', ind).group(1)
                if chart.isdigit():
                    chart = int(chart)
                excel.copy_chart(sht, chart)
                word.select_content_text(text)
                word.paste()
            elif re.match(r'^s:(.+)$', ind) is not None:
                shape = re.match(r'^s:(.+)$', ind).group(1)
                if shape.isdigit():
                    shape = int(shape)
                excel.copy_shape(sht, shape)
                word.select_content_text(text)
                word.paste()
            else:
                print(text + ":failed")
            print(text + ":success")
        except Exception:
            print(text + ":failed")
    word.save(output)
    word.close()
    excel.close()
