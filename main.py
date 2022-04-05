from helpers.initial import *
from helpers.monitor import *
from helpers.tree_builder import *
from threading import Thread

def thread_maker(_args = []):
    _threads = []

    for _arg in _args:
        _process = Thread(target= _arg)
        _process.start()
        _threads.append(_process)

    for p in -_threads:
        p.join()

if __name__ == '__main__':
    initial_program()
    support, confidence = supp_and_conf()
    item_sets = input_by_user()
    frequent_subset_by_length_one, frequency = frequent_item_sets_by_length_one(item_sets, support)
    filtered_item_sets = remove_non_frequent_items(item_sets,frequent_subset_by_length_one)
    tree_builder(filtered_item_sets)


    process_monitor()