# -*- coding: utf-8 -*-
import base64
import gzip
import sys
import zlib
from Crypto.Cipher import AES
from binascii import b2a_base64, a2b_base64
salt='resset'
url='http://192.168.0.228:5555'

errinfo=[
    # "账号或密码错误",
    # '该数据库无权限',
    # '登录成功',
    # '该数据库无权限',
    # '该接口不存在',
    # '剩余流量不足',
    # '该数据库权限已到期',
    # 'null'

]


def rpad(text, divisor: int, suffix):
    remain = len(text) % divisor
    if remain > 0:
        text += suffix * (divisor - remain)
    return text

def encrypt(text,  key):
    fmtkey, fmtiv = map(lambda s: s.encode()[:16].ljust(16, b'\0'), (key, salt))
    cryptor = AES.new(fmtkey, AES.MODE_CBC, fmtiv)
    fmttext = rpad(text.encode(), 16, b'\0')
    ciphertext = cryptor.encrypt(fmttext)
    return str(b2a_base64(ciphertext))[2:-3].rstrip('=')

def decrypt(text, key):
    fmtkey, fmtiv = map(lambda s: s.encode()[:16].ljust(16, b'\0'), (key, salt))
    cryptor = AES.new(fmtkey, AES.MODE_CBC, fmtiv)
    fmttext = rpad(text, 4, '=')
    return cryptor.decrypt(a2b_base64(fmttext)).rstrip(b'\0').decode()

def gzip_zip_base64(content):
    """
    Gzip 压缩方法
    字节比 1000(压缩前) : 263.78(压缩后)
    Gzip + Base64 压缩方法
    字节比大约在 1000(源字符串字节) : 353.46(压缩后所占字节)
    Args:
        content: 传入的文本

    Returns:
        Gzip > Bytes
        Gzip + Base64 > String
    """
    bytes_com = gzip.compress(str(content).encode("utf-8"))
    base64_data = base64.b64encode(bytes_com)
    back_content = str(base64_data.decode())
    print(f"## 源字符串所占字节大小: {sys.getsizeof(content)}, "
          # f"压缩后 Gzip 所占字节大小: {sys.getsizeof(bytes_com)}, "
          f"压缩后 Gzip + Base64 所占字节大小: {sys.getsizeof(back_content)}")
    return back_content

def gzip_unzip_base64(content,key):
    """
    Gzip + Base64 解压方法
    Args:
        content: 传入的文本

    Returns:
        String
    """
    md5data=decrypt(content, key)
    base64_data = base64.b64decode(md5data)
    bytes_decom = gzip.decompress(base64_data)
    back_content = bytes_decom.decode()
    return back_content

def zlib_zip(content):
    """
    Zlib 压缩方法
    字节比 1000(压缩前) : 261.27(压缩后)
    Zlib + Base64 压缩方法
    字节比 1000(压缩前) : 349.81(压缩后)
    Args:
        content: 传入的文本

    Returns:
        Zlib > Bytes
        Zlib + Base64 > String
    """
    print("## 正在使用 Zlib + Base64 压缩方法")
    bytes_com = zlib.compress(str(content).encode("utf-8"))
    base64_data = base64.b64encode(bytes_com)
    back_content = str(base64_data.decode())
    print(f"## 源字符串所占字节大小: {sys.getsizeof(content)}, "
          f"Zlib 压缩后所占字节大小: {sys.getsizeof(bytes_com)}, "
          f"压缩后 Zlib + Base64 所占字节大小: {sys.getsizeof(back_content)}")
    return back_content

def unzlib_zip(content):
    """
    Zlib 解压方法
    Args:
        content: 传入的文本

    Returns:
        String
    """
    base64_data = base64.b64decode(content)
    bytes_decom = zlib.decompress(base64_data)
    back_content = bytes_decom.decode()
    return back_content
