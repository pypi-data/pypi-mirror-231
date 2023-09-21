__INIT_NUM__ = 100000000
__XOR_NUM__ = 0xF0F0F0

__all__ = ["uid_encode", "uid_decode"]
__auth__ = "baozilaji@gmail.com"


def uid_encode(uid):
    if not uid:
        return 0
    return (uid ^ __XOR_NUM__) + __INIT_NUM__


def uid_decode(pid):
    if not pid:
        return 0
    return (pid - __INIT_NUM__) ^ __XOR_NUM__
