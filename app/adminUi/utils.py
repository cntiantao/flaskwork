import os
import uuid



def random_filename(old_filename):
    ext = os.path.splitext(old_filename)[1]
    new_filename = uuid.uuid4().hex + ext
    return new_filename


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ['jpg', 'jpeg', 'png', 'gif']




import pprint


class Tree(object):
    def __init__(self, data):
        self.data = data
        self.root_node = list()
        self.common_node = dict()
        self.tree = list()
        self.other = dict()
        self.node_name = dict()

    def find_root_node(self, father_id) -> list:
        """
        查找根节点
        :return:根节点列表
        """
        # self.root_node = list(filter(lambda x: x["father_id"] is None, data))
        for node in self.data:
            # 假定father_id是None就是根节点
            # 例如有些数据库设计会直接把根节点标识出来
            if node[father_id] is None:
                self.root_node.append(node)
        return self.root_node

    def find_common_node(self, father_id) -> dict:
        """
        寻找同级的对象
        :return: 共同的父节点字典
        """

        for node in self.data:
            father = node.get(father_id)
            # 排除根节点情况
            if father is not None:
                # 如果父节点ID不在字典中则添加到字典中
                if father not in self.common_node:
                    self.common_node[father] = list()
                self.common_node[father].append(node)
        return self.common_node

    def build_tree(self, primary_id, father_id, node, *args) -> list:
        """
        生成目录树
        :return:
        """
        self.find_root_node(father_id)
        self.find_common_node(father_id)
        self.node_name[node] = list()
        for root in self.root_node:
            # 生成其他字段
            for i in args:
                self.other[i] = root[i]

            self.other[primary_id] = root[primary_id]
            # 生成字典
            base = dict(**self.node_name, **self.other)

            self.other.clear()

            # 遍历查询子节点
            self.find_child(primary_id, base[primary_id], base[node], node, *args)
            # 添加到列表
            self.tree.append(base)
        return self.tree

    def find_child(self, primary_id, father_id: int, child_node: list, node, *args):
        """
        查找子节点, 深度优先
        :param father_id:父级ID
        :param child_node: 父级孩子节点
        :return:
        """
        # 获取共同父节点字典的子节点数据
        child_list = self.common_node.get(father_id, [])
        for item in child_list:
            # 生成其他字段
            for i in args:
                self.other[i] = item[i]

            self.other[primary_id] = item[primary_id]
            # 生成字典
            base = dict(**self.node_name, **self.other)

            self.other.clear()

            # 遍历查询子节点
            self.find_child(primary_id, item[primary_id], base[node], node, *args)
            # 添加到列表
            child_node.append(base)


data = [
    {"a_id": 1, "parent_id": None, "name": "01", "name1": "01"},
    {"a_id": 2, "parent_id": 1, "name": "0101", "name1": "01"},
    {"a_id": 3, "parent_id": 1, "name": "0102", "name1": "01"},
    {"a_id": 4, "parent_id": 1, "name": "0103", "name1": "01"},
    {"a_id": 5, "parent_id": 2, "name": "010101", "name1": "01"},
    {"a_id": 6, "parent_id": 2, "name": "010102", "name1": "01"},
    {"a_id": 7, "parent_id": 2, "name": "010103", "name1": "01"},
    {"a_id": 8, "parent_id": 3, "name": "010201", "name1": "01"},
    {"a_id": 9, "parent_id": 4, "name": "010301", "name1": "01"},
    {"a_id": 10, "parent_id": 9, "name": "01030101", "name1": "01"},
    {"a_id": 11, "parent_id": 9, "name": "01030102", "name1": "01"},
]
new_tree = Tree(data=data)

result = new_tree.build_tree('a_id', 'parent_id', 'items', 'name', 'name1')

pprint.pprint(result)
