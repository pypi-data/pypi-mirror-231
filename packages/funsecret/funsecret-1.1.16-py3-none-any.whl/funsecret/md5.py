import hashlib


def get_md5_str(strs: str):
    """
    计算字符串md5值
    :param strs: 输入字符串
    :return: 字符串md5
    """
    m = hashlib.md5()
    m.update(strs.encode())
    return m.hexdigest()


def get_md5_file(path, chunk=1024 * 4):
    m = hashlib.md5()
    with open(path, "rb") as f:
        while True:
            data = f.read(chunk)
            if not data:
                break
            m.update(data)

    return m.hexdigest()
