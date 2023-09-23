import contextlib
import errno
import hashlib
import json
import os
import stat
import tempfile
import time
import yaml

_DEFAULT_MODE = stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO


def ensure_tree(path, mode=_DEFAULT_MODE):
    """创建一个目录(以及所需的任何祖先目录)
    :param path: 要创建的目录
    :param mode: 目录创建权限
    """
    try:
        os.makedirs(path, mode)
    except OSError as exc:
        if exc.errno == errno.EEXIST:
            if not os.path.isdir(path):
                raise
        else:
            raise


def delete_if_exists(path, remove=os.unlink):
    """删除文件，但忽略文件未找到错误
    :param path: 要删除的文件
    :param remove: 删除传递路径的可选函数
    """
    try:
        remove(path)
    except OSError as e:
        if e.errno != errno.ENOENT:
            raise


def write_to_tempfile(content, path=None, suffix='', prefix='tmp'):
    """创建一个包含数据的临时文件
    Create a temporary file containing specified content, with a specified
    filename suffix and prefix. The tempfile will be created in a default
    location, or in the directory `path`, if it is not None. `path` and its
    parent directories will be created if they don't exist.
    :param content: bytestring to write to the file
    :param path: same as parameter 'dir' for mkstemp
    :param suffix: same as parameter 'suffix' for mkstemp
    :param prefix: same as parameter 'prefix' for mkstemp
    For example: it can be used in database tests for creating
    configuration files.
    .. versionadded:: 1.9
    """
    if path:
        ensure_tree(path)
    (fd, path) = tempfile.mkstemp(suffix=suffix, dir=path, prefix=prefix)
    try:
        os.write(fd, content)
    finally:
        os.close(fd)
    return path


def compute_file_checksum(path, read_chunksize=65536, algorithm='sha256'):
    """计算文件内容的校验和
    :param path: 文件路径
    :param read_chunksize: 从文件中读取的最大字节数,默认值是65536字节或64KB
    :param algorithm: 要使用的哈希算法名称。例如，'md5'，'sha256'， 'sha512'等等。默认为'sha256'
    :return: 校验和的十六进制摘要字符串
    """
    checksum = hashlib.new(algorithm)
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(read_chunksize), b''):
            checksum.update(chunk)
            time.sleep(0)
    return checksum.hexdigest()


def is_json(file_path):
    """检查文件是否为json类型
    :param file_path: The file path to check
    :returns: bool
    """
    with open(file_path, 'r') as fh:
        data = fh.read()
    try:
        json.loads(data)
        return True
    except ValueError:
        return False


def is_yaml(file_path):
    """检查文件是否为yaml类型
    :param file_path: The file path to check
    :returns: bool
    """
    with open(file_path, 'r') as fh:
        data = fh.read()
        is_yaml = False
        try:
            json.loads(data)
        except ValueError:
            try:
                yaml.safe_load(data)
                is_yaml = True
            except yaml.scanner.ScannerError:
                pass
        return is_yaml