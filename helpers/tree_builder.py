from .tree import Tree
from .inside_node_data_structure import *


def tree_builder(_filtered_items):

    _tree_nodes = []
    _tree = Tree()
    for i_index,i_item in enumerate(_filtered_items):
        for j_index,j_item in enumerate(i_item):
            if i_index == 0 and j_index == 0:
                _tree_nodes = InsideNodeDS(name="root",value=None)
                _tree = Tree(_tree_nodes)
                pass
            else:
                _tree.add_child(InsideNodeDS(j_item,1))


        return _tree

