"""
小小明的代码
CSDN主页：https://blog.csdn.net/as604049322
"""
__author__ = '小小明'
__time__ = '2021/8/17'

import re

import chardet


def read_bytes(file):
    with open(file, "rb") as f:
        txt_bytes = f.read()
    return txt_bytes


def read_txt(file):
    txt_bytes = read_bytes(file)
    encoding = chardet.detect(txt_bytes[:1024])["encoding"]
    if encoding is None:
        encoding = "u8"
    encoding = encoding.upper()
    if encoding in ("GB2312", "GBK"):
        encoding = "GB18030"
    return txt_bytes.decode(encoding)


def format_filename(title):
    return re.sub(r"[/\\:\*\?\<\>\|\"\s]+", " ", title).strip()


def write_txt(file, txt, mode="w", encoding="u8"):
    with open(file, mode, encoding=encoding) as f:
        f.write(txt)
