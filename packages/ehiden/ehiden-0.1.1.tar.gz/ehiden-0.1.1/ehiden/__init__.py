import fitz
import math
from .ehiden_client import EhidenClient


def split_pdf_dm(pdf_data:bytes, length:int):
    """
    DMの伝票pdfデータを伝票毎に分割する

    Args:
        pdf_data:DMのPDFデータ
        length:分割数

    Returns:
        list[bytes]: 分割されたPDFデータ
    """
    ret = []
    doc = fitz.open(stream=pdf_data, filetype="pdf")
    for i in range(length):
        # 対応する伝票のページ、列、行を算出
        page_num = math.floor(i / 10)
        row_num = math.floor((i % 10) / 2)
        col_num = i % 2
        page = doc[page_num]

        # 250x200のboxで切り抜く
        top = 30
        left = 30
        width = 270
        height = 156
        rect = fitz.Rect(
            left + width * col_num,
            top + height * row_num,
            left + width * col_num + width,
            top + height * row_num + height)
        page.set_cropbox(rect)
        _doc = fitz.open()
        _doc.insert_pdf(doc, from_page=page_num, to_page=page_num)
        ret.append(_doc.tobytes())
    return ret
