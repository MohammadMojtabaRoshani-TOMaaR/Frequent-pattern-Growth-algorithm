from .inside_node_data_structure import InsideNodeDS


# from audioop import add
# from itertools import accumulate
# from typing import List, Sequence
#
#
# class Node:
#     def __init__(self):
#         self.data: InsideNodeDS
#         self.children: List[Node] = []
#         self.parent: Node = self
#
#
#
#     def __getitem__(self, i: int) -> 'Node':
#         return self.children[i]
#
#     def add_child(self):
#         child = Node()
#         self.children.append(child)
#         child.parent = self
#         return child
#
#     def get_node_value(self,_node):
#         return _node.data.value
#
#     def increment_node_value(self,_node):
#         _node.data.value = _node.data.value + 1
#
#
#     def __eq__(self, other):
#         if isinstance(other, Node):
#             return self.data.name == other.data.name and self.data.value == other.data.value
#         return False
#
#     def __len__(self):
#         return len(self.children)
#
#     # def __str__(self) -> str:
#     #     def _get_character(x, left, right) -> str:
#     #         if x < left:
#     #             return '/'
#     #         elif x >= right:
#     #             return '\\'
#     #         else:
#     #             return '|'
#     #
#     #     if len(self.children):
#     #         children_lines: Sequence[List[str]] = list(map(lambda child: str(child).split('\n'), self.children))
#     #         widths: Sequence[int] = list(map(lambda child_lines: len(child_lines[0]), children_lines))
#     #         max_height: int = max(map(len, children_lines))
#     #         total_width: int = sum(widths) + len(widths) - 1
#     #         left: int = (total_width - len(self.data) + 1) // 2
#     #         right: int = left + len(self.data)
#     #
#     #         return '\n'.join((
#     #             self.data.center(total_width),
#     #             ' '.join(map(lambda width, position: _get_character(position - width // 2, left, right).center(width), widths, accumulate(widths, add))),
#     #             *map(
#     #                 lambda row: ' '.join(map(
#     #                     lambda child_lines: child_lines[row] if row < len(child_lines) else ' ' * len(child_lines[0]),
#     #                     children_lines)),
#     #                 range(max_height))))
#     #     else:
#     #         return self.data


class Tree(object):
    def __init__(self, data: InsideNodeDS = None, children=None):
        self.data = data
        self.children = []
        if children is not None:
            for child in children:
                self.add_child(child)

    def __repr__(self):
        return self.data

    def __len__(self):
        return len(self.children)

    def add_child(self, _node: InsideNodeDS):
        # assert isinstance(_node, Tree)

        for index, _item in enumerate(self.children):
            if _node == _item:
                self.children[index].data.value = _item.data.value + 1
            else:
                self.children.append(_node)
