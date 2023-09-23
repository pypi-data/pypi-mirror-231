import xoffice
from xoffice.utils import md_to_html

if __name__ == '__main__':
    xoffice.excel2word("template.docx", "data.xlsx", "output.docx")
    xoffice.img_to_pdf("pdf-test", compress=True)
    xoffice.pdf_to_img("pdf-test.pdf", out_dir="pdf-test2", rotation_angle=-180)
    e = xoffice.EMail("1174543101@qq.com", "tdtcbhnckchbgbbd")
    with open("test.md", "r", encoding="utf-8") as f:
        e.easy_send(["xyw19970228@sina.com"], "test", md_to_html(f.read()), ["pdf-test/001.jpg", "wrong/path"])
