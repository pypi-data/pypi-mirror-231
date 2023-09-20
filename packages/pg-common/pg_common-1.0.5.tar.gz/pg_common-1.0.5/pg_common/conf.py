from enum import Enum, unique


__all__ = ["GlobalRedisKey", "ObjectType", "RuntimeException", "GLOBAL_DEBUG"]
__auth__ = "baozilaji@gmail.com"


GLOBAL_DEBUG = True


class GlobalRedisKey(Enum):
    """
      redis key的父类，枚举类型，方便统一命名，避免冲突
    """
    pass


@unique
class ObjectType(Enum):
    REDIS = 0
    MONGO = 1
    BOTH = 2


class RuntimeException(Exception):
    """
      全局运行时异常
    """
    def __init__(self, name, msg):
        self.name = name
        self.msg = msg
