from anytree import Node, RenderTree


def tree_builder(_filtered_items):
    _nodes = []

    for i_index,i_item in enumerate(_filtered_items):
        for j_index,j_item in enumerate(i_item):
            if i_index == 0 and j_index == 0:
                new_node = Node(dict(j_item,1), parent=None)
                _nodes.append(new_node)
                pass
            elif [x for x in _nodes if x.name[0] == j_item]:
                _nodes.index()
            new_node = Node(dict(_item,1), parent=_nodes[index - 1])
            _nodes.append(new_node)

        return _nodes

