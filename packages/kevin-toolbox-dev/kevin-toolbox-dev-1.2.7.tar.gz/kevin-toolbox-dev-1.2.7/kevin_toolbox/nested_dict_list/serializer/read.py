import os
import time
from kevin_toolbox.patches import for_os
from kevin_toolbox.data_flow.file import json_
import kevin_toolbox.nested_dict_list as ndl
from kevin_toolbox.nested_dict_list.serializer.variable import SERIALIZER_BACKEND


def read(input_path, **kwargs):
    """
        读取 input_path 中保存的嵌套字典列表

        参数：
            input_path:             <path> 文件夹或者 .tar 文件，具体结构参考 write()
    """
    assert os.path.exists(input_path)

    # 解压
    temp_dir = None
    if os.path.isfile(input_path) and input_path.endswith(".tar"):
        while True:
            temp_dir = os.path.join(os.path.dirname(input_path), f'temp{time.time()}')
            if not os.path.isdir(temp_dir):
                os.makedirs(temp_dir)
                break
        for_os.unpack(source=input_path, target=temp_dir)
        input_path = os.path.join(temp_dir, os.listdir(temp_dir)[0])

    # 读取 var
    var = json_.read(file_path=os.path.join(input_path, "var.json"), b_use_suggested_converter=True)

    # 读取被处理的节点
    processed_nodes = []
    if os.path.isfile(os.path.join(input_path, "record.json")):
        for name, value in ndl.get_nodes(
                var=json_.read(file_path=os.path.join(input_path, "record.json"),
                               b_use_suggested_converter=True)["processed"], level=-1, b_strict=True):
            if value:
                processed_nodes.append(name)
    else:
        def converter(idx, value):
            processed_nodes.append(idx)
            return value

        ndl.traverse(
            var=var,
            match_cond=lambda _, __, value: isinstance(value, (dict,)) and "backend" in value and "name" in value,
            action_mode="replace", converter=converter, b_use_name_as_idx=True, traversal_mode="bfs",
            b_traverse_matched_element=False)

    # 恢复被处理的节点
    for name in processed_nodes:
        value = ndl.get_value(var=var, name=name)
        if isinstance(value, (dict,)) and "backend" in value and "name" in value:
            bk = SERIALIZER_BACKEND.get(name=value.pop("backend"))(folder=os.path.join(input_path, "nodes"))
            ndl.set_value(var=var, name=name, value=bk.read(**value))

    #
    if temp_dir is not None:
        for_os.remove(path=temp_dir, ignore_errors=True)

    return var


if __name__ == '__main__':
    res = read(
        "/home/SENSETIME/xukaiming/Desktop/my_repos/python_projects/kevin_toolbox/kevin_toolbox/nested_dict_list/serializer/temp3.tar")
    print(res)
