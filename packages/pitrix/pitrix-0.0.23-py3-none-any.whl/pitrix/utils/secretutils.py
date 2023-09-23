import hashlib
import hmac


def _constant_time_compare(first, second):
    """
    如果字符串或二进制输入相等，则返回True，否则返回False
    @param first:
    @param second:
    @return:
    """
    first = str(first)
    second = str(second)
    if len(first) != len(second):
        return False
    result = 0
    for x, y in zip(first, second):
        result |= ord(x) ^ ord(y)
    return result == 0


try:
    constant_time_compare = hmac.compare_digest
except AttributeError:
    constant_time_compare = _constant_time_compare

try:
    _ = hashlib.md5(usedforsecurity=False)


    def md5(string=b'', usedforsecurity=True):
        """
        返回md5哈希库对象
        @param string:
        @param usedforsecurity:
        @return:
        """
        return hashlib.md5(string, usedforsecurity=usedforsecurity)  # nosec
except TypeError:
    def md5(string=b'', usedforsecurity=True):
        """返回不带usedforsecurity参数的md5哈希库对象
        """
        return hashlib.md5(string)
