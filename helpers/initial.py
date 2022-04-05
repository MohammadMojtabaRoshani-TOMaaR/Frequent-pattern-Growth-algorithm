import sys
from collections import Counter
from termcolor import colored
from tabulate import tabulate


def initial_program():
    try:
        n = len(sys.argv)
        if n < 3:
            print(colored("ERROR> missing value, support and confident are required", "red"))
    except Exception:
        print("Exception")

def supp_and_conf():
    _support = int(sys.argv[1])
    _confidence = int(sys.argv[2])
    print(colored("Info> support: {} and confidence: {} are defined".format(_support, _confidence), "blue"))
    return _support, _confidence


def input_by_user():
    print(colored("Pattern> M O N K E Y", "yellow"))
    print(colored("Pattern> D O N K E Y", "yellow"))
    print(colored("Pattern> M A K E", "yellow"))
    print(colored("Pattern> *", "yellow"))
    print(colored("Info> Input the sets like the upper patter and at the end enter *", "blue"))

    _flag = True
    _item_sets = []

    while (_flag):
        user_input = input()
        if user_input == '*':
            _flag = False
            break

        _item = [x for x in user_input.split(" ") if x != "" ]
        _item = list(dict.fromkeys(_item))

        _item_sets.append(_item)

    return _item_sets

def _item_set_by_length_one(_item_set):
    _one_length_items = []
    for i_item in _item_set:
        for j_item in i_item:
            _one_length_items.append(j_item)

    return _one_length_items

def frequent_item_sets_by_length_one(_items, _support):

    _one_length_items = _item_set_by_length_one(_items)
    _one_length_result = []
    _one_length_frequent = []



    for item in _one_length_items:
        if _one_length_items.count(item) >= _support:
            _one_length_result.append(item)

    _counter = Counter(_one_length_result)
    _counter = sorted(_counter.items(), key=lambda pair: pair[1], reverse=True)

    _one_length_result = []
    _one_length_frequent = []

    for _item in _counter:
        _one_length_result.append(_item[0])
        _one_length_frequent.append(_item[1])

    print(colored("Info> Your first item set: {} frequency is: {}".format(_one_length_result, _one_length_frequent),
                  "blue"))

    return _one_length_result,_one_length_frequent

def remove_non_frequent_items(_item_set,_frequent_item):

    _final_result = []

    _sorted = lambda x: (x)

    for i_item in _item_set:
        _temp_values = []
        for j_item in i_item:
            if j_item in _frequent_item and j_item not in _temp_values:
                _temp_values.append(j_item)

        _final_result.append(
            sorted(_temp_values,key=_item_set_by_length_one(_item_set).count, reverse=True)
        )

    _table = tabulate({"Item": _final_result}, headers="keys", showindex="always",tablefmt="simple")

    print(colored(
        "Info> Table of frequent sets:\n","blue"
        ),
        _table
    )

    return _final_result
