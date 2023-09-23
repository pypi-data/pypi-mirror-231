from typing import Dict
from xmlrpc.client import Boolean

remember_dict: Dict[str, object] = {
    "packages": [],
    "current_pid": "",
    "pids": ""
}


def remember_value_force(key, value):
    remember_dict[key] = value


# 当传入value的时候全局缓存中以key为键保存value
#       - False表示已存在同样的值
#       - True表示值不一样直接保存
# 当不传入value的时候表示取出值
def remember_value(key, value=None):
    if value:
        if key in remember_dict:
            var = remember_dict[key]
            if equal_any(var, value):
                # 已存在就认为保存失败
                return False
        remember_dict[key] = value
        # 保存成功
        return True
    else:
        if key in remember_dict:
            return remember_dict[key]
        return None


def remember_values_reset():
    packages = remember_dict["packages"]
    remember_dict.clear()
    remember_dict["packages"] = packages
    remember_dict["pids"] = []


# 当传入pid的时候表示全局缓存中保存pid
# 当bu传入pid的时候表示取出全局缓存中的pid
def remember_current_pid(pid=None):
    if pid:
        remember_dict["current_pid"] = pid
    if "current_pid" not in remember_dict:
        remember_dict["current_pid"] = ""
    return remember_dict["current_pid"]


# 把value保存到key对应的list中
# 如果不传入value，则表示取出key对应的list
def remember_list(key, value=None):
    if value:
        if key not in remember_dict:
            remember_dict[key] = [value]
            return True
        values: list = remember_dict[key]
        if values.count(value) == 0:
            values.append(value)
            return True
        return False
    else:
        if key in remember_dict:
            return remember_dict[key]
        return []


# 移除全局缓存中key对应的集合中的value
def global_list_remove(key, value):
    if key in remember_dict:
        values: list = remember_dict[key]
        if values.count(value) != 0:
            values.remove(value)
            return True
    return False


def equal_len(left: str, right: str):
    if any([not left, not right]):
        return False
    length = len(left)
    if length == len(right):
        if length <= 5:
            return left == right
        else:
            # 取3个数比较是否一致即可 6 2 4 6
            i = int(length / 3)
            i1 = i * 2
            i2 = i * 3 - 1
            return all([left[i] == right[i], left[i1] == right[i1], left[i2] == right[i2], ])
    return False


def equal_any(left, right):
    if hasattr(left, '__len__') and hasattr(right, '__len__'):
        # if all([hasattr("left", '__len__'), hasattr("right", '__len__')]):
        return equal_len(left, right)
    else:
        return left == right


# 字符串转为列表
# my_string = "Hello, World!"
# my_list = list(my_string)
# print(my_list)  # 输出: ['H', 'e', 'l', 'l', 'o', ',', ' ', 'W', 'o', 'r', 'l', 'd', '!']

# 元组转为列表
# my_tuple = (1, 2, 3)
# my_list = list(my_tuple)
# print(my_list)  # 输出: [1, 2, 3]

# 字典转为列表
# my_dict = {'a': 1, 'b': 2, 'c': 3}
# my_list = list(my_dict)
# print(my_list)  # 输出: ['a', 'b', 'c']

# tuple()：将可迭代对象转换为元组类型
# my_list = [1, 2, 3]
# my_tuple = tuple(my_list)
# print(my_tuple)  # 输出: (1, 2, 3)
# print(type(my_tuple))  # 输出: <class 'tuple'>

# str()：将对象转换为字符串类型  str(9090)
# float()：将对象转换为浮点数类型。 float("90")
# int()：将对象转换为浮点数类型。 int("90")


if __name__ == '__main__':
    print(int(6 / 4))
    print(remember_list("te", 90))
    print(remember_list("te"))
    print(remember_value("te", "90"))
    print(not remember_value("te", "90"))
    print(all([hasattr("left", '__len__'), hasattr("right", '__len__')]))
    print(hasattr("left", '__len__') and hasattr("right", '__len__'))
    print(equal_len("1234543", "1234543"))
    print(equal_len("1234543", "1234"))
    print(remember_current_pid("pid") in remember_list("pids"))
