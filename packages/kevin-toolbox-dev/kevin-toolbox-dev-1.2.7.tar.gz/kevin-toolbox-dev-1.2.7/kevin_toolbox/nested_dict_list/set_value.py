from kevin_toolbox.nested_dict_list import get_value
from kevin_toolbox.nested_dict_list.name_handler import parse_name, escape_node


def set_value(var, name, value, b_force=False):
    """
        通过解释名字得到取值方式，然后到 var 中将对应部分的值修改为 value。

        参数：
            var:            任意支持索引赋值的变量
            name:           <string> 名字
                                名字 name 的具体介绍参见函数 name_handler.parse_name()
                                假设 var=dict(acc=[0.66,0.78,0.99])，如果你想将 var["acc"][1] 设置为 100，那么可以将 name 写成：
                                    ":acc@1" 或者 "|acc|1" 等。
                                注意，在 name 的开头也可以添加任意非取值方式的字符，本函数将直接忽略它们，比如下面的:
                                    "var:acc@1" 和 "xxxx|acc|1" 也能正常写入。
            value:          待赋给的值
            b_force:        <boolean> 当无法设置时，是否尝试创建或者修改节点
                                默认为 False，此时若无法设置，则报错
                                当设置为 True，可能会对 var 的结构产生不可逆的改变，请谨慎使用。
                                    - 根据取值方式的不同，新创建或者修改的节点的类型可能是 dict 或者 list，
                                        对于 list，其中缺省值填充 None。
                                    - 当需要创建节点时，| 方式将优先创建 dict
                注意：
                    若 b_force 为 True 有可能不会在 var 的基础上进行改变，而是返回一个新的ndl结构，
                    因此建议使用赋值 var = ndl.set_value(var) 来避免可能的错误。
    """
    _, method_ls, node_ls = parse_name(name=name, b_de_escape_node=False)
    if len(node_ls) == 0:
        return value

    raw_key = escape_node(node=node_ls[-1], b_reversed=True, times=1)

    try:
        item = get_value(var=var, name=name[:-1 - len(node_ls[-1])])
        if method_ls[-1] == "@":
            key = eval(raw_key)
        elif method_ls[-1] == "|":
            try:
                _ = item[raw_key]
                key = raw_key
            except:
                key = eval(raw_key)
        else:
            key = raw_key

        if isinstance(item, (list,)) and isinstance(key, (int,)) and len(item) <= key:
            item.extend([None] * (key - len(item) + 1))
        item[key] = value
    except:
        if not b_force:
            raise ValueError(f'The location pointed to by name {name} does not exist in var')
        else:
            if method_ls[-1] in "|:":
                value = {raw_key: value}
            else:
                key = eval(raw_key)
                assert isinstance(key, (int,)) and key >= 0
                value = [None] * key + [value]
            var = set_value(var=var, name=name[:-1 - len(node_ls[-1])], value=value, b_force=b_force)

    return var
