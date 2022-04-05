from helpers.initial import *
from helpers.monitor import *
from helpers.tree_builder import *


if __name__ == '__main__':
    initial_program()
    support, confidence = supp_and_conf()
    item_sets = input_by_user()
    frequent_subset_by_length_one, frequency = frequent_item_sets_by_length_one(item_sets, support)
    filtered_item_sets = remove_non_frequent_items(item_sets,frequent_subset_by_length_one)
    tree = tree_builder(filtered_item_sets)

    print(len(tree))
    for i in tree.children:
        print(i.name, i.value)

    process_monitor()